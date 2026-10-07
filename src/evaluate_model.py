import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


with open("data/training_data.json", "r") as file:
    data = json.load(file)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(features, labels)

predictions = model.predict(features)

accuracy = accuracy_score(labels, predictions)

print("Machine Learning Model Evaluation")
print("=================================")
print(f"Training examples: {len(data)}")
print(f"Training accuracy: {accuracy:.2f}")

print("\nClassification Report")
print("---------------------")

print(
    classification_report(
        labels,
        predictions,
        zero_division=0
    )
)