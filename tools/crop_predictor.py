import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class CropPredictorTool:
    def __init__(self, model_path='../models/crop_model.pkl'):
        self.model = joblib.load(model_path)
        self.scaler = MinMaxScaler()  # For demo; fit on real training data
    
    def preprocess(self, data_dict):
        # data_dict = {'N': 90, 'P': 42, 'K': 43, 'temperature': 20, 'humidity': 80, 'ph': 6.5, 'rainfall': 200}
        df = pd.DataFrame([data_dict])
        df['soil_fertility'] = (df['N'] + df['P'] + df['K']) / 3
        df['climate_index'] = df['temperature'] * df['humidity']
        numeric_cols = ['N','P','K','temperature','humidity','ph','rainfall','soil_fertility','climate_index']
        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        return df[numeric_cols]

    def predict(self, data_dict):
        X = self.preprocess(data_dict)
        prediction = self.model.predict(X)[0]
        return f"Recommended Crop: {prediction}"
