import feedparser

from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_changelog():
    f = feedparser.parse('https://github.blog/changelog/feed/')
    changelogs = dict(title=[], published=[], link=[])

    for i in range(0, 8):
        title = f['entries'][i]['title']
        published = f['entries'][i]['published']
        link = f['entries'][i]['link']
        changelogs["title"].append(title[:])
        changelogs["published"].append(published[:])
        changelogs["link"].append(link[:])
        if i == 7:
            return changelogs
        else:
            pass


def get_github_status():
    html = urlopen('https://www.githubstatus.com/')
    soup = BeautifulSoup(html, 'html.parser')

    raw = soup.find('h2', {'class': 'status font-large'})
    status = raw.get_text().strip()
    return status

def get_latest_incident():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    incident = dict(title=[], published=[], link=[])
    title = a['entries'][0]['title']
    published = a['entries'][0]['published']
    link = a['entries'][0]['link']

    incident["title"].append(title[:])
    incident["published"].append(published[:])
    incident["link"].append(link[:])

    return incident

def get_incident_history():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    incidentHistory = dict(title=[], published=[], link=[])
    for i in range(1, 8):
        title = a['entries'][i]['title']
        published = a['entries'][i]['published']
        link = a['entries'][i]['link']
        incidentHistory["title"].append(title[:])
        incidentHistory["published"].append(published[:])
        incidentHistory["link"].append(link[:])
        if i == 7:
            return incidentHistory
    else:
        pass

def get_blogfeed():
    b = feedparser.parse('https://github.blog/feed/')
    blogfeed = dict(title=[], published=[], link=[])
    for i in range(0, 10):
        title = b['entries'][i]['title']
        published = b['entries'][i]['published']
        link = b['entries'][i]['link']
#        if 'Availability' in title:

        blogfeed["title"].append(title[:])
        blogfeed["published"].append(published[:])
        blogfeed["link"].append(link[:])

        if i == 9:

            return blogfeed
        else:
            pass

def main():
    date = datetime.now()
    get_github_status()
    print(date.strftime("%a, %-d %b %Y %-H:%M:%S +0000"))
    get_latest_incident()
    get_incident_history()
    get_blogfeed()
    get_changelog()

main()
