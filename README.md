# ARGO bot, both that likes tweets :robot:

Twitter bot named ARGO which likes tweets. Made with python and selenium. **!!!!!Just be advised Twitter doesn't like automatic liking and your account can be suspended for a few days!!!!!**

## How does it work

It opens selenium and logs into your account. Then goes to the specified tag and loads all tweets on the page. Than it scrolls and loads again. This goes until it repeats this process enough times specified in historySearch variable. Than goes for another specified tags and so on. After loading all tweets from all tags it starts to like them. With some brake (TTL). After his all tweets are liked he gets a pause and after that repeats the whole process.

## Install

You need python3 and few conda packages to run this, also **MOZZILA BROWSER!**

```
conda install -c conda-forge geckodriver
conda install -c conda-forge selenium
```

## Variables

In code there are three variables ttl, breakTime and historySearch. You can modify this to make bot faster (more suspicious) or slower (less suspicious). Also the times are in seconds!

* TTL - break between each like
* breakTime - time between new posts to like can be loaded
* historySearch - how many times should the feed scroll and load all tweets before considering the tag "finished"

## Running

You just need to provide email and passord + tags that you would like the bot to like

```
python main.py "EMAIL" "PASSWORD" "TAG" "TAG" "TAG" ...
```

For example

```
python main.py "..." "..." "python" "gamedev" "vr"
```