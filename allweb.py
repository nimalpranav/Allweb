from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RENDER_API_KEY = os.getenv("RENDER_API_KEY")


def get_github():
    repos_list = []

    if not GITHUB_TOKEN:
        return []

    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    res = requests.get(url, headers=headers).json()

    if isinstance(res, dict):
        return []

    for repo in res:
        repos_list.append({
            "name": repo.get("name"),
            "url": repo.get("html_url")
        })

    return repos_list


def get_render():
    services_list = []

    if not RENDER_API_KEY:
        return []

    url = "https://api.render.com/v1/services"
    headers = {"Authorization": f"Bearer {RENDER_API_KEY}"}

    res = requests.get(url, headers=headers).json()

    if not isinstance(res, list):
        return []

    for s in res:
        srv = s.get("service", {})
        services_list.append({
            "name": srv.get("name"),
            "url": srv.get("serviceDetails", {}).get("url")
        })

    return services_list


@app.route("/")
def home():
    github = get_github()
    render = get_render()

    html = """
    <html>
    <head>
        <title>My Websites</title>
        <style>
            body { font-family: Arial; background: #0f172a; color: white; }
            h1 { text-align: center; }
            .card {
                background: #1e293b;
                padding: 15px;
                margin: 10px;
                border-radius: 10px;
            }
            a { color: #38bdf8; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>🚀 My Websites Dashboard</h1>

        <h2>GitHub</h2>
        {% for repo in github %}
            <div class="card">
                {{ repo.name }} <br>
                <a href="{{ repo.url }}" target="_blank">Open</a>
            </div>
        {% endfor %}

        <h2>Render</h2>
        {% for site in render %}
            <div class="card">
                {{ site.name }} <br>
                <a href="{{ site.url }}" target="_blank">Open</a>
            </div>
        {% endfor %}

    </body>
    </html>
    """

    return render_template_string(html, github=github, render=render)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)