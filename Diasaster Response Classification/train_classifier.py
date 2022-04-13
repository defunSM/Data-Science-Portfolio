"""
    ML Pipeline

    train_classifier.py, machine learning pipeline that:

    Loads data from the SQLite database
    Splits the dataset into training and test sets
    Builds a text processing and machine learning pipeline
    Trains and tunes a model using GridSearchCV
    Outputs results on the test set
    Exports the final model as a pickle file
    
    Example Usage: python train_classifier.py data/DisasterResponse.db classifier.pkl

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

def under_sampling_multilabel(df, y_feature_index=1, samples=200):
    """This is an undersampling function for multilabel data.
       Part of this code is used to make a transformer to be used in a
       ml pipeline 

    Args:
        df (Dataframe): The imbalanced dataframe
        ---
        y_feature_index (int, optional): indexing where the independent features begin for the dataset. 
        
        Example: Imagine a simple dataset with columns ['age', 'smoker', 'college student']
        
        If trying to predict smoker and college student using the age column then y_feature_index should be 1
        ----
        samples (int, optional): The number of samples for each category. Defaults to 200.

    Returns:
        Dataframe: Returns an undersampled dataset using sample
    """
    print("Applying undersampling...")
    
    df_resampled = []
    
    # Adding samples if the categatory matches.
    # IMPROVEMENT: This process can be improved
    # by trying to also not select categories that were
    # already added in. This way you don't accumulate extra
    # samples. This is the reason why the sample is kept low.
    
    for i in df.iloc[:,y_feature_index:].columns:
        new_df = df[df[i]==1]
        #print(new_df.shape)
        df_resampled.append(new_df.sample(200, replace=True))
        
    df = pd.concat(df_resampled)
    print(df.shape)
    
    return df

def load_data(db_filepath):
    """ Loads the features from the database into dataframes needed to train the ML model

    Args:
        db_filepath (string): Path to the disaster database created by process_data.py

    Returns:
        X: Dataframe of the messages column from the database
        Y: Dataframe of the different kind of disaster categoires
        col_names: List of category names
    """
    # Reading from the database
    engine = create_engine('sqlite:///' + db_filepath)
    df = pd.read_sql_table(db_filepath, engine)
    
    # Drop child_alone since there are no samples for it and so
    # it doesn't make sense to predict for it if there are no samples
    try:
        df.drop(['child_alone'], axis=1, inplace=True)
    except:
        pass
    
    # Applying underSampling
    df = under_sampling_multilabel(df, y_feature_index=4, samples=200)
    
    # Setting up the X and Y dataframes
    X = df.iloc[:,1].dropna()
    Y = df.iloc[:,4:]
    col_names = Y.columns.unique()
    
    return X, Y, col_names

def tokenize(text):
    """Performs preprocessing on text so that it can be used in the ML model

    Args:
        text (string): Takes text from the database column 'messages'.

    Returns:
        clean_tokens: Words that have been stemmed, lowercased, removed of punctuation and stop words.
    """
    clean_tokens = []
    
    # lowercasing and removing punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower().strip())
    tokens = word_tokenize(text)
    # Remove stop words + stem
    stemmer = PorterStemmer()
    
    
    stop_words = stopwords.words("english")
    clean_tokens = [ stemmer.stem(word) for word in tokens if word not in stop_words]

    return clean_tokens

def ml_pipeline():
    # Creating ml pipeline
    pipeline = Pipeline([
        ('count-vector', CountVectorizer(tokenizer=tokenize)),
        ('tf-idf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier(), n_jobs=-1))
    ])
    
    return pipeline

def classification_model_report(model, X_test, Y_test, col_names):
    
    Y_pred = model.predict(X_test)
    print(classification_report(Y_test, Y_pred, target_names=col_names))

def save_model(model, model_filepath):
    # Export the model as a pickle file
    joblib.dump(model, model_filepath)

def main():

    if len(sys.argv) == 3:
        db_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(db_filepath))
        X, Y, col_names = load_data(db_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = ml_pipeline()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        classification_model_report(model, X_test, Y_test, col_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
