
## 1. Buisiness problem
Health care fraud  is a huge problem in the United States. As the FBI website notes, health care fraud is not a victimless crime and it causes tens of billions of dollars in losses each year. It can raise health insurance premiums, expose you to unnecessary medical procedures, and increased taxes. In this project, I will predict the potentially fraudulent providers based on providers claims. The dataset for this analysis is from [Kaggle](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis/data). It contians infromation about claims and beneficiary information for several patients and providers.

## 2. Exploratory data analysis (EDA) 
As expected the data is heavily unabalanced with a lot more providers who have not commited fraud than those who did commit fraud by a factor of 9 with 506 out of 5410 providers potentially commiting fraud. From the beneficiaries datase, it is clear and that the most of the beneficiaries were covered for the entire 12 months in an year and a large percentage of them have chronic conditions.Furthermore we can can look at procedure codes and diagnostic codes for the inpatient and outpatient claims and extract the top100 most common codes as features to improve our prediction of fraudulent providers. A word cloud of the procedure codes for in patient claims is shown below.
<img title="Out patient Claim diagnostic codes" alt="Alt text" src="/images/ClaimsDiagnosisOutpatient.png">
An important feature in prediction of fraduent providers could be the days of stay at the hospital for in_patient claims which is shown in the figure below.
<img title="Days spent in Hosptial for in patients" alt="Alt text" src="/images/DaysInHospital.png">

## 3. Data cleaning and Preperation
Since some of the variables are categorical, we need to convert them currently as strings to categorical variables. Furthermore, a lot of variables on the patient conditions are further converted into Boolean to be used as features for the machine learnign algorithms.  Additionally we can look at in-patient and out-patient claim process times as features. We extract the top 100 diagnosis codes and procedure codes for  in_patient and out_patient claims from the claims data. Since, we are provided with the beneficiary and claims data and we are interested  in the classification of providers, we first join the claim data with the beneficiary, and group the joined data by providers. We then use the aggregated information from providers as features for our machine learning classification models.

## 4. Modeling & Optimization
We then split the data into trainig and test set and aim to fit the following machine on the train data features:
    1. Linear SVM
    2. Logistic regression
    3. Random Forest
    4. XGBoost
    5. CatBoost 
    6. K-nearest neighbors
Furthermore we use either grid search or randomized search along with cross-validation for choosing the optimal set of hyperparameters for the above classifiers. We then save the model with the optimal set of hyperparameters.

## 5. Evaluation
We evaluated the best models with optimal set of hyperparameters  for each classifier tested on the hold-out test data. The ROC curves which plot the false-positive rates and the true-positive rates for serveral thresholds as well as the precision-recall curves are shown for all the classifiers. Furthermore, the classifiers are evaluated in several metrics including, accuracy, recall, precision, F1-score, AUC for the ROC curve.
<img title="ROC Curves" alt="Alt text" src="/images/ROCCurve.png" width="100%">
<img title="Precision-Recall Curves" alt="Alt text" src="/images/PRCurve.png" width="100%">

|           Classifier | F1 Score |Precision |  Recall  | Accuracy |   AUC    |
|  ------------------- | -------- | -------- | -------- | -------- | -------  |
|                  SVM | 0.564885 | 0.860465 | 0.420455 | 0.943170 | 0.875534 |
|  Logistic Regression | 0.438889 | 0.290441 | 0.897727 | 0.798604 | 0.913736 |
|        Random Forest | 0.577778 | 0.829787 | 0.443182 | 0.943170 | 0.960463 |
|              XGBoost | 0.597403 | 0.696970 | 0.522727 | 0.938185 | 0.952931 |
|             CatBoost | 0.697368 | 0.828125 | 0.602273 | 0.954138 | 0.958594 |
|                  KNN | 0.560000 | 0.945946 | 0.397727 | 0.945165 | 0.951465 |

From the above performance metrics, it appears that CatBoost provides a good balance between precision and recall. Hence this is the model we would deploy.

## 6. Deployment
Since, the trained CatBoost model has several hundreds of features, we would want to deploy a model with fewer features. The plot below shows the feature importance for the top features. 
<img title="Top important features scores" alt="Alt text" src="/images/FeatureImportance.png">
From the plot, it is clear that top 5 features have very high scores. Hence we select the 5 most informative features from CatBoost based on the feature importance and train a new model on those 5 features which we will deploy on StreamLit. 
The distribution of values for the top 5 features is shown below
<img title="Top 5 most important features" alt="Alt text" src="/images/Top5Features.png">
THe ROC Curve and the precision-recall curve for the CatBoost classifier with just the top 5 features is shown below. 
<img title="PR and ROC curves" alt="Alt text" src="/images/CatBoost5.png">

The deployed model is hosted on Streamlit at [Provider-fraud-detection](https://medical-fraud-detection-analysis-pradlanka.streamlit.app) where the user can enter the provider's features  and get a prediction on the whether a provider is potentially fraudulent or not. A screenshot of the App is displayed below 

[<img title="App GUI" alt="Alt text" src="/images/AppGUI.png">](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis/data)
