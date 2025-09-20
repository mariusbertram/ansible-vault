import requests
import re
import json
from collections import defaultdict


def list_versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['releases'].keys()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from PyPI: {e}")
        return []

# Group all versions by major version and return the latest version for the n most recent majors
def get_latest_per_major(versions, count=4):
    major_dict = defaultdict(list)
    semver_pattern = re.compile(r'^(\d+)\.(\d+)\.(\d+)(?:[.-].*)?$')
    for v in versions:
        match = semver_pattern.match(v)
        if match:
            major = int(match.group(1))
            major_dict[major].append(v)
    latest = []
    for major in sorted(major_dict.keys(), reverse=True)[:count]:
        # Sort all versions of this major by SemVer and pick the latest
        latest_version = sorted(major_dict[major], key=lambda x: [int(i) for i in re.match(r'^(\d+)\.(\d+)\.(\d+)', x).groups()], reverse=True)[0]
        latest.append(latest_version)
    return latest

if __name__ == "__main__":
    versions = list_versions('ansible')
    if versions:
        latest_versions = get_latest_per_major(versions)
        with open('.ansible_versions.json', 'w') as f:
            json.dump(latest_versions, f)
        print(latest_versions)
    else:
        print("No versions found or error occurred.")
