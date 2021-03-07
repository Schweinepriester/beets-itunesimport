from beets.plugins import BeetsPlugin
import pythoncom
import win32com.client as win32

class ItunesImportPlugin(BeetsPlugin):
    def __init__(self):
        super(ItunesImportPlugin, self).__init__()
        self.register_listener('album_imported', self.album_imported)

    def album_imported(self, lib, album):
        dir = album.item_dir()
        self._log.debug('album dir: ' + dir.decode("utf-8"))
        if dir:
            pythoncom.CoInitialize()  # threading, added via https://stackoverflow.com/a/51240037
            itunes = win32.gencache.EnsureDispatch('iTunes.Application')
            lib = itunes.LibraryPlaylist
            lib.AddFile(dir)
