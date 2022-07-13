import os
import shutil
import sys
import tempfile

# Test resources path.
TEST_RESOURCES_PATH = os.path.join(os.path.dirname(__file__), 'files')

# OS feature test.
HAVE_SYMLINK = sys.platform != 'win32'

# Convenience methods for setting up a temporary sandbox directory for tests
# that need to interact with the filesystem.


class TempDirMixin(object):
    """Text mixin for creating and deleting a temporary directory.
    """

    def create_temp_dir(self):
        """Create a temporary directory and assign it into `self.temp_dir`.
        Call `remove_temp_dir` later to delete it.
        """
        path = tempfile.mkdtemp()
        if not isinstance(path, bytes):
            path = path.encode('utf8')
        self.temp_dir = path

    def remove_temp_dir(self):
        """Delete the temporary directory created by `create_temp_dir`.
        """
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)
