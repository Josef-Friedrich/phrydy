# -*- coding: utf-8 -*-

"""
Metadata fields:

    Ordinary metadata:

    - title
    - artist
    - artist_sort:         The “sort name” of the track artist
                           (e.g., “Beatles, The” or “White, Jack”).
    - artist_credit:       The track-specific artist credit name,
                           which may be a variation of the artist’s
                           “canonical” name.
    - artistsafe:          The first available value of this metatag
                           order: “albumartist” -> “artist” ->
                           “albumartist_credit” -> “artist_credit”
    - artistsafe_sort:     The first available value of this metatag
                           order: “albumartist_sort” ->
                           “artist_sort” -> “artistsafe”
    - artist_initial:      First character in lowercase of
                            “artistsafe_sort”
    - album
    - albumartist:         The artist for the entire album, which
                           may be different from the artists for the
                           individual tracks.
    - albumartist_sort
    - albumartist_credit
    - album_initial:       First character in lowercase of “album”.
    - genre
    - composer
    - grouping
    - year, month, day:    The release date of the specific release.
    - original_year, original_month, original_day:
                           The release date of the original version
                           of the album.
    - year_safe
    - track
    - tracktotal
    - disc
    - disctotal
    - disctrack:           Combination of disc and track in the
                           format: disk-track, e.g. 1-01, 3-099
    - lyrics
    - comments
    - bpm
    - comp:                 Compilation flag.
    - albumtype:            The MusicBrainz album type; the
                            MusicBrainz wiki has a list of type
                            names.
    - label
    - asin
    - catalognum
    - script
    - language
    - country
    - albumstatus
    - media
    - albumdisambig
    - disctitle
    - encoder

    Audio information:

    - length                (in seconds)
    - bitrate               (in kilobits per second, with units:
                            e.g., “192kbps”)
    - format                (e.g., “MP3” or “FLAC”)
    - channels
    - bitdepth              (only available for some formats)
    - samplerate            (in kilohertz, with units: e.g.,
                            “48kHz”)

    MusicBrainz and fingerprint information:

    - mb_trackid
    - mb_albumid
    - mb_artistid
    - mb_albumartistid
    - mb_releasegroupid
    - acoustid_fingerprint
    - acoustid_id
    """
