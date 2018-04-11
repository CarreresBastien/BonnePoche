#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import unicodedata
import json
from elasticsearch import *

import nltk
nltk.download('punkt')

from textblob import TextBlob

es = Elasticsearch()

def return_sentences_polarity_subjectivity(ligne):

    blb = TextBlob(ligne)
    try:
        blb = blb.translate(to='en')
    except:
        blb = TextBlob(reponse)

    sumPolarity = 0
    sumSubjectivity = 0

    for sentences in blb.sentences:
        sumPolarity += sentences.sentiment.polarity
        sumSubjectivity += sentences.sentiment.subjectivity

    to_return = {
        'response': ligne,
        'polarity': sumPolarity/len(blb.sentences),
        'subjectivity': sumSubjectivity/len(blb.sentences)
    }

    return to_return

# f_out =open("./logstash-6.2.2/input_processed.tsv",'w',encoding = 'utf-8')
with open("./input.tsv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    data = {}
    data['raiponce'] = []
    num_ligne = 0
    for ligne in reader:
        for i, reponse in enumerate(ligne):

            reponse = reponse.replace(" \\t", "\\t")
            blb = TextBlob(reponse)

            try:
                blb = blb.translate(to='en')
            except:
                blb = TextBlob(reponse)

            ligne[i] = reponse
        ligne = ligne[0].split('\\t')
        for index in range(len(ligne)):
                ligne[index] = return_sentences_polarity_subjectivity(ligne[index])
        print(ligne)
        if num_ligne != 0:
            es.create(index='raiponce', doc_type='_doc', id=num_ligne, body=
            {
                'House': {
                    'response': ligne[0]['response'],
                    'polarity': ligne[0]['polarity'],
                    'subjectivity': ligne[0]['subjectivity']
                },
                'Cooking':{
                    'response': ligne[1]['response'],
                    'polarity': ligne[1]['polarity'],
                    'subjectivity': ligne[1]['subjectivity']
                },
                'Music': {
                    'response': ligne[2]['response'],
                    'polarity': ligne[2]['polarity'],
                    'subjectivity': ligne[2]['subjectivity']
                },
                'Game': {
                    'response': ligne[3]['response'],
                    'polarity': ligne[3]['polarity'],
                    'subjectivity': ligne[3]['subjectivity']
                },
                'Sport': {
                    'response': ligne[4]['response'],
                    'polarity': ligne[4]['polarity'],
                    'subjectivity': ligne[4]['subjectivity']
                },
                'Phone': {
                    'response': ligne[5]['response'],
                    'polarity': ligne[5]['polarity'],
                    'subjectivity': ligne[5]['subjectivity']
                },
                'DigitalService': {
                    'response': ligne[6]['response'],
                    'polarity': ligne[6]['polarity'],
                    'subjectivity': ligne[6]['subjectivity']
                },
                'Gender': ligne[7]['response'],
                'Age': ligne[8]['response'],
                'City': ligne[9]['response'],
                'Date': ligne[10]['response'],
                'UserId': ligne[11]['response']
            })
        num_ligne += 1


