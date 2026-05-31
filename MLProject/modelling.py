"""
Module: modelling.py
Author: I Putu Dhiandika Aditya Permana (username: npemburu6)
Description: Training script used inside MLflow Project.
             Trains a baseline Random Forest classifier and tracks parameters and metrics.
"""

import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn

def train_model():
    print("=== RUNNING TRAINING INSIDE MLPROJECT ===")
    
    # Paths
    train_path = os.path.join(".", "namadataset_preprocessing", "heart-disease_train.csv")
    test_path = os.path.join(".", "namadataset_preprocessing", "heart-disease_test.csv")
    
    if not os.path.exists(train_path) or not os.path.exists(test_path):
        raise FileNotFoundError("Preprocessed dataset files not found inside MLProject folder.")
        
    # Load Data
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    X_train = train_df.drop('target', axis=1)
    y_train = train_df['target']
    X_test = test_df.drop('target', axis=1)
    y_test = test_df['target']
    
    # Enable Autologging for Scikit-Learn
    mlflow.sklearn.autolog()
    
    # Train Model
    with mlflow.start_run(run_name="MLProject_RandomForest") as run:
        print("Training RandomForest model...")
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        print(f"\nTraining Successful!")
        print(f"Accuracy: {acc:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        run_id = run.info.run_id
        print(f"MLflow Run ID: {run_id}")
        
    print("=== MLPROJECT TRAINING COMPLETED ===\n")

if __name__ == "__main__":
    train_model()
