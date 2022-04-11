# Disaster Response Classification
In an emergency situation such as a diasaster, diasaster response workers may be flooded with new messages requesting aid. This web app is intended to classify these messages into several categories in order to help emergency workers response quicker!
### Table of Contents
---

+ [**Setup Instructions**](#instructions)
    + [**Flowchart**](#flowchart)
    + [**Motivation**](#motivation)
    + [**Preprocessing**](#preprocessing)
+ [**NLP Pipeline**](#nlp-pipeline)
    + [**Tokenization**](#tokenization)
+ [**ML Pipeline**](#ML-pipeline)
    + [**MultiOutputClassifier**](#classifier)
---
### Instructions
___
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

#### Flowchart
---
```mermaid
graph TB
    A[Text Data] -->|Tokenization| B(Transformed Text Data)
    B --> D[Machine Learning Pipeline]
    C[Labeled Output] --> |Feature Extraction| D[Machine Learning Pipeline]
    D --> |Exported Classifier| E{Multi Label Classifier}
    G[User Text Data] --> |NLP Pipeline| E
    E --> F[(New Labeled Output)]
```
#### Motivation
---
In an emergency situation such as a diasaster, diasaster response workers may be flooded with new messages requesting aid. This web app is intended to classify these messages into several categories in order to help emergency workers response quicker!

As such this project utilizes both a [NLP pipeline](#nlp-pipeline) as we are dealing with text data and a [ML pipeline](#ml-pipeline) to optimize our classifier. 

#### Preprocessing
----

---
### NLP pipeline
---
process_data.py, write a data cleaning pipeline that:

    Loads the messages and categories datasets
    Merges the two datasets
    Cleans the data
    Stores it in a SQLite database


#### Tokenization
---
### ML pipeline
---
train_classifier.py, write a machine learning pipeline that:

    Loads data from the SQLite database
    Splits the dataset into training and test sets
    Builds a text processing and machine learning pipeline
    Trains and tunes a model using GridSearchCV
    Outputs results on the test set
    Exports the final model as a pickle file


#### MultiOutputClassifier
---