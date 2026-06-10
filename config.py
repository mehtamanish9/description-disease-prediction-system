# Configuration for disease prediction system
# Schemas aligned with real-world datasets (UCI/Kaggle) where possible
# Format: (min, max, type, description)

DISEASES = {
    'Heart Disease': {
        'features': {
            'age': (29, 77, 'int', 'Age in years'),
            'sex': (0, 2, 'choice', '0=Female, 1=Male'),
            'cp': (0, 4, 'choice', 'Chest Pain Type: 0=Typical Angina, 1=Atypical Angina, 2=Non-anginal Pain, 3=Asymptomatic'),
            'trestbps': (94, 200, 'int', 'Resting Blood Pressure (mm Hg)'),
            'chol': (126, 564, 'int', 'Serum Cholesterol (mg/dl)'),
            'fbs': (0, 2, 'choice', 'Fasting Blood Sugar > 120 mg/dl: 0=False, 1=True'),
            'restecg': (0, 3, 'choice', 'Resting ECG: 0=Normal, 1=ST-T wave abnormality, 2=Left ventricular hypertrophy'),
            'thalach': (71, 202, 'int', 'Maximum Heart Rate Achieved'),
            'exang': (0, 2, 'choice', 'Exercise Induced Angina: 0=No, 1=Yes'),
            'oldpeak': (0.0, 6.2, 'float', 'ST depression induced by exercise relative to rest'),
            'slope': (0, 3, 'choice', 'Slope of the peak exercise ST segment: 0=Upsloping, 1=Flat, 2=Downsloping'),
            'ca': (0, 5, 'choice', 'Number of major vessels (0-4) colored by flourosopy'),
            'thal': (0, 4, 'choice', 'Thalassemia: 0=Normal, 1=Fixed defect, 2=Reversable defect')
        },
        'logic': lambda df: (df['age'] > 55) * 0.2 + (df['cp'] > 0) * 0.2 + (df['thalach'] < 150) * 0.2 + (df['oldpeak'] > 2.0) * 0.2 + (df['ca'] > 0) * 0.2
    },
    'Diabetes': {
        'features': {
            'Pregnancies': (0, 17, 'int', 'Number of times pregnant'),
            'Glucose': (0, 199, 'int', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test'),
            'BloodPressure': (0, 122, 'int', 'Diastolic blood pressure (mm Hg)'),
            'SkinThickness': (0, 99, 'int', 'Triceps skin fold thickness (mm)'),
            'Insulin': (0, 846, 'int', '2-Hour serum insulin (mu U/ml)'),
            'BMI': (0.0, 67.1, 'float', 'Body mass index (weight in kg/(height in m)^2)'),
            'DiabetesPedigreeFunction': (0.078, 2.42, 'float', 'Diabetes pedigree function'),
            'Age': (21, 81, 'int', 'Age in years')
        },
        'logic': lambda df: (df['Glucose'] > 140) * 0.4 + (df['BMI'] > 30) * 0.2 + (df['Age'] > 45) * 0.2 + (df['DiabetesPedigreeFunction'] > 0.5) * 0.2
    },
    'Hypertension': {
        'features': {
            'age': (18, 90, 'int', 'Age in years'),
            'sex': (0, 2, 'choice', '0=Female, 1=Male'),
            'cp': (0, 4, 'choice', 'Chest Pain Type (0-3)'),
            'trestbps': (90, 200, 'int', 'Resting Blood Pressure (mm Hg)'),
            'chol': (100, 400, 'int', 'Cholesterol (mg/dl)'),
            'fbs': (0, 2, 'choice', 'Fasting Blood Sugar > 120 mg/dl: 0=No, 1=Yes'),
            'thalach': (60, 220, 'int', 'Max Heart Rate'),
            'exang': (0, 2, 'choice', 'Exercise Induced Angina: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['trestbps'] > 140) * 0.5 + (df['age'] > 60) * 0.3 + (df['chol'] > 240) * 0.2
    },
    'Stroke': {
        'features': {
            'gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'age': (0, 82, 'int', 'Age in years'),
            'hypertension': (0, 2, 'choice', '0=No, 1=Yes'),
            'heart_disease': (0, 2, 'choice', '0=No, 1=Yes'),
            'ever_married': (0, 2, 'choice', '0=No, 1=Yes'),
            'work_type': (0, 5, 'choice', '0=Private, 1=Self-employed, 2=Govt_job, 3=Children, 4=Never_worked'),
            'Residence_type': (0, 2, 'choice', '0=Urban, 1=Rural'),
            'avg_glucose_level': (55.0, 271.0, 'float', 'Average Glucose Level'),
            'bmi': (10.0, 97.0, 'float', 'Body Mass Index'),
            'smoking_status': (0, 4, 'choice', '0=formerly smoked, 1=never smoked, 2=smokes, 3=Unknown')
        },
        'logic': lambda df: (df['age'] > 65) * 0.3 + (df['hypertension'] == 1) * 0.2 + (df['heart_disease'] == 1) * 0.2 + (df['avg_glucose_level'] > 200) * 0.2 + (df['smoking_status'] == 1) * 0.1
    },
    'Kidney Disease': {
        'features': {
            'age': (2, 90, 'int', 'Age in years'),
            'bp': (50, 180, 'int', 'Blood Pressure (mm/Hg)'),
            'sg': (1.005, 1.025, 'float', 'Specific Gravity'),
            'al': (0, 5, 'choice', 'Albumin (0-4)'),
            'su': (0, 5, 'choice', 'Sugar (0-4)'),
            'rbc': (0, 2, 'choice', 'Red Blood Cells: 0=Normal, 1=Abnormal'),
            'pc': (0, 2, 'choice', 'Pus Cell: 0=Normal, 1=Abnormal'),
            'pcc': (0, 2, 'choice', 'Pus Cell Clumps: 0=Not Present, 1=Present'),
            'ba': (0, 2, 'choice', 'Bacteria: 0=Not Present, 1=Present'),
            'bgr': (22, 490, 'int', 'Blood Glucose Random (mgs/dl)'),
            'bu': (1.5, 391.0, 'float', 'Blood Urea (mgs/dl)'),
            'sc': (0.4, 76.0, 'float', 'Serum Creatinine (mgs/dl)'),
            'hemo': (3.1, 17.8, 'float', 'Hemoglobin (gms)')
        },
        'logic': lambda df: (df['al'] > 0) * 0.3 + (df['sc'] > 1.2) * 0.3 + (df['hemo'] < 12) * 0.2 + (df['bp'] > 140) * 0.2
    },
    'Liver Disease': {
        'features': {
            'Age': (4, 90, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Total_Bilirubin': (0.4, 75.0, 'float', 'Total Bilirubin'),
            'Direct_Bilirubin': (0.1, 19.7, 'float', 'Direct Bilirubin'),
            'Alkaline_Phosphotase': (63, 2110, 'int', 'Alkaline Phosphotase'),
            'Alamine_Aminotransferase': (10, 2000, 'int', 'Alamine Aminotransferase'),
            'Aspartate_Aminotransferase': (10, 4929, 'int', 'Aspartate Aminotransferase'),
            'Total_Protiens': (2.7, 9.6, 'float', 'Total Protiens'),
            'Albumin': (0.9, 5.5, 'float', 'Albumin'),
            'Albumin_and_Globulin_Ratio': (0.3, 2.8, 'float', 'Albumin and Globulin Ratio')
        },
        'logic': lambda df: (df['Total_Bilirubin'] > 1.2) * 0.3 + (df['Alkaline_Phosphotase'] > 200) * 0.2 + (df['Alamine_Aminotransferase'] > 40) * 0.3 + (df['Albumin'] < 3.0) * 0.2
    },
    'Asthma': {
        'features': {
            'Age': (5, 80, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Wheezing': (0, 2, 'choice', 'Wheezing: 0=No, 1=Yes'),
            'Shortness_of_Breath': (0, 2, 'choice', 'Shortness of Breath: 0=No, 1=Yes'),
            'Chest_Tightness': (0, 2, 'choice', 'Chest Tightness: 0=No, 1=Yes'),
            'Coughing': (0, 2, 'choice', 'Coughing: 0=No, 1=Yes'),
            'Night_Symptoms': (0, 2, 'choice', 'Night Symptoms: 0=No, 1=Yes'),
            'Exercise_Induced': (0, 2, 'choice', 'Exercise Induced: 0=No, 1=Yes'),
            'Family_History': (0, 2, 'choice', 'Family History: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Wheezing'] == 1) * 0.3 + (df['Shortness_of_Breath'] == 1) * 0.2 + (df['Family_History'] == 1) * 0.2 + (df['Night_Symptoms'] == 1) * 0.2
    },
    'COPD': {
        'features': {
            'Age': (35, 90, 'int', 'Age in years'),
            'Smoking_Years': (0, 60, 'int', 'Years of Smoking'),
            'Packs_Per_Day': (0.0, 3.0, 'float', 'Packs Smoked Per Day'),
            'Shortness_of_Breath': (0, 2, 'choice', 'Shortness of Breath: 0=No, 1=Yes'),
            'Chronic_Cough': (0, 2, 'choice', 'Chronic Cough: 0=No, 1=Yes'),
            'Sputum_Production': (0, 2, 'choice', 'Sputum Production: 0=No, 1=Yes'),
            'Wheezing': (0, 2, 'choice', 'Wheezing: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Smoking_Years'] > 10) * 0.4 + (df['Shortness_of_Breath'] == 1) * 0.2 + (df['Chronic_Cough'] == 1) * 0.2 + (df['Age'] > 40) * 0.2
    },
    'Pneumonia': {
        'features': {
            'Fever': (0, 2, 'choice', 'Fever: 0=No, 1=Yes'),
            'Cough': (0, 2, 'choice', 'Cough: 0=No, 1=Yes'),
            'Chest_Pain': (0, 2, 'choice', 'Chest Pain: 0=No, 1=Yes'),
            'Rapid_Breathing': (0, 2, 'choice', 'Rapid Breathing: 0=No, 1=Yes'),
            'Fatigue': (0, 2, 'choice', 'Fatigue: 0=No, 1=Yes'),
            'Confusion': (0, 2, 'choice', 'Confusion: 0=No, 1=Yes'),
            'Age': (0, 100, 'int', 'Age in years')
        },
        'logic': lambda df: (df['Fever'] == 1) * 0.3 + (df['Cough'] == 1) * 0.3 + (df['Chest_Pain'] == 1) * 0.2 + (df['Rapid_Breathing'] == 1) * 0.2
    },
    'Arthritis': {
        'features': {
            'Age': (20, 90, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Joint_Pain': (0, 2, 'choice', 'Joint Pain: 0=No, 1=Yes'),
            'Stiffness': (0, 2, 'choice', 'Stiffness: 0=No, 1=Yes'),
            'Swelling': (0, 2, 'choice', 'Swelling: 0=No, 1=Yes'),
            'Redness': (0, 2, 'choice', 'Redness: 0=No, 1=Yes'),
            'Range_of_Motion_Loss': (0, 2, 'choice', 'Loss of Range of Motion: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Joint_Pain'] == 1) * 0.4 + (df['Stiffness'] == 1) * 0.3 + (df['Age'] > 50) * 0.3
    },
    'Osteoporosis': {
        'features': {
            'Age': (40, 95, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Bone_Density_T_Score': (-4.0, 1.0, 'float', 'Bone Density T-Score'),
            'Fracture_History': (0, 2, 'choice', 'History of Fractures: 0=No, 1=Yes'),
            'Calcium_Intake': (0, 2, 'choice', 'Calcium Intake: 0=Low, 1=Adequate'),
            'Vitamin_D_Intake': (0, 2, 'choice', 'Vitamin D Intake: 0=Low, 1=Adequate'),
            'Physical_Activity': (0, 2, 'choice', 'Physical Activity: 0=Sedentary, 1=Active')
        },
        'logic': lambda df: (df['Bone_Density_T_Score'] < -2.5) * 0.5 + (df['Age'] > 60) * 0.2 + (df['Fracture_History'] == 1) * 0.2 + (df['Gender'] == 0) * 0.1
    },
    'Alzheimers': {
        'features': {
            'Age': (60, 100, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'MMSE': (0, 30, 'int', 'Mini-Mental State Examination Score (0-30)'),
            'CDR': (0.0, 2.0, 'float', 'Clinical Dementia Rating (0-2)'),
            'eTIV': (1100, 2000, 'int', 'Estimated Total Intracranial Volume'),
            'nWBV': (0.6, 0.9, 'float', 'Normalize Whole Brain Volume'),
            'ASF': (0.8, 1.6, 'float', 'Atlas Scaling Factor')
        },
        'logic': lambda df: (df['CDR'] > 0.5) * 0.5 + (df['MMSE'] < 24) * 0.3 + (df['Age'] > 75) * 0.2
    },
    'Parkinsons': {
        'features': {
            'MDVP:Fo(Hz)': (88.0, 260.0, 'float', 'Average vocal fundamental frequency'),
            'MDVP:Fhi(Hz)': (102.0, 592.0, 'float', 'Max vocal fundamental frequency'),
            'MDVP:Flo(Hz)': (65.0, 239.0, 'float', 'Min vocal fundamental frequency'),
            'MDVP:Jitter(%)': (0.0, 1.0, 'float', 'MDVP:Jitter(%)'),
            'MDVP:Shimmer': (0.0, 1.0, 'float', 'MDVP:Shimmer'),
            'HNR': (8.0, 33.0, 'float', 'Harmonics-to-Noise Ratio'),
            'RPDE': (0.2, 0.7, 'float', 'Recurrence period density entropy'),
            'DFA': (0.5, 0.9, 'float', 'Detrended fluctuation analysis')
        },
        'logic': lambda df: (df['MDVP:Jitter(%)'] > 0.006) * 0.3 + (df['MDVP:Shimmer'] > 0.04) * 0.3 + (df['HNR'] < 20) * 0.2 + (df['RPDE'] > 0.4) * 0.2
    },
    'Migraine': {
        'features': {
            'Age': (15, 70, 'int', 'Age in years'),
            'Duration': (0, 72, 'int', 'Duration of attack (hours)'),
            'Frequency': (0, 30, 'int', 'Frequency (days per month)'),
            'Location': (0, 3, 'choice', 'Location: 0=Unilateral, 1=Bilateral, 2=Other'),
            'Character': (0, 3, 'choice', 'Character: 0=Pulsating, 1=Pressing, 2=Other'),
            'Intensity': (0, 10, 'int', 'Pain Intensity (0-10)'),
            'Nausea': (0, 2, 'choice', 'Nausea: 0=No, 1=Yes'),
            'Vomit': (0, 2, 'choice', 'Vomiting: 0=No, 1=Yes'),
            'Phonophobia': (0, 2, 'choice', 'Phonophobia (sensitivity to sound): 0=No, 1=Yes'),
            'Photophobia': (0, 2, 'choice', 'Photophobia (sensitivity to light): 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Intensity'] > 6) * 0.3 + (df['Nausea'] == 1) * 0.2 + (df['Photophobia'] == 1) * 0.2 + (df['Location'] == 0) * 0.2
    },
    'Anemia': {
        'features': {
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Hemoglobin': (5.0, 18.0, 'float', 'Hemoglobin (g/dL)'),
            'MCH': (15.0, 40.0, 'float', 'Mean Corpuscular Hemoglobin'),
            'MCHC': (25.0, 40.0, 'float', 'Mean Corpuscular Hemoglobin Concentration'),
            'MCV': (60.0, 120.0, 'float', 'Mean Corpuscular Volume'),
            'Platelet_Count': (100000, 450000, 'int', 'Platelet Count')
        },
        'logic': lambda df: (df['Hemoglobin'] < 12.0) * 0.6 + (df['MCV'] < 80) * 0.2 + (df['MCH'] < 27) * 0.2
    },
    'Hypothyroidism': {
        'features': {
            'Age': (18, 90, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'TSH': (0.0, 20.0, 'float', 'Thyroid Stimulating Hormone'),
            'T3': (0.5, 5.0, 'float', 'Triiodothyronine'),
            'TT4': (40.0, 200.0, 'float', 'Total Thyroxine'),
            'T4U': (0.5, 2.0, 'float', 'Thyroxine Utilization'),
            'FTI': (50.0, 200.0, 'float', 'Free Thyroxine Index')
        },
        'logic': lambda df: (df['TSH'] > 4.5) * 0.6 + (df['TT4'] < 60) * 0.2 + (df['FTI'] < 70) * 0.2
    },
    'Malaria': {
        'features': {
            'Fever_History': (0, 2, 'choice', 'History of Fever: 0=No, 1=Yes'),
            'Chills': (0, 2, 'choice', 'Chills: 0=No, 1=Yes'),
            'Headache': (0, 2, 'choice', 'Headache: 0=No, 1=Yes'),
            'Vomiting': (0, 2, 'choice', 'Vomiting: 0=No, 1=Yes'),
            'RBC_Count': (3.0, 6.0, 'float', 'Red Blood Cell Count'),
            'Hemoglobin': (5.0, 16.0, 'float', 'Hemoglobin'),
            'Parasite_Density': (0, 100000, 'int', 'Parasite Density (per microliter)')
        },
        'logic': lambda df: (df['Parasite_Density'] > 0) * 0.8 + (df['Fever_History'] == 1) * 0.2
    },
    'Dengue': {
        'features': {
            'Fever_Days': (0, 14, 'int', 'Days of Fever'),
            'Body_Temperature': (36.0, 41.0, 'float', 'Body Temperature (C)'),
            'Platelet_Count': (10000, 400000, 'int', 'Platelet Count'),
            'Hematocrit': (30.0, 60.0, 'float', 'Hematocrit (%)'),
            'WBC_Count': (2000, 15000, 'int', 'White Blood Cell Count'),
            'Muscle_Pain': (0, 2, 'choice', 'Muscle Pain: 0=No, 1=Yes'),
            'Eye_Pain': (0, 2, 'choice', 'Eye Pain: 0=No, 1=Yes'),
            'Vomiting': (0, 2, 'choice', 'Vomiting: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Platelet_Count'] < 100000) * 0.4 + (df['Fever_Days'] > 2) * 0.2 + (df['Eye_Pain'] == 1) * 0.2 + (df['Hematocrit'] > 45) * 0.2
    },
    'Typhoid': {
        'features': {
            'Fever_Duration': (0, 30, 'int', 'Duration of Fever (days)'),
            'Temperature': (36.0, 41.0, 'float', 'Body Temperature (C)'),
            'Abdominal_Pain': (0, 2, 'choice', 'Abdominal Pain: 0=No, 1=Yes'),
            'Constipation': (0, 2, 'choice', 'Constipation: 0=No, 1=Yes'),
            'Diarrhea': (0, 2, 'choice', 'Diarrhea: 0=No, 1=Yes'),
            'Rose_Spots': (0, 2, 'choice', 'Rose Spots: 0=No, 1=Yes'),
            'Widal_Test_Positive': (0, 2, 'choice', 'Widal Test Positive: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Widal_Test_Positive'] == 1) * 0.6 + (df['Fever_Duration'] > 5) * 0.2 + (df['Abdominal_Pain'] == 1) * 0.2
    },
    'Jaundice': {
        'features': {
            'Age': (0, 100, 'int', 'Age in years'),
            'Gender': (0, 2, 'choice', '0=Female, 1=Male'),
            'Total_Bilirubin': (0.1, 30.0, 'float', 'Total Bilirubin'),
            'Direct_Bilirubin': (0.1, 15.0, 'float', 'Direct Bilirubin'),
            'ALT': (10, 2000, 'int', 'ALT (SGPT)'),
            'AST': (10, 2000, 'int', 'AST (SGOT)'),
            'Yellow_Skin': (0, 2, 'choice', 'Yellowish Skin: 0=No, 1=Yes'),
            'Dark_Urine': (0, 2, 'choice', 'Dark Urine: 0=No, 1=Yes')
        },
        'logic': lambda df: (df['Total_Bilirubin'] > 2.0) * 0.5 + (df['Yellow_Skin'] == 1) * 0.3 + (df['Dark_Urine'] == 1) * 0.2
    }
}
