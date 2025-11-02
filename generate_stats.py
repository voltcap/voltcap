# generate_stats.py
import requests
import datetime
import os

USERNAME = "voltcap"  # change if needed
OUTPUT_FILE = "github_stats.svg"

# Fetch user data from GitHub API
url = f"https://api.github.com/users/{USERNAME}"
response = requests.get(url)
data = response.json()

# Basic check
if "message" in data and data["message"] == "Not Found":
    raise ValueError(f"User '{USERNAME}' not found on GitHub!")

# Extract stats
name = data.get("name", USERNAME)
public_repos = data.get("public_repos", 0)
followers = data.get("followers", 0)
following = data.get("following", 0)
updated = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Create SVG content
svg = f"""
<svg width="480" height="180" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <text x="50%" y="30" text-anchor="middle" fill="#58a6ff" font-size="20" font-family="monospace">{name}</text>
  <text x="50%" y="70" text-anchor="middle" fill="#c9d1d9" font-size="16" font-family="monospace">📦 Public Repos: {public_repos}</text>
  <text x="50%" y="100" text-anchor="middle" fill="#c9d1d9" font-size="16" font-family="monospace">👥 Followers: {followers} | Following: {following}</text>
  <text x="50%" y="140" text-anchor="middle" fill="#6e7681" font-size="12" font-family="monospace">Updated: {updated}</text>
</svg>
"""

# Save SVG file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"✅ Generated {OUTPUT_FILE} for {USERNAME}")
