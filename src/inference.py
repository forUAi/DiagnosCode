
import pandas as pd
import joblib

def generate_code(model_file, new_data_file, output_file):
    # Load trained model
    model = joblib.load(model_file)
    
    # Load new data
    new_data = pd.read_csv(new_data_file)
    
    # Generate predictions
    predictions = model.predict(new_data)
    
    # Save predictions
    new_data['predictions'] = predictions
    new_data.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    generate_code('models/random_forest_model.pkl', 'data/processed/new_patient_data.csv', 'data/processed/predictions.csv')
