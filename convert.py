#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import glob
import sys
import codecs

from mutagen.easyid3 import EasyID3

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

song_list = glob.glob(u'**/*.mp3', recursive=True)

print(song_list)

for file in song_list:
	# get tag
	song = EasyID3(file)
	# print('Old album: '+str(song['album']).encode(sys.stdout.encoding, errors='replace'))
	print('Old album: ' + song['album'][0])

	# get album name
	album = file.replace(u'『', u'「').replace(u'』',u'」')
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
	# print('New album: '+album.encode(sys.stdout.encoding, errors='replace'))
	print('New album: ' + album)

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
