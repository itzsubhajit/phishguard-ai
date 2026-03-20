import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from app.features.extractor import extract_features

def main():
    df = pd.read_csv('training/data/dataset.csv')
    
    X_list = []
    y_list = []
    for idx, row in df.iterrows():
        try:
            feats = extract_features(row['url'])
            X_list.append(feats)
            y_list.append(row['label'])
        except ValueError:
            continue
            
    X = np.array(X_list)
    y = np.array(y_list)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    model = joblib.load('app/model/artifacts/model.pkl')
    
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
