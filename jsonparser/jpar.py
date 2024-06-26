import os
import sys
import json
import argparse

class Dependency:
    def __init__(self, repo, id, version, paths):
        self.repo = repo
        self.id = id
        self.version = version
        self.paths = paths

    # Override the __str__ method for better print during debug.
    def __str__(self):
        return f"Dependency(repo: {self.repo}, id: {self.id}, version: {self.version}, paths: {self.paths})"
    
def readDependencies(jsonfile, verbosity):
    # Replace 'your_file.json' with the path to your JSON file
    with open(jsonfile, 'r') as file:
        data = json.load(file)

    dependencies = [Dependency(dep.get('repo', 'no repo'), dep.get('id', 'no id'), dep.get('version', '0.0.0'), dep.get('paths', [])) for dep in data['dependencies']]

    if(verbosity != 0):
        for dep in dependencies: print(dep)

    return dependencies

def main(args):
    dependencies = readDependencies(args.file, args.verbosity)


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Example with non-optional arguments')

    # Add arguments
    parser.add_argument('--file', type=str, required=True, help='Path to json file')
    parser.add_argument('--verbosity', type=int, help='Increase verbosity', default=0)

    # Parse the arguments
    args = parser.parse_args()

    main(args)