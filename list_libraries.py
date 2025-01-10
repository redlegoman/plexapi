#!/usr/bin/python3
from plexapi.myplex import MyPlexAccount
import sys

#
# this really simple script gets the items last added to each section,
# checks if they are "artist" types, or in other words "music" and
# then refreshes the metadata (reads the ID3 tags again).

# account = MyPlexAccount('<email>', '<password>')
# username and password found in ~/.config/plexapi/config.ini 
# see: https://python-plexapi.readthedocs.io/en/latest/configuration.html
try:
  days=str(sys.argv[1])
except:
  days="1d"


print(days)

account = MyPlexAccount()
plex = account.resource('plex').connect()  # returns a PlexServer instance
plex_library = plex.library.section('Music: Tidal tmp')


for lib in plex.library.sections():
  for path in lib.locations:
    if lib.title.startswith("Music:"):
      print(lib.title +","+ lib.uuid +", "+path)

exit()


