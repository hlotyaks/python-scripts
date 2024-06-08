import unittest
from unittest.mock import patch, mock_open
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jpar import readDependencies

class TestReadDependencies(unittest.TestCase):
    def test_readDependencies(self):
        # Mock the JSON file content
        json_data = {
            "dependencies": [
                {
                    "repo": "repo1",
                    "id": "id1",
                    "version": "1.0.0",
                    "paths": ["path1", "path2"]
                },
                {
                    "repo": "repo2",
                    "id": "id2",
                    "version": "2.0.0",
                    "paths": ["path3", "path4"]
                },
                {
                    "repo": "repo3",
                    "id": "id3",
                    "version": "3.0.0",
                    "paths": []
                }                
            ]
        }

        mock_file = mock_open(read_data=json.dumps(json_data))
        # Mock the 'open' function to return the JSON data
        with patch('builtins.open', mock_file):
            # Call the function with the mock JSON file
            dependencies = readDependencies('mock_file.json', 1)

            # Assert the expected dependencies
            self.assertEqual(len(dependencies), 3)
            self.assertEqual(dependencies[0].repo, 'repo1')
            self.assertEqual(dependencies[0].id, 'id1')
            self.assertEqual(dependencies[0].version, '1.0.0')
            self.assertEqual(dependencies[0].paths, ['path1', 'path2'])
            self.assertEqual(dependencies[1].repo, 'repo2')
            self.assertEqual(dependencies[1].id, 'id2')
            self.assertEqual(dependencies[1].version, '2.0.0')
            self.assertEqual(dependencies[1].paths, ['path3', 'path4'])
            self.assertEqual(dependencies[2].repo, 'repo3')
            self.assertEqual(dependencies[2].id, 'id3')
            self.assertEqual(dependencies[2].version, '3.0.0')
            self.assertEqual(dependencies[2].paths, [])

if __name__ == '__main__':
    unittest.main()