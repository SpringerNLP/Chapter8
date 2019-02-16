    1  source tools/env.sh 
    2  cd egs/commonvoice/s5/
    3  ls
    4  vim run.sh 
    5  apt-get install vim
    6  vim run.sh 
    7  ./run.sh 
    8  mv /kaldi/tools/sequitur-g2p /kaldi/tools/sequitur
    9  vim /kaldi/tools/env.sh 
   10  mv /kaldi/tools/sequitur /kaldi/tools/sequitur-g2p
   11  ./run.sh 
   12  vim run.sh 
   13  ls
   14  vim cmd.sh 
   15  ./run.sh 
   16  vim exp/make_mfcc/valid_train/make_mfcc_valid_train.1.log 
   17  sox
   18  sox /data/datasets/cv_corpus_v1/cv-valid-train/sample-000000.mp3 -t wav -r 16k -b 16 -e signed test.wav
   19  ls
   20  rm exp/make_mfcc/valid_train/make_mfcc_valid_train.*
   21  apt-get install libsox-fmt-mp3
   22  sox /data/datasets/cv_corpus_v1/cv-valid-train/sample-000000.mp3 -t wav -r 16k -b 16 -e signed test.wav
   23  ls
   24  rm test.wav 
   25  ./run.sh 
   26  ls exp/make_mfcc/valid_train/
   27* 
   28  vim ./run.sh 
   29  ./run.sh 
   30  vim cmd.sh 
   31  ./run.sh 
