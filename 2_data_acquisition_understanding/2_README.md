# Exploratory Data Analysis (EDA)

**Main Objectives:**
- Understand the distribution of the target variable (benign vs. malignant).
- Assess data quality and identify any missing or irrelevant features.
- Explore the relationships and distributions of key numeric features.
- Identify and remove highly correlated features to reduce redundancy.

**Key Steps & Findings:**
1. **Initial Data Inspection:**  
   - Confirmed data shape, column types, and presence of target variable.
   - Dropped irrelevant columns (`Unnamed: 32`, `id`) to simplify the dataset.

2. **Target Variable Analysis:**  
   - The diagnosis distribution (benign vs. malignant) was visualized via a bar chart.
   - Confirmed a balanced or at least a sufficient representation of both classes.

3. **Numeric Features Exploration:**  
   - Created histograms and violin plots to understand the distribution of features and their relationship to the target.
   - Visualized data with pairplots to examine feature interactions and potential clustering patterns.
   - Applied standardization to facilitate comparison across different scales.

4. **Feature Correlation & Reduction:**  
   - Generated a correlation heatmap to identify strongly correlated features.
   - Removed highly correlated features to avoid redundancy and potential overfitting.
   - Saved the reduced feature set in `reduced_features.csv`.

5. **Dimensionality Reduction with PCA:**  
   - Examined explained variance ratios to determine the number of principal components needed.
   - Identified that a relatively small number of components capture most of the variance.
   - Provided cumulative explained variance plot to illustrate how many components preserve 95% of the variance.

**Outcome:**
- The data is now cleaner, reduced in dimensionality, and better understood.
- These findings set a strong foundation for model development and optimization in subsequent phases.
