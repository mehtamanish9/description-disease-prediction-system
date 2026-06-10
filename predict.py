import pandas as pd
import numpy as np
import os
import joblib
from config import DISEASES

def get_user_input(disease_name, features_list):
    print(f"\n--- Enter Details for {disease_name} ---")
    print("Please enter the following values within the specified ranges.")
    
    # Get config for this disease to show ranges
    disease_config = DISEASES.get(disease_name)
    if not disease_config:
        # Fallback if name mismatch (shouldn't happen if names match exactly)
        for d_name, d_conf in DISEASES.items():
            if d_name.lower().replace(' ', '_') == disease_name.lower().replace(' ', '_'):
                disease_config = d_conf
                break
    input_values = []
    try:
        for feature in features_list:
            prompt = f"{feature.replace('_', ' ').title()}"
            
            # Add range info if available
            if disease_config and feature in disease_config['features']:
                config_tuple = disease_config['features'][feature]
                low, high, type_ = config_tuple[:3]
                desc = config_tuple[3] if len(config_tuple) > 3 else ""
                
                if desc:
                    prompt += f" ({desc})"
                else:
                    if type_ == 'int':
                        prompt += f" (Range: {low}-{high}, Integer)"
                    elif type_ == 'float':
                        prompt += f" (Range: {low}-{high}, Decimal)"
                    elif type_ == 'choice':
                        prompt += f" (Enter {low} to {high-1})"
            
            prompt += ": "
            
            while True:
                try:
                    val = float(input(prompt))
                    input_values.append(val)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
        return np.array([input_values])
    except Exception as e:
        print(f"Error reading input: {e}")
        return None

def predict_disease():
    model_dir = 'models'
    if not os.path.exists(model_dir):
        print("Models directory not found. Please run train_model.py first.")
        return

    # diseases list
    files = [f for f in os.listdir(model_dir) if f.endswith('_model.pkl')]
    diseases = sorted([f.replace('_model.pkl', '') for f in files])
    
    if not diseases:
        print("No models found.")
        return

    print("\n--- Available Diseases ---")
    for i, disease in enumerate(diseases):
        print(f"{i+1}. {disease.replace('_', ' ').title()}")

    try:
        choice_input = input("\nSelect a disease to predict (enter number): ")
        choice = int(choice_input) - 1
        if choice < 0 or choice >= len(diseases):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_disease_file_name = diseases[choice]
    # display name if possible or just title case 
    display_name = selected_disease_file_name.replace('_', ' ').title()
    # find exact key in config for better looking name
    for d_name in DISEASES.keys():
        if d_name.lower().replace(' ', '_') == selected_disease_file_name:
            display_name = d_name
            break

    print(f"\nSelected: {display_name}")

    # Load model
    try:
        model = joblib.load(f'{model_dir}/{selected_disease_file_name}_model.pkl')
        scaler = joblib.load(f'{model_dir}/{selected_disease_file_name}_scaler.pkl')
        features = joblib.load(f'{model_dir}/{selected_disease_file_name}_features.pkl')
    except Exception as e:
        print(f"Error loading model files: {e}")
        return

    # for manual input or demo
    print("\n1. Enter patient details manually")
    print("2. Run demo with random data")
    mode = input("Choose an option (1/2): ")

    if mode == '1':
        input_data = get_user_input(display_name, features)
        if input_data is None:
            return
    else:
        # for quick testing without typing
        print("\nGenerating random test data...")
        input_data = scaler.mean_.reshape(1, -1) + np.random.normal(0, 1, (1, len(features)))
        
        print("Generated Input:")
        for i, feature in enumerate(features):
            print(f"  {feature}: {input_data[0][i]:.2f}")

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    print("\n--- Prediction Result ---")
    if prediction[0] == 1:
        print(f"Result: HIGH RISK of {display_name}")
        print(f"Probability: {probability:.2%}")
    else:
        print(f"Result: LOW RISK of {display_name}")
        print(f"Probability: {probability:.2%}")

if __name__ == "__main__":
    predict_disease()
