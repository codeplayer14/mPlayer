# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 518)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(46, 52, 54);"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.NowPlaying = QtGui.QLabel(self.centralWidget)
        self.NowPlaying.setGeometry(QtCore.QRect(140, -11, 170, 50))
        self.NowPlaying.setObjectName(_fromUtf8("NowPlaying"))
        self.SongLabel = QtGui.QLabel(self.centralWidget)
        self.SongLabel.setGeometry(QtCore.QRect(20, 184, 111, 21))
        self.SongLabel.setObjectName(_fromUtf8("SongLabel"))
        self.SongName = QtGui.QLabel(self.centralWidget)
        self.SongName.setGeometry(QtCore.QRect(18, 224, 361, 41))
        self.SongName.setObjectName(_fromUtf8("SongName"))
        self.AlbumLabel = QtGui.QLabel(self.centralWidget)
        self.AlbumLabel.setGeometry(QtCore.QRect(20, 274, 67, 17))
        self.AlbumLabel.setObjectName(_fromUtf8("AlbumLabel"))
        self.AlbumName = QtGui.QLabel(self.centralWidget)
        self.AlbumName.setGeometry(QtCore.QRect(20, 311, 351, 31))
        self.AlbumName.setObjectName(_fromUtf8("AlbumName"))
        self.ArtistLabel = QtGui.QLabel(self.centralWidget)
        self.ArtistLabel.setGeometry(QtCore.QRect(20, 354, 67, 17))
        self.ArtistLabel.setObjectName(_fromUtf8("ArtistLabel"))
        self.Artist = QtGui.QLabel(self.centralWidget)
        self.Artist.setGeometry(QtCore.QRect(20, 380, 361, 21))
        self.Artist.setObjectName(_fromUtf8("Artist"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 420, 801, 51))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(239, 41, 41);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.MusicVal = QtGui.QSlider(self.frame)
        self.MusicVal.setGeometry(QtCore.QRect(250, 10, 301, 31))
        self.MusicVal.setOrientation(QtCore.Qt.Horizontal)
        self.MusicVal.setObjectName(_fromUtf8("MusicVal"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(597, 15, 31, 21))
        self.pushButton.setStyleSheet(_fromUtf8("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(239, 41, 41);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.stopButton = QtGui.QPushButton(self.frame)
        self.stopButton.setGeometry(QtCore.QRect(560, 15, 30, 21))
        self.stopButton.setStyleSheet(_fromUtf8("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(239, 41, 41);"))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.albumArt = QtGui.QLabel(self.centralWidget)
        self.albumArt.setGeometry(QtCore.QRect(110, 40, 231, 171))
        self.albumArt.setObjectName(_fromUtf8("albumArt"))
        self.MusicList = QtGui.QListWidget(self.centralWidget)
        self.MusicList.setGeometry(QtCore.QRect(430, 40, 281, 341))
        self.MusicList.setObjectName(_fromUtf8("MusicList"))
        self.addDirectory = QtGui.QPushButton(self.centralWidget)
        self.addDirectory.setGeometry(QtCore.QRect(430, 360, 51, 25))
        self.addDirectory.setStyleSheet(_fromUtf8("color:white;"))
        self.addDirectory.setObjectName(_fromUtf8("addDirectory"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.NowPlaying.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Now Playing</span></p></body></html>", None))
        self.SongLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Song</span></p></body></html>", None))
        self.SongName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Song Name</span></p></body></html>", None))
        self.AlbumLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Album</span></p></body></html>", None))
        self.AlbumName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Album Name</span></p></body></html>", None))
        self.ArtistLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Artist</span></p></body></html>", None))
        self.Artist.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Artist Name</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "II", None))
        self.stopButton.setText(_translate("MainWindow", "⏹", None))
        self.albumArt.setText(_translate("MainWindow", "Hello Peeps", None))
        self.addDirectory.setText(_translate("MainWindow", "+", None))

