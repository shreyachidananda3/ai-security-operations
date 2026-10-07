import json

from incident_classifier import IncidentClassifier
from vulnerability_analyzer import VulnerabilityAnalyzer
from response_engine import ResponseEngine
from risk_analyzer import RiskAnalyzer


class SecurityOperations:
    def __init__(self):
        self.classifier = IncidentClassifier()
        self.vulnerability_analyzer = VulnerabilityAnalyzer()
        self.response_engine = ResponseEngine()
        self.risk_analyzer = RiskAnalyzer()

    def analyze_incident(self, incident):
        classification = self.classifier.classify(
            incident["description"]
        )

        incident_type = classification["incident_type"]
        confidence = classification["confidence"]

        vulnerability = self.vulnerability_analyzer.analyze(
            incident_type
        )

        recommendations = self.response_engine.recommend(
            incident_type
        )

        risk = self.risk_analyzer.calculate_risk(
            incident_type,
            confidence
        )

        return {
            "id": incident["id"],
            "description": incident["description"],
            "source": incident["source"],
            "incident_type": incident_type,
            "confidence": confidence,
            "vulnerability": vulnerability["vulnerability"],
            "impact": vulnerability["impact"],
            "security_checks": vulnerability["checks"],
            "response_recommendations": recommendations,
            "risk_score": risk["risk_score"],
            "severity": risk["severity"]
        }

    def analyze_all(self, incidents):
        results = []

        for incident in incidents:
            result = self.analyze_incident(incident)
            results.append(result)

        return results


if __name__ == "__main__":
    with open("data/incidents.json", "r") as file:
        incidents = json.load(file)

    operations = SecurityOperations()
    results = operations.analyze_all(incidents)

    print("AI-Powered Security Operations")
    print("==============================")

    for result in results:
        print()
        print(f"Incident: {result['id']}")
        print(f"Type: {result['incident_type']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Risk Score: {result['risk_score']}/5")
        print(f"Severity: {result['severity']}")
        print(f"Vulnerability: {result['vulnerability']}")
        print("Response:")

        for recommendation in result["response_recommendations"]:
            print(f"- {recommendation}")