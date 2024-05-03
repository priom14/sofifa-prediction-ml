# EAFC24 Player Market Value Prediction

This project aims to predict the market value of FIFA players using machine learning techniques. The data is scraped from Sofifa, a popular website that provides comprehensive information on football players avilable on EAFC24.

## Overview

The project consists of the following steps:

1. **Data Collection**: Scraping player data from Sofifa using web scraping techniques.
2. **Data Preprocessing**: Cleaning and preparing the scraped data for analysis.
3. **Feature Engineering**: Creating relevant features to improve model performance.
4. **Model Selection**: Trying out different machine learning models and selecting the best-performing one.
5. **Model Training**: Training the selected model on the prepared data.
6. **Model Evaluation**: Evaluating the model's performance using appropriate metrics.
7. **Deployment**: Making the trained model accessible for market value predictions.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/priom14/sofifa-prediction-ml.git

```

2. Install the required dependencies:

To run the project, you need the following dependencies:

- Python 3.9
- Flask
- Beautiful Soup
- scikit-learn
- pandas
- numpy

You can install these dependencies using pip:

```bash
pip install -r requirments.txt

```

## Usage
1. Run the Flask application:

```bash
python app.py

```
2. Access the application in your web browser at http://127.0.0.1:5000/


## Project Structure

The project directory is structured as follows:

- `app.py`: Main Flask application file.
- `src/`: Contains source code files.
  - `pipeline/`: Custom data pipeline and prediction model.
    - `prediction_pipieline.py` : Contains the necessary pipielines for prediction.
  - `components/`: Contains all the data related wokrs.
    - `data_ingestion.py`: Process of data ingestion.
    - `data_transformation.py`: Process of ingested data transformation.
    - `model_trainer.py` : Model training.
  - `execption.py` : Execpetion Handling.
  - `logger.py` : Codes for Logging.
  - `utils.py`:  Necessary codes to be used overall.
- `templates/`: HTML templates for the web application.
- `setup.py`: For setting up the project.


## Acknowledgements

- The Sofifa website for providing valuable player data.