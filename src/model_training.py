
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(input_file, model_file):
    # Load processed data
    data = pd.read_csv(input_file)
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # Save trained model
    joblib.dump(model, model_file)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    train_model('data/processed/cleaned_patient_records.csv', 'models/random_forest_model.pkl')
