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

Overview provided by article: https://medium.com/@salmanhossain500/what-you-need-to-know-about-airbnb-in-nyc-92ab935144f6 

## Features of the Dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Latitude and Longitude** - Geographical location of the property

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Prop_Type** - The type of property as Private Room, Entire House

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Min_Nights** - Minimum nights of stay

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Host_Listing_Cnt** - How long they have listed it

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Days_Available** - Availability of property in days

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Review_Cnt** - Count of reviews in the property

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reviews30d** - Activeness of reviews/ how many reviews have been posted in 30 days

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Price** - What is the market price they are askin for

## Insights

### 1. Correlation Matrix

![](https://cdn-images-1.medium.com/max/800/1*7_cx9RQ7FUKH7qxasR6lRw.png)

From this correlation matrix we can gather the different linear of relationships that may exist between the features. The strongest relationship seems to be between Min_Nights and Host_Listing_Cnt suggesting that as the greater number of minimum nights required by the listing the longer that listing is available for. So having lower minimum nights correlates to less time the property is listed on airbnb.

### 2. Box and Whiskers Plot

![](https://cdn-images-1.medium.com/max/800/1*TXYCO3zJm_66nGt4IwoleA.png)

From the box and whiskers plot we can see the median prices grouped by the different boroughs. From this graph we can extract a few things such as entire homes typically have more variance in their pricing than the other property types.

### 3. Scatter Plot

![](https://cdn-images-1.medium.com/max/800/1*iJT3Oz77s5DmrHZesdFwNQ.png)

Private rooms tend ot have a steeper drop in price which makes sense since most people would not want to pay more when they could just get an entire home listing. This is indicated when seeing how right skewed the Private room is compared to Enitre home

## Libraries
- Numpy
- Pandas
- Sklearn
- XGBoost

## Credits:
Dataset from https://www.kaggle.com/sarthakniwate13/air-bnb-nyc-data
