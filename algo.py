'''
Created on Fri Nov 3 2017
@author: vipulkhatana
'''
import numpy as np 
import xlsxwriter
import sys
from googletrans import Translator
from xlrd import open_workbook
translator = Translator(service_urls=['translate.google.co.in'])

if(len(sys.argv)!=2):
	sys.exit("Usage: python algo.py <input_filename.xlsx>")

# translate to Hindi 
def translate_to():
	post = []

	book = open_workbook(sys.argv[1])
	sheet = book.sheet_by_index(0)
	ctr = 0
	for row in sheet.col(1):
		if ctr!=0:
			post.append(row.value.encode('utf-8'))
		ctr+=1
	for i in range(0,len(post)):
		str(post[i])


	translations=[] 
	xbook = xlsxwriter.Workbook('hinglish.xlsx')
	xsheet = xbook.add_worksheet('Test')
	for i in range(0,len(post)):
		translation = translator.translate(post[i],src='en', dest='hi')
		xsheet.write(i,1,''.join((translation.text)))
	











