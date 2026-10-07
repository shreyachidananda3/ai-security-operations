import unittest

from src.incident_classifier import IncidentClassifier


class TestIncidentClassifier(unittest.TestCase):

    def setUp(self):
        self.classifier = IncidentClassifier()

    def test_brute_force_detection(self):
        result = self.classifier.classify(
            "Someone tried many passwords to access the administrator account"
        )
        self.assertEqual(result["incident_type"], "brute_force")

    def test_phishing_detection(self):
        result = self.classifier.classify(
            "An employee clicked a fake company login link"
        )
        self.assertEqual(result["incident_type"], "phishing")

    def test_malware_detection(self):
        result = self.classifier.classify(
            "A suspicious executable started running on a laptop"
        )
        self.assertEqual(result["incident_type"], "malware")

    def test_unauthorized_access_detection(self):
        result = self.classifier.classify(
            "A user accessed a restricted database without permission"
        )
        self.assertEqual(result["incident_type"], "unauthorized_access")

    def test_data_exposure_detection(self):
        result = self.classifier.classify(
            "A confidential customer file was accessed without authorization"
        )
        self.assertEqual(result["incident_type"], "data_exposure")


if __name__ == "__main__":
    unittest.main()