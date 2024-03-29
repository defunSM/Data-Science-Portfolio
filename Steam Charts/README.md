## Project Definition
### Project Overview

In the gaming industry many games experience a sharp decline in player activity after their initial launch as players move on to other games. We want to be able to forecast and identify which games will continue to see growth or decline. Our datasets will consist of the 5 most currently played games on Steam as of June 2022 which are Lost Ark, Counter-Strike, Dota 2, ARK, and Apex Legends. The data will be collected from https://steamdb.info which are time series csv files.

The meat of this project are in `notebooks/eda.ipynb` which contains all of the exploratory data analysis and `notebooks/models.ipynb` which contains the the different models used to forecast player activity. There is also a [medium post](https://medium.com/@salmanhossain500/forecasting-player-activity-for-apex-legends-using-time-series-data-b874495f51a2) which tries to summarize the findings and thought process behind them.

### Problem Statement

How to build a performant predictive model from univariate time series data? In order to approach this one way to begin is to determine the time series characteristics of our datasets such as trend, seasonality, noise, and stationary. Afterwards we can use some common time series models like ARIMA, LSTM and FB Prophet for forecasting and use metrics to evaluate their performance.

### Metrics

In order to evaluate the performance of the models we will be using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) as metrics to evaluate our regression models. The RMSE will give us an idea of the standard deviation of the residuals, aka how far from the line of best fit the data points are. The MAE metric refers to the difference between the observation and the true value which will help determine the accuracy of the models. 


## Table of Contents

- [Project Definition](#project-definition)
- [Setup](#setup)
- [Exploration and Visualizations](#project-exploration-and-visualizations)
- [Models](#models)
- [Conclusion](#conclusion)
- [Sources](#sources)

## Setup

    pip install -r requirements.txt

## Exploration and Visualizations
Summary Statistics providing a general overview of the dataset for both players and twitch viewers for Apex Legends.

![](/Steam%20Charts/visualizations/summary_statistics.png)

The violin plot and line plot below indicates that most players play on Saturday around 3-4 PM.
![](/Steam%20Charts/visualizations/players_distribution.png)
![](/Steam%20Charts/visualizations/players_time.png)

Plots of player activity and twitch viewers for Apex Legends in the month of June.
![](/Steam%20Charts/visualizations/players_june.png)

The simple moving average has a trend line that has an indirect relationship. The slope of the trendline for the simple moving average is -11.4 and with a y-intercept of ~184000.

![](/Steam%20Charts/visualizations/players_trend.png)

Below is a breakdown of the characteristics of the time series data into its components (trend, seasonal, residuals).

![](/Steam%20Charts/visualizations/players_decomposition.png)

## Models

### Naive Model
The naive model assumes that the forecasted player activity will be whatever the last previous activity. This is not a good model and is only meant to serve as a baseline model for the FB Prophet and AutoRegression model. The model has about a ~22% accuracy with a RMSE of ~59000. 

![](/Steam%20Charts/visualizations/naive_model.png)

### FB Prophet Model
The FB Prophet model is an automated forecasting model meant for usage in real world business applications. The model does rather well with an accuracy of 87% and RMSE of ~19000. A huge improvement from the naive model. Some observations from the prediction made by FB Prophet seems to overexagerate the dips in player activity. One of the benefits of this model is that it works without knowing any characteristics of the univariate data.

![](/Steam%20Charts/visualizations/fbprophet_model.png)

### AutoRegression Model
In an autoregression model forecasts are made by using linear combinations of past values. The characteristics of the past values are decomposed into components such as trend, seasonal, and residuals. As such this model benefits from having prior information such as the period or likely cyclic behavior. The autoregression model outperformed the other models with a 91% accuracy and ~17000 RMSE.  

![](/Steam%20Charts/visualizations/autoregression_model.png)

## Conclusion

Three models was created in order to forecast player activity. The naive model which served as the baseline on evaluating the other models. The FB Prophet model which was developed by Facebook for real world business applications. Last but not least the autoregression model which was developed for univariate data with known characteristics such as period, trend, and seasonality. 

The FB Prophet model does rather well considering there is no hyperparameter tuning involved and no prior information about the characteristics of the univariate data is needed. The accuracy of the model is 87% with RMSE ~19120. One noticable trend in the FB Prophet model is the exageration of the down trends. 

While the FB Prophet model does well it does not beat the performance of the autoregression model. The autogression model does have a downside which requires a solid understanding of the underlying data. Whereas the FB Prophet model did not require us to understand any of the data. This can also be a con for FB Prophet model is that it is more difficult to explain as it takes a additive approach.

The autoregression model is a more intuitive model and easier to understand. Similar to linear regression the univariate data is decomposed into linear combinations and thus one advantage is the model is more explainable. The disadvantage is that this model while more performant than any of the other models does require some knowledge on the data. 

Throughout creating these models the most difficult aspect was the autoregression model since it required an extensive amount of exploratory data analysis beforehand. Another challenge is dealing with univariate data means that the values are dependent on each other and not independent unlike other types of datasets. This means that normal cross validation techniques can not be used.

## Sources

FB Prophet - https://github.com/facebook/prophet

AutoRegression - https://otexts.com/fpp2/AR.html