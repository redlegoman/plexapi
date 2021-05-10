#!/usr/bin/python3
from plexapi.myplex import MyPlexAccount

#
# this really simple script gets the items last added to each section,
# checks if they are "artist" types, or in other words "music" and
# then refreshes the metadata (reads the ID3 tags again).

# account = MyPlexAccount('<email>', '<password>')
# username and password found in ~/.config/plexapi/config.ini 
# see: https://python-plexapi.readthedocs.io/en/latest/configuration.html
account = MyPlexAccount()
plex = account.resource('plex').connect()  # returns a PlexServer instance


for section in plex.library.sections():
  print(section.title +"|"+section.type)
  music = plex.library.section(section.title)
  if section.type == "artist":
    for item in music.searchAlbums(**{"addedAt>>": "20d"}):
      print(item)
      item.refresh()

