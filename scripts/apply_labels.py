import os
import json
import requests
import sys
import re
from urllib.parse import quote

REPO_OWNER = os.environ.get("REPO_OWNER")
REPO_NAME = os.environ.get("REPO_NAME")
TOKEN = os.environ.get("GITHUB_TOKEN")

if not all([REPO_OWNER, REPO_NAME, TOKEN]):
    print("Error: REPO_OWNER, REPO_NAME or GITHUB_TOKEN is missing.")
    sys.exit(1)

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def normalize(s):
    if not s:
        return ""
    return re.sub(r'\s+', ' ', s.strip()).lower()

def get_existing_labels():
    labels = []
    page = 1
    while True:
        url = f"{BASE_URL}?per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to fetch labels. Status: {response.status_code}")
            sys.exit(1)
        data = response.json()
        if not data:
            break
        labels.extend(data)
        page += 1
    return {normalize(l['name']): l for l in labels}

def sync_labels():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'labels.json')
    
    try:
        with open(json_path, 'r') as f:
            desired_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: labels.json not found at {json_path}")
        sys.exit(1)

    current_map = get_existing_labels()
    desired_map_keys = set()

    for label in desired_list:
        name = label['name']
        color = label['color'].replace("#", "")
        description = label.get('description', "")
        norm_name = normalize(name)
        
        desired_map_keys.add(norm_name)
        
        data = {
            "name": name,
            "color": color,
            "description": description
        }

        if norm_name in current_map:
            print(f"Updating: {name}")
            encoded_name = quote(current_map[norm_name]['name'])
            requests.patch(f"{BASE_URL}/{encoded_name}", headers=HEADERS, json=data)
        else:
            print(f"Creating: {name}")
            requests.post(BASE_URL, headers=HEADERS, json=data)

    for norm_name, label_obj in current_map.items():
        if norm_name not in desired_map_keys:
            real_name = label_obj['name']
            print(f"Deleting: {real_name}")
            requests.delete(f"{BASE_URL}/{quote(real_name)}", headers=HEADERS)

    print("Sync complete.")

if __name__ == "__main__":
    sync_labels()
