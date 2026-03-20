import pytest
from unittest.mock import patch, MagicMock
from app.model.scorer import compute_risk_score
from app.recommendations.advisor import get_recommendation
from app.model.predictor import predict

def test_compute_risk_score():
    assert compute_risk_score(-0.1) == 0
    assert compute_risk_score(1.1) == 100
    assert compute_risk_score(0.456) == 46

def test_get_recommendation():
    # 0-29 SAFE
    assert get_recommendation(0)['level'] == 'SAFE'
    assert get_recommendation(29)['level'] == 'SAFE'
    # 30-69 SUSPICIOUS
    assert get_recommendation(30)['level'] == 'SUSPICIOUS'
    assert get_recommendation(69)['level'] == 'SUSPICIOUS'
    # 70-100 DANGER
    assert get_recommendation(70)['level'] == 'DANGER'
    assert get_recommendation(100)['level'] == 'DANGER'

@patch('app.model.predictor._get_model')
def test_predict(mock_get_model):
    mock_model = MagicMock()
    # Mock predict_proba to return [[prob_safe, prob_phishing]]
    mock_model.predict_proba.return_value = [[0.2, 0.8]]
    mock_get_model.return_value = mock_model
    
    result = predict([0]*12) # dummy features
    
    mock_get_model.assert_called_once()
    assert result['label'] == 'PHISHING'
    assert result['phishing_probability'] == 0.8
