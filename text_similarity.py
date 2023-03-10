# -*- coding: utf-8 -*-
"""text similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RIE6vpLLoTBh5aZjuEA8a2lOAHdaGtdz
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

Document1 = """Mahendra Singh Dhoni (/məˈheɪndrə ˈsɪŋ dhæˈnɪ/ (listen); born 7 July 1981), commonly known as MS Dhoni, is a former Indian cricketer and captain of the Indian national team in limited-overs formats from 2007 to 2017, and in Test cricket from 2008 to 2014. He is also the current captain of Chennai Super Kings in the Indian Premier League. Under his captaincy, India won the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 ICC Champions Trophy, the most by any captain. He also led India to victory in the 2010 and 2016 Asia Cup. Additionally, under his leadership, India won the 2010 and 2011 ICC Test Mace and 2013 ICC ODI Championship. Dhoni is a right-handed wicket-keeper batsman known for his calm captaincy and his ability to finish matches in tight situations. He scored over 10,000 runs in One Day Internationals and is considered one of the best finishers in the game. He is also one of the greatest wicket-keepers and captains in the history of cricket.

In Indian domestic cricket he played for Bihar and Jharkhand Cricket team. He is the captain of Chennai Super Kings (CSK) in the Indian Premier League. He captained the side to championships in the 2010, 2011, 2018 and 2021 editions of IPL league. Also under his captaincy Chennai Super Kings (CSK) Won Champions League T20 two times, in 2010 and 2014.

Dhoni made his ODI debut on 23 December 2004, against Bangladesh in Chittagong,[2] and played his first Test a year later against Sri Lanka.[3] He played his first T20I also a year later against South Africa.[4] In 2007, he took over the ODI captaincy from Rahul Dravid and he also selected as T20I captain of India in this year.[5] In 2008, he was selected as Test captain.[6] His captaincy record in Tests format was mixed, successfully leading India to a series win against New Zealand in 2008 and the Border-Gavaskar Trophy (home series in 2010 and 2013) against Australia while losing to Sri Lanka, Australia, England, and South Africa by big margins in away conditions.[7]

He announced his retirement from Tests on 30 December 2014,[8] and stepped down as captain of T20Is and ODIs in 2017. On 15 August 2020, Dhoni retired from all formats of international cricket and continues to play in the IPL.[9][10]

Dhoni received India's highest sports honour, the Major Dhyanchand Khel Ratna Award in 2008 for his outstanding achievements and the Government of India honoured him India's fourth civilian award Padma Shri in 2009 and third civilian award Padma Bhushan in 2018. He is the only cricket captain in the world to win all three of the Cricket World Cup, ICC Men's T20 World Cup and ICC Champions Trophy."""

Document2 = """In the pre-credits sequence there is a scene of the 2011 Cricket World Cup Final. MS Dhoni, India's captain, walks out to bat after Virat Kohli's wicket.

The film begins in Ranchi, 7 July 1981. At the hospital maternity unit, Paan Singh Dhoni is confused whether he has got a girl or boy. He later names his baby boy Mahendra 'Mahi' Singh Dhoni. Paan Singh is a pump operator who waters the practice ground. Fourteen years later, Mahi is spotted by a cricket coach while goalkeeping in a football game. He invites him to try out for the school cricket team as a wicketkeeper and selects him after being impressed. Mahi improves his batting and becomes a regular member of the team.

Three years later, a grown up Mahi helps win an inter-school cricket match. After achieving much fame, Mahi is selected for the Ranji Trophy but his draft notice is held up due to which he is late in reaching Kolkata despite his friends' help. But Mahi does not give up and, to please his father, he joins the Kharagpur Station as a ticket collector. Years later, Mahi's sister Jayanti is married to his friend Gautam Gupta.

After some time, Mahi is depressed with his job. With the insistence of his manager, Mahi decides to play cricket alongside his work, and after his day-shifts he goes to practice cricket. He participates in different tournaments and as a result he gets selected for the Railways. After a good performance, he tries-out for the India national under-19 cricket team selections. Bihar loses to Punjab where Yuvraj Singh scores 301 and Mahi does not succeed though he is selected for the Duleep Trophy.

Mahi leaves his job and admits to his father that cricket is his only ambition and he wants to become a professional cricketer. He works hard and is selected in the national team and makes his debut. He meets and befriends Priyanka Jha, an office consultant, and scores a century after meeting her. She buys a watch for him as a Valentine's Day gift but dies in a truck accident on her way. Mahi again goes into depression and has bad form in the 2007 Cricket World Cup. As captain of the national side, he wins the T-20 World Cup, and leads India to the number one ranking in Test matches.

In 2010, Mahi arrives at a hotel. Sakshi Singh Rawat, a hotel official fails to recognize him and later apologizes to him. They soon start dating and Mahi eventually proposes marriage to her after she mentions buying him a Valentine's Day's gift which he refuses. They marry and Mahi begins training for the 2011 World Cup. He eventually develops the team with new players. The film returns to the final where Mahi eases the pressure with a crucial innings. With 4 runs required, Mahi hits a six and India wins the final. His family, friends and coaches watching the match cry happy tears.

After the credits, the real MS Dhoni walks by the boundaries."""

corpus = [Document1,Document2]

X_train_counts = count_vect.fit_transform(corpus)

pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names(),index=['Document 1','Document 2'])

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

trsfm=vectorizer.fit_transform(corpus)
pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=['Document 1','Document 2'])

from sklearn.metrics.pairwise import cosine_similarity

cosine_similarity(trsfm[0:1], trsfm)

Document3 = """Data science is an interdisciplinary field that uses 
scientific methods, processes, algorithms and systems to extract 
knowledge and insights from noisy, structured and unstructured data,
and apply knowledge and actionable insights from data across a broad 
range of application domains. Data science is related to data mining, 
machine learning and big data."""

corpus = [Document1,Document3]

X_train_counts = count_vect.fit_transform(corpus)

pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names(),index=['Document 1','Document 3'])

vectorizer = TfidfVectorizer()

trsfm=vectorizer.fit_transform(corpus)
pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=['Document 1','Document 3'])

cosine_similarity(trsfm[0:1], trsfm)

