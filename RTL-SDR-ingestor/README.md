cusignal-nifi Nar wrapper for cusignal 
====================================

conda installation:

Due to a know bug in conda conda 4.7.x [1] we can not use: `cuda creade cusignal-nifi -f cusignal-conda-env.yaml`

We simply split the commsnd for now :
```
conda create cusignal-nifi
```

```
conda create cusignal-nifi 
```
```
conda activate cusignal-nifi
```


this will put you into the cusignal-nifi virtual envronments and install al python dependencies.

we wil soo
Alternatively, you can run make all




[1] https://github.com/conda/conda/issues/8205