# Model Report

## 1. Model Configuration

**Target Variable:**
- **diagnosis_binary (0 = benign, 1 = malignant)**

**Input Features:**
- A reduced set of numerical features selected after EDA and feature reduction steps.
- Example features:
  - `radius_mean`, `texture_mean`, `smoothness_mean`, `compactness_mean`, `symmetry_mean`,
    `fractal_dimension_mean`, `radius_se`, `texture_se`,
    `smoothness_se`, `compactness_se`, `concavity_se`, `concave points_se`,
    `symmetry_se`, `fractal_dimension_se`, `smoothness_worst`,
    `symmetry_worst`, `fractal_dimension_worst`.

**Algorithms & Pipelines:**
- Multiple classification algorithms were evaluated:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting Classifier
  - Explainable Boosting Machine (EBM)

**Hyperparameter Tuning:**
- Conducted using `RandomizedSearchCV` with 5-fold cross-validation.
- Example tuning parameters:
  - **Logistic Regression:** Penalty type (`l1`, `l2`, `elasticnet`), regularization strength (`C`), 
  solver (`lbfgs`, `liblinear`, `saga`).
  - **Random Forest:** Number of estimators, max depth, min samples split/leaf, max features.
  - **Gradient Boosting:** Number of estimators, learning rate, max depth, min samples split/leaf.
  - **EBM:** Max bins, max rounds, learning rate, min samples leaf, number of interactions.

**Final Selected Model:**
- Based on performance and interpretability, a Logistic Regression model was ultimately chosen.
- The final pipeline includes:
  - Preprocessing (imputation, scaling)
  - Optional dimensionality reduction (PCA)
  - Tuned Logistic Regression classifier

## 2. Model Performance

**Evaluation Metrics:**
- Accuracy, AUC (ROC), Recall, Precision, and F1-score on the test set.
- Confusion matrices to visualize classification errors.

**Overall Results:**
- Logistic Regression achieved high accuracy (>95%) on the test set.
- High AUC indicating strong model discrimination.
- Balanced Recall and Precision ensure accurate detection of malignant cases without excessive false alarms.

**Comparison of Candidates:**
- Decision Tree and basic Gradient Boosting did not meet the 95% accuracy threshold.
- Random Forest performed better than the single-tree models.
- EBM provided strong performance and interpretability, making it a close contender alongside Logistic Regression.

**Artifacts for Reference:**
- **`confusion_matrices.png`**: Shows confusion matrices for top models.
- **`combined_misclassification_table.csv`**: Highlights misclassified cases across models.
- **`feature_distribution_misclassified.png`**: Depicts how misclassified samples differ for certain features.

## 3. Model Interpretation

**Global Feature Importance:**
- Key features (e.g. `radius_mean`, `texture_mean`, `smoothness_worst`) stood out as main predictors.
- EBM and Logistic Regression coefficients confirmed their influence in predicting malignancy vs. benign.

**Local Interpretability (LIME & SHAP):**
- LIME explanations (e.g., `lr_lime_explanation_B.html` and `lr_lime_explanation_M.html`) show how individual 
features influenced specific predictions.
- SHAP summary plots (e.g., `lr_shap_summary_plot.png`) illustrate feature contributions across many samples.

**Partial Dependence & ICE Plots:**
- `pdp_top_features_rf.png` demonstrates how changes in a single feature affect the model’s predictions.

**Key Drivers:**
- Metrics and visualizations (e.g., `lr_feature_importance.png`, `rf_feature_importance.png`) confirm that 
certain size and texture metrics heavily impact predictions.
- Understanding these drivers helps domain experts trust the model’s reasoning process.

---

**Conclusion:**
The chosen model (Logistic Regression) excels in predictive performance and interpretability. Accompanying 
artifacts (feature importance plots, LIME explanations, SHAP summaries, confusion matrices) provide transparency 
and aid stakeholders in understanding both the strengths and weaknesses of the model’s decision-making process.
