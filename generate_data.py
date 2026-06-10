import pandas as pd
import numpy as np
import os

def generate_dataset(name, features, logic_fn, num_samples=1000):
    np.random.seed(42)
    data = {}
    
    # Generate features
    for feature_name, config_tuple in features.items():
        low, high, type_ = config_tuple[:3]
        if type_ == 'int':
            data[feature_name] = np.random.randint(low, high, num_samples)
        elif type_ == 'float':
            data[feature_name] = np.random.uniform(low, high, num_samples)
        elif type_ == 'choice':
            # For choice, low is usually 0 and high is the number of options (exclusive in randint, but choice uses a range)
            # In config we defined it as (0, N, 'choice'), so we want values from 0 to N-1
            # np.random.choice(N) generates 0 to N-1
            data[feature_name] = np.random.randint(low, high, num_samples)
            
    df = pd.DataFrame(data)
    
    # Generate target
    target_prob = logic_fn(df)
    df['target'] = (target_prob > 0.5).astype(int)
    
    return df

def main():
    if not os.path.exists('datasets'):
        os.makedirs('datasets')

    from config import DISEASES

    for name, config in DISEASES.items():
        print(f"Generating data for {name}...")
        df = generate_dataset(name, config['features'], config['logic'])
        filename = f"datasets/{name.lower().replace(' ', '_')}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved {filename}")

if __name__ == "__main__":
    main()
