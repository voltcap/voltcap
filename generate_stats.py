import requests

USERNAME = "voltcap"
user_data = requests.get(f"https://api.github.com/users/{USERNAME}").json()
repos = requests.get(f"https://api.github.com/users/{USERNAME}/repos").json()

total_stars = sum(r["stargazers_count"] for r in repos)
public_repos = len(repos)

svg = f"""<svg width="480" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0D0D0D" />
  <text x="24" y="40" font-size="22" font-family="monospace" fill="#00FFB3">voltcap</text>
  <text x="24" y="70" font-size="14" font-family="monospace" fill="#CCCCCC">
    ⭐ Stars: {total_stars}
  </text>
  <text x="24" y="95" font-size="14" font-family="monospace" fill="#CCCCCC">
    📦 Public Repos: {public_repos}
  </text>
  <text x="24" y="120" font-size="14" font-family="monospace" fill="#CCCCCC">
    👥 Followers: {followers}
  </text>
  <rect x="20" y="150" width="440" height="2" fill="#00FFB3" />
  <text x="24" y="175" font-size="10" fill="#888">Last updated automatically</text>
</svg>"""

with open("github_stats.svg", "w") as f:
    f.write(svg)
