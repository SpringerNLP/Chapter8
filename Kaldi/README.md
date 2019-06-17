# Kaldi-Docker
This is a docker wrapper around [Kaldi](http://kaldi-asr.org/). 

## Docker
```
docker run -v <local data directory>:/data/ -p 8888:8888 springernlp:chapter_8k:latest /bin/bash
```

If a GPU is available, run: 
```
docker run -it --runtime=nvidia -v /data/:/data/ -p 8888:8888 springernlp/chapter8k:gpu /bin/bash
```

Start the python notebook.
```
jupyter notebook --no-browser --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token=''
```
Go to [localhost:8888](http://localhost:8888).


## Build the Docker Image from Scratch
Additional requirements due to licenses:

SRILM: 
SRILM has an more restrictive license and therefore requires you to fill out a form. 
Download SRILM from [here](http://www.speech.sri.com/projects/srilm/download.html).
change the name of the file to `srilm.tgz` and move it into the root directory of this repository. 
```
/kaldi-docker/srilm.tgz
```
The Dockerfile will add this to the image build.

Warning: If you are building this image from scratch, it can take a very long time (to the tune of an hour).
```
docker build -t chapter_8k:latest .
```

## Running the Common Voice example
- Source /kaldi/tools/env.sh
- Change data directory in /kaldi/egs/commonvoice/s5/run.sh
- If dataset is downloaded already, make sure there is a `.complete` file in the cv_corpus_v1 directory (`touch .complete`). Otherwise it will download the dataset again.
- Change cmd.sh from `queue.pl` to `run.pl` (don't use distributed queue library)


```
cd /kaldi/egs/commonvoice/s5/
./run.sh
```

TODO:
[x] Change to correct directory
[x] Must change run.sh for dnn run (it sources that file before running)
[] Still haveing to run the install at the beginning of the file for now.. not sure why
[] Copy notebook into dir 
[] Split cpu and gpu containers appropriately
[] Push GPU container
``` jupyter notebook --ip=0.0.0.0 --allow-root```
