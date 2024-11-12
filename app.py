from flask import Flask, redirect, url_for, render_template
from gh import get_changelog, get_incident_history, get_latest_incident, get_blogfeed, get_github_status
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/dashboard/", code=302)

@app.route("/dashboard/")
def dashboard():
    changelogs = get_changelog()
    incident = get_latest_incident()
    status = get_github_status()
    incidentHistory = get_incident_history()
    blogfeed = get_blogfeed()
    now = datetime.now()
    time = now.strftime("%a, %-d %b %Y %-H:%M:%S ")

    return render_template("dashboard.html",
                           changelogs=changelogs,
                           incident=incident,
                           status=status,
                           incidentHistory=incidentHistory,
                           blogfeed=blogfeed,
                           time=time)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
