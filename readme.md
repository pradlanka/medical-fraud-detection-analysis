

## 1. Buisiness problem
Health care fraud  is a huge problem in the United States. As the FBI website notes, health care fraud is not a victimless crime and it causes tens of billions of dollars in losses each year. It can raise health insurance premiums, expose you to unnecessary medical procedures, and increased taxes. In this project, I will predict the potentially fraudulent providers based on providers claims.
## 2. Dataset used
 The dataset for this analysis is from Kaggle <https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis/data> It contians infromation about claims and beneficiary information for several patients and providers.
 
## 3. Exploratory data analysis (EDA) 
As expected the data is heavily unabalanced with a lot more providers who have not commited fraud than those who did commit fraud by a factor of 9 with 506 out of 5410 providers potentially commiting fraud. From the beneficiaries datase, it is clear and that the most of the beneficiaries were covered for the entire 12 months in an year and a large percentage of them have chronic conditions as shown in the figure below. 
<img title="Chronic condition prevalance in the our sample" alt="Alt text" src="/images/ChronicCond.png">

Furthermore we can can look at procedure codes and diagnostic codes for the inpatient and outpatient claims and extract the top100 most common codes as features to improve our prediction of fraudulent providers. t word cloud of the procedure codes for in patient claims is shown below.
<img title="In patient Claim diagnostic codes" alt="Alt text" src="/images/ClaimsDiagnosisInpatient.png">

## 3. Data cleaning and Preperation
Since some of the variables are categorical, we need to convert them currently as strings to categorical variables. Furthermore, a lot of variables on the patient conditions are further converted into Boolean to be used as features for the machine learnign algorithm. An important feature in prediction of fraduent providers could be the days of stay at the hospital for in_patient claims which is shown in the figure below.
<img title="Days spent in Hosptial for in patients" alt="Alt text" src="/images/DaysInHosptial.png">

Furthermore we can look at in-patient and out-patient claim process times as features. We extract the top 100 diagnosis codes and procedure codes for  

## 4. Modeling & Optimization
## 5. Evaluation
<img title="ROC Curves" alt="Alt text" src="/images/ROCCurve.png">
## 6. Deployment

