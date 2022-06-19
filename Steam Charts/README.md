## Project Definition
### Project Overview

In the gaming industry many games fail after their initial launch as players begin to decline while other games thrive and prosper. We want to be able to forecast and identify which games will continue to see growth or decline. Our datasets will consist of the 5 most currently played games on Steam as of June 2022 which are Lost Ark, Counter-Strike, Dota 2, ARK, and Apex Legends. The data will be collected from https://steamdb.info which are time series csv files.

### Problem Statement

How to build a performant predictive model from univariate time series data? In order to approach this one way to begin is to determine the time series characteristics of our datasets such as trend, seasonality, noise, and stationary. Afterwards we can use some common time series models like ARIMA, LSTM and FB Prophet for forecasting and use metrics to evaluate their performance.

### Metrics

In order to evaluate the performance of our models we will be using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) as metrics to evaluate our regression models.


## Table of Contents
---

- [Project Definition](#project-definition)