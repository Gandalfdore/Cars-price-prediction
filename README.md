# Car Price Determination Project

This project aims to determine car prices using data science techniques. It involves data cleaning, exploratory data analysis (EDA), building machine learning models, and deploying a web application to predict car prices.

## Overview

The project is structured into several components:

- **Presentation document**: Showcasing the findings of the project and the methods that were used.

- **Data Cleaning**: In this phase, the dataset is processed to handle missing values, outliers, and inconsistencies.

- **Exploratory Data Analysis (EDA)**: EDA is conducted to gain insights into the relationships between different features and the target variable (car prices). Visualizations generated during this phase are stored in the `images` folder.

- **Machine Learning**: Various machine learning models are trained on the cleaned dataset to predict car prices. The models are saved in the `Models` folder.

- **Web Application**: A web application is developed to provide a user-friendly interface for predicting car prices using the trained machine learning model.

- **Synthetic data generator**: A script that uses an LLM to learn and generate more data from a dataframe.

## Repository Structure

- **Notebooks**: Contains Jupyter notebooks for different stages of the project, including data cleaning, EDA, and machine learning.

- **Data**: Contains the dataset used in the project.

- **Models**: Contains saved machine learning models.

- **Images**: Stores images generated during the EDA phase.

## Usage

Clone the repository:

   ```bash
   git clone <repository_url>
  ```

## Dependencies

    Python 3.x
    Jupyter Notebook
    Pandas
    NumPy
    Matplotlib
    Seaborn
    Scikit-learn
    Streamlit (for the web application)

## Contributors

    Boris Nedyalkov

## License
  
    This project is licensed under the MIT License.
    Acknowledgments

## Web application

   To start the web application just eneter the main directory of the project write in the console:

   ```bash
   streamlit run example_app.py
  ```
Its a calculator that takes the parameters of: ['engine-size','curb-weight','city-mpg','horsepower','highway-mpg'].
And it outputs the hypothetical price of a car with such parameters. 
Also it gives you information about how this price compares to the other prices and which brands tend to offer such priced vehicles.

## High-level plan of action

To use the above constructed prototype as a backbend of B2B application, few general steps should be observed:

 * A docker container will be created for the project
 * A script that automatically takes new data and cleans and prepares it would be created
     * optionally another script that trains and hyper-tunes the model on accumulated/new data can be constructed that periodically runs and outputs a new pickle model file
 * A script that generates the inference from the model given some data (which will be preprocessed by the previous point)
 * Finally a HTTP (Rest) API will be used to accept the queries from the user (or business), run them trough the scripts and send the inferred data back
