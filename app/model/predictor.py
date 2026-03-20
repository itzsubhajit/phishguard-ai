import joblib
import os

_model = None

def _get_model():
    global _model
    if _model is None:
        path = os.path.join(os.path.dirname(__file__), 'artifacts', 'model.pkl')
        _model = joblib.load(path)
    return _model

def predict(feature_vector: list) -> dict:
    model = _get_model()
    proba = model.predict_proba([feature_vector])[0]
    phishing_prob = proba[1]  # index 1 = phishing class
    label = 'PHISHING' if phishing_prob >= 0.5 else 'SAFE'
    return {'label': label, 'phishing_probability': float(phishing_prob)}
