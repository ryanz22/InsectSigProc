import os
import sys
import pathlib
import numpy as np
import pprint
from typing import Tuple, List
import logging
import functional as pyf
import shutil
from enum import Enum
from typing_extensions import Annotated
import typer
from functools import partial

from pytorchstudy.insect_snd_sep.prepare_data import (
    prepare_librimix,
)


app = typer.Typer()


@app.command(help="prepare sound separation dataset")
def prepare(
    datapath: Annotated[
        pathlib.Path,
        typer.Option(
            # default=...,
            exists=True,
            file_okay=False,
            dir_okay=True,
            help="input dir of dataset",
        ),
    ],
    savepath: Annotated[
        pathlib.Path,
        typer.Option(
            # default=...,
            exists=True,
            file_okay=False,
            dir_okay=True,
            help="output dir of dataset",
        ),
    ],
    n_spks: int = 2,
    fs: int = 8000,
    version: Annotated[str, typer.Option()] = "wav8k/min/",
    set_types: Annotated[Tuple[str, str, str], typer.Option()] = (
        "train-360",
        "dev",
        "test",
    ),
):
    print(f"datapath: {datapath}")
    print(f"saveapth: {savepath}")
    print(f"n_spks: {n_spks}")
    print(f"fs: {fs}")
    print(f"version: {version}")
    print(f"set_types: {set_types}")

    prepare_librimix(
        datapath=str(datapath),
        savepath=str(savepath),
        n_spks=n_spks,
        skip_prep=False,
        librimix_addnoise=False,
        fs=fs,
        version=version,
        set_types=set_types,
    )


@app.command(help="sepformer inference")
def inference(
    test_sample: Annotated[
        pathlib.Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            help="test sample file",
        ),
    ],
    model_dir: Annotated[
        pathlib.Path,
        typer.Option(
            exists=True,
            file_okay=False,
            dir_okay=True,
            help="model folder",
        ),
    ],
    out_dir: Annotated[
        pathlib.Path,
        typer.Option(
            exists=True,
            file_okay=False,
            dir_okay=True,
            help="output folder for estimated sources",
        ),
    ],
    sr: int = 44100,
    n_src: int = 2,
    cuda: bool = False,
):
    from speechbrain.pretrained import SepformerSeparation as separator
    import soundfile as sf

    if cuda:
        model = separator.from_hparams(
            source=str(model_dir), run_opts={"device": "cuda"}
        )
    else:
        model = separator.from_hparams(source=str(model_dir))

    est_sources = model.separate_file(path=str(test_sample))

    print(est_sources.shape)

    sample_stem = test_sample.stem

    print("\nseparated source 1")
    est_src_1 = est_sources[:, :, 0].detach().cpu().squeeze()
    sf.write(out_dir / f"{sample_stem}_est_s1.wav", est_src_1, sr)

    print("\nseparated source 2")
    est_src_2 = est_sources[:, :, 1].detach().cpu().squeeze()
    sf.write(out_dir / f"{sample_stem}_est_s2.wav", est_src_2, sr)

    if n_src == 3:
        print("\nseparated source 3")
        est_src_3 = est_sources[:, :, 2].detach().cpu().squeeze()
        sf.write(out_dir / f"{sample_stem}_est_s3.wav", est_src_3, sr)


if __name__ == "__main__":
    print(f"python version is {sys.version_info}")
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 9):
        sys.exit("this program needs python 3.9 and above to run")

    # https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
    print(f"sys.path:\n{sys.path}")

    # l_fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    # logging.basicConfig(level=logging.ERROR, format=l_fmt)

    l_fmt = "[%(name)s %(levelname)s] %(asctime)s - %(message)s"
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(l_fmt))
    logger = logging.getLogger("dataset_tool")
    logger.addHandler(ch)
    logger.setLevel(logging.ERROR)

    app()
