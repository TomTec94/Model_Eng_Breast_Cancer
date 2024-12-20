# README

## Overview

This project aims to develop an interpretable machine learning model to predict whether a breast tumor is benign or malignant. The goals are high prediction accuracy (F1-score > 0.95) and transparency to build trust among oncologists and medical staff.

The project structure and workflow are guided by the Microsoft Team Data Science Process (TDSP), a methodology that promotes a standardized, modular approach to data science projects. Each folder corresponds to a TDSP phase, ensuring clarity and traceability.

## Project Structure

```
Model_Eng_Breast_Cancer/
│
├─ 1_business_understanding/
│   ├─ 1_README.md              # Business goals and understanding
│
├─ 2_data_acquisition_understanding/
│   ├─ artifacts/               # Data exploration visualizations
│   │   ├─ boxplots.png
│   │   ├─ correlations.png
│   │   ├─ diagnosis_bar_chart.png
│   │   └─ ...
│   ├─ data/
│   │   ├─ raw/                 # Original datasets
│   │   └─ processed/           # Cleaned and processed datasets
│   │       ├─ cleaned_data.csv
│   │       └─ reduced_features.csv
│   ├─ notebooks/
│   │   ├─ EDA.ipynb            # Exploratory Data Analysis
│   │   └─ ...
│   └─ 2_README.md              # Details on data handling and exploration
│
├─ 3_modeling/
│   ├─ artifacts/               # Model evaluation outputs
│   │   ├─ confusion_matrices.png
│   │   ├─ lr_feature_importance.png
│   │   ├─ rf_feature_importance.png
│   │   └─ ...
│   ├─ models/                  # Trained models
│   │   ├─ lr_pipeline.pkl
│   │   ├─ best_ebm.pkl
│   │   └─ ...
│   ├─ notebooks/
│   │   ├─ model_pipeline.ipynb # Training and evaluation workflows
│   │   └─ ...
│   └─ 3_README.md              # Model details and comparisons
│
├─ 4_deployment/
│   ├─ artifacts/               # Deployment artifacts
│   │   ├─ lime_explanation_case_1.html
│   │   └─ ...
│   ├─ samples/                 # Example input files for predictions
│   │   ├─ new_patient_data_benign.csv
│   │   └─ ...
│   ├─ scripts/
│   │   ├─ run_prediction.py    # Prediction script
│   │   └─ ...
│   ├─ notebooks/
│   │   ├─ deployed_model.ipynb # Deployment preparation
│   │   └─ ...
│   └─ 4_README.md              # Deployment instructions
│
├─ 5_customer_acceptance/
│   ├─ Exit_report.md           # Final project report
│   ├─ integrated_model.png     # Model integration diagram
│   └─ ...
│
├─ 6_monitoring/                # Placeholder for monitoring scripts
│
├─ requirements.txt             # Project dependencies
└─ README.md                    # Main project overview
```

## Requirements

- Python 3.9+ (or compatible)
- Key libraries:
  - pandas
  - scikit-learn
  - pycaret
  - interpret (for EBM)
  - lime
  - shap

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Predictions

1. **Check Trained Model**  
   Ensure a trained model file is available in `3_modeling/models/`, e.g., `lr_pipeline.pkl` or `best_ebm.pkl`.

2. **Prepare Input Data**  
   Create a CSV file with required features in the same format as during training.  
   Example `new_patient_data.csv`:
   ```csv
   radius_mean,texture_mean,smoothness_mean,compactness_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,smoothness_se,compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,smoothness_worst,symmetry_worst,fractal_dimension_worst
   14.2,19.3,0.08,0.05,0.17,0.005,0.5,0.8,0.01,0.03,0.01,0.02,0.16,0.009,0.12,0.20,0.007
   ```

3. **Run the Prediction Script**  
   ```bash
   python 4_deployment/scripts/run_prediction.py --model_path 3_modeling/models/lr_pipeline.pkl --input_csv 4_deployment/samples/new_patient_data.csv
   ```

   **Parameters**:
   - `--model_path`: Path to the trained model pipeline (e.g., `3_modeling/models/lr_pipeline.pkl`).
   - `--input_csv`: Path to the new patient CSV file.

4. **View Output**  
   The script will display the prediction and probability, e.g.,:
   ```
   Prediction: malignant (Probability: 96%)
   ```
   If LIME explanations are enabled, an HTML file with explanations will be saved in `4_deployment/artifacts/`.

## Notes

- This project structure adheres to the **Microsoft Team Data Science Process (TDSP)**, ensuring systematic workflows and clear modularization across different stages.
- Use the notebooks in `2_data_acquisition_understanding/notebooks/` and `3_modeling/notebooks/` to retrain models or conduct further analysis.
- Ensure input data matches the expected feature set (same columns, correct formats, no missing features).

