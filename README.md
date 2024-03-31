# Real Estate Price Prediction Capstone Project Summary

This project explores the application of data science techniques for real estate price prediction in the Gurgaon area.

## Data Collection and Preparation:

- Raw data was used gathered by scraping real estate listings from the 99acres website, along with exploration of other property listing platforms.
- The collected data underwent meticulous cleaning to address missing values and inconsistencies. Information on houses and flats was merged into a unified dataset.
- Feature engineering techniques were employed to enrich the data and create new features that provide a more detailed representation of the properties. Examples include additional room indicators, area with type specifications, and age of possession.
- Exploratory Data Analysis (EDA) was conducted using techniques like Pandas Profiling to understand the data distribution, identify patterns, and uncover relationships between various features.

## Model Building and Evaluation:

- Feature selection methods like correlation analysis and feature importance analysis were used to identify the most relevant features for price prediction. Techniques like removing highly correlated features and leveraging Random Forest's feature importance were considered.
- XGBoost, a gradient boosting regression model, was trained on the prepared data and achieved the best accuracy in predicting property prices. Other regression models have also been explored during the project. XGBoost performed the best.
- The model was evaluated on unseen data using metrics like R-squared and Mean Squared Error (MSE). This assessment helps gauge the model's effectiveness in predicting property prices.
- Missing value imputation techniques like deletion, mean/median imputation were explored to address missing values in the data.

## Building the Price Prediction Pipeline:

The project outlines the steps involved in creating a real estate price prediction model:
1. Data preprocessing
2. Model selection (XGBoost in this case)
3. Model training
4. Model evaluation
5. Model selection and refinement 

Streamlit is being used to develop a user-friendly web application. This application will allow users to interact with the model and potentially predict property prices based on user-provided features.


## Deployment on AWS:

Amazon Web Services (AWS) is used to deploy the web application. This ensures scalability to accommodate increasing user traffic and maintain accessibility for users from various locations.


## Performance with Streamlit
[Link of the website:] (http://35.170.202.251:8501/)

[Book Recommendor Demo Video](https://youtu.be/sNNPdjwtsyc?si=gfsHSQoA-2t8lerJ)
Some of the screenshots of our Web application are below:
![ Website screenshot](webscreenshots/Homepage.png)
![](webscreenshots/dataAnalysis.png)
![](webscreenshots/dataAnalysis2.png)
![](webscreenshots/priceprediction.png)
![](webscreenshots/Recommender.png)



# How to use
1. Clone the repository:
   ```bash
   git clone (https://github.com/ravina029/book-recommendor)

2. run the command 
   streamlit run website/Homepage.py
 


# Deployed Streamlit app on EC2 instance

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone https://github.com/ravina029/RealEstateProject.git
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```

```bash
#Temporary running
python3 -m streamlit run website/Homepage.py
```

```bash
#Permanent running
nohup python3 -m streamlit run website/Homepage.py
```

Note: Streamlit runs on this port: 8501


Overall, this project showcases the power of data science in real estate price prediction. By leveraging data collection, cleaning, feature engineering, model building with XGBoost achieving the best accuracy, and deployment on a cloud platform, the project aims to create a valuable tool for users to gain insights into the Gurgaon real estate market.

