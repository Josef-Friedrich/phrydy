import unittest
from phrydy import MediaFile

class TestPackageInterface(unittest.TestCase):
    def setUp(self):
        import os
        mp3 = os.path.join(os.path.dirname(__file__), 'files','full.mp3')
        self.media = MediaFile(mp3)

    def test_title(self):
        self.assertEqual(self.media.title, 'fulll')

    def test_artitst(self):
        self.assertEqual(self.media.artist, 'the artist')

if __name__ == '__main__':
    unittest.main()
