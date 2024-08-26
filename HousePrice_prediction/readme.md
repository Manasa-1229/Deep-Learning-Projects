# House Price Prediction Project

This project involves building and evaluating various machine learning models to predict house prices using the Ames Housing dataset. The dataset is sourced from [Ames Housing Dataset](http://jse.amstat.org/v19n3/decock/AmesHousing.txt), which includes detailed information on various properties in Ames, Iowa. The goal of this project is to explore different regression techniques and determine which model best predicts house prices.

## Repository Structure
```
/House_Price_Prediction
│
├── BigData_House_price.ipynb # Jupyter notebook containing data analysis, model training, and evaluation
├── Housing_LR.pkl # Saved model: Linear Regression
├── Housing_Lasso.pkl # Saved model: Lasso Regression
├── Housing_Poly.pkl # Saved model: Polynomial Regression
├── Housing_RandomForest.pkl # Saved model: Random Forest Regression
├── Housing_Ridge.pkl # Saved model: Ridge Regression
├── Housing_poly2.pkl # Saved model: Another Polynomial Regression model with different parameters
└── readme.md # Project documentation (this file)

```


## Project Description

This project uses the Ames Housing dataset to build and evaluate multiple regression models to predict house prices. The following models are trained and compared:

- **Linear Regression** (`Housing_LR.pkl`)
- **Lasso Regression** (`Housing_Lasso.pkl`)
- **Polynomial Regression** (`Housing_Poly.pkl`, `Housing_poly2.pkl`)
- **Ridge Regression** (`Housing_Ridge.pkl`)
- **Random Forest Regression** (`Housing_RandomForest.pkl`)

### Key Steps in the Notebook

1. **Data Preprocessing**:  
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling

2. **Model Training and Evaluation**:  
   - Training the above models on the preprocessed dataset
   - Evaluating models based on performance metrics like RMSE (Root Mean Squared Error), R², etc.
   - Saving the trained models for future predictions

3. **Model Comparison**:  
   - Comparing model performance to determine the most effective model for house price prediction.

## Dataset Information

The dataset used in this project is the Ames Housing dataset, which provides comprehensive details on housing features and prices in Ames, Iowa. This dataset is a popular alternative to the Boston Housing dataset and provides a more challenging prediction problem due to the complexity and diversity of the housing data.

## Acknowledgements

Special thanks to the creators of the Ames Housing dataset and the authors of the machine learning libraries utilized in this project.


