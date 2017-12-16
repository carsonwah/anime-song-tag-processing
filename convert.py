#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
from mutagen.easyid3 import EasyID3
import sys

song_list = glob.glob(u'*/*.mp3')

for file in song_list:
	# get tag
	song = EasyID3(file)
	print 'Old album: '+str(song['album']).encode(sys.stdout.encoding, errors='replace')

	# get album name
	album = file
	start = album.find(u']') # [yymmdd] ...
	if start >= 0:
		album = album[start+1:]
	album = album.replace(u'TVアニメ',u'') # TVアニメ...
	end = album.find(u'[320K') # ... [320K]
	if end >= 0:
		album = album[:end]
	end = album.find(u'[MP3') # ... [MP3]
	if end >= 0:
		album = album[:end]
	album = album.strip()
	end = album.find(u'」／') # ...／artist
	if end >= 0:
		album = album[:end+1]
	print 'New album: '+album.encode(sys.stdout.encoding, errors='replace')

	# set new album
	song['album'] = album
	song.save()

	### backup
	# album = file.split(u'TVアニメ')
	# if (len(album) <= 1):
	# 	continue
	# album = album[1].split(u'」／')
	# if (len(album) != 2):
	# 	continue
	# album = album[0]
	# album += u'」'
