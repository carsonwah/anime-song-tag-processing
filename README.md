# anime-song-tag-processing

Process MP3 ID3 tag for songs downloaded from 動漫花園 Mashin.

## Main function

- Modify "Album" attribute of songs for better information in tags  
  - E.g. Filename: `[171018] TVアニメ「DYNAMIC CHORD」EDテーマ「because the sky…」／KYOHSO [MP3]`
      - Original ablum tag: `"because the sky…"`
      - New ablum tag: `"「DYNAMIC CHORD」EDテーマ「because the sky…」"`

## Dependencies

- python3
- [Mutagen](http://mutagen.readthedocs.io/en/latest/index.html)

## Run

- Run in same directory as the songs

```bash
cd songs/
python convert.py
```

## Other useful tools

- [Map3tag](https://www.mp3tag.de/en/)
