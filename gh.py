import feedparser
from datetime import datetime
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_changelog():
    try:
        f = feedparser.parse('https://github.blog/changelog/feed/')
        entries = f.get('entries', [])
        changelogs = dict(title=[], published=[], link=[])
        for i in range(min(8, len(entries))):
            entry = entries[i]
            changelogs["title"].append(entry.get('title', ''))
            changelogs["published"].append(entry.get('published', ''))
            changelogs["link"].append(entry.get('link', ''))
        return changelogs
    except Exception as e:
        print(f"Error in get_changelog: {e}")
        return dict(title=[], published=[], link=[])

def get_github_status():
    try:
        html = urlopen('https://www.githubstatus.com/', timeout=10)
        soup = BeautifulSoup(html, 'html.parser')
        raw = soup.find('div', {'class': 'incident-title font-large'})
        if raw:
            status = raw.get_text().strip()
            status = status.replace('Subscribe', '')
            print(status)
            return status
        else:
            return "Systems Operational"
    except URLError as e:
        print(f"Network error in get_github_status: {e}")
        return "Could not fetch status"
    except Exception as e:
        print(f"Error in get_github_status: {e}")
        return "Error"

def get_latest_incident():
    try:
        a = feedparser.parse('https://www.githubstatus.com/history.rss')
        entries = a.get('entries', [])
        incident = dict(title=[], published=[], link=[])
        for entry in entries:
            if 'maintenanceenddate' in entry:
                continue
            incident["title"].append(entry.get('title', ''))
            incident["published"].append(entry.get('published', ''))
            incident["link"].append(entry.get('link', ''))
            break   # Only the first non-maintenance entry
        return incident
    except Exception as e:
        print(f"Error in get_latest_incident: {e}")
        return dict(title=[], published=[], link=[])

def get_maintenance_events():
    try:
        a = feedparser.parse('https://www.githubstatus.com/history.rss')
        entries = a.get('entries', [])
        events = dict(title=[], endtime=[], link=[])
        date = datetime.now()
        current = date.timestamp()
        found = False
        for entry in entries:
            if 'maintenanceenddate' in entry:
                title = entry.get('title', '')
                endtime = entry.get('maintenanceenddate', '')
                link = entry.get('link', '')
                events["title"].append(title)
                events["endtime"].append(endtime)
                events["link"].append(link)
                found = True
                break
        if not found:
            events["title"].append('No maintenance event to report')
            events["endtime"].append('')
            events["link"].append('#')
        return events
    except Exception as e:
        print(f"Error in get_maintenance_events: {e}")
        return dict(title=['No maintenance event to report'], endtime=[''], link=['#'])

def get_incident_history():
    try:
        a = feedparser.parse('https://www.githubstatus.com/history.rss')
        entries = a.get('entries', [])
        incidentHistory = dict(title=[], published=[], link=[])
        for i in range(1, min(8, len(entries))):
            entry = entries[i]
            incidentHistory["title"].append(entry.get('title', ''))
            incidentHistory["published"].append(entry.get('published', ''))
            incidentHistory["link"].append(entry.get('link', ''))
        return incidentHistory
    except Exception as e:
        print(f"Error in get_incident_history: {e}")
        return dict(title=[], published=[], link=[])

def get_blogfeed():
    try:
        b = feedparser.parse('https://github.blog/feed/')
        entries = b.get('entries', [])
        blogfeed = dict(title=[], published=[], link=[])
        for i in range(min(10, len(entries))):
            entry = entries[i]
            blogfeed["title"].append(entry.get('title', ''))
            blogfeed["published"].append(entry.get('published', ''))
            blogfeed["link"].append(entry.get('link', ''))
        return blogfeed
    except Exception as e:
        print(f"Error in get_blogfeed: {e}")
        return dict(title=[], published=[], link=[])

def main():
    date = datetime.now()
    print(date.strftime("%a, %-d %b %Y %-H:%M:%S +0000"))
    print("GitHub Status:", get_github_status())
    print("Latest Incident:", get_latest_incident())
    print("Incident History:", get_incident_history())
    print("Blog Feed:", get_blogfeed())
    print("Changelog:", get_changelog())
    print("Maintenance Events:", get_maintenance_events())

if __name__ == "__main__":
    main()
