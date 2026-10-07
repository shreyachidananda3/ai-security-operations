class RiskAnalyzer:
    """Assigns a security risk level based on incident type and confidence."""

    BASE_RISK = {
        "brute_force": 3,
        "phishing": 3,
        "malware": 4,
        "unauthorized_access": 3,
        "data_exposure": 4
    }

    def calculate_risk(self, incident_type, confidence):
        """Return a risk score and severity level."""

        base_score = self.BASE_RISK.get(incident_type, 2)

        if confidence >= 0.50:
            score = base_score + 1
        else:
            score = base_score

        score = min(score, 5)

        if score >= 5:
            severity = "HIGH"
        elif score >= 3:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {
            "risk_score": score,
            "severity": severity
        }


if __name__ == "__main__":
    analyzer = RiskAnalyzer()

    result = analyzer.calculate_risk("brute_force", 0.58)

    print("Risk Assessment")
    print("---------------")
    print(f"Risk Score: {result['risk_score']}/5")
    print(f"Severity: {result['severity']}")