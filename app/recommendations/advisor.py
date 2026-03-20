def get_recommendation(score: int) -> dict:
    if score <= 29:
        return {
            'level': 'SAFE',
            'color_class': 'safe',
            'message': 'This URL appears legitimate. Standard caution still applies.'
        }
    elif score <= 69:
        return {
            'level': 'SUSPICIOUS',
            'color_class': 'suspicious',
            'message': 'Proceed with caution. Do not enter credentials on this page.'
        }
    else:
        return {
            'level': 'DANGER',
            'color_class': 'danger',
            'message': 'High phishing risk detected. Do not visit this URL.'
        }
