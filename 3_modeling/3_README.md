# Modeling Phase

**Key Steps & Highlights:**
1. **Data Preparation for Modeling:**
   - Loaded the processed dataset (`reduced_features.csv`) containing the reduced set of features and the target variable.
   - Split the data into training and testing sets to ensure an unbiased evaluation of model performance.
   - Applied preprocessing pipelines (e.g., imputation, scaling, one-hot encoding) to ensure consistent input formats for models.

2. **Model Candidate Selection:**
   - Explored multiple classification algorithms, including:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - Gradient Boosting 
     - Explainable Boosting Machine (EBM)
   - Used PyCaret or manual setup to quickly compare baseline performance metrics.

3. **Hyperparameter Tuning & Optimization:**
   - For each promising model, performed parameter tuning using techniques like `RandomizedSearchCV`.
   - Adjusted hyperparameters to improve accuracy, recall, precision, F1-score, and AUC.
   - Selected the model with the best balance of performance metrics.

4. **Model Comparison & Selection:**
   - Compared model candidates against the test set, evaluating metrics and highlighting best-in-class performance.
   - Created confusion matrices and calculated metrics to understand where models excel or fall short.
   - Identified a top-performing model (e.g., Logistic Regression or EBM) based on both predictive 
   performance and interpretability.

5. **Model Interpretability & Explanation:**
   - Examined feature importance plots to understand which factors drive predictions.
   - Applied SHAP and LIME for local explanations, clarifying why certain predictions were made.
   - Conducted Partial Dependence and Individual Conditional Expectation (ICE) plots to show feature sensitivity.

6. **Error Analysis & Business Communication:**
   - Investigated misclassified cases to understand model weaknesses.
   - Created visualizations illustrating how model predictions vary across different feature values.
   - Prepared material (e.g., explanation HTML reports, charts) to help non-technical stakeholders interpret the 
     results and gain confidence in the chosen model.

**Outcome:**
- A well-performing model pipeline is saved (e.g., `lr_pipeline.pkl`, `best_ebm.pkl`) for the deployment phase.
- Thorough documentation and artifacts (plots, tables, explanation files) facilitate transparency and trust in the 
model’s decision-making process.

By the end of the modeling phase, we have a reliable, interpretable model ready for integration into 
the daily workflow of the business stakeholders.
