'''
Created on Thu Nov 2 2017
@author: vipulkhatana
'''
import subprocess

def getTag(data):
	f = open('tagdata.txt','w')
	f.write(data)
	f.close()
	proc = subprocess.Popen(["./tag-request.sh ./cdacm-model/hin-accurate.tagger tagdata.txt", ""], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return out
