# Starbucks Promotional Analysis

<p align="center"><img src="https://opj.ca/wp-content/uploads/2018/02/New-Starbucks-Logo-1200x969.jpg" width="300" height="300"></p>


# 1. Abstract

A randomized experiment was conducted by Starbucks and the results are stored in **training.csv**. Treatment group includes customers that was exposed to the promotional material. The objective is to analyze the results of the experiment and identify both the efect on product purchase and **Net Incremental Revenue**. 

# 2. Table of Contents

1. [Abstract](#abstract)
2. [Table of Contents](#table-of-contents)
3. [Introduction](#introduction)
4. [Materials and Methods](#materials-and-methods)
5. [Results](#results)
6. [Correlation Matrix](#correlation-matrix) 
7. [Hypothesis Test](#hypothesis-test)
8. [Model](#model)
9. [Conclusion](#conclusion)
10. [Discussion](#discussion)
11. [References](#references)

# 3. Introduction

The dataset resulting from the initial starbucks randomized experiment was preprocessed and examined. Upon inspection the dataset was found to be class-imbalanced. Therefore resampling methods (bootstraping) were used in order to combat the class-imbalanced dataset issue during modeling stage.

In order to investigate if the effect of the promotional material on purchases is statistically significant. A statistical hypothesis test was conducted between the treatment and control group. Since purchase is a binary feature meaning it is either "yes" or "no". It is appropriate to conduct a binomial test to evaluate the success rate between both groups with success being "yes" and failure being "no".

The analysis of the Incremental Response Rate (IRR) and the Net Incremental Revenue (NIR) was conducted in order to investigate if the promotional would yield potential profit. Specifically if the cost of the promotion be made up with purchases by the customer. 

# 4. Materials and Methods

The starbucks training dataset containing 80,000+ data points on customers who purchased and didn't purchase the product. Including information on if the customer was exposed to the promotional material. The sample size of treatment and control groups were roughly equal ~40,000 for each group since it was randomized. However upon inspection of the dataset, the number of purchases were rather low compared to the size of the total samples. It was found that ~1000 customers purchased the product out of the total sample size ~80,000 which equates to ~0.0125% of customers buying the product.  

# 5. Results
### 5.1 Correlation Matrix

![](https://i.imgur.com/NiJUzjQ.png)
A 0.043 correlation coefficient between promotion and purchase which is higher than the other features. V4 feature seems to affect purchasing decision. Thus leveraging this we can say looking at V4 will be helpful in swaying customers to purchase.

### 5.2 Hypothesis Test

![Figure 1](https://i.imgur.com/zQcubTS.png)

There was statistically significant difference in the probability of purchase between the treatment and control group. The treatment group had a **~1.7%** probability of purchase which was roughly **~1%** higher than the control group. 

### 5.3 Model

When training the model there was a lot of variance found when retraining. The highest IRR and NIR Achieved was 0.05 and 21.75 while some of the lowest was 0.01 and -1200.

# 6. Discussion

The randomized experiment by starbucks indicated that simply exposing the promotional material to customers would not result in positive revenue as the cost of showing the promotion would overtake that of the revenue earned. Thus a more efficient promotional strategy would need to be developed.

While the best model was found to be better then the IRR and NIR of the training dataset it can further be improved. Other methods to look into potentially is better imbalanced data handling. Purhaps feature engineering could be implemented or better data can be used. We could also improve our model accuracy just by hacking around with the random state as there is a lot of variance with our model.

# 7. Conclusion



One way to improve the model is to conduct another randomized experiment targeting customers that have higher V3 as that was found to be highly correlated with purchasing.

# References
