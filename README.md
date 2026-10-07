# AI-Powered Security Operations & Incident Response

## Overview

A Python-based security operations simulation that uses machine learning and rule-based security analysis to classify cybersecurity incidents, assess vulnerabilities, calculate risk, and recommend incident-response actions.

The project demonstrates how machine-learning-assisted analysis can support security operations workflows.

## Key Features

- Machine-learning-based incident classification
- TF-IDF text feature extraction
- Logistic Regression classification
- Vulnerability assessment
- Risk scoring and severity assessment
- Security control checks
- Incident-response recommendations
- Automated security operations pipeline
- Security assessment reporting
- Unit testing

## Architecture

Simulated Security Incidents
↓
TF-IDF Vectorization
↓
Logistic Regression
↓
Incident Classification
↓
Vulnerability Analysis
↓
Risk Assessment
↓
Security Checks
↓
Response Recommendations
↓
Security Operations Report

## Incident Categories

The system analyzes five common cybersecurity incident categories:

- Brute-force attacks
- Phishing
- Malware
- Unauthorized access
- Data exposure

## Machine Learning

The project uses a lightweight supervised machine-learning approach:

- TF-IDF converts incident descriptions into numerical text features.
- Logistic Regression classifies incidents into predefined security categories.
- The model provides a confidence score for each classification.

The training dataset is synthetic and designed for demonstration and learning purposes. Model training accuracy should not be interpreted as production-level performance.

## Security Analysis

After classification, the system performs additional security analysis.

### Vulnerability Analysis

Maps each incident category to:

- Potential security weakness
- Possible security impact
- Recommended security checks

### Risk Assessment

Calculates a risk score from 1 to 5 and assigns:

- LOW
- MEDIUM
- HIGH

### Incident Response

Generates recommended actions such as:

- Reviewing authentication logs
- Investigating suspicious links
- Isolating affected endpoints
- Reviewing access permissions
- Assessing potential data exposure

The system provides recommendations only and does not automatically execute defensive actions.

## Project Structure

data/
- incidents.json
- training_data.json

src/
- incident_classifier.py
- vulnerability_analyzer.py
- risk_analyzer.py
- response_engine.py
- security_operations.py
- security_report.py
- evaluate_model.py

tests/
- test_incident_classifier.py

docs/
- architecture.md

screenshots/
- Project output screenshots

## Testing

The project includes automated unit tests for incident classification.

Example test categories:

- Brute-force detection
- Phishing detection
- Malware detection
- Unauthorized access detection
- Data exposure detection

Run the tests with:

python -m unittest tests/test_incident_classifier.py

## Technology Stack

- Python
- scikit-learn
- TF-IDF
- Logistic Regression
- JSON
- unittest

## Deployment

This project runs locally and does not require:

- AWS
- Paid cloud services
- External APIs
- Production security infrastructure

It is intended as a cybersecurity learning and portfolio project demonstrating machine-learning-assisted security operations.

## Author

Shreya Chidananda

MS Cybersecurity
Stevens Institute of Technology
