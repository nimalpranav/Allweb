import requests

# 🔑 Add your tokens here
GITHUB_TOKEN = "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"
RENDER_API_KEY = "rnd_y9qW4wZImCWKMOV5PQLiUX9PhVr2"
# ----------------------------
# 📦 GitHub Repositories
# ----------------------------
def get_github_repos():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    repos = response.json()

    print("\n🔵 GitHub Websites:\n")
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        print(f"{name} → {url}")

# ----------------------------
# ☁️ Render Services
# ----------------------------
def get_render_services():
    url = "https://api.render.com/v1/services"
    headers = {
        "Authorization": f"Bearer {RENDER_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    services = response.json()

    print("\n🟣 Render Websites:\n")
    for service in services:
        name = service["service"]["name"]
        url = service["service"].get("serviceDetails", {}).get("url", "No URL")
        print(f"{name} → {url}")

# ----------------------------
# 🚀 Run
# ----------------------------
get_github_repos()
get_render_services()