from textblob import TextBlob
import csv
f = open("./input.tsv", encoding='utf-8')
fw = open("./output.txt", 'w', encoding='utf-8')

reader = csv.reader(f, delimiter='\t')
for ligne in reader:
    for i, reponse in enumerate(ligne):
        # reponse = unicodedata.normalize('NFD', reponse).encode('ascii', 'ignore').decode('ASCII')
        reponse = reponse.replace(" \\t", "\\t")
        ligne[i] = reponse
    ligne = ligne[0].split('\\t')
    for response in ligne:
        blb = TextBlob(response)
        try:
            blb = blb.translate(to='en')
        except:
            blb = TextBlob(response)

        for sentences in blb.sentences:
            # print(sentences.sentiment)
            fw.write(str(sentences) + ' pol: ' + str(sentences.sentiment.polarity) + ' sub: ' + str(sentences.sentiment.subjectivity) + '\n')

fw.close()
f.close()