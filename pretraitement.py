#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import unicodedata

with open("./logstash-6.2.2/input.tsv",encoding ='utf-8') as f:
	reader = csv.reader(f, delimiter = '\t')
	for ligne in reader:
		for reponse in ligne:
			# for reponse in reponses
			reponse = unicodedata.normalize('NFD', reponse).encode('ascii', 'ignore').decode('ASCII')
			reponse = reponse.replace(" \\t","\\t")
			print(reponse) 
			#print(reponse)