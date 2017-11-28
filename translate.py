# -*- coding: utf-8 -*-

import numpy as np 
from googletrans import Translator
translator = Translator(service_urls=['translate.google.co.in'])


def translate(word):
	return translator.translate(word,src='hi' , dest='en')
