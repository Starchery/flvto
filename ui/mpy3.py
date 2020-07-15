import sys

from typing import List
from PySide2.QtCore import QFile, QAbstractTableModel
from PySide2.QtCore import Qt
from PySide2.QtCore import QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QMainWindow, QTableView)


class App(QApplication):
    def __init__(self, filename: str, args: List[str] = None) -> None:
        QApplication.__init__(self, args)
        self.main = Main(filename)
        self.main = self.main.window
        print(self.main.transfersInfoParagraph.text().split("<br>"))

    def run(self) -> None:
        self.main.show()
        sys.exit(self.exec_())


class MainFactory(QMainWindow):
    def __new__(cls, filename: str) -> QMainWindow:
        inst: QMainWindow = QMainWindow.__new__(cls)
        inst = MainFactory.load_ui(filename)
        return inst

    @classmethod
    def load_ui(cls, filename: str) -> QMainWindow:
        ui_file: QFile = QFile("start2.ui")
        ui_file.open(QFile.ReadOnly)
        loader: QUiLoader = QUiLoader()
        window: QMainWindow = loader.load(ui_file)
        ui_file.close()
        return window


class Main(QMainWindow):
    def __init__(self, filename: str) -> None:
        QMainWindow.__init__(self)
        self.window = MainFactory(filename)
        self.songs = []
        self.songs.append(Song("Medhane", "DOLOMEALS"))
        self.songs.append(Song("Roc Marciano", "Here I Am"))
        self.songs.append(Song("Mid-Air Thief", "These Chains"))
        self.songs.append(Song("Suzi Analogue", "WAY LIVE"))
        self.songs.append(Song("Liv.e", "SirLadyMakemFall"))
        self.songs.append(Song("Frank Ocean", "In My Room"))
        self.playlist = Playlist2(self.songs)
        print(self.playlist.tView)
        self.oldTable = self.window.tableWidget
        self.window.tableWidget = self.playlist
        print(self.oldTable)


class Song:
    def __init__(self, artist: str = "", title: str = "") -> None:
        self.data = QStandardItem(text=f"{artist} - {title}")
        a = {
            "song_info": {
                "artist": artist,
                "title": title,
            },
            "video_info": {
                "name": f"{artist} - {title} (1974)",
                "uploader": "slam",
                "upload_date": "2019-08-24",
                "description": "Oldie but goodie!"
            },
            "meta": {
                "download_date": "2020-03-22",
                "download_dir": "DL/samples/2020-03-22",
                "encoding": "320kbps",
                "filename": f"{title}.mp3",
            },
        }
        self.data = QStandardItem(str(a))
        # self.data.setData(a)
        # for subdict in a:
        #     item = QStandardItem(str(subdict))
        #     self.data.appendRow(item)
        # for key in a:
        #     val = a[key]
        #     if isinstance(val, dict):
        #         self.data = QStandardItem(f"{key}: {str(val)}")
        #     else:
        #         self.data = QStandardItem(f"{key}: {str(val)}")
    # def __init__(self, artist: str = "", title: str = "") -> None:
    #     self.data: Dict[str, str] = {artist: artist, title: title}

    # def get(self, idx: int = 0) -> str:
    #     return self.data[list(self.data)[abs(idx)]]

    # def set(self, idx: int, val: str) -> None:
    #     self.data[list(self.data)[abs(idx)]] = val


class Playlist(QAbstractTableModel):
    def __init__(self, songs: List[Song] = []):
        QAbstractTableModel.__init__(self)
        self.songs: List[Song] = songs

    def rowCount(self,
                 parent: QModelIndex = QModelIndex()) -> int:
        return (0 if parent.isValid() else len(self.songs))

    def columnCount(self,
                    parent: QModelIndex = QModelIndex()) -> int:
        return (0 if parent.isValid() else 3)

    def data(self, index: QModelIndex,
             role: Qt.ItemDataRole = Qt.DisplayRole) -> str:
        return self.songs[index.row()].get(index.column())

    def headerData(self,
                   section: int,
                   orientation: Qt.Orientation = Qt.Horizontal,
                   role: Qt.ItemDataRole = Qt.DisplayRole) -> List[str]:
        return [val.get(section) for val in self.songs]

    def setData(self,
                index: QModelIndex,
                value: str,
                role: Qt.ItemDataRole = Qt.DisplayRole) -> bool:
        try:
            self.songs[index.row()].set(index.column(), value)
            self.dataChanged.emit(index, index)
            return True
        except (KeyError, ValueError):
            return False

    def insertRows(self,
                   row: int,
                   count: int,
                   parent: QModelIndex = QModelIndex()) -> bool:
        if not parent.isValid():
            return False

        try:
            self.beginInsertRows(parent, first=row, last=row + count)
            [self.songs.insert(row, Song()) for _ in range(count)]
            self.endInsertRows()
            return True
        except Exception:
            return False

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled


class Playlist2:
    def __init__(self, songs: List[Song]):
        r = len(songs)  # [Song1, Song2, Song3]
        c = 2
        self.table = QStandardItemModel(r, c)
        for row in range(r):
            i = QStandardItem(row)
            self.table.setItem(row, 0, i)
            self.table.setItem(row, 1, songs[row].data)

        self.tView = QTableView()
        self.tView.setModel(self.table)
        self.tView.clicked[QModelIndex].connect(self.clicked)

    def clicked(self, index):
        item = self.table.itemFromIndex(index)
        print(item)


def main(args: List[str] = []):
    app = App("start2.ui", args)
    app.run()


if __name__ == '__main__':
    main(sys.argv)
