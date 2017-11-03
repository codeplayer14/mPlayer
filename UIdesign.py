
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 511)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.NowPlaying = QtWidgets.QLabel(self.centralWidget)
        self.NowPlaying.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.NowPlaying.setObjectName("NowPlaying")
        self.SongLabel = QtWidgets.QLabel(self.centralWidget)
        self.SongLabel.setGeometry(QtCore.QRect(20, 218, 111, 21))
        self.SongLabel.setObjectName("SongLabel")
        self.SongName = QtWidgets.QLabel(self.centralWidget)
        self.SongName.setGeometry(QtCore.QRect(18, 233, 361, 41))
        self.SongName.setObjectName("SongName")
        self.AlbumLabel = QtWidgets.QLabel(self.centralWidget)
        self.AlbumLabel.setGeometry(QtCore.QRect(20, 288, 67, 17))
        self.AlbumLabel.setObjectName("AlbumLabel")
        self.AlbumName = QtWidgets.QLabel(self.centralWidget)
        self.AlbumName.setGeometry(QtCore.QRect(20, 308, 351, 31))
        self.AlbumName.setObjectName("AlbumName")
        self.ArtistLabel = QtWidgets.QLabel(self.centralWidget)
        self.ArtistLabel.setGeometry(QtCore.QRect(20, 353, 67, 20))
        self.ArtistLabel.setObjectName("ArtistLabel")
        self.Artist = QtWidgets.QLabel(self.centralWidget)
        self.Artist.setGeometry(QtCore.QRect(20, 378, 361, 21))
        self.Artist.setObjectName("Artist")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 420, 801, 51))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("\n"
"background-color: rgb(239, 41, 41);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.MusicVal = QtWidgets.QSlider(self.frame)
        self.MusicVal.setGeometry(QtCore.QRect(216, 12, 301, 31))
        self.MusicVal.setOrientation(QtCore.Qt.Horizontal)
        self.MusicVal.setObjectName("MusicVal")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(597, 15, 31, 21))
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(239, 41, 41);")
        self.pushButton.setObjectName("pushButton")
        self.stopButton = QtWidgets.QPushButton(self.frame)
        self.stopButton.setGeometry(QtCore.QRect(560, 15, 30, 21))
        self.stopButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(239, 41, 41);")
        self.stopButton.setObjectName("stopButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 18, 31, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(524, 18, 31, 17))
        self.label_2.setObjectName("label_2")
        self.albumArt = QtWidgets.QLabel(self.centralWidget)
        self.albumArt.setGeometry(QtCore.QRect(20, 40, 191, 171))
        self.albumArt.setText("")
        self.albumArt.setObjectName("albumArt")
        self.MusicList = QtWidgets.QListWidget(self.centralWidget)
        self.MusicList.setGeometry(QtCore.QRect(430, 40, 281, 341))
        self.MusicList.setObjectName("MusicList")
        self.addDirectory = QtWidgets.QPushButton(self.centralWidget)
        self.addDirectory.setGeometry(QtCore.QRect(430, 360, 51, 25))
        self.addDirectory.setStyleSheet("color:white;")
        self.addDirectory.setObjectName("addDirectory")
        self.NowPlaying.raise_()
        self.AlbumLabel.raise_()
        self.AlbumName.raise_()
        self.ArtistLabel.raise_()
        self.Artist.raise_()
        self.frame.raise_()
        self.albumArt.raise_()
        self.MusicList.raise_()
        self.addDirectory.raise_()
        self.SongName.raise_()
        self.SongLabel.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 738, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NowPlaying.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Now Playing</span></p></body></html>"))
        self.SongLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#555753;\">Song</span></p></body></html>"))
        self.SongName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Song Name</span></p></body></html>"))
        self.AlbumLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#555753;\">Album</span></p></body></html>"))
        self.AlbumName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Album Name</span></p></body></html>"))
        self.ArtistLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#555753;\">Artist</span></p></body></html>"))
        self.Artist.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Artist Name</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "II"))
        self.stopButton.setText(_translate("MainWindow", "⏹"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0:00</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">--:--</span></p></body></html>"))
        self.addDirectory.setText(_translate("MainWindow", "+"))

