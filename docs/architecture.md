# System Architecture

## Overview

The AI-Powered Security Operations system is a local Python-based cybersecurity simulation that uses machine learning and rule-based security analysis to process simulated security incidents.

The system does not require a live cloud environment or external security infrastructure.

## Architecture Flow

Simulated Security Incidents
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression Model
        ↓
Incident Classification
        ↓
Vulnerability Analysis
        ↓
Risk Assessment
        ↓
Security Checks
        ↓
Incident Response Recommendations
        ↓
Security Operations Report

## Components

### 1. Incident Data

Simulated cybersecurity incidents are stored in:

data/incidents.json

The dataset contains examples involving:

- Brute-force attacks
- Phishing
- Malware
- Unauthorized access
- Data exposure

### 2. Machine Learning Classification

src/incident_classifier.py

The classifier uses:

- TF-IDF for text feature extraction
- Logistic Regression for incident classification

The model predicts the most likely incident category and provides a confidence score.

### 3. Vulnerability Analysis

src/vulnerability_analyzer.py

The predicted incident type is mapped to a potential security weakness, its possible impact, and recommended security checks.

### 4. Risk Assessment

src/risk_analyzer.py

The system assigns a risk score from 1 to 5 based on the incident type and model confidence.

The score is converted into:

- LOW
- MEDIUM
- HIGH

### 5. Incident Response

src/response_engine.py

The system provides recommended actions for each incident category.

Examples include:

- Reviewing authentication logs
- Investigating suspicious links
- Isolating affected endpoints
- Reviewing access permissions
- Assessing potential data exposure

These are recommendations only. The system does not automatically perform defensive actions.

### 6. Security Operations Pipeline

src/security_operations.py

This module integrates all major components into a single workflow:

1. Classify the incident
2. Analyze the vulnerability
3. Calculate risk
4. Generate security checks
5. Generate response recommendations

### 7. Security Report

src/security_report.py

The final report summarizes:

- Incident classifications
- Risk severity
- Risk scores
- Vulnerabilities
- Potential impact
- Security checks
- Response recommendations

## Testing

Automated tests are located in:

tests/test_incident_classifier.py

The classifier is tested against five previously unseen incident descriptions.

The project also includes a model evaluation script:

src/evaluate_model.py

The evaluation script reports performance on the available training dataset. Because the dataset is small and synthetic, the training accuracy should not be interpreted as real-world model accuracy.

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

It is designed as a cybersecurity learning and portfolio project demonstrating machine-learning-assisted security operations.