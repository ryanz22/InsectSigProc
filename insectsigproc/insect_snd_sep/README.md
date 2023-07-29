# Speech separation with LibriMix

This folder contains some popular recipes for the [LibriMix Dataset](https://arxiv.org/pdf/2005.11262.pdf) (2/3 sources).

* This recipe supports train with several source separation models on LibriMix, including [Sepformer](https://arxiv.org/abs/2010.13154), [DPRNN](https://arxiv.org/abs/1910.06379), [ConvTasnet](https://arxiv.org/abs/1809.07454), [DPTNet](https://arxiv.org/abs/2007.13975).

## How to setup

Additional dependencies:
```
pip install mir_eval
pip install pyloudnorm
```

## How to run
To run it:

```shell
python train.py hparams/sepformer-libri2mix.yaml --data_folder yourpath/Libri2Mix
python train.py hparams/sepformer-libri3mix.yaml --data_folder yourpath/Libri3Mix
```

Run on 3090/4090

```shell
PYTHONPATH=. nohup python3 \
pytorchstudy/insect_snd_sep/train_insect.py \
config/insect_snd_sep/hparams/insect-mix2-gh-gh-clean.yaml \
--data_folder datasets/pestdataprocess/sound/insect_sep_ds/train-ds/mix2-gh-gh-clean/ &> mix2-gh-gh-clean_nohup.txt &
```

Run on A100-80GB

```shell
PYTHONPATH=. CUDA_VISIBLE_DEVICES=3 nohup python3 \
pytorchstudy/insect_snd_sep/train_insect.py \
config/insect_snd_sep/hparams/insect-mix2-gh-gh-clean.yaml \
--data_folder datasets/pestdataprocess/sound/insect_sep_ds/train-ds/mix2-gh-gh-clean/ &> mix2-gh-gh-clean_nohup.txt &
```

How to run multiple GPU:

  "To use data_parallel backend, start your script with:\n\t"
                "python experiment.py hyperparams.yaml "
                "--data_parallel_backend=True"
                "To use DDP backend, start your script with:\n\t"
                "python -m torch.distributed.lunch [args]\n"
                "experiment.py hyperparams.yaml --distributed_launch=True "
                "--distributed_backend=nccl"


Note that during training we print the negative SI-SNR (as we treat this value as the loss).

### Inference

```shell
PYTHONPATH=. python app/snd_sep.py inference --test-sample data/test/mix3-gh-cricket-bird-clean/mix_0.wav --model-dir models/mix3-gh-cricket-bird-clean-k8s4/ --out-dir data/test/mix3-gh-cricket-bird-clean/ --n-src 3

PYTHONPATH=. python app/snd_sep.py inference --test-sample ext-data/test/mix2-gh-cricket-aug-clean/mix_4.wav --model-dir ext-models/convtasnet/mix2-gh-cricket-aug-clean-k16s8/ --out-dir ext-data/test/mix2-gh-cricket-aug-clean/cnvtasnet/k16s8/ --n-src 2
```

### Results

Here are the SI - SNRi results (in dB) on the test set of LibriMix dataset with SepFormer:

| | SepFormer. Libri2Mix |
| --- | --- |
|SpeedAugment | 20.1|
|DynamicMixing | 20.4|


| | SepFormer. Libri3Mix |
| --- | --- |
|SpeedAugment | 18.4|
|DynamicMixing | 19.0|


### Example calls for running the training scripts

* Libri2Mix with dynamic mixing `python train.py hparams/sepformer-libri2mix.yaml --data_folder yourpath/Libri2Mix/ --base_folder_dm yourpath/LibriSpeech_processed --dynamic_mixing True`

* Libri3Mix with dynamic mixing `python train.py hparams/sepformer-libri3mix.yaml --data_folder yourpath/Libri3Mix/ --base_folder_dm yourpath/LibriSpeech_processed --dynamic_mixing True`

* Libri2Mix with dynamic mixing with WHAM! noise in the mixtures `python train.py hparams/sepformer-libri2mix.yaml --data_folder yourpath/Libri2Mix/ --base_folder_dm yourpath/LibriSpeech_processed --dynamic_mixing True --use_wham_noise True`

* Libri3Mix with dynamic mixing with WHAM! noise in the mixtures `python train.py hparams/sepformer-libri3mix.yaml --data_folder yourpath/Libri3Mix/ --base_folder_dm yourpath/LibriSpeech_processed --dynamic_mixing True --use_wham_noise True`


The output folder with the trained model and the logs can be found [here](https://drive.google.com/drive/folders/1DN49LtAs6cq1X0jZ8tRMlh2Pj6AecClz?usp=sharing) for 3-speaker mixtures and [here](https://drive.google.com/drive/folders/1NPTXw4i9Vmahhr5BSQQa-ZTTm45FwYJA?usp=sharing) for 2-speakers ones.

### Multi-GPU training

You can run the following command to train the model using Distributed Data Parallel (DDP) with 2 GPUs:

```
python -m torch.distributed.launch --nproc_per_node=2 train.py hparams/sepformer-libri2mix.yaml --data_folder /yourdatapath --distributed_launch --distributed_backend='nccl'

PYTHONPATH=. CUDA_VISIBLE_DEVICES=2,3 nohup python3 -m torch.distributed.launch --nproc_per_node=2 pytorchstudy/insect_snd_sep/train_insect.py config/insect_snd_sep/hparams/insect-mix2-gh-gh-aug-clean-k8s4.yaml --data_folder data/sound/insect_sep_ds/train-ds/mix2-gh-gh-aug-clean/ --distributed_launch --distributed_backend='nccl' &> mix2-gh-gh-clean-k8s4.out &
```
You can add the other runtime options as appropriate. For more complete information on multi-GPU usage, take a look at this [tutorial](https://colab.research.google.com/drive/13pBUacPiotw1IvyffvGZ-HrtBr9T6l15?usp=sharing).

## Datasets

### Libri2/3 Mix
* The Dataset can be created using the scripts at `https://github.com/JorisCos/LibriMix`.


### Dynamic Mixing:

* This recipe supports dynamic mixing where the training data is dynamically created in order to obtain new utterance combinations during training.


## **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/


## **Citing SpeechBrain**
Please, cite SpeechBrain if you use it for your research or business.

```bibtex
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}
```

