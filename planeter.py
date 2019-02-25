#https://www.youtube.com/watch?v=XfnqBnOA-7I&index=7&list=PLA-CsqNypl-SzVcegxi5mJRz-iqF-nsgT

import numpy as np

import pandas as pd
from keras import layers

dataset = pd.read_csv(r'C:\Users\Inception\PycharmProjects\FIRSTproject\Datasets\Restaurant_Reviews.tsv',delimiter='\t', quoting=3)

import re
import nltk
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords  #collection of text
corpus=[]
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review=review.lower()
    review= review.split()
    ps=PorterStemmer()
    review= [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)

print(corpus)

from keras.models import Model
from keras.layers import Input, Dense
# Input - Layer
Model.add(layers.Dense(50, activation = "relu", input_shape=(10000, )))
# Hidden - Layers
Model.add(layers.Dropout(0.3, noise_shape=None, seed=None))
Model.add(layers.Dense(50, activation = "relu")
Model.add(layers.Dropout(0.2, noise_shape=None, seed=None))
Model.add(layers.Dense(50, activation = "relu"))
# Output- Layer
Model.add(layers.Dense(1, activation = "sigmoid"))model.summary()
Model.summary()
