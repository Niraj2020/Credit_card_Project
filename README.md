# Credit Card Deafalter Prediction

## Problem Statement:
Financial threats are displaying a trend about the credit risk of commercial banks as the incredible improvement in the financial industry has arisen. In this way, one of the biggest threats faces by commercial banks is the risk prediction of credit clients. The goal is to predict the probability of credit default based on credit card owner's characteristics and payment history.

## Data Description
The client will send data in multiple sets of files in batches at a given location. The data has been extracted from the census bureau. The data contains 30000 instances with the following attributes and the dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

### Features:
1. LIMIT_BAL: continuous Credit Limit of the person.

2. SEX: Categorical: 1 = male; 2 = female

3. EDUCATION: Categorical: 1 = graduate school; 2 = university; 3 = high school; 4 = others

4. MARRIAGE: 1 = married; 2 = single; 3 = others

5. AGE-num: continuous.

6. PAY_0 to PAY_6: History of past payment. We tracked the past monthly payment records (from April to September, 2005)

7. BILL_AMT1 to BILL_AMT6: Amount of bill statements.Target Label: Whether a person shall default in the credit card payment or not.

8. PAY_BILL_AMT1 to PAY_BILL_AMT6: Amount of pay the bill statements.Target Label: Whether a person shall default in the credit card payment or not.

9. default payment next month: Yes = 1, No = 0.


## Data Preprocessing:
Before we could start building the model, we had to preprocess the data. This involved checking for missing values, removing any unnecessary features, and normalizing the data. We used pandas and scikit-learn libraries to perform these tasks.

## Exploratory Data Analysis:
Next, we performed some exploratory data analysis to gain insights into the relationships between the different features and the target variable, i.e., diabetes. We used the matplotlib and Seaborn libraries to visualize the data and understand any patterns or correlations in the dataset. We also computed some summary statistics to understand the central tendency and variability of the data.

## Model Building:
With the preprocessed data and insights from exploratory data analysis, we started building the machine learning models. We trained and test various Machine Learning Models, Random Forest and Decision tree has highest Accuracy rate which is 99% and 100%,so We choose to use a Decision Tree Machine Learning model to Predict the Credit Card Defaulters.

## Application Development
1. Built a conda Environment
2. Building and hosting a Flask web app on Azure Cloud Plateform.
3. Build the web app using Flask API
4. Install the necessary dependencies and libraries
5. Get the customer information from Web app
6. Display the prediction
7. Upload the project on GitHub
8. Create a project image using Docker hub as Containerize the app
9. Deploy the project on Azure Cloud Plateform.


## Initialize the Git Repositry
    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin <github_url>
    git push -u origin main

### To update the modification or modification on github repositry
    git add .
    git commit -m "proper message"
    git push -u origin main

## Create a file "Dockerfile" with below content
    FROM python:3.9
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    ENTRYPOINT [ "python" ]
    CMD [ "app.py" ]

 ## To Build the Docker Image on DockerHub
     docker build -t "docker_profile_name/app_name": latest .
        
 ## To run the container Image
      docker container run -d -p "port number:EX-5000" "docker_profile_name/app_name": latest

 ## To Upload the Docker Image on DockerHub
      docker push "docker_profile_name/app_name": latest

## Create a "Procfile" with following content
     web: gunicorn main:app