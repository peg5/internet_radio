# internet_radio
A Python script to launch VLC and listen to an internet radio station.

# What This Does
When you run this script in the command line, along with one argument, it  searches a dictionary of internet radio stations, grabs the URL of the specific station and begins playing that station in VLC Media Player.

# Why I Wrote This
The Adobe Flash plugin is required to listen to most internet radio stations via the web, and said plugin is incompatible with the system at work. Also, none of the HTML5 players seem to work either.

So I took matters into my own hands. I started manually grabbing the URLs of the stations' live streams and opening them in VLC. I quickly became tired of going through this process every time I wanted to listen to music at work, so I wrote this script to automate it.