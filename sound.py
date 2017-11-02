
from playsound import playsound
import requests
import configparser
import base64
import pygame
from subprocess import call
from eyed3 import id3
from PyQt5 import QtCore, QtGui,QtWidgets

from PyQt5.QtWidgets import QAction,QFileDialog
from PyQt5.QtGui import QPixmap,QIcon
import sys
import os
import UIdesign


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

class ExampleApp(QtWidgets.QMainWindow,UIdesign.Ui_MainWindow):
	
	def onClick(self):

		if self.currentTrack != self.fileName:
			self.count=0

		if self.pushButton.state is "Pause":
			self.pushButton.state= "Play"
			self.pushButton.setText("||")
			if self.count==0:
				wavFile = self.fileName[:len(self.fileName)-4]+'.wav'
				print(wavFile)
				call(['ffmpeg', '-i', self.fileName,wavFile])
				pygame.mixer.music.load(wavFile)
				self.currentTrack = self.fileName
				self.count=1
				pygame.mixer.music.play()
			else:
				pygame.mixer.music.unpause()
		else:
			self.pushButton.state = "Pause"
			self.pushButton.setText(">")
			pygame.mixer.music.pause()

	def __init__(self,parent=None):

		super(ExampleApp,self).__init__(parent)

		self.currentTrack = None
		self.setupUi(self)
		self.setUI()

	def setUI(self):
		self.count=0
		self.pushButton.setText(">")
		self.MusicVal.setMaximum(30)
		self.pushButton.state = "Pause"

		self.pushButton.clicked.connect(self.onClick)
		self.pixelImage = QPixmap('img.jpg')
		self.pixelImage= self.pixelImage.scaled(64,64)
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
		pygame.mixer.music.load(self.fileName)
		

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
	pygame.mixer.init()
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

