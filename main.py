import feedparser
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_changelog():
    f = feedparser.parse('https://github.blog/changelog/feed/')
    for i in range(0, 8):
        title = f['entries'][i]['title']
        published = f['entries'][i]['published']
        link = f['entries'][i]['link']

        print(f"<h3>{title}</h3>"
              f"<a href='{link}'>Change Entry</a>"
              f"<p>{published}</p>")

def get_github_status():
    html = urlopen('https://www.githubstatus.com/')
    soup = BeautifulSoup(html, 'html.parser')
    raw = soup.find('span', {'class': 'status font-large'})

    status = raw.text.lstrip()

    if 'All Systems Operational' in status:
        print(f"<h3>🟢 {status}</h3>")
    else:
        print(f"<h3>🟠 {status}</h3>")


def get_latest_incident():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    title = a['entries'][0]['title']
    published = a['entries'][0]['published']
    link = a['entries'][0]['link']
    print(f"<h3>{title}</h3>"
          f"<a href='{link}'>Incident Link</a>"
          f"<p>{published}</p>")

def get_incident_history():
    a = feedparser.parse('https://www.githubstatus.com/history.rss')
    for i in range(1, 4):
        title = a['entries'][i]['title']
        published = a['entries'][i]['published']
        link = a['entries'][i]['link']
        print(f"<h3>{title}</h3>"
              f"<a href='{link}'>Incident Link</a>"
              f"<p>{published}</p>")

def get_availability_reports():
    b = feedparser.parse('https://github.blog/feed/')
    for i in range(0, 10):
        title = b['entries'][i]['title']
        published = b['entries'][i]['published']
        link = b['entries'][i]['link']
        if 'Availability' in title:

            print(f"<h3>{title}</h3>"
                  f"<a href='{link}'>Article Link</a>"
                  f"<p>{published}</p>")
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
