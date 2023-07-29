# Explain prepare_data.py

## How to run

```sh
PYTHONPATH=. python3 app/snd_sep.py prepare --help

PYTHONPATH=. python3 app/snd_sep.py prepare \
--datapath datasets/sound/LibriMix/dataset/Libri3Mix/ \
--savepath ~/tmp/ml --n_spks 3 --fs 16000 --version 'wav16k/min/' \
--set_types train-100 dev test
```

The script will generate 3 CSV files to '--savepath' and they are:

Among the columns, what the train.py really cares are:
ID, mix_wav, s1_wav, s2_wav, s3_wav if mix3, noise_wav if use_wham_noise.

columns duration, mix_wav_format, mix_wav_opts, s1_wav_format, s1_mix_wav_opts, 2_wav_format, s2_wav_opts, s3_wav_format, mix_wav_opts, noise_wav_format, noise_wav_opts are optional.

libri3mix_dev.csv

```csv
ID,duration,mix_wav,mix_wav_format,mix_wav_opts,s1_wav,s1_wav_format,s1_wav_opts,s2_wav,s2_wav_format,s2_wav_opts,s3_wav,s3_wav_format,s3_wav_opts,noise_wav,noise_wav_format,noise_wav_opts
0,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/mix_clean/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s1/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s2/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s3/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/noise/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,
1,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/mix_clean/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s1/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s2/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s3/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/noise/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,
```

libri3mix_test.csv

```csv
ID,duration,mix_wav,mix_wav_format,mix_wav_opts,s1_wav,s1_wav_format,s1_wav_opts,s2_wav,s2_wav_format,s2_wav_opts,s3_wav,s3_wav_format,s3_wav_opts,noise_wav,noise_wav_format,noise_wav_opts
0,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/mix_clean/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s1/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s2/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s3/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/noise/6313-66125-0003_1673-143396-0014_6345-93302-0027.wav,wav,
1,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/mix_clean/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s1/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s2/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/s3/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/dev/noise/1919-142785-0054_777-126732-0057_3752-4944-0042.wav,wav,
```

libri3mix_train-100.csv

```csv
ID,duration,mix_wav,mix_wav_format,mix_wav_opts,s1_wav,s1_wav_format,s1_wav_opts,s2_wav,s2_wav_format,s2_wav_opts,s3_wav,s3_wav_format,s3_wav_opts,noise_wav,noise_wav_format,noise_wav_opts
0,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/mix_clean/3436-172171-0055_730-360-0044_2989-138028-0071.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s1/3436-172171-0055_730-360-0044_2989-138028-0071.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s2/3436-172171-0055_730-360-0044_2989-138028-0071.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s3/3436-172171-0055_730-360-0044_2989-138028-0071.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/noise/3436-172171-0055_730-360-0044_2989-138028-0071.wav,wav,
1,1.0,datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/mix_clean/6019-3185-0037_2289-152257-0014_2989-138028-0037.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s1/6019-3185-0037_2289-152257-0014_2989-138028-0037.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s2/6019-3185-0037_2289-152257-0014_2989-138028-0037.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/s3/6019-3185-0037_2289-152257-0014_2989-138028-0037.wav,wav,,/media/ryanz/ml-data/projects/ml/datasets/sound/LibriMix/dataset/Libri3Mix/wav16k/min/train-100/noise/6019-3185-0037_2289-152257-0014_2989-138028-0037.wav,wav,
```

