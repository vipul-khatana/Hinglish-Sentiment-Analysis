#!/bin/sh
#
# usage: ./cdacm-postagger.sh inputfile
# usage: bash cdacm-postagger.sh inputfile
CURRDIR=`pwd`
bash tag-request.sh $CURRDIR/cdacm-model/hin-accurate.tagger $1
