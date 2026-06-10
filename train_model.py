import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(file_path):
    disease_name = os.path.basename(file_path).replace('.csv', '')
    print(f"Training model for {disease_name}...")
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Evaluate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"  Accuracy: {accuracy:.4f}")

    # Save model & scaler
    if not os.path.exists('models'):
        os.makedirs('models')
        
    joblib.dump(model, f'models/{disease_name}_model.pkl')
    joblib.dump(scaler, f'models/{disease_name}_scaler.pkl')
    # Save feature names for prediction
    joblib.dump(X.columns.tolist(), f'models/{disease_name}_features.pkl')

def main():
    dataset_dir = 'datasets'
    if not os.path.exists(dataset_dir):
        print("Datasets directory not found. Please run generate_data.py first.")
        return

    files = [f for f in os.listdir(dataset_dir) if f.endswith('.csv')]
    
    if not files:
        print("No CSV files found in datasets directory.")
        return

    print(f"Found {len(files)} datasets. Starting training...")
    
    for file in files:
        train_model(os.path.join(dataset_dir, file))
        
    print("\nAll models trained and saved.")

if __name__ == "__main__":
    main()
