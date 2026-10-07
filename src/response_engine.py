class ResponseEngine:
    """Generates incident-response recommendations."""

    RESPONSE_MAP = {
        "brute_force": [
            "Investigate the source IP address",
            "Review authentication logs",
            "Verify multi-factor authentication",
            "Consider temporarily locking the affected account"
        ],
        "phishing": [
            "Quarantine the suspicious email",
            "Investigate the embedded link",
            "Check whether credentials were submitted",
            "Notify affected users and security personnel"
        ],
        "malware": [
            "Isolate the affected endpoint",
            "Investigate suspicious processes",
            "Run an endpoint security scan",
            "Review system and network activity"
        ],
        "unauthorized_access": [
            "Review the user's permissions",
            "Investigate access logs",
            "Verify whether the access was authorized",
            "Remove unnecessary permissions if required"
        ],
        "data_exposure": [
            "Identify the affected sensitive data",
            "Review file access logs",
            "Verify the user's authorization",
            "Assess potential data exposure"
        ]
    }

    def recommend(self, incident_type):
        """Return response recommendations for an incident type."""
        return self.RESPONSE_MAP.get(
            incident_type,
            ["Perform a detailed security investigation"]
        )


if __name__ == "__main__":
    engine = ResponseEngine()

    recommendations = engine.recommend("malware")

    print("Incident Response Recommendations")
    print("---------------------------------")

    for recommendation in recommendations:
        print(f"- {recommendation}")