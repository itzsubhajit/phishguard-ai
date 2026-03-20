def compute_risk_score(phishing_probability: float) -> int:
    score = int(round(phishing_probability * 100))
    return max(0, min(100, score))  # clamp to [0, 100]
