import json

from security_operations import SecurityOperations


def generate_report(results):
    """Generate a security operations assessment report."""

    print()
    print("=" * 60)
    print("SECURITY OPERATIONS ASSESSMENT REPORT")
    print("=" * 60)

    print(f"Total Incidents Analyzed: {len(results)}")

    incident_types = {}
    severity_levels = {}

    for result in results:
        incident_type = result["incident_type"]
        severity = result["severity"]

        incident_types[incident_type] = (
            incident_types.get(incident_type, 0) + 1
        )

        severity_levels[severity] = (
            severity_levels.get(severity, 0) + 1
        )

    print("\nIncident Classification Summary")
    print("--------------------------------")

    for incident_type, count in incident_types.items():
        print(f"{incident_type}: {count}")

    print("\nRisk Severity Summary")
    print("---------------------")

    for severity, count in severity_levels.items():
        print(f"{severity}: {count}")

    print("\nDetailed Findings")
    print("-----------------")

    for result in results:
        print()
        print(f"Incident ID: {result['id']}")
        print(f"Type: {result['incident_type']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Risk Score: {result['risk_score']}/5")
        print(f"Severity: {result['severity']}")
        print(f"Vulnerability: {result['vulnerability']}")
        print(f"Impact: {result['impact']}")

        print("Security Checks:")
        for check in result["security_checks"]:
            print(f"- {check}")

        print("Response Recommendations:")
        for recommendation in result["response_recommendations"]:
            print(f"- {recommendation}")

    print()
    print("=" * 60)
    print("END OF SECURITY OPERATIONS REPORT")
    print("=" * 60)


if __name__ == "__main__":
    with open("data/incidents.json", "r") as file:
        incidents = json.load(file)

    operations = SecurityOperations()
    results = operations.analyze_all(incidents)

    generate_report(results)