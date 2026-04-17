import requests
import os

# 🔐 Get tokens from environment (IMPORTANT for Render)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RENDER_API_KEY = os.getenv("RENDER_API_KEY")

# ----------------------------
# 🔵 GitHub Repositories
# ----------------------------
def get_github_repos():
    print("\n🔵 GitHub Websites:\n")

    if not GITHUB_TOKEN:
        print("❌ GITHUB_TOKEN not set")
        return

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        print("❌ GitHub request failed:", e)
        return

    # 🚨 Handle API errors
    if isinstance(data, dict) and "message" in data:
        print("❌ GitHub Error:", data["message"])
        return

    # ✅ Show repos
    for repo in data:
        name = repo.get("name", "No name")
        html_url = repo.get("html_url", "No URL")

        # 🔥 Optional: Detect GitHub Pages
        pages_url = None
        if repo.get("has_pages"):
            pages_url = f"https://{repo['owner']['login']}.github.io/{name}"

        print(f"📦 {name}")
        print(f"   Repo: {html_url}")
        if pages_url:
            print(f"   🌐 Live: {pages_url}")
        print()


# ----------------------------
# 🟣 Render Services
# ----------------------------
def get_render_services():
    print("\n🟣 Render Websites:\n")

    if not RENDER_API_KEY:
        print("❌ RENDER_API_KEY not set")
        return

    url = "https://api.render.com/v1/services"
    headers = {
        "Authorization": f"Bearer {RENDER_API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        print("❌ Render request failed:", e)
        return

    # 🚨 Handle API errors
    if not isinstance(data, list):
        print("❌ Render Error:", data)
        return

    # ✅ Show services
    for service in data:
        srv = service.get("service", {})

        name = srv.get("name", "No name")
        url = srv.get("serviceDetails", {}).get("url", "No URL")
        type_ = srv.get("type", "Unknown")

        print(f"🚀 {name}")
        print(f"   Type: {type_}")
        print(f"   🌐 URL: {url}")
        print()


# ----------------------------
# 🚀 MAIN
# ----------------------------
if __name__ == "__main__":
    print("🔍 Fetching your websites...\n")

    get_github_repos()
    get_render_services()

    print("\n✅ Done!\n")    
    for service in services:
        name = service["service"]["name"]
        url = service["service"].get("serviceDetails", {}).get("url", "No URL")
        print(f"{name} → {url}")

# ----------------------------
# 🚀 Run
# ----------------------------
get_github_repos()
get_render_services()
