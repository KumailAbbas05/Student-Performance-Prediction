import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/student_performance_synthetic.csv")

print("First 5 rows:")
print(df.head())

# Input features
X = df[
    [
        "Study_Hours",
        "Attendance_Percentage",
        "Assignment_Score",
        "Sleep_Hours",
        "Previous_Score",
    ]
]

# Target
y = df["Final_Score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Results")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("R2 Score:", round(r2, 2))

# Compare actual and predicted values
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nSample Predictions:")
print(results.head(10))

# Predict for one new student
new_student = pd.DataFrame({
    "Study_Hours": [5.0],
    "Attendance_Percentage": [88],
    "Assignment_Score": [82],
    "Sleep_Hours": [7.0],
    "Previous_Score": [75]
})

predicted_score = model.predict(new_student)

print("\nPredicted score for new student:")
print(round(predicted_score[0], 2))

# Plot actual vs predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, predictions)
plt.xlabel("Actual Final Score")
plt.ylabel("Predicted Final Score")
plt.title("Actual vs Predicted Student Scores")
plt.grid(True)
plt.show()
