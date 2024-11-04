import feedparser

from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_changelog():
    f = feedparser.parse('https://github.blog/changelog/feed/')
    changelogs = []

    for i in range(0, 8):
        title = f['entries'][i]['title']
        published = f['entries'][i]['published']
        link = f['entries'][i]['link']
        changelogs.append(title)
        changelogs.append(published)
        changelogs.append(link)
        if i == 7:
            return changelogs
        else:
            pass




def get_github_status():
    html = urlopen('https://www.githubstatus.com/')
    soup = BeautifulSoup(html, 'html.parser')
    raw = soup.find('span', {'class': 'status font-large'})

    status = raw.text.lstrip()

    if 'All Systems Operational' in status:
        print(f"\n🟢 {status}")
        return status
    else:
        print(f"\n🟠 {status}")
        return status

def get_latest_incident():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    incident = []
    title = a['entries'][0]['title']
    published = a['entries'][0]['published']
    link = a['entries'][0]['link']

    incident.append(title)
    incident.append(published)
    incident.append(link)
    return incident

    #print(f"<h3>{title}</h3>"
          #f"<a href='{link}'>Incident Link</a>"
          #f"<p>{published}</p>")

def get_incident_history():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    incidentHistory = {}
    for i in range(1, 8):
        title = a['entries'][i]['title']
        published = a['entries'][i]['published']
        link = a['entries'][i]['link']


        incidentHistory.(title)
        incidentHistory.(published)
        incidentHistory.(link)

    if i == 7:

        return incidentHistory
    else:
        pass

def get_availability_reports():
    b = feedparser.parse('https://github.blog/feed/')
    availabilityReports = []
    for i in range(0, 10):
        title = b['entries'][i]['title']
        published = b['entries'][i]['published']
        link = b['entries'][i]['link']
#        if 'Availability' in title:

        availabilityReports.append(title)
        availabilityReports.append(published)
        availabilityReports.append(link)

        if i == 9:

            return availabilityReports
        else:
            pass

def main():
    date = datetime.now()
    get_github_status()
    print(date.strftime("%a, %-d %b %Y %-H:%M:%S +0000"))
    get_latest_incident()
    get_incident_history()
    get_availability_reports()
    get_changelog()

main()
