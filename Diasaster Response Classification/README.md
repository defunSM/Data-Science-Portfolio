# Disaster Response Classification

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

```mermaid
graph TB
    A[Text Message] -->|Tokenization| B(Transformed Text Message)
    B --> D[Machine Learning Pipeline]
    C[Labeled Output] --> |Feature Extraction| D[Machine Learning Pipeline]
    D --> |Exported Classifier| E{Multi Label Classifier}
    G[User Input Text Messages] --> |NLP Pipeline| E
    E --> F[(New Labeled Output)]
```
