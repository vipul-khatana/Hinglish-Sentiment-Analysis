# -*- coding: utf-8 -*-
import subprocess

def getTag(data):
	f = open('tagdata.txt','w')
	f.write(data)
	f.close()
	proc = subprocess.Popen(["./tag-request.sh ./cdacm-model/hin-accurate.tagger tagdata.txt", ""], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return out