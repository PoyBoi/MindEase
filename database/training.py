import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("D:\\Codes\\ML\\MINDEASE\\Gen_db.csv")
data.columns = data.columns.to_series().apply(lambda x: x.strip())
# Preprocessing
# Fill missing values with the mean (for numerical features) or mode (for categorical features)
for col in data.columns:
    if data[col].dtype == np.dtype('O'):
        data[col].fillna(data[col].mode()[0], inplace=True)
    else:
        data[col].fillna(data[col].mean(), inplace=True)

# Define categorical and numerical features
cat_features = ['gender', 'LGBTQ', 'Ethnicity', 'Locality']
num_features = ['Age', 'previous mental health history']
target_features = ['Loss of interest','Feeling down','Loss of sleep','Feeling tired','Poor apetite','Guilt','Lack of concenteration','restlessness/lethargy','Self harm']

# Split the dataset into training and testing sets
X = data[cat_features + num_features]
y = data[target_features]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(), cat_features)])

# Model pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', RandomForestRegressor())])

# Model training
pipeline.fit(X_train, y_train)

# Model evaluation
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# Predict traits and compute depression scores
predictions = pipeline.predict(X)
depression_scores = np.sum(predictions, axis=1)

# Add the depression scores to the dataset
data['Depression Score'] = depression_scores

def predict_depression_score(age, gender, lgbtq, ethnicity, locality, prev_mental_health_history):
    # Create a DataFrame with user-defined inputs
    user_input = pd.DataFrame(
        data=[[age, gender, lgbtq, ethnicity, locality, prev_mental_health_history]],
        columns=['Age', 'gender', 'LGBTQ', 'Ethnicity', 'Locality', 'previous mental health history']
    )

    # Use the trained model to make predictions on the user input
    user_pred = pipeline.predict(user_input)
    
    # Compute the depression score by summing up the predicted trait values
    depression_score = np.sum(user_pred, axis=1)

    return depression_score[0]

# Example user input
age = 25
gender = 2
lgbtq = 0
ethnicity = 0
locality = 1
prev_mental_health_history = 1

# Predict depression score
depression_score = predict_depression_score(age, gender, lgbtq, ethnicity, locality, prev_mental_health_history)
print(f"Depression Score: {depression_score:.2f}")
