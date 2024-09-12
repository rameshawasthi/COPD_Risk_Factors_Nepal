#### COPD Risk Factors in Nepal: Machine Learning Prediction Model

This repository focuses on predicting Chronic Obstructive Pulmonary Disease (COPD) diagnosis in Nepal using a machine learning model. The project leverages patient data and various risk factors for early identification, potentially aiding in timely intervention and management of COPD in Nepal.

Data Source and Structure:
•	Sources: The data was obtained from a variety of online sources including research articles, social media, the Ministry of Health and Population of Nepal, and health-related sites such as Open Data Nepal.
•	Features:
o	Demographics: Age, Gender
o	Lifestyle factors: Smoking Status, Biomass Fuel Exposure, Occupational Exposure
o	Medical history: Family History of COPD, Respiratory Infections in Childhood
o	Health indicators: BMI
o	Environmental factors: Location, Air Pollution Level
o	Target variable: COPD Diagnosis (binary: 0 = No COPD, 1 = COPD)
No missing values were present, and categorical features were encoded for model training.
Model and Performance:
•	A Logistic Regression model was used to predict COPD diagnosis.
•	Performance metrics:
o	Accuracy: 
o	Precision: 
o	Recall: 
o	F1-Score: 
The results demonstrate strong predictive performance, suggesting the chosen features are effective for identifying individuals at risk of COPD in Nepal.
Project Structure:
•	COPD_Data_Nepal.csv: Dataset for analysis.
•	Final_Project_COPD_NEPAL.ipynb: Contains data exploration, preprocessing, and model training.
•	requirements.txt: Python package dependencies.
•	README.md: Overview of the project.

How to Run:
1.	Clone the repository.
2.	Install required packages: pip install -r requirements.txt.
3.	Run the Jupyter Notebook: COPD_Prediction_Notebook.ipynb.
   
Potential Impact:
This project can assist in the early identification and management of COPD in Nepal, improving patient outcomes and reducing disease burden. The model could be integrated into healthcare systems for risk assessment and guiding interventions.

Future Work:
•	Explore other machine learning algorithms and feature engineering techniques.
•	Validate the model on larger datasets for improved generalizability.
•	Develop a user-friendly interface for clinical use.
Data Sources:
•	Ministry of Health and Population, Nepal
•	Open Data Nepal
•	ResearchGate: Age-standardized death rates of COPD in Nepal 
For any inquiries, contact: rmh.awasthi@gmail.com.

