'''
Created on Fri Nov 3 2017
@author: vipulkhatana
'''
import HSWN
import preprocess
import MF
import tagger
import sys
import xlrd
import translate
import moduleeng
import nltk
import algo
import sys
import xlsxwriter
from googletrans import Translator
from xlrd import open_workbook
translator = Translator(service_urls=['translate.google.co.in'])

if(len(sys.argv)!=2):
	sys.exit("Usage: python algo.py <input_filename.xlsx>")

#### Read the corpus

tweets = []

book = open_workbook(sys.argv[1])
sheet = book.sheet_by_index(0)
ctr = 0
for row in sheet.col(1):
	if ctr!=0:
		tweets.append(row.value.encode('utf-8'))
	ctr+=1
for i in range(0,len(tweets)):
	str(tweets[i])

xbook = xlsxwriter.Workbook('hinglish.xlsx')
xsheet = xbook.add_worksheet('Test')
for i in range(0,len(tweets)):
	translation = translator.translate(tweets[i],src='en', dest='hi')
	xsheet.write(i,1,''.join((translation.text)))

posts = []

book = open_workbook('hinglish.xlsx')
sheet = book.sheet_by_index(0)
ctr = 0
for row in sheet.col(1):
	if ctr!=0:
		posts.append(row.value.encode('utf-8'))
	ctr+=1
print posts[1]


#### Write posts with polirity
writeDoc = open('OUTPUT.csv','w+')


#### STEP 1 - Apply preprocessing

for i in range(len(posts)):
	posts[i] = preprocess.preProcess(posts[i])

#### STEP 2 - Actual work

sno = 1
for post in posts:

	## Get multipliers
	totalPol = 0.0

	tagdata = tagger.getTag(post)
	## List of multiplying factors
	MFlist = MF.getMF(tagdata)

	for word in post.split(' '):
		## Get tag info
		for mf in MFlist:
			if mf[0] == word:
				mult = mf[1]
				typ = mf[2]

		# If word exists in HSWN
		if HSWN.searchHSWN(word) != 'NF':
			wordPol = HSWN.searchHSWN(word)

			####### HANDLE MULTIPLIER
			wordPol = wordPol*mult

			totalPol += wordPol


	writeDoc.write(str(sno)+',')
	
	if totalPol>0.1:
		writeDoc.write('1\n')
	elif totalPol<-0.1:
		writeDoc.write('-1\n')
	else:
		writeDoc.write('0\n')

	sno+=1

