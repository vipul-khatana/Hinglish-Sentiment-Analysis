'''
Created on Sat Nov 4 2017
@author: vipulkhatana
'''
from nltk.corpus import sentiwordnet as swn

def polarity( a,b ):
   score = 0;
   if((b=='VB')and(len(swn.senti_synsets(a,'v'))>0)):
       for i in swn.senti_synsets(a,'v'):

   	        score+=(i).pos_score()-(i).neg_score() 
       score=score/len(swn.senti_synsets(a,'v'))
       return score

   if((b=='NN')and(len(swn.senti_synsets(a,'n'))>0)):
       for i in swn.senti_synsets(a,'n'):

   	        score+=(i).pos_score()-(i).neg_score() 
       score=score/len(swn.senti_synsets(a,'n'))
       return score
   


   if((b=='JJ')and(len(swn.senti_synsets(a,'a'))>0)):
       for i in swn.senti_synsets(a,'a'):

   	        score+=(i).pos_score()-(i).neg_score() 
       score=score/len(swn.senti_synsets(a,'a'))
       return score
    
   if((b=='RB')and(len(swn.senti_synsets(a,'r'))>0)):
       for i in swn.senti_synsets(a,'r'):

   	        score+=(i).pos_score()-(i).neg_score() 
       score=score/len(swn.senti_synsets(a,'r'))
       return score
   if(score==0):
        return 'NF'         
