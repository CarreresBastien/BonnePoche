#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import unicodedata

with open("./logstash-6.2.2/input.tsv",encoding ='utf-8') as f:
	with open("./logstash-6.2.2/input_processed.tsv",encoding='utf-8') as f_out:
		reader = csv.reader(f, delimiter = '\t')
		for ligne in reader:
			for reponse in ligne:
				reponse = unicodedata.normalize('NFD', reponse).encode('ascii', 'ignore').decode('ASCII')
				reponse = reponse.replace(" \\t","\\t")
				print(reponse) 


	#TODO reecrire les modifs dans un fichier .csv