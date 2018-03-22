#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import unicodedata

f_out =open("./logstash-6.2.2/input_processed.tsv",'w',encoding = 'utf-8')
with open("./logstash-6.2.2/input.tsv",encoding ='utf-8') as f:
	reader = csv.reader(f, delimiter = '\t')
	for ligne in reader:
		for i,reponse in enumerate(ligne):
			print(reponse)
			reponse = unicodedata.normalize('NFD', reponse).encode('ascii', 'ignore').decode('ASCII')
			reponse = reponse.replace(" \\t","\\t")
			ligne[i] = reponse
		print(ligne) 
		data_writer = csv.writer(f_out,delimiter = '\t')
		data_writer.writerow(ligne)

f_out.close()
