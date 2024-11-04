from flask import Flask, redirect, url_for, render_template
from gh import get_changelog, get_incident_history, get_latest_incident, get_availability_reports, get_github_status
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("minimal.html")

@app.route("/dashboard/")
def dashboard():
    changelogs = get_changelog()
    incident = get_latest_incident()
    status = get_github_status()
    incidentHistory = get_incident_history()
    availabilityReports = get_availability_reports()
    now = datetime.now()
    time = now.strftime("%a, %-d %b %Y %-H:%M:%S +0000")

    return render_template("dashboard.html",
                           changelogs=changelogs,
                           incident=incident,
                           status=status,
                           incidentHistory=incidentHistory,
                           availabilityReports=availabilityReports,
                           time=time)


if __name__ == "__main__":
    app.run(debug=True)
