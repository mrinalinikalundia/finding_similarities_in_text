# -*- coding: utf-8 -*-
"""finding similarities in text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BQaA8mnJiZ_ZoMiVjDx_Oa8MQ2RfEYQD
"""

import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import re
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

documents=['Mahendra Singh Dhoni(born 7 July 1981) is an Indian former international cricketer who was captain of the Indian national cricket team in limited-overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014. He is also the current captain of CSK in the IPL. He led India to victory in three ICC trophies 2007 ICC World Twenty20, 2011 Cricket World Cup and 2013 ICC Champions Trophy, the most by any Indian captain. Under his captaincy India also won 2010 and 2016 Asia Cup. A right-handed wicket-keeper batsman. He scored over 10,000 runs in One Day Internationals, with the reputation as one of the best finishers in the game. He is also one of the greatest wicket-keepers in the history of cricket.',
          'In Indian domestic cricket he played for Bihar and Jharkhand Cricket team. He is the captain of Chennai Super Kings (CSK) in the Indian Premier League. He captained the side to championships in the 2010, 2011, 2018 and 2021 editions of IPL league. Also under his captaincy Chennai Super Kings (CSK) Won Champions League T20 two times, in 2010 and 2014.',
          'Dhoni made his ODI debut on 23 December 2004, against Bangladesh in Chittagong, and played his first Test a year later against Sri Lanka. He played his first T20I also a year later against South Africa. In 2007, he took over the ODI captaincy from Rahul Dravid and he also selected as T20I captain of India in this year. In 2008, he was selected as Test captain. His captaincy record in Tests format was mixed, successfully leading India to a series win against New Zealand in 2008 and the Border-Gavaskar Trophy (home series in 2010 and 2013) against Australia while losing to Sri Lanka, Australia, England, and South Africa by big margins in away conditions.',
          'He announced his retirement from Tests on 30 December 2014, and stepped down as captain of T20Is and ODIs in 2017. On 15 August 2020, Dhoni retired from all formats of international cricket and continues to play in the IPL.',
          'Dhoni received India highest sports honour, the Major Dhyanchand Khel Ratna Award in 2008 for his outstanding achievements and the Government of India honoured him India fourth civilian award Padma Shri in 2009 and third civilian award Padma Bhushan in 2018. He is the only cricket captain in the world to win all three of the Cricket World Cup, ICC Men T20 World Cup and ICC Champions Trophy.']

documents_df=pd.DataFrame(documents,columns=['documents'])

documents_df

stop_words_l=stopwords.words('english')
documents_df['documents_cleaned']=documents_df.documents.apply(lambda x: " ".join(re.sub(r'[^a-zA-Z]',' ',w).lower() for w in x.split() if re.sub(r'[^a-zA-Z]',' ',w).lower() not in stop_words_l) )

tfidfvectoriser=TfidfVectorizer()
tfidfvectoriser.fit(documents_df.documents_cleaned)
tfidf_vectors=tfidfvectoriser.transform(documents_df.documents_cleaned)

pairwise_similarities=np.dot(tfidf_vectors,tfidf_vectors.T).toarray()
pairwise_differences=euclidean_distances(tfidf_vectors)

def most_similar(doc_id,similarity_matrix,matrix):
    print (f'Document: {documents_df.iloc[doc_id]["documents"]}')
    print ('\n')
    print ('Similar Documents:')
    if matrix=='Cosine Similarity':
        similar_ix=np.argsort(similarity_matrix[doc_id])[::-1]
    elif matrix=='Euclidean Distance':
        similar_ix=np.argsort(similarity_matrix[doc_id])
    for ix in similar_ix:
        if ix==doc_id:
            continue
        print('\n')
        print (f'Document: {documents_df.iloc[ix]["documents"]}')
        print (f'{matrix} : {similarity_matrix[doc_id][ix]}')

most_similar(0,pairwise_similarities,'Cosine Similarity')
most_similar(0,pairwise_differences,'Euclidean Distance')

print (tfidf_vectors[0].toarray())
print (pairwise_similarities.shape)
print (pairwise_similarities[0][:])

! pip install -U sentence-transformers

from sentence_transformers import SentenceTransformer

sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')

document_embeddings = sbert_model.encode(documents_df['documents_cleaned'])

pairwise_similarities=cosine_similarity(document_embeddings)
pairwise_differences=euclidean_distances(document_embeddings)

most_similar(0,pairwise_similarities,'Cosine Similarity')

most_similar(0,pairwise_differences,'Euclidean Distance')

