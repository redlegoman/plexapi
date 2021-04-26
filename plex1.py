#!/usr/bin/python3
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount()
plex = account.resource('plex').connect()  # returns a PlexServer instance

for section in plex.library.sections():
  print(section.title)
  music = plex.library.section(section.title)
  for item in music.recentlyAdded(maxresults=1):
    print(item)
    print(item.type)
  
#
#for playlist in plex.playlists():
    #print(playlist.title)
#

#for item in plex.library.recentlyAdded():
#  if item.type == "album":
#    print(item)
#    print(item.type)
#    item.refresh()

#music = plex.library.section('Music')
#print(music.filterTypes())
#for item in music.recentlyAdded(maxresults=1):
  #print(item)
  #print(item.type)


