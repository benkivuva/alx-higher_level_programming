#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest) of a
specified repository by a given user using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for listing commits
    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            commits_data = response.json()
            # Print the most recent 10 commits
            for commit in commits_data[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error:", response.status_code)
            print("Failed to fetch commits.")
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
