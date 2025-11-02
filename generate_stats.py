import requests
from datetime import datetime

USERNAME = "voltcap"
url = f"https://api.github.com/users/{USERNAME}"

try:
    response = requests.get(url)
    data = response.json()
except Exception as e:
    print(f"Error fetching GitHub data: {e}")
    data = {}

followers = data.get("followers", 0)
public_repos = data.get("public_repos", 0)
created = data.get("created_at", "N/A")[:10]
name = data.get("name", USERNAME)
updated_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

svg = f"""<svg width="480" height="200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title {{ font: bold 20px monospace; fill: #00FFF7; }}
    .label {{ font: 14px monospace; fill: #40E0D0; }}
    .small {{ font: 11px monospace; fill: #3BBEBE; }}
  </style>

  <!-- Background -->
  <rect width="100%" height="100%" fill="#2B2A2A" />

  <!-- HUD Frame -->
  <rect x="10" y="10" width="460" height="180" rx="10" ry="10" fill="none" stroke="#00FFF7" stroke-width="1" opacity="0.5" />

  <!-- Title -->
  <text x="30" y="45" class="title">{name} // GITHUB NODE</text>

  <!-- Stats -->
  <text x="30" y="85" class="label">› Followers: {followers}</text>
  <text x="30" y="110" class="label">› Public Repos: {public_repos}</text>
  <text x="30" y="135" class="label">› Joined: {created}</text>

  <!-- Footer Info -->
  <text x="30" y="170" class="small">SYS UPDATE: {updated_time}</text>
  <text x="340" y="170" class="small">voltcap // GH MONITOR</text>
</svg>
"""

with open("github_stats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ github_stats.svg generated successfully for voltcap!")
