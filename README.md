This repository contains a machine learning model for predicting COPD diagnosis in Nepal, using patient data and various risk factors.

COPD Prediction in Nepal This repository contains a machine learning project focused on predicting Chronic Obstructive Pulmonary Disease (COPD) diagnosis in Nepal. The project utilizes patient data and various risk factors to develop a predictive model for early identification and potential intervention strategies.

Data Source and Structure The dataset used in this project was obtained from online different websites, social media, ministry of health and population. It consists of the following features:

Demographic information: Age, Gender Lifestyle factors: Smoking Status, Biomass Fuel Exposure, Occupational Exposure Medical history: Family History of COPD, Respiratory Infections in Childhood Health indicators: BMI Environmental factors: Location, Air Pollution Level Target variable: COPD Diagnosis (binary: 0 = No COPD, 1 = COPD) The dataset contains no missing values, and categorical features have been appropriately encoded for model training.

Model Prediction A logistic regression model was trained on the dataset to predict COPD diagnosis. The model achieved the following performance metrics on the test set:

Accuracy: 98% Precision: 97% Recall: 97% F1-Score: 97% These results indicate the model's strong predictive capability, suggesting that the selected features are informative for identifying individuals at risk of COPD in the Nepalese population.

Project Structure COPD_Data_Nepal.csv: The dataset used for analysis. COPD_Prediction_Notebook.ipynb: Jupyter Notebook containing the data exploration, preprocessing, model training, and evaluation. requirements.txt: List of required Python packages. README.md: This file providing an overview of the project. How to Run the Project Clone the repository. Install the required packages: pip install -r requirements.txt Open and run the COPD_Prediction_Notebook.ipynb in Jupyter Notebook or a compatible environment. Potential Impact This project has the potential to contribute to the early identification and management of COPD in Nepal, leading to improved patient outcomes and reduced disease burden. The developed model could be integrated into healthcare systems to assist in risk assessment and guide intervention strategies.

Future Work Explore additional machine learning algorithms and feature engineering techniques to further improve model performance. Validate the model on a larger, independent dataset to assess its generalizability. Develop a user-friendly interface or application to facilitate the use of the model in clinical settings. Acknowledgments

Mention any individuals or organizations that contributed to the project or provided the dataset. Contact For any questions or collaborations, please contact rmh.awasthi@gmail.com.
