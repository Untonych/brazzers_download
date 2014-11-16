Mechanism to download brazzers.com videos automatically while you sleep

Installation
============

You need to have a torrent client installed like Vuze, uTorrent or any
other.

Right now there are 2 scripts that you can use. Depending on the script
you'll need to install either a gem or a python package.

## Using the Ruby script
> gem install mechanize

## Using the Python script
> sudo pip install httplib2 beautifulsoup4

Place the python or ruby script anywhere and then use either a CRON job
in Linux or launchd (plist example provided in the repo, you just need
to edit the paths to the script) in OSX and you are done.
