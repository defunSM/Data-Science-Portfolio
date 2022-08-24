## Project Definition
### Project Overview

In the gaming industry many games experience a sharp decline in player activity after their initial launch as players move on to other games. We want to be able to forecast and identify which games will continue to see growth or decline. Our datasets will consist of the 5 most currently played games on Steam as of June 2022 which are Lost Ark, Counter-Strike, Dota 2, ARK, and Apex Legends. The data will be collected from https://steamdb.info which are time series csv files.

### Problem Statement

How to build a performant predictive model from univariate time series data? In order to approach this one way to begin is to determine the time series characteristics of our datasets such as trend, seasonality, noise, and stationary. Afterwards we can use some common time series models like ARIMA, LSTM and FB Prophet for forecasting and use metrics to evaluate their performance.

### Metrics

In order to evaluate the performance of the models we will be using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) as metrics to evaluate our regression models. The RMSE will give us an idea of the standard deviation of the residuals, aka how far from the line of best fit the data points are. The MAE metric refers to the difference between the observation and the true value which will help determine the accuracy of the models. 


## Table of Contents
---

- [Project Definition](#project-definition)
- [Setup](#setup)
- [Exploration and Visualizations](#project-exploration-and-visualizations)
- [Conclusion](#conclusion)

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

## Conclusion