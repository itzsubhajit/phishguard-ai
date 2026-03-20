from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.validators.url_validator import validate_url
from app.features.extractor import extract_features
from app.model.predictor import predict
from app.model.scorer import compute_risk_score
from app.recommendations.advisor import get_recommendation

detection_bp = Blueprint('detection', __name__)

@detection_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@detection_bp.route('/analyze', methods=['POST'])
def analyze():
    raw_url = request.form.get('url', '')
    try:
        url = validate_url(raw_url)
    except ValueError as e:
        flash(str(e), 'error')
        return redirect(url_for('detection.index'))
    features = extract_features(url)
    prediction = predict(features)
    score = compute_risk_score(prediction['phishing_probability'])
    recommendation = get_recommendation(score)
    return render_template('result.html', url=url, score=score, prediction=prediction, recommendation=recommendation)
