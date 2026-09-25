# Student Performance Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Linear%20Regression-yellow)

An end-to-end beginner Machine Learning project that predicts a student's final score from academic and lifestyle features.

## Project Overview

The project follows a complete supervised-learning workflow:

1. Load and inspect the dataset
2. Select input features and target
3. Split data into training and testing sets
4. Train a Linear Regression model
5. Generate predictions
6. Evaluate model performance
7. Predict the score of a new example student

## Features

The model uses:

- Study hours
- Attendance percentage
- Assignment score
- Sleep hours
- Previous score

Target:

- Final score

## Model Results

Using an 80/20 train-test split with `random_state=42`:

| Metric | Result |
|---|---:|
| Mean Absolute Error | 3.41 |
| Mean Squared Error | 15.54 |
| R² Score | 0.84 |

These results are from the included synthetic dataset and are intended only for learning and portfolio demonstration.

## Dataset

The repository contains **200 synthetic student records**.

> The data is artificially generated. It is not real student data and should not be used for actual educational decisions.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Project Structure

```text
Student-Performance-Prediction/
├── data/
│   └── student_performance_synthetic.csv
├── notebooks/
│   └── student_performance_ml.ipynb
├── src/
│   └── train_model.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Run the Project

```bash
pip install -r requirements.txt
python src/train_model.py
```

The Jupyter notebook provides the same workflow step by step.

## What I Practiced

- Regression problems
- Feature/target separation
- Train-test splitting
- Model fitting
- Prediction
- MAE, MSE and R²
- Comparing actual and predicted values
- Basic ML visualization

## Future Improvements

- Compare Linear Regression with Random Forest
- Add cross-validation
- Add feature-importance analysis
- Use a real public dataset
- Build a small prediction interface

## Author

**Kumail Abbas**  
BS Artificial Intelligence Student
