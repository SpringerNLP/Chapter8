FROM ubuntu:16.04

RUN apt-get update && apt-get install -y bash git ssh \
    autoconf libtool automake g++ make bison python \
    python-dev python3-pip swig ffmpeg subversion

RUN pip3 install --upgrade pip && pip3 install jupyter wget pandas

RUN mkdir /cmusphinx
WORKDIR /cmusphinx
# sphinxbase
RUN git clone https://github.com/cmusphinx/sphinxbase.git
WORKDIR /cmusphinx/sphinxbase
RUN ./autogen.sh
RUN make && make install
WORKDIR /cmusphinx

# sphinxtrain
RUN git clone https://github.com/cmusphinx/sphinxtrain.git
WORKDIR /cmusphinx/sphinxtrain
RUN ./autogen.sh
RUN make && make install
WORKDIR /cmusphinx

# pocketsphinx
RUN git clone https://github.com/cmusphinx/pocketsphinx.git
WORKDIR /cmusphinx/pocketsphinx
RUN ./autogen.sh
RUN make && make install
WORKDIR /cmusphinx

# CMUCLMTK
RUN svn checkout svn://svn.code.sf.net/p/cmusphinx/code/trunk/cmuclmtk
WORKDIR /cmusphinx/cmuclmtk
RUN ./autogen.sh
RUN make && make install
ENV LD_LIBRARY_PATH="/usr/local/lib"
RUN ldconfig
WORKDIR /cmusphinx

WORKDIR /cmusphinx/common_voice/
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]