#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import unicodedata
import json
from elasticsearch import *

es = Elasticsearch()

# f_out =open("./logstash-6.2.2/input_processed.tsv",'w',encoding = 'utf-8')
with open("./input.tsv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    data = {}
    data['raiponce'] = []
    num_ligne = 0
    for ligne in reader:
        for i, reponse in enumerate(ligne):
            # reponse = unicodedata.normalize('NFD', reponse).encode('ascii', 'ignore').decode('ASCII')
            reponse = reponse.replace(" \\t", "\\t")
            ligne[i] = reponse
        ligne = ligne[0].split('\\t')
        print(ligne)
        if num_ligne != 0:
            es.create(index='raiponce', doc_type='response', id=num_ligne, body=
            {
                'House': ligne[0],
                'Cooking': ligne[1],
                'Music': ligne[2],
                'Game': ligne[3],
                'Sport': ligne[4],
                'Phone': ligne[5],
                'DigitalService': ligne[6],
                'Gender': ligne[7],
                'Age': ligne[8],
                'City': ligne[9],
                'Date': ligne[10],
                'UserId': ligne[11]
            })
        num_ligne += 1

# data_writer = csv.writer(f_out,delimiter = '\t')
# 		#data_writer.writerow(ligne)
# with open('input_json.txt','w') as f_out:
# 	json.dump(data,f_out)
# f_out.close()
