from flask import Blueprint, render_template, current_app, request
from ..services.news_api import fetch_news

bp = Blueprint("public", __name__)

@bp.route("/")
def index():
    default_q = "cybersecurity OR infosec OR ransomware OR phishing"
    q = (request.args.get("q") or default_q).strip()
    if len(q) > 120:
        q = q[:120]

    page_size = request.args.get("page_size", type=int, default=12)
    if page_size is None:
        page_size = 12
    page_size = max(5, min(page_size, 50))

    articles, error = fetch_news(
        api_key=current_app.config.get("NEWSAPI_KEY", ""),
        query=q,
        page_size=page_size,
    )
    return render_template(
    "index.html",
    articles=articles,
    error=error,
    query=q,
    page_class="bg-home",
)


@bp.route("/admin/login", methods=["GET"])
def admin_login():
    return render_template("login.html", page_class="bg-login")

