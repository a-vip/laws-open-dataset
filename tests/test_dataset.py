import unittest
import os
import json
import csv

class TestLAWSOpenDataset(unittest.TestCase):
    def test_dataset_files_exist(self):
        data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        json_file = os.path.join(data_dir, "laws_systems.json")
        csv_file = os.path.join(data_dir, "laws_systems.csv")

        self.assertTrue(os.path.exists(json_file))
        self.assertTrue(os.path.exists(csv_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertGreater(len(data), 0)
            self.assertIn("system_name", data[0])
            self.assertIn("canonical_dossier_url", data[0])

    def test_citation_cff_exists(self):
        cff_file = os.path.join(os.path.dirname(__file__), "..", "CITATION.cff")
        self.assertTrue(os.path.exists(cff_file))
        with open(cff_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Avi", content)
            self.assertIn("0009-0005-1903-6868", content)

if __name__ == "__main__":
    unittest.main()
