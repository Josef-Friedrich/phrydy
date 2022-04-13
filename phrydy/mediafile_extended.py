from mediafile import \
    ASFStorageStyle, \
    MediaField, \
    MediaFile, \
    MP3DescStorageStyle, \
    MP3StorageStyle, \
    MP4StorageStyle, \
    StorageStyle, \
    Image  # noqa: F401
from typing import Any, Dict, Generator


class MediaFileExtended(MediaFile):

    @classmethod
    def fields(cls) -> Generator[str, None, None]:
        """Get the names of all writable properties that reflect
        metadata tags (i.e., those that are instances of
        :class:`MediaField`).
        """
        seen = set()

        # Same fields are duplicate because they are overwritten in this
        # class.
        f: Dict[str, Any] = {}
        for field, descriptor in MediaFile.__dict__.items():
            f[field] = descriptor
        for field, descriptor in cls.__dict__.items():
            f[field] = descriptor

        for field, descriptor in f.items():
            if isinstance(descriptor, MediaField) and field not in seen:
                seen.add(field)
                yield field

    @classmethod
    def readable_fields(cls) -> Generator[str, None, None]:
        """Get all metadata fields: the writable ones from
        :meth:`fields` and also other audio properties.
        """
        for field in cls.fields():
            yield field
        for field in ('length', 'samplerate', 'bitdepth', 'bitrate',
                      'bitrate_mode', 'channels', 'encoder_info',
                      'encoder_settings', 'format'):
            yield field

    # albumartist_sort = MediaField(
    #     MP3DescStorageStyle(u'ALBUMARTISTSORT'),
    #     MP4StorageStyle('soaa'),
    #     StorageStyle('ALBUMARTISTSORT'),
    #     ASFStorageStyle('WM/AlbumArtistSortOrder'),
    # )
    albumartist_sort = MediaField(
        MP3StorageStyle('TSO2'),
        MP3DescStorageStyle('ALBUMARTISTSORT'),
        MP4StorageStyle('soaa'),
        StorageStyle('ALBUMARTISTSORT'),
        ASFStorageStyle('WM/AlbumArtistSortOrder'),
    )
    """Changed field. Uses TSO2"""

    # composer_sort = MediaField(
    #     MP3StorageStyle('TSOC'),
    #     MP4StorageStyle('soco'),
    #     StorageStyle('COMPOSERSORT'),
    #     ASFStorageStyle('WM/Composersortorder'),
    # )
    composer_sort = MediaField(
        MP3StorageStyle('TSOC'),
        MP3DescStorageStyle('composersortorder'),
        MP4StorageStyle('soco'),
        StorageStyle('composersort'),
        StorageStyle('composersortorder'),
        ASFStorageStyle('WM/ComposerSortOrder'),
    )
    """Changed field. Uses MP3 description storage style composersortorder."""

    # mb_workid = MediaField(
    #     MP3DescStorageStyle(u'MusicBrainz Work Id'),
    #     MP4StorageStyle('----:com.apple.iTunes:MusicBrainz Work Id'),
    #     StorageStyle('MUSICBRAINZ_WORKID'),
    #     ASFStorageStyle('MusicBrainz/Work Id'),
    # )
    mb_workid = MediaField(
        MP3DescStorageStyle('MusicBrainz Work Id'),
        MP4StorageStyle('----:com.apple.iTunes:MusicBrainz Work Id'),
        StorageStyle('MUSICBRAINZ_WORKID'),
        StorageStyle('musicbrainz work id'),
        ASFStorageStyle('MusicBrainz/Work Id'),
    )
    """Changed Field: The MusicBrainz’ Work ID"""

    mb_workhierarchy_ids = MediaField(
        MP3DescStorageStyle('MusicBrainz Work Hierarchy Ids'),
        MP4StorageStyle('----:com.apple.iTunes:'
                        'MusicBrainz Work Hierarchy Ids'),
        StorageStyle('MUSICBRAINZ_WORKHIERARCHY_IDS'),
        ASFStorageStyle('MusicBrainz/Work Hierarchy Ids'),
    )
    """
    All IDs in the work hierarchy. This field corresponds to the field
    ``work_hierarchy``. The top level work ID appears first. As separator a
    slash (``/``) is used.

    Example:

    ``e208c5f5-5d37-3dfc-ac0b-999f207c9e46``
    ``/``
    ``5adc213f-700a-4435-9e95-831ed720f348``
    ``/``
    ``eafec51f-47c5-3c66-8c36-a524246c85f8``
    """

    work = MediaField(
        MP3DescStorageStyle('Work'),
        MP4StorageStyle('----:com.apple.iTunes:WORK'),
        StorageStyle('Work'),
        ASFStorageStyle('WM/Work'),
    )
    """The last work in the work hierarchy."""

    work_hierarchy = MediaField(
        MP3DescStorageStyle('MusicBrainz Work Hierarchy'),
        MP4StorageStyle('----:com.apple.iTunes:MusicBrainz Work Hierarchy'),
        StorageStyle('MUSICBRAINZ_WORKHIERARCHY'),
        ASFStorageStyle('MusicBrainz/Work Hierarchy'),
    )
    """
    The hierarchy of works: The top level work appears first. As separator is
    this string used: ``-->``

    Example:

    ``Die Zauberflöte, K. 620``
    ``-->``
    ``Die Zauberflöte, K. 620: Akt I``
    ``-->``
    ``Die Zauberflöte, K. 620: Act I, Scene II. No. 2 Aria "Was hör' ...``

    """

    releasegroup_types = MediaField(
        MP3DescStorageStyle('MusicBrainz Release Group Types'),
        MP4StorageStyle('----:com.apple.iTunes:'
                        'MusicBrainz Release Group Types'),
        StorageStyle('MUSICBRAINZ_RELEASEGROUPTYPES'),
        ASFStorageStyle('MusicBrainz/Release Group Types'),
    )
    """This field collects all items in the MusicBrainz’ API related to
    type: ``type``, ``primary-type`` and``secondary-type-list``. Main usage
    of this field is to determine in a secure manner if the release is a
    soundtrack.

    .. code:: JSON

        "release-group": {
          "first-release-date": "1994-09-27",
          "secondary-type-list": [
            "Compilation",
            "Soundtrack"
          ],
          "primary-type": "Album",
          "title": "Pulp Fiction: Music From the Motion Picture",
          "type": "Soundtrack",
          "id": "1703cd63-9401-33c0-87c6-50c4ba2e0ba8"
        }

    """
