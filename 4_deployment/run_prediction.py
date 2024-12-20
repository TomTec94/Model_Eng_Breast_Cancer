import pandas as pd
import joblib
from lime.lime_tabular import LimeTabularExplainer
import numpy as np

# adjust path
model_path = "../3_modeling/models/lr_pipeline.pkl"  # Logistic regression pipeline
reference_data_path = "X_train_reference.csv"        # For LIME initialization
input_csv_path = "samples/new_patient_data_critical.csv"  # Input data

# Load the logistic regression pipeline (model + preprocess)
lr_pipeline = joblib.load(model_path)

# Define expected features
expected_features = [
    'radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean',
    'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
    'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
    'symmetry_se', 'fractal_dimension_se', 'smoothness_worst',
    'symmetry_worst', 'fractal_dimension_worst'
]

# Load reference training data for LIME
X_train_ref = pd.read_csv(reference_data_path)
X_train_ref = X_train_ref[expected_features]

# Preprocess reference data
X_train_preprocessed = lr_pipeline.named_steps['preprocess'].transform(X_train_ref)
feature_names = expected_features

# Initialize LIME explainer
lime_explainer = LimeTabularExplainer(
    training_data=X_train_preprocessed,
    feature_names=feature_names,
    class_names=['benign', 'malignant'],
    mode='classification'
)

# Load input CSV data
X_input_raw = pd.read_csv(input_csv_path)

# Check for missing features
missing_feats = [f for f in expected_features if f not in X_input_raw.columns]
if missing_feats:
    raise ValueError(f"Missing required features in the input CSV: {missing_feats}")

X_input = X_input_raw[expected_features]

# Preprocess input
X_input_prepared = lr_pipeline.named_steps['preprocess'].transform(X_input)

# Predict probabilities (index 1 is malignant)
pred_probs = lr_pipeline.named_steps['model'].predict_proba(X_input_prepared)[:, 1]

# ANSI color codes for green/red output
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# For each patient case
for i in range(len(X_input)):
    pred_proba = pred_probs[i]
    prediction = "malignant" if pred_proba > 0.5 else "benign"
    input_row = X_input.iloc[i].values

    # Wrapper for LIME
    def predict_fn(x):
        return lr_pipeline.named_steps['model'].predict_proba(
            lr_pipeline.named_steps['preprocess'].transform(pd.DataFrame(x, columns=feature_names))
        )

    lime_exp = lime_explainer.explain_instance(
        data_row=input_row,
        predict_fn=predict_fn,
        num_features=17
    )

    explanation_map = lime_exp.as_list()
    explanation_sorted = sorted(explanation_map, key=lambda x: abs(x[1]), reverse=True)
    top_contributors = explanation_sorted[:7]

    # Check critical range for radius_mean
    radius_mean_value = X_input.iloc[i]['radius_mean']
    warning_msg = ""
    if 12 <= radius_mean_value <= 14:
        warning_msg = (
            "Note: The radius_mean value is in a critical range where misclassifications "
            "occur more frequently. A manual expert review is recommended."
        )

    # Print results
    print(f"--- Patient Case {i + 1} ---")
    print(f"Prediction: {prediction} (Malignant probability: {pred_proba * 100:.2f}%)")
    if warning_msg:
        print(f"**Warning:** {warning_msg}")
    print("\nInput Feature Values:")

    # Create a dictionary from top_contributors to get direction of each feature
    contribution_dict = dict(explanation_map)  # {feature_condition: weight}


    def get_feature_weight(feature):
        for cond, wght in explanation_map:
            if feature in cond:
                return wght
        return 0.0  # If not found, neutral

    # Print input features with color coding
    for feat_idx, feat_val in enumerate(input_row):
        feat_name = feature_names[feat_idx]
        weight = get_feature_weight(feat_name)
        color = GREEN if weight > 0 else RED
        print(f"{color}{feat_name}: {feat_val}{RESET}")


    # Save LIME explanation as HTML
    lime_exp.save_to_file(f"artifacts/lime_explanation_case_{3}.html")

#
