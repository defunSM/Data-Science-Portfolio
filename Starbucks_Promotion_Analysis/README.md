# Starbucks Promotional Analysis

# Abstract

A randomized experiment was conducted by Starbucks and the results are stored in **training.csv**. Treatment group includes customers that was exposed to the promotional material. The objective is to analyze the results of the experiment and identify both the efect on product purchase and **Net Incremental Revenue**. 

# Table of Contents

1. [Abstract](#abstract)
2. [Table of Contents](#table-of-contents)
3. [Introduction](#introduction)
4. [Materials and Methods](#materials-and-methods)
5. [Results](#results)
6. [Conclusion](#conclusion)
7. [Discussion](#discussion)
8. [References](#references)

# Introduction

The dataset resulting from the initial starbucks randomized experiment was preprocessed and examined. Upon inspection the dataset was found to be class-imbalanced. Therefore resampling methods (bootstraping) were used in order to combat the class-imbalanced dataset issue during modeling stage.

In order to investigate if the effect of the promotional material on purchases is statistically significant. A statistical hypothesis test was conducted between the treatment and control group. Since purchase is a binary feature meaning it is either "yes" or "no". It is appropriate to conduct a binomial test to evaluate the success rate between both groups with success being "yes" and failure being "no".

# Materials and Methods

The starbucks training dataset containing 80,000+ data points on customers who purchased and didn't purchase the product. Including information on if the customer was exposed to the promotional material. The sample size of treatment and control groups were roughly equal ~40,000 for each group since it was randomized. However upon inspection of the dataset the number of purchases were rather low compared to the size of the total samples. It was found that ~1000 customers purchased the product out of the total sample size ~80,000 which equates to ~0.0125% of customers buying the product.  

# Results

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

# Discussion

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# References
