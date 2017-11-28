#!/bin/sh
#
# usage: ./tag-request.sh model textFile
#  e.g., ./tag-request.sh models/hin-accurate-tagger sample-input.txt
CURRDIR=`pwd`

java -mx512M -cp 'stanford-postagger.jar:' edu.stanford.nlp.tagger.maxent.MaxentTagger -model $1 -tokenized 'false' -textFile $2
