# Chapter 8 - Sphinx

The CMUSphinx case study trains a speech recognition model using GMM/HMM models.

## Requirements
* [Docker](https://docs.docker.com/install/) 

## Running the Docker Image
The docker images for this case study are located on dockerhub. Running the commands below will automatically download and start a jupyter notebook.

Run the Docker image:
```
docker run -p 8888:8888 --rm springernlp/chapter_8s:latest
```


## Building the Docker image
If you want to build the Docker image from scratch, use the following command. 
```
docker build -t chapter_8s:latest .
```
