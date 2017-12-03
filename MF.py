'''
Created on Thu Nov 2 2017
@author: vipulkhatana
'''
def getMF(l):
	y = []
	for s in l.splitlines():
		s = s.split()
		x = []
		for i in s:
			x.append(i.split('|'))
		mf = 1
		nf = 1
		cf = 1
		for a,b in x:
			if b in "QF INTF".split():
				mf = 2
				y.append([a, 0, b])
			elif b in "NEG".split():
				nf *= -1
				y.append([a, 0, b])
			elif b in "PUNC SYM".split():
				nf = 1
				cf = 1
				y.append([a, 0, b])
			elif b in "CC CCO CCS CCD".split():
				cf = 1.5
				y.append([a, 0, b])
			# elif b in "UNK QTC".split():
			# 	#translate and check
			# 	y.append([a, 99, b])
			elif b in "JJ RB VM VAUX UNK":
				y.append([a, cf*nf*mf*1, b])
				mf-=1
				if mf<1:
					mf=1
			else:
				# print b, a
				y.append([a, cf*nf*mf*1, b])
	return y
