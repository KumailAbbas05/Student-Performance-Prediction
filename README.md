# Student Performance Prediction

A beginner-friendly end-to-end Machine Learning project that predicts a student's final score using academic and lifestyle features.

## Project Goal

The goal of this project is to build a simple regression model that predicts `Final_Score` using:

- Study hours
- Attendance percentage
- Assignment score
- Sleep hours
- Previous score

## Machine Learning Workflow

1. Load the dataset
2. Explore the data
3. Select input features and target
4. Split the data into training and testing sets
5. Train a Linear Regression model
6. Make predictions
7. Evaluate the model
8. Predict a score for a new student

## Dataset

This repository includes a **synthetic dataset** created only for learning and portfolio demonstration.

It is **not real student data** and should not be used for real educational decisions.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Repository Structure

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

## How to Run

Install the libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python src/train_model.py
```

You can also open the Jupyter notebook for a step-by-step version of the project.

## Model

This project uses **Linear Regression** because it is simple, interpretable, and suitable for a beginner regression project.

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## Author

**Kumail Abbas**  
BS Artificial Intelligence Student
