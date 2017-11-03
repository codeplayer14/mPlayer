import time
from playsound import playsound
import requests
import configparser
import base64
import vlc
from subprocess import call
from eyed3 import id3
from PyQt5 import QtCore, QtGui,QtWidgets

from PyQt5.QtWidgets import QAction,QFileDialog
from PyQt5.QtGui import QPixmap,QIcon
import sys
import os
import UIdesign
from mutagen.mp3 import MP3
import threading

# pic = QtGui.Label(window)

# tag = id3.Tag()
# tag.parse('FindMe.mp3')
# artist = tag.artist
# FNULL = open(os.devnull, 'w')	
# call(['eyeD3','--write-images='+'./','FindMe.mp3'], stdout=FNULL)


# audio = eyed3.load("cool.mp3")
# print(audio.tag.artist)
# tag.link('cool.mp3')
# print(tag.getArtist())

class moveSlider(threading.Thread):

	def __init__(self,appObj):

		threading.Thread.__init__(self)
		self.appObj = appObj
		self.seconds=0

	def run(self):
		song = self.appObj.currentTrack
		while(self.seconds<self.appObj.duration and self.appObj.songStatus=="Play"):
			time.sleep(1)
			self.seconds = self.seconds+1
			self.appObj.MusicVal.setValue(self.seconds)
			if(song != self.appObj.fileName or self.appObj.songStatus =='Stop' ):
				break


class dataFetcher(threading.Thread):

	def __init__(self,appObj):

		# print("here")
		threading.Thread.__init__(self)
		self.appObj = appObj

	def run(self):
		_translate = QtCore.QCoreApplication.translate
		tag = id3.Tag() 
		tag.parse(self.appObj.fileName)

		artistName = "Unavailable"
		albumName = "Unavailable"
		songName = "Unavailable"

		if(tag.artist is not None):
			artistName = tag.artist
		
		if(tag.album is not None):
			albumName = tag.album

		if(tag.title is not None):
			songName = tag.title

		self.appObj.Artist.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600; color:#ffffff;\">"+artistName+"</span></p></body></html>"))
		self.appObj.SongName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">"+songName+"</span></p></body></html>"))
		self.appObj.AlbumName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600; color:#ffffff;\">"+albumName+"</span></p></body></html>"))       

class ExampleApp(QtWidgets.QMainWindow,UIdesign.Ui_MainWindow):
	
	def onClick(self):
		if self.currentTrack != self.fileName:
			self.count=0

		if self.songStatus is "Pause" or self.songStatus is 'Stopped':
			self.songStatus= "Play"
			self.pushButton.setText("||")
			if self.count==0:
				
				self.MusicVal.setValue(0)
				dataFetchThread = dataFetcher(self)
				dataFetchThread.start()
				self.currentTrack = self.fileName
				self.track = vlc.MediaPlayer('file://'+self.currentTrack)
				self.duration = MP3(self.fileName).info.length
				self.MusicVal.setMaximum(self.duration)
				self.progressBar = moveSlider(self)		
				self.progressBar.start()

				self.track.play()
				self.count=1
			else:
				self.track.pause()
		else:
			self.songStatus = "Pause"
			self.pushButton.setText(">")
			self.track.pause()


		print(self.artist)
	def __init__(self,parent=None):

		super(ExampleApp,self).__init__(parent)

		self.currentTrack = None
		self.setupUi(self)
		self.setUI()
		self.progressBar = None
		self.artist = None

	def setUI(self):

		self.count=0
		self.pushButton.setText(">")
		# self.MusicVal.setMaximum(30)
		self.songStatus = "Pause"
		self.stopButton.clicked.connect(self.stopMusic)

		self.pushButton.clicked.connect(self.onClick)
		self.pixelImage = QPixmap('img.jpg')
		self.pixelImage= self.pixelImage.scaled(128,128)
		# self.pixelImage.scaledToHeight(30)
		self.albumArt.setPixmap(self.pixelImage)
		print(self.MusicVal.setValue(0))

		self.addDirectory.clicked.connect(self.showDialog)
		
		self.MusicList.currentItemChanged.connect(self.selectTrack)
		# fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '/home')
		# self.showMaximized()

	def selectTrack(self):
		self.fileName = self.MusicList.currentItem().text()
		self.fileName = self.currentFolder+'/'+self.fileName
		
	
	def stopMusic(self):
		self.track.stop()
		self.songStatus = "Stopped"
		self.MusicVal.setValue(0)


	def showDialog(self):
		fname = QFileDialog.getExistingDirectory()
		self.currentFolder = fname
		for file in os.listdir(fname):
			if file[-4:] =='.mp3':
				self.MusicList.addItem(file)

		# with folder:
		# 	data=folder.read()
		# 	print(data)
	# def listMusic(self,directoryName):



def main():
	
	app = QtWidgets.QApplication(sys.argv)
	form = ExampleApp()

	form.show()
	app.exec_()


if __name__ == '__main__':
	main()
# def make_authorization_headers(client_id, client_secret):
#     auth_header = base64.b64encode(six.text_type(client_id + ':' + client_secret).encode('ascii'))
#     return {'Authorization': 'Basic %s' % auth_header.decode('ascii')}

# Config = configparser.ConfigParser()
# Config.read('config.ini')
# idVal = Config.get('client_id','idVal')
# secretVal  = Config.get('client_secret','secretVal')

# grant_type = 'client_credentials'

# url = 'https://accounts.spotify.com/api/token'
# body_params = {'grant_type' : grant_type}

# authHeader = make_authorization_headers(idVal,secretVal)

# reqObj = requests.post(url,data=body_params,headers=authHeader)

# authToken  = reqObj.json().get('access_token')
# print(authToken)

# header = {'Authorization':'Bearer '+authToken}
# track =  requests.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V',headers=header)

# print(track.json())




# post_payload = {'grant_type':grant_type,'code':code}
# postObj = requests.post('https://accounts.spotify.com/api/'+grant_token)

