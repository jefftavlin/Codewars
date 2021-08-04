def song_decoder(song):
    song = song.split('WUB')
    song = [l for l in song if l != '']
    return ' '.join(song)
