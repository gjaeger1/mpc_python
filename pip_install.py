# Source - https://stackoverflow.com/a
# Posted by Ahmed
# Retrieved 2025-11-28, License - CC BY-SA 4.0

import os

import yaml

with open("env.yml") as file_handle:
    environment_data = yaml.safe_load(file_handle)

for dependency in environment_data["dependencies"]:
    if isinstance(dependency, dict):
        for lib in dependency["pip"]:
            os.system(f"pip install {lib}")
