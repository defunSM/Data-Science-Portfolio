# New York City Airbnb Dataset

## Table of Contents
**[Setup](#setup)**<br>
**[Motivation](#motivation)**<br>
**[Features of the Dataset](#features-of-the-dataset)**<br>
**[Insights](#insights)**<br>
**[Libraries](#libraries)**<br>
**[Credits](#credits)**<br>

## Setup

### 1. To get started install the requirements using pip

```
pip install -r requirements.txt
```
### 2. Content of the files

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Airbnb_NYC.csv** - is the NYC airbnb dataset (Features are described below)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NYC_airbnb.ipynb** - contains the data exploratory data analysis (graphs and other visualizations)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**classification_models_to_predict_borough.ipynb** - models to predict the borough of an airbnb listing

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**classification_models_to_predict_property_type.ipynb** - Predicting the property type

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**helpers.py** - contains helper functions used in the other files for scoring the models, etc.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**requirements.txt** - required python packages needed to run the files 


## Motivation
The motivation for examining this data set is to see what kind of insights we can extract to help answer the following questions below:

Questions answered by this dataset:
  1. **What is a fair price for an airbnb?** $150 for Entire Home, $75 for Private Room and $45 for Shared Room
  2. **Which borough has the highest or lowest prices per night?** Manhattan
  3. **What kind of properties are rented out the most?** Entire Homes
  4. **What kind of price point have the most reviews?** Most of the reviews are on properties priced around the median**
  5. **Is there a relationship between the number of reviews and the price?** Slight positive correlation between reviews and price
    - 

## Features of the Dataset

**Latitude and Longitude** - Geographical location of the property

**Prop_Type** - The type of property as Private Room, Entire House

**Min_Nights** - Minimum nights of stay

**Host_Listing_Cnt** - How long they have listed it

**Days_Available** - Availability of property in days

**Review_Cnt** - Count of reviews in the property

**Reviews30d** - Activeness of reviews/ how many reviews have been posted in 30 days

**Price** - What is the market price they are askin for

## Insights



## Libraries
- Numpy
- Pandas
- Sklearn
- XGBoost

## Credits:
Dataset from https://www.kaggle.com/sarthakniwate13/air-bnb-nyc-data
