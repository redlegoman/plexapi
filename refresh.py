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
    if lib.uuid == "39725fb1-2c23-45ec-9277-a1b7c5b77f09" or lib.uuid == "f2497ca5-6d89-47e8-b1de-fd4763fa4e67" or lib.uuid == "bc1c2250-2c8c-4151-96db-de8e3dec0ae7":
      print(lib.title +", "+ lib.uuid+", "+path)
      print("-- scanning "+lib.title)
      scan = lib.update()
      print(scan)
      #scan = plex.library.librarysection.update(path)

#exit()



for section in plex.library.sections():
  print(section.title +"|"+section.type)
  music = plex.library.section(section.title)
  if section.type == "artist":
    #for item in music.searchAlbums(**{"addedAt>>": "20d"}):
    for item in music.searchAlbums(**{"addedAt>>": days}):
      print(item)
      item.refresh()

