# Key Insights

## Class Imbalance
- The dataset is imbalanced with more benign (B) cases than malignant (M).
- Maybe requires handling during model training (e.g., resampling or weighted metrics).

## Highly Correlated Features
- Strong correlations observed between `radius_mean`, `area_mean`, and `perimeter_mean` (>0.9).
- Similar high correlations between "mean" and "worst" variants of features.
- Multicollinearity may affect models like Logistic Regression.

## Separation of Classes
- Significant differences between malignant and benign tumors in:
  - `radius_mean`, `area_mean`, `perimeter_mean`, `compactness_mean`, and `concave points_mean`.

## Outliers
- Outliers detected in features such as `area_mean` and `perimeter_mean`.
- May require handling (e.g., scaling or transformation).

## Independent Features
- Features like `symmetry_mean` and `fractal_dimension_mean` show lower correlations with others.
- Could provide unique predictive value.
