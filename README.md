### GRMDASH

grmdash is a flask dashboard for public-facing GitHub updates 

It shows current status, most recent incident, incident history, changelogs, and blog posts. 

It mostly utilizes the feedparser module to parse public rss feeds to populate the data. Rather than tracking multiple feeds each day, grmdash provides a single, minimal pane of glass for awareness around public-facing changes. 

Run it locally with: 

`python3 -m flask run` 

If you want to have the app autoupdate based on code changes or page refreshes, run it in debug mode

`python3 -m flask run --debug` 

<img width="1316" alt="dash" src="https://github.com/user-attachments/assets/bc303eef-6669-49a8-bafe-1d1eabcd67af">


TODO: 
- setup a Pages site 
- update latest status utilizing a webhook for tracking incoming status changes
- consider update frequency and methodology 
- look into adding public roadmap entries
- implement testing and robust error-handling
- add logic to determine if incident is occurring now 
- update image based on incident status
