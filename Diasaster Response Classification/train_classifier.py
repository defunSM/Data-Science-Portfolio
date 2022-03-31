"""
    ML Pipeline

    train_classifier.py, machine learning pipeline that:

    Loads data from the SQLite database
    Splits the dataset into training and test sets
    Builds a text processing and machine learning pipeline
    Trains and tunes a model using GridSearchCV
    Outputs results on the test set
    Exports the final model as a pickle file
    
    Example Usage: python train_classifier.py ../data/DisasterResponse.db classifier.pkl

"""
# import libraries
import numpy as np
import pandas as pd
import sys
from sqlalchemy import create_engine
import nltk
import joblib

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

import re

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier

from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

from sklearn.neighbors import KNeighborsClassifier



def load_data(filepath):
    
    # Reading from the database
    engine = create_engine('sqlite:///' + filepath)
    df = pd.read_sql_table(filepath)
    
    # Setting up the X and Y dataframes
    X = df.iloc[:,1].dropna()
    Y = df.iloc[:,4:]

def tokenize(text):
    
    clean_tokens = []
    
    # lowercasing and removing punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower().strip())
    tokens = word_tokenize(text)
    # Remove stop words + stem
    stemmer = PorterStemmer()
    
    
    stop_words = stopwords.words("english")
    clean_tokens = [ stemmer.stem(word) for word in tokens if word not in stop_words]

    return clean_tokens

def model_data():
    pass

def main():
    pass

if __name__ == '__main__':
    pass
