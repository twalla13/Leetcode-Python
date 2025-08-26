import os
import re
import json
import time
import shutil
import requests

# Folder categories (based on screenshots)
valid_topics = {
    "array": "arrays_strings",
    "string": "arrays_strings",
    "stack": "stacks_queues",
    "queue": "stacks_queues",
    "monotonic-stack": "stacks_queues",
    "tree": "trees",
    "graph": "trees",
    "breadth-first-search": "trees",
    "depth-first-search": "trees",
    "hash-table": "hashing",
    "linked-list": "linkedlists",
    "heap": "heaps",
    "greedy": "greedy",
    "binary-search": "binarysearch",
    "backtracking": "backtracking",
    "dynamic-programming": "dynamicprogramming"
}

repo_path = os.getcwd()
cache_file = os.path.join(repo_path, ".slug_topic_cache.json")

# Load or initialize cache
if os.path.exists(cache_file):
    with open(cache_file, "r") as f:
        slug_cache = json.load(f)
else:
    slug_cache = {}

headers = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0"
}

graphql_url = "https://leetcode.com/graphql"

def fetch_topic_from_leetcode(slug):
    query = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            topicTags {
              name
              slug
            }
          }
        }
        """
    }

    try:
        response = requests.post(graphql_url, json=query, headers=headers)
        data = response.json()
        tags = data["data"]["question"]["topicTags"]

        priority_order = [
            "hash-table", "linked-list", "stack", "queue", "monotonic-stack",
            "tree", "graph", "breadth-first-search", "depth-first-search",
            "heap", "greedy", "binary-search", "backtracking", "dynamic-programming",
            "array", "string"
        ]

        tags.sort(key=lambda tag: priority_order.index(tag["slug"]) if tag["slug"] in priority_order else len(priority_order))

        for tag in tags:
            if tag["slug"] in valid_topics:
                return valid_topics[tag["slug"]]
    except Exception as e:
        print(f"⚠️ Failed to fetch topic for {slug}: {e}")
    return None

for root, _, files in os.walk(repo_path):
    for filename in files:
        if not filename.endswith(".py") or filename == os.path.basename(__file__):
            continue

        filepath = os.path.join(root, filename)

        try:
            with open(filepath, "r") as f:
                first_line = f.readline()
        except:
            print(f"❌ Could not read file: {filename}")
            continue

        match = re.search(r"leetcode\.com/problems/([\w\-]+)/?", first_line)
        if not match:
            print(f"❓ Skipped (no link found): {filename}")
            continue

        slug = match.group(1)

        # Use cache if possible
        topic = slug_cache.get(slug)
        if not topic:
            topic = fetch_topic_from_leetcode(slug)
            slug_cache[slug] = topic
            time.sleep(0.5)  # prevent hitting rate limit

        if not topic:
            print(f"❓ Skipped (no topic found): {filename} ({slug})")
            continue

        dest_folder = os.path.join(repo_path, topic)
        os.makedirs(dest_folder, exist_ok=True)
        dst = os.path.join(dest_folder, filename)
        shutil.move(filepath, dst)
        print(f"✅ Moved {filename} → {topic}/")

# Save updated cache
with open(cache_file, "w") as f:
    json.dump(slug_cache, f, indent=2)