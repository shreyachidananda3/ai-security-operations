import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class IncidentClassifier:
    """Machine-learning classifier for common cybersecurity incidents."""

    def __init__(self, training_file="data/training_data.json"):
        self.training_file = Path(training_file)
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=1000)

        self._load_training_data()
        self._train_model()

    def _load_training_data(self):
        with open(self.training_file, "r") as file:
            data = json.load(file)

        self.training_texts = [item["text"] for item in data]
        self.training_labels = [item["label"] for item in data]

    def _train_model(self):
        features = self.vectorizer.fit_transform(self.training_texts)
        self.model.fit(features, self.training_labels)

    def classify(self, incident_text):
        """Classify an incident and return the predicted type and confidence."""
        features = self.vectorizer.transform([incident_text])

        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        confidence = max(probabilities)

        return {
            "incident_type": prediction,
            "confidence": round(float(confidence), 2)
        }


if __name__ == "__main__":
    classifier = IncidentClassifier()

    test_incident = (
        "Repeated failed login attempts were detected against "
        "an administrator account."
    )

    result = classifier.classify(test_incident)

    print("Incident Classification")
    print("-----------------------")
    print(f"Incident: {test_incident}")
    print(f"Type: {result['incident_type']}")
    print(f"Confidence: {result['confidence']}")