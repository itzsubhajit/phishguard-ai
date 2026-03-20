import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from app.features.extractor import extract_features, FEATURE_NAMES

def main():
    print("Loading dataset...")
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
    
    print("Training models...")
    lr = LogisticRegression(max_iter=1000, C=1.0)
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    
    lr_scores = cross_val_score(lr, X_train, y_train, cv=5, scoring='f1')
    rf_scores = cross_val_score(rf, X_train, y_train, cv=5, scoring='f1')
    
    lr_f1 = np.mean(lr_scores)
    rf_f1 = np.mean(rf_scores)
    
    print(f"LR F1: {lr_f1:.4f}")
    print(f"RF F1: {rf_f1:.4f}")
    
    best_model = rf if rf_f1 >= lr_f1 else lr
    
    print("Fitting best model on full train set...")
    best_model.fit(X_train, y_train)
    
    os.makedirs('app/model/artifacts', exist_ok=True)
    joblib.dump(best_model, 'app/model/artifacts/model.pkl')
    # Create .gitkeep as well
    with open('app/model/artifacts/.gitkeep', 'w') as f:
        pass
    print("Model saved to app/model/artifacts/model.pkl")

if __name__ == "__main__":
    main()
