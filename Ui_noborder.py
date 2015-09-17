# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoBorder.ui'
#
# Created: Thu Jun 26 17:18:32 2014
#	  by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import images, ConfigParser, pythoncom, ctypes, ctypes.wintypes, sip, sys, win32api, win32con, sip
# from win32com.shell import shell, shellcon
from PIL import Image


try:
	_fromUtf8 = QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
		
try:
	_toUtf8 = QString.toUtf8
except AttributeError:
	def _toUtf8(s):
		return s

try:
	_encoding = QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig)

fileTypes = ['*.jpg', '*.png', '*.bmp', '*.gif', '*.jpeg', '*.ico', '*.ppm', '*.tiff']
		
class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		sip.setdestroyonexit(False)
		self.setObjectName(_fromUtf8("MainWindow"))
		icon = QIcon()
		icon.addPixmap(QPixmap(_fromUtf8(":/icon.png")), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.setWindowTitle('PhotoViewer')
		self.resize(779, 488)
		self.setMinimumSize(350, 300)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.centralwidget = QWidget(self)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout = QVBoxLayout(self.centralwidget)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.setAttribute(Qt.WA_TranslucentBackground)
		
		# title bar setup
		self.title = QFrame(self.centralwidget)
		self.title.setMinimumSize(QSize(0, 30))
		self.title.setMaximumSize(QSize(16777215, 30))
		self.title.setLayoutDirection(Qt.LeftToRight)
		self.title.setFrameShape(QFrame.NoFrame)
		self.title.setFrameShadow(QFrame.Raised)
		self.title.setObjectName(_fromUtf8("title"))
		self.horizontalLayout = QHBoxLayout(self.title)
		self.horizontalLayout.setSpacing(0)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setContentsMargins(5, 0, 5, 0)
		self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label_1 = QLabel(self.title)
		self.label_1.setScaledContents(True)
		self.label_1.setObjectName(_fromUtf8("label_1"))	
		self.label_1.setMaximumSize(16, 16)
		self.label = QLabel(self.title)
		self.label.setContentsMargins(5, 0, 0, 0)
		self.label.setScaledContents(False)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout.addWidget(self.label_1)
		self.horizontalLayout.addWidget(self.label)
		self.horizontalLayout.addStretch()
		self.skinBt = PushButton(self.title)
		self.skinBt.loadPixmap(":/skin_button.png")
		self.horizontalLayout.addWidget(self.skinBt, 0, Qt.AlignTop)		
		self.menuBt = PushButton(self.title)
		self.menuBt.loadPixmap(":/main_menu.png")
		self.horizontalLayout.addWidget(self.menuBt, 0, Qt.AlignTop)		
		self.minBt = PushButton(self.title)
		self.minBt.loadPixmap(":/min_button.png")
		self.horizontalLayout.addWidget(self.minBt, 0, Qt.AlignTop)
		self.maxBt = PushButton(self.title)
		self.maxBt.loadPixmap(":/max_button.png")
		self.horizontalLayout.addWidget(self.maxBt, 0, Qt.AlignTop)
		self.closeBt = PushButton(self.title)
		self.closeBt.loadPixmap(":/close_button.png")
		self.horizontalLayout.addWidget(self.closeBt, 0, Qt.AlignTop)
		self.verticalLayout.addWidget(self.title)
		# main menu
		self.main_menu = QMenu(self.title)	
		# File menu
		self.action_file =  QMenu(self.main_menu)
		self.open_m = QAction(self.action_file)
		self.save_m = QAction(self.action_file)
		self.settings_m = QAction(self.action_file)
		self.print_m = QAction(self.action_file)
		self.exit_m = QAction(self.action_file)
		self.action_file.addAction(self.open_m)
		self.action_file.addAction(self.save_m)
		self.action_file.addSeparator()
		self.action_file.addAction(self.settings_m)
		self.action_file.addSeparator()
		self.action_file.addAction(self.print_m)
		self.action_file.addSeparator()
		self.action_file.addAction(self.exit_m)		
		#About menu
		self.action_about =  QMenu(self.main_menu)
		self.help_m = QAction(self.action_about)
		self.about_m = QAction(self.action_about)
		self.action_about.addAction(self.help_m)
		self.action_about.addSeparator()
		self.action_about.addAction(self.about_m)		
		self.main_menu.addAction(self.action_file.menuAction())
		self.main_menu.addAction(self.action_about.menuAction())		
		self.action_file.setMinimumWidth(150)				
		
		# skin menu
		self.skin_menu = QMenu(self.title)
		self.orange = QAction(self.skin_menu)
		self.blue = QAction(self.skin_menu)
		self.red = QAction(self.skin_menu)
		self.transparent = QAction(self.skin_menu)
		self.orange.setCheckable(True)
		self.blue.setCheckable(True)
		self.red.setCheckable(True)
		self.transparent.setCheckable(True)
		self.themeGroup = QActionGroup(self.skin_menu)
		self.themeGroup.addAction(self.blue)
		self.themeGroup.addAction(self.orange)
		self.themeGroup.addAction(self.red)
		self.themeGroup.addAction(self.transparent)
		self.skin_menu.addAction(self.blue)
		self.skin_menu.addAction(self.orange)
		self.skin_menu.addAction(self.red)
		self.skin_menu.addAction(self.transparent)
		
		# main UI setup 
		self.scrollArea = QScrollArea(self.centralwidget)
		self.scrollArea.setFrameShape(QFrame.Panel)
		self.scrollArea.setFrameShadow(QFrame.Plain)
		self.scrollArea.setLineWidth(0)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 414))
		self.scrollAreaWidgetContents.setMouseTracking(False)
		self.scrollAreaWidgetContents.setFocusPolicy(Qt.NoFocus)
		self.scrollAreaWidgetContents.setContextMenuPolicy(Qt.DefaultContextMenu)
		self.scrollAreaWidgetContents.setAcceptDrops(False)
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.label_img = MyLabel(self.scrollAreaWidgetContents)
		self.label_img.setMouseTracking(False)
		self.label_img.setFocusPolicy(Qt.NoFocus)
		self.label_img.setAcceptDrops(True)
		self.label_img.setLayoutDirection(Qt.LeftToRight)
		self.label_img.setFrameShape(QFrame.Panel)
		self.label_img.setLineWidth(0)
		self.label_img.setText(_fromUtf8(""))
		self.label_img.setAlignment(Qt.AlignCenter)
		self.label_img.setIndent(0)
		self.label_img.setObjectName(_fromUtf8("label_img"))
		self.label_img.setFocus()
		self.verticalLayout_2.addWidget(self.label_img)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.frame = QFrame(self.centralwidget)
		self.verticalLayout.addWidget(self.scrollArea)
		self.frame.setMinimumSize(QSize(0, 70))
		self.frame.setMaximumSize(QSize(16777215, 70))
		self.frame.setAutoFillBackground(False)
		self.frame.setFrameShape(QFrame.Panel)
		self.frame.setFrameShadow(QFrame.Plain)
		self.frame.setLineWidth(0)
		self.frame.setMidLineWidth(0)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.horizontalLayout_2 = QHBoxLayout(self.frame)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.frame_3 = QFrame(self.frame)
		self.frame_3.setMaximumSize(QSize(325, 58))
		self.frame_3.setLayoutDirection(Qt.LeftToRight)
		self.frame_3.setFrameShape(QFrame.Box)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.frame_3.setLineWidth(0)
		self.frame_3.setObjectName(_fromUtf8("frame_3"))
		self.frame_3.setStyleSheet(_fromUtf8("background-image: url(:/background.png);"))
		self.gridLayout = QGridLayout(self.frame_3)
		self.gridLayout.setMargin(0)
		self.gridLayout.setSpacing(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.gridLayout.setContentsMargins(20, 0, 20, 0)
		self.iconDelete = QIcon()		
		self.iconDelete.addPixmap(QPixmap(_fromUtf8(":/delete.png")), QIcon.Normal, QIcon.Off)				
		self.enlargeBt = QToolButton(self.frame_3)
		self.enlargeBt.setMinimumSize(QSize(24, 24))
		self.enlargeBt.setMaximumSize(QSize(24, 24))
		self.enlargeBt.setStyleSheet(_fromUtf8("background-color:0; border:none;background-image: url();"))
		self.enlargeBt.setDisabled(True)
		self.enlargeBt.setIconSize(QSize(18, 18))
		self.enlargeBt.setAutoRaise(True)
		self.enlargeBt.setArrowType(Qt.NoArrow)
		self.enlargeBt.setObjectName(_fromUtf8("enlargeBt"))
		self.enlargeBt.setText('Enlarge')
		self.gridLayout.addWidget(self.enlargeBt, 0, 0, 1, 1)
		self.deleteBt = QToolButton(self.frame_3)
		self.deleteBt.setMinimumSize(QSize(24, 24))
		self.deleteBt.setMaximumSize(QSize(24, 24))
		self.deleteBt.setStyleSheet(_fromUtf8("background-color:0;border: none;background-image: url();"))
		self.deleteBt.setText(_fromUtf8(""))	
		self.deleteBt.setToolTip(_fromUtf8("Delete(Del)"))	
		self.deleteBt.setIconSize(QSize(18, 18))
		self.deleteBt.setAutoRaise(True)
		self.deleteBt.setIcon(self.iconDelete)
		self.deleteBt.setShown(True)
		self.deleteBt.setArrowType(Qt.NoArrow)
		self.deleteBt.setObjectName(_fromUtf8("deleteBt"))
		self.gridLayout.addWidget(self.deleteBt, 0, 6, 1, 1)		
		self.rightBt = QToolButton(self.frame_3)
		self.rightBt.setMinimumSize(QSize(36, 36))
		self.rightBt.setMaximumSize(QSize(78, 36))
		self.rightBt.setStyleSheet(_fromUtf8("background-color:0;border: none;background-image: url();"))
		self.rightBt.setText(_fromUtf8(""))
		self.rightBt.setToolTip(_fromUtf8("Next (WheelDown)"))
		self.rightBt.setIconSize(QSize(79, 36))
		self.rightBt.setAutoRaise(True)
		self.rightBt.setArrowType(Qt.NoArrow)
		self.rightBt.setObjectName(_fromUtf8("rightBt"))
		self.gridLayout.addWidget(self.rightBt, 0, 4, 1, 1)
		self.leftBt = QToolButton(self.frame_3)
		self.leftBt.setMinimumSize(QSize(36, 36))
		self.leftBt.setMaximumSize(QSize(78, 36))
		self.leftBt.setText(_fromUtf8(""))
		self.leftBt.setToolTip(_fromUtf8("Previous (WheelUp)"))
		self.leftBt.setIconSize(QSize(79, 36))
		self.leftBt.setAutoRaise(True)
		self.leftBt.setObjectName(_fromUtf8("leftBt"))
		self.leftBt.setStyleSheet(_fromUtf8("background-color:0;border: none;background-image: url();"))	
		self.gridLayout.addWidget(self.leftBt, 0, 2, 1, 1)		
		self.fullscreenBt = QToolButton(self.frame_3)
		self.fullscreenBt.setMinimumSize(QSize(48, 48))
		self.fullscreenBt.setMaximumSize(QSize(48, 48))
		self.fullscreenBt.setText(_fromUtf8(""))
		self.fullscreenBt.setToolTip(_fromUtf8("Fullscreen"))
		self.fullscreenBt.setIconSize(QSize(48, 48))
		self.fullscreenBt.setAutoRaise(True)
		self.fullscreenBt.setObjectName(_fromUtf8("fullscreenBt"))
		self.fullscreenBt.setStyleSheet(_fromUtf8("background-color:0;border: none;background-image: url();"))
		self.gridLayout.addWidget(self.fullscreenBt, 0, 3, 1, 1)
		self.line_3 = QFrame(self.frame_3)
		self.line_3.setMaximumSize(QSize(16, 0))
		self.line_3.setLineWidth(0)
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)
		self.line_3.setObjectName(_fromUtf8("line_3"))
		self.gridLayout.addWidget(self.line_3, 0, 5, 1, 1)
		self.line_2 = QFrame(self.frame_3)
		self.line_2.setWindowModality(Qt.ApplicationModal)
		self.line_2.setMaximumSize(QSize(16, 0))
		self.line_2.setFrameShadow(QFrame.Raised)
		self.line_2.setLineWidth(0)
		self.line_2.setMidLineWidth(0)
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)
		self.line_2.setObjectName(_fromUtf8("line_2"))
		self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)		
		self.horizontalLayout_2.addWidget(self.frame_3)
		self.verticalLayout.addWidget(self.frame)
		
		self.connect(self.skinBt, SIGNAL("clicked()"), self.showSkinMenu)
		self.connect(self.menuBt, SIGNAL("clicked()"), self.showMainMenu)
		self.connect(self.minBt, SIGNAL("clicked()"), self.showMinimized)
		self.connect(self.maxBt, SIGNAL("clicked()"), self.showMax)
		self.connect(self.closeBt, SIGNAL("clicked()"), self.close)		
		
		self.connect(self.label_img, SIGNAL("openfile(QString)"), self.open)
		self.connect(self, SIGNAL("autoSave(QString)"), self.exportIni)
		self.connect(self, SIGNAL("quitfullscreen()"), self.quitFullScreen)
		self.connect(self, SIGNAL("resize()"), self.resizeWindow)
		self.connect(self.exit_m, SIGNAL(_fromUtf8("triggered()")), self.close)
		self.connect(self.open_m, SIGNAL('triggered()'), self.open)
		self.connect(self.print_m, SIGNAL('triggered()'), self.print_)
		self.connect(self.save_m, SIGNAL('triggered()'), self.saveAs)
		self.connect(self.settings_m, SIGNAL('triggered()'), self.showSettings)
		self.connect(self.help_m, SIGNAL('triggered()'), self.showHelp)
		self.connect(self.deleteBt, SIGNAL('clicked()'), self.delete)
		self.connect(self.orange, SIGNAL('triggered()'), self.themeOrange)
		self.connect(self.blue, SIGNAL('triggered()'), self.themeBlue)
		self.connect(self.red, SIGNAL('triggered()'), self.themeRed)	
		self.connect(self.transparent, SIGNAL('triggered()'), self.themeTrans)	
		self.connect(self.enlargeBt, SIGNAL('clicked()'), self.normalSize)
		self.connect(self.leftBt, SIGNAL('clicked()'), self.previous)
		self.connect(self.fullscreenBt, SIGNAL('clicked()'), self.fullscreen)
		self.connect(self.rightBt, SIGNAL('clicked()'), self.next)
		self.connect(self.about_m, SIGNAL('triggered()'), self.about)
		self.connect(self.label_img, SIGNAL("previous()"), self.previous)
		self.connect(self.label_img, SIGNAL("next()"), self.next)
		self.connect(self.label_img, SIGNAL("delete()"), self.delete)
		self.connect(self.label_img, SIGNAL("rotateL()"), self.rotateL)
		self.connect(self.label_img, SIGNAL("rotateR()"), self.rotateR)
		self.connect(self.label_img, SIGNAL("properties()"), self.showFileProperties)
		self.connect(self.scrollArea, SIGNAL("resize()"), self.resizeWindow)
		self.connect(self.label_img, SIGNAL("zoomin(QPoint)"), self.zoomIn)
		self.connect(self.label_img, SIGNAL("zoomout(QPoint)"), self.zoomOut)
		self.connect(self.label_img, SIGNAL("drag(QPoint)"), self.drag)
		self.connect(self.label_img, SIGNAL("hand(int)"), self.hand)
		self.connect(self.label_img, SIGNAL("open()"), self.open)
		self.connect(self.label_img, SIGNAL("fullscreen()"), self.fullscreen)
		self.connect(self.label_img, SIGNAL("setWallpaper()"), self.setWallpaper)
		
		self.isMax = False
		self.path = './'
		self.imgFile = QFileInfo()
		self.imageQ = QImage()
		self.curImageQ = QImage()
		self.imgType = QStringList()
		self.imgList = QStringList()
		self.theme('blue')
		self.menuStatus()
		self.border = 4
		self.desktop = QDesktopWidget()
		self.desktopSize = QDesktopWidget.availableGeometry(self.desktop).size()
		self.setFont(QFont(_fromUtf8('Tahoma')))
		# supported image type
		global fileTypes
		for type in fileTypes:
			self.imgType.append(type)
	
		# load config file	
		config = QFileInfo('./PhotoViewer.ini')
		if config.isReadable():
			self.importIni(config.filePath())			
		self.setCentralWidget(self.centralwidget)
		QMetaObject.connectSlotsByName(self)
		self.retranslateUi()
		self.setTitleIcon(":/icon.png")

	def retranslateUi(self):
		self.skinBt.setToolTip(u"Change skin")
		self.menuBt.setToolTip(u"Main menu")
		self.minBt.setToolTip(u"Minimize")
		self.maxBt.setToolTip(u"Maximize")
		self.closeBt.setToolTip(u"Close")
		self.leftBt.setShortcut(_translate("MainWindow", "Left", None))
		self.rightBt.setShortcut(_translate("MainWindow", "Right", None))
		self.label.setText(u"Photo Viewer")
		self.orange.setText(u"Orange")
		self.blue.setText(u"Blue")
		self.red.setText(u"Red")
		self.transparent.setText(u"Transparent")
		
		self.action_file.setTitle(u"&File")
		self.open_m.setText(u"&Open...")
		self.save_m.setText(u"&Save as...")
		self.settings_m.setText(u"Preferences...")
		self.print_m.setText(u"&Print...")
		self.exit_m.setText(u"E&xit")
		
		self.action_about.setTitle(u"&About")
		self.help_m.setText(u"Help")
		# self.help_m.setShortcut(_translate("action_about", "F1", "showHelp()"))
		self.about_m.setText(u"About")
		
	def setTitleIcon(self, str):
		self.label_1.setPixmap(QPixmap(str))
	
	def setTitle(self, str):
		self.label.setText(str + _fromUtf8("Photo Viewer"))
	
	def showMax(self):
		if not self.isMax:
			self.isMax = True
			self.maxBt.loadPixmap(":/max_button_2.png")
			self.positionX = self.pos().x()
			self.positionY = self.pos().y()
			self.mainWidth = self.rect().width()
			self.mainHeight = self.rect().height()		
			self.resize(self.desktopSize)
			self.move(0, 0)
		else:
			self.isMax = False
			self.maxBt.loadPixmap(":/max_button.png")
			self.resize(self.mainWidth, self.mainHeight)
			self.move(self.positionX, self.positionY)
		
	def showMainMenu(self):
		p = self.rect().topRight()
		p.setX(p.x() - 155)
		p.setY(p.y() + 22)
		self.main_menu.exec_(self.mapToGlobal(p))	

	def showSkinMenu(self):
		p = self.rect().topRight()
		p.setX(p.x() - 170)
		p.setY(p.y() + 22)
		self.skin_menu.exec_(self.mapToGlobal(p))
	
	def isInTitle(self, xPos, yPos):
		return yPos <= 30 and not (yPos <= 22 and (xPos > self.skinBt.pos().x() and xPos < self.closeBt.pos().x() + self.closeBt.width()))
	
	def isLeft(self, xPos):
		return xPos >= 0 and xPos <= self.border	
		
	def isRight(self, xPos):
		return xPos <= self.width() and xPos >= self.width() - self.border	
		
	def isTop(self, yPos):
		return yPos >= 0 and yPos <= self.border	
		
	def isTopLeft(self, xPos, yPos):
		return (xPos >= 0 and xPos <= self.border) and (yPos >= 0 and yPos <= self.border)	
	
	def isTopRight(self, xPos, yPos):
		return (xPos <= self.width() and xPos >= self.width() - self.border) and (yPos >= 0 and yPos <= self.border)
		
	def isBottom(self, yPos):
		return yPos <= self.height() and yPos >= self.height() - self.border	
	
	def isBottomLeft(self, xPos, yPos):
		return (yPos <= self.height() and yPos >= self.height() - self.border) and (xPos >= 0 and xPos <= self.border)
	
	def isBottomRight(self, xPos, yPos):
		return (yPos <= self.height() and yPos >= self.height() - self.border) and (xPos <= self.width() and xPos >= self.width() - self.border)

	def closeEvent(self, event):
		if self.isFullScreen():
			self.emit(SIGNAL("quitfullscreen()"))
			event.ignore()
		else:
			self.emit(SIGNAL("autoSave(QString)"), _fromUtf8('./PhotoViewer.ini'))
			event.accept()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape and self.isFullScreen():
			self.emit(SIGNAL("quitfullscreen()"))
	
	def resizeEvent(self, event):
		self.emit(SIGNAL("resize()"))
				
	def importIni(self, file):
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(_toUtf8(file).data())
			if eval(cf.get('common', 'maximized')):
				self.showMax()
				return
			self.resize(int(cf.get('common', 'width')), int(cf.get('common', 'height')))
			self.move(int(cf.get('common', 'x')), int(cf.get('common', 'y')))
			self.path = cf.get('common', 'path')
			self.theme(cf.get('common', 'theme').lower())
		except:
			reminder = QWidget()
			reminder.setWindowIcon(QIcon(':/icon.png'))
			QMessageBox.warning(reminder,'Warning', 'Bad config file.', QMessageBox.Ok)
		
	def exportIni(self, file):
		cfg = open(_toUtf8(file).data(), 'w+')
		cf = ConfigParser.ConfigParser()
		cf.add_section('common')
		cf.set('common', 'maximized', str(self.isMax))
		cf.set('common', 'x', self.pos().x())
		cf.set('common', 'y', self.pos().y())
		cf.set('common', 'width', self.rect().width())
		cf.set('common', 'height', self.rect().height())
		cf.set('common', 'path', self.path)
		cf.set('common', 'theme', self.themeGroup.checkedAction().text().toLower())
		cf.write(cfg)
		cfg.close()
		
	def next(self):
		self.imgFile.refresh()		
		if not self.imgList.isEmpty():
			curIndex = self.imgList.indexOf(self.imgFile.fileName())
			self.imgFile.setFile(self.imgFile.absolutePath() + '/' + self.imgList[curIndex+1-self.imgList.count()])
			while not self.imgFile.isReadable() and not self.imgList.isEmpty():
				nextIndex = self.imgList.indexOf(self.imgFile.fileName())
				self.imgList.removeAt(nextIndex)
				if not self.imgList.isEmpty():
					self.imgFile.setFile(self.curPath.path() + '/' + self.imgList[nextIndex-self.imgList.count()])				
				else:
					self.label_img.clear()
					self.imageQ = QImage()
			self.open(self.imgFile.filePath(), 0)	
					
	def previous(self):
		self.imgFile.refresh()		
		if not self.imgList.isEmpty():
			curIndex = self.imgList.indexOf(self.imgFile.fileName())
			self.imgFile.setFile(self.imgFile.absolutePath() + '/' + self.imgList[curIndex-1])
			while not self.imgFile.isReadable() and not self.imgList.isEmpty():
				preIndex = self.imgList.indexOf(self.imgFile.fileName())
				self.imgList.removeAt(preIndex)
				if not self.imgList.isEmpty():
					self.imgFile.setFile(self.curPath.path() + '/' + self.imgList[preIndex-1])									
				else:
					self.label_img.clear()
					self.imageQ = QImage()
			self.open(self.imgFile.filePath(), 0)		
			
	def delete(self):	  
		if self.imageQ.isNull():
			return
			
		confirm = QMessageBox.question(self,'Delete File',"Are you sure to delete this file?", QMessageBox.Yes, QMessageBox.No)
		if confirm == QMessageBox.Yes:
			path = self.imgFile.filePath()
			self.next()	
			QFile.remove(path)
	
		else:
			return

	def rotateL(self):
		self.imgFile.refresh()
		if not self.imgFile.isReadable() or self.imageQ.isNull():
			return
		angle = QMatrix()
		self.imageQ = self.imageQ.transformed(angle.rotate(-90))
		if not self.resizeWindow():
			self.label_img.setPixmap(QPixmap(self.imageQ))
		self.imageQ.save(self.imgFile.filePath())
		
	def rotateR(self):
		self.imgFile.refresh()
		if not self.imgFile.isReadable() or self.imageQ.isNull():
			return
		angle = QMatrix()
		self.imageQ = self.imageQ.transformed(angle.rotate(90))
		if not self.resizeWindow():
			self.label_img.setPixmap(QPixmap(self.imageQ))
		self.imageQ.save(self.imgFile.filePath())
			
	def about(self):
		ab = about(self)	
		ab.setTheme(self.themeGroup.checkedAction().text().toLower())
		ab.show()
			
	def open(self, file = None, getAll = 1):	
		if file == None:
			IMG = QFileDialog.getOpenFileName(self, 'Open an image file', self.path,'Image File (*.JPG; *.BMP; *.PNG; *.GIF; *.JPEG; *.ico; *.ppm; *.tiff)')
		else:
			IMG = file
			
		self.imgFile.setFile(IMG)	
		if IMG.length() and self.imgFile.isReadable():
			self.label_img.clear()		
			self.imageQ.load(self.imgFile.filePath())	
			self.curImageQ = self.imageQ
			self.curPath = QDir(self.imgFile.absolutePath())
			self.path = self.curPath.absolutePath().toUtf8().data()
			self.enlargeBt.setText('Shrink')		
			self.enlargeBt.setIcon(self.iconShrink)		
			if self.imgFile.suffix().contains('gif'):
				self.movie = QMovie(self.imgFile.filePath(), QByteArray(), self) 
				self.movie.setCacheMode(QMovie.CacheAll) 
				time = Image.open(_toUtf8(self.imgFile.filePath()).data()).info['duration']
				print time
				if time != 0:
					self.movie.setSpeed(time)
				else:
					self.movie.setSpeed(100)					
				self.label_img.setMovie(self.movie)
				self.movie.start()
				
			else:
				if not self.resizeWindow():
					self.label_img.setPixmap(QPixmap(self.imageQ))
			self.setTitle(self.imgFile.fileName() + _fromUtf8(" - "))
			if getAll == 1:
				self.imgList = self.curPath.entryList(self.imgType, QDir.Files, QDir.Time)	
		self.menuStatus()
		
	def themeOrange(self):
		self.theme('orange')
		
	def themeBlue(self):
		self.theme('blue')
	
	def themeTrans(self):
		self.theme('transparent')
		
	def themeRed(self):
		self.theme('red')

	def theme(self, str):
		if str == 'orange':
			self.label_img.setStyleSheet(_fromUtf8("background-color: #FFFAF0;"))
			self.orange.setChecked(True)
		elif str == 'blue':
			self.label_img.setStyleSheet(_fromUtf8("background-color: rgb(238, 243, 250);"))
			self.blue.setChecked(True)
		elif str == 'red':
			self.label_img.setStyleSheet(_fromUtf8("background-color: #FAF0E6;"))
			self.red.setChecked(True)
		else: 
			self.label_img.setStyleSheet(_fromUtf8("background-color: rgb(238, 243, 250);"))
			self.transparent.setChecked(True)
		
		iconLeft = QIcon()
		iconLeft.addPixmap(QPixmap(_fromUtf8(":/" + str + "_left.png")), QIcon.Normal, QIcon.Off)		
		iconFullscreen = QIcon()
		iconFullscreen.addPixmap(QPixmap(_fromUtf8(":/" + str + "_fullscreen.png")), QIcon.Normal, QIcon.Off)
		iconRight = QIcon()
		iconRight.addPixmap(QPixmap(_fromUtf8(":/" + str + "_right.png")), QIcon.Normal, QIcon.Off)
		self.iconShrink = QIcon()
		self.iconEnlarge = QIcon()
		self.iconShrink.addPixmap(QPixmap(_fromUtf8(":/" + str + "_shrink.png")), QIcon.Normal, QIcon.Off)			
		self.iconEnlarge.addPixmap(QPixmap(_fromUtf8(":/" + str + "_enlarge.png")), QIcon.Normal, QIcon.Off)			
		self.leftBt.setIcon(iconLeft)	
		self.fullscreenBt.setIcon(iconFullscreen)	
		self.rightBt.setIcon(iconRight)
		self.pixmap = QPixmap(":/" + str + "Theme.png")
		
		if self.enlargeBt.text() == 'Enlarge':
			self.enlargeBt.setIcon(self.iconEnlarge)
		else:
			self.enlargeBt.setIcon(self.iconShrink)
		
		self.update()	
		
	def saveAs(self):
		imgFormat = 'BMP File (*.bmp);;JPG File (*.jpg);;JPEG File (*.jpeg);;PNG File (*.png);;PPM File (*.ppm);;TIFF File(*.tiff)'				
		imgFile = QFileDialog.getSaveFileName(self, 'Save photo', './', imgFormat)
		self.imageQ.save(imgFile)
	
	def print_(self):
		self.prt = QPrinter()
		dialog = QPrintDialog(self.prt, self)
		if dialog.exec_():
			painter = QPainter(self.prt)
			rect = painter.viewport()
			size = self.label_img.pixmap().size()
			size.scale(rect.size(), Qt.KeepAspectRatio)
			painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
			painter.setWindow(self.label_img.pixmap().rect())
			painter.drawPixmap(0, 0, self.label_img.pixmap())

	def normalSize(self):
		if self.enlargeBt.text() == 'Shrink':
			self.curImageQ = self.imageQ
			self.label_img.setPixmap(QPixmap(self.curImageQ))
			self.enlargeBt.setIcon(self.iconEnlarge)
			self.enlargeBt.setToolTip('Fit to window')
			self.enlargeBt.setText('Enlarge')
		else:
			self.enlargeBt.setIcon(self.iconShrink)
			self.enlargeBt.setToolTip('Actual size')
			self.enlargeBt.setText('Shrink')
			self.resizeWindow()
		self.menuStatus()
		
	def resizeWindow(self):
		if self.imageQ.isNull():
			return
		if self.largerThan(self.imageQ, self.scrollArea) and \
			(self.enlargeBt.text() == 'Shrink' or not self.enlargeBt.isEnabled()) and not self.imgFile.suffix().contains('gif'):			
			self.curImageQ = self.imageQ.scaled(self.scrollArea.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
			self.label_img.setPixmap(QPixmap(self.curImageQ))
			self.menuStatus()
			return True
		elif not self.largerThan(self.imageQ, self.scrollArea) and \
			self.enlargeBt.text() == 'Shrink' and not self.imgFile.suffix().contains('gif'):
			self.curImageQ = self.imageQ
			self.label_img.setPixmap(QPixmap(self.imageQ))
			self.menuStatus()
			return False
		else:
			self.menuStatus()
			return False	
			
	def menuStatus(self):
		self.save_m.setDisabled(self.imageQ.isNull())
		self.print_m.setDisabled(self.imageQ.isNull())
		self.deleteBt.setDisabled(self.imageQ.isNull())
		self.label_img.actionDelete.setDisabled(self.imageQ.isNull())
		self.label_img.actionPre.setDisabled(self.imageQ.isNull())
		self.label_img.actionNext.setDisabled(self.imageQ.isNull())
		self.label_img.actionProperties.setDisabled(self.imageQ.isNull())
		self.label_img.actionTurnRight.setDisabled(self.imageQ.isNull() or self.imgFile.suffix().contains('gif') or self.imgFile.suffix().contains('ico'))
		self.label_img.actionTurnLeft.setDisabled(self.imageQ.isNull() or self.imgFile.suffix().contains('gif') or self.imgFile.suffix().contains('ico'))
		self.label_img.action.setDisabled(self.imageQ.isNull())
		self.label_img.actionZoomIn.setDisabled(self.imgFile.suffix().contains('gif') or self.getScaleFactor() > 6.0 or self.imageQ.isNull())
		self.label_img.actionZoomOut.setDisabled(self.imgFile.suffix().contains('gif') or self.imageQ.isNull() or \
							((self.largerThan(self.imageQ, self.scrollArea) and not self.largerThan(self.curImageQ, self.scrollArea)) or \
							(not self.largerThan(self.imageQ, self.scrollArea) and self.equalTo(self.imageQ, self.curImageQ))))
		
		if not self.imgFile.suffix().contains('gif') and not self.imageQ.isNull():
			if  self.largerThan(self.curImageQ, self.scrollArea):
					self.enlargeBt.setEnabled(True)
					self.enlargeBt.setToolTip('Fit to window')
					self.enlargeBt.setText('Enlarge')
					self.enlargeBt.setIcon(self.iconEnlarge)
					self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
			else:
				self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
				if self.largerThan(self.imageQ, self.scrollArea):
					self.enlargeBt.setEnabled(True)
					self.enlargeBt.setToolTip('Actual size')
					self.enlargeBt.setText('Shrink')
					self.enlargeBt.setIcon(self.iconShrink)
				else:
					if self.equalTo(self.curImageQ, self.imageQ):
						self.enlargeBt.setEnabled(False)
						self.enlargeBt.setToolTip('')
						self.enlargeBt.setText('Enlarge')
						self.enlargeBt.setIcon(self.iconEnlarge)
					else:
						self.enlargeBt.setEnabled(True)
						self.enlargeBt.setToolTip('Fit to window')
						self.enlargeBt.setText('Enlarge')
						self.enlargeBt.setIcon(self.iconEnlarge)

		else:
			self.imgFile.suffix().contains('gif')
			self.enlargeBt.setEnabled(False)
			self.enlargeBt.setToolTip('')
			self.enlargeBt.setText('Enlarge')
			self.enlargeBt.setIcon(self.iconEnlarge)				
	
	def showSettings(self):
		st = settings(self)
		st.setTheme(self.themeGroup.checkedAction().text().toLower())
		st.show()
	
	def zoomIn(self, pos):
		if self.getScaleFactor() > 6.0 or self.imgFile.suffix().contains('gif') or self.imageQ.isNull() or not self.label_img.actionZoomIn.isEnabled():
			return
		newsize = 1.25 * self.curImageQ.size()
		if self.largerThan(newsize, self.imageQ):		
			self.scaleImage(newsize, pos)
		else:
			self.scaleImage(newsize, pos, Qt.SmoothTransformation)

	def zoomOut(self, pos):
		if self.imgFile.suffix().contains('gif') or self.imageQ.isNull() or not self.label_img.actionZoomOut.isEnabled():
			return
		newsize = 0.8 * self.curImageQ.size()	
		if self.largerThan(self.imageQ, self.scrollArea):
			if self.largerThan(newsize, self.scrollArea):
				if self.largerThan(newsize, self.imageQ):		
					self.scaleImage(newsize, pos)
				else:
					self.scaleImage(newsize, pos, Qt.SmoothTransformation)
			else:
				self.scaleImage(self.scrollArea.size(), pos, Qt.SmoothTransformation)
		else:
			if self.largerThan(newsize, self.imageQ):
				self.scaleImage(newsize, pos)
			else:
				self.scaleImage(self.imageQ.size(), pos)
					
	def scaleImage(self, newsize, pos, scaleMode=Qt.FastTransformation):
		if newsize.width() * newsize.height() > 120000000:
			return
		preSize = self.curImageQ.size()
		self.curImageQ = self.imageQ.scaled(newsize, Qt.KeepAspectRatio, scaleMode)
		self.label_img.setPixmap(QPixmap(self.curImageQ))

		if self.curImageQ.width() > self.scrollArea.horizontalScrollBar().pageStep():
			self.scrollArea.horizontalScrollBar().setMaximum(self.curImageQ.width() - self.scrollArea.horizontalScrollBar().pageStep())
		if self.curImageQ.height() > self.scrollArea.verticalScrollBar().pageStep():
			self.scrollArea.verticalScrollBar().setMaximum(self.curImageQ.height() - self.scrollArea.verticalScrollBar().pageStep())	
		
		self.scrollArea.horizontalScrollBar().setValue(int((pos.x() * self.scrollArea.horizontalScrollBar().maximum()/preSize.width())))	
		self.scrollArea.verticalScrollBar().setValue(int((pos.y() * self.scrollArea.verticalScrollBar().maximum()/preSize.height())))
		self.menuStatus()	
		
	def drag(self, point):
		self.scrollArea.horizontalScrollBar().setValue(self.scrollArea.horizontalScrollBar().value() - point.x())
		self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().value() - point.y())

	def hand(self, i):
		if self.largerThan(self.curImageQ, self.scrollArea):
			if i == 0:
				self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.ClosedHandCursor))
			elif i == 1:
				self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))

	def setWallpaper(self):
		self.imgFile.refresh()
		if self.imageQ.isNull() or not self.imgFile.isReadable():
			return
			
		desktop = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
		desktop.SetWallpaper(_toUtf8(self.imgFile.filePath()).data().replace('/', '\\'), 0)
		desktop.ApplyChanges(shellcon.AD_APPLY_ALL)

	def fullscreen(self):
		if self.imageQ.isNull():
			return
		self.title.hide()
		self.frame.hide()
		self.label_img.setStyleSheet('background-color: rgb(0, 0, 0);')
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.showFullScreen()
		if self.enlargeBt.text() == 'Enlarge':
			self.normalSize()
		self.menuStatus()
		
	def quitFullScreen(self):
		self.title.show()
		self.frame.show()
		self.theme(self.themeGroup.checkedAction().text().toLower())
		self.showNormal()
		self.verticalLayout.setContentsMargins(5, 0, 5, 0)
		self.menuStatus()
		
	def showHelp(self):
		hp = help(self)
		hp.setTheme(self.themeGroup.checkedAction().text().toLower())
		hp.show()
		
	def largerThan(self, s1, s2):
		if s1.width() > s2.width() or s1.height() > s2.height():
			return True
		else:
			return False
	
	def equalTo(self, s1, s2):
		if s1.width() != s2.width() or s1.height() != s2.height():
			return False
		else:
			return True
	
	def getScaleFactor(self):
		if self.imageQ.isNull():
			return 1.0
		else:
			return float(self.curImageQ.size().width())/self.imageQ.size().width()

	def showFileProperties(self):
		if self.imageQ.isNull():
			return
		SEE_MASK_NOCLOSEPROCESS = 0x00000040
		SEE_MASK_INVOKEIDLIST = 0x0000000C
		ShellExecuteEx = ctypes.windll.shell32.ShellExecuteEx
		ShellExecuteEx.restype = ctypes.wintypes.BOOL

		sei = FileProperties()
		sei.cbSize = ctypes.sizeof(sei)
		sei.fMask = SEE_MASK_NOCLOSEPROCESS | SEE_MASK_INVOKEIDLIST
		sei.lpVerb = "properties"
		sei.lpFile = self.imgFile.filePath().toUtf8().data().decode('utf-8')
		sei.nShow = 1
		ShellExecuteEx(ctypes.byref(sei))
			
	def paintEvent(self,event):	
		self.painter = QPainter(self)
		self.painter2 = QPainter(self)
		self.painter3 = QPainter(self)
		self.painter4 = QPainter(self)
		self.painter5 = QPainter(self)
		self.painter6 = QPainter(self)
		self.painter7 = QPainter(self)
		self.painter8 = QPainter(self)
		# self.painter.begin(self)
		self.topLeft = self.pixmap.copy(10, 0, 7, 30)
		self.topRight = self.pixmap.copy(17, 0, 7, 30)
		self.bottomLeft = self.pixmap.copy(35, 0, 9, 70)
		self.bottomRight = self.pixmap.copy(44, 0, 10, 70)
		self.titlePix = self.pixmap.copy(5, 0, 5, 30)
		self.leftMargin = self.pixmap.copy(0, 60, 5, 4)
		self.rightMargin = self.pixmap.copy(0, 64, 5, 4)
		self.statusBar = self.pixmap.copy(28, 0, 4, 70)

		# self.setMask(self.topLeft.mask())
		# self.setMask(self.titlePix.mask())
		# self.setMask(self.topRight.mask())
		# self.setMask(self.leftMargin.mask())
		# self.frame.setMask(self.bottomLeft.mask())
		# self.frame.setMask(self.bottomRight.mask())
		
		self.painter.drawPixmap(0, 0, self.topLeft.width(), self.topLeft.height(), self.topLeft)
		self.painter2.drawPixmap(self.topLeft.width(), 0, self.width()-self.topLeft.width()-self.topRight.width(), self.titlePix.height(), self.titlePix)
		self.painter3.drawPixmap(self.width()-self.topRight.width(), 0, self.topRight.width(), self.topRight.height(), self.topRight)
		self.painter4.drawPixmap(0, self.topLeft.height(), self.leftMargin.width(), self.height()-self.statusBar.height()-self.titlePix.height(), self.leftMargin)
		self.painter5.drawPixmap(self.width()-self.rightMargin.width(), self.topRight.height(), self.rightMargin.width(), self.height()-self.statusBar.height()-self.titlePix.height(), self.rightMargin)
		self.painter6.drawPixmap(0, self.height()-self.bottomLeft.height(), self.bottomLeft.width(), self.bottomLeft.height(), self.bottomLeft)
		self.painter7.drawPixmap(self.width()-self.bottomRight.width(), self.height()-self.bottomRight.height(), self.bottomRight.width(), self.bottomRight.height(), self.bottomRight)
		self.painter8.drawPixmap(self.bottomLeft.width(), self.height()-self.statusBar.height(), self.width()-self.bottomLeft.width()-self.bottomRight.width(), self.statusBar.height(), self.statusBar)
		self.painter.end()		
		self.painter2.end()		
		self.painter3.end()		
		self.painter4.end()		
		self.painter5.end()		
		self.painter6.end()		
		self.painter7.end()		
		self.painter8.end()		
		
class PushButton(QPushButton):
	def __init__(self,parent = None):
		super(PushButton,self).__init__(parent)	
		self.status = 0 

	def loadPixmap(self, pic_name):	
		self.pixmap = QPixmap(pic_name)
		self.btn_width = self.pixmap.width()/4
		self.btn_height = self.pixmap.height()
		self.setFixedSize(self.btn_width, self.btn_height)
		
	def enterEvent(self,event):	
		self.status = 1 #self.ENTER
		self.update()
	
	def mousePressEvent(self,event):	
		if event.button() == Qt.LeftButton:		
			self.mouse_press = True
			self.status = 2 #self.PRESS
			self.update()		

	def mouseReleaseEvent(self,event):	
		if self.mouse_press:		
			self.mouse_press = False
			self.status = 3 #self.ENTER
			self.update()
			self.clicked.emit(True)		
			self.released.emit()		

	def leaveEvent(self,event):	
		self.status = 0 #self.NORMAL
		self.update()
	
	def paintEvent(self,event):	
		self.painter = QPainter()
		self.painter.begin(self)
		self.painter.drawPixmap(self.rect(), self.pixmap.copy(self.btn_width * self.status, 0, self.btn_width, self.btn_height))
		self.painter.end()				

	# def showMinimized(self):
		# self.paintEvent()
		# self.showMinimized()
	
class FileProperties(ctypes.Structure):
	_fields_ = (
		("cbSize",ctypes.wintypes.DWORD),
		("fMask",ctypes.c_ulong),
		("hwnd",ctypes.wintypes.HANDLE),
		("lpVerb",ctypes.c_char_p),
		("lpFile",ctypes.c_char_p),
		("lpParameters",ctypes.c_char_p),
		("lpDirectory",ctypes.c_char_p),
		("nShow",ctypes.c_int),
		("hInstApp",ctypes.wintypes.HINSTANCE),
		("lpIDList",ctypes.c_void_p),
		("lpClass",ctypes.c_char_p),
		("hKeyClass",ctypes.wintypes.HKEY),
		("dwHotKey",ctypes.wintypes.DWORD),
		("hIconOrMonitor",ctypes.wintypes.HANDLE),
		("hProcess",ctypes.wintypes.HANDLE),
	)
	
class MyLabel(QLabel):
	def __init__(self, parent=None):
		self.cursorPos = QPoint()
		QLabel.__init__(self, parent)
		self.contextMenu = QMenu(self)
		self.contextMenu.setStyleSheet(_fromUtf8("background-color:0;"))
		iconRight = QIcon()
		iconDelete = QIcon()
		iconZoomIn = QIcon()
		iconZoomOut = QIcon()
		iconTurnLeft = QIcon()
		iconTurnRight = QIcon()										
		iconRight.addPixmap(QPixmap(_fromUtf8(":/next_m.png")), QIcon.Normal, QIcon.Off)		
		iconDelete.addPixmap(QPixmap(_fromUtf8(":/delete_m.png")), QIcon.Normal, QIcon.Off)
		iconZoomIn.addPixmap(QPixmap(_fromUtf8(":/zoomin_m.png")), QIcon.Normal, QIcon.Off)		
		iconZoomOut.addPixmap(QPixmap(_fromUtf8(":/zoomout_m.png")), QIcon.Normal, QIcon.Off)
		iconTurnLeft.addPixmap(QPixmap(_fromUtf8(":/turnleft_m.png")), QIcon.Normal, QIcon.Off)
		iconTurnRight.addPixmap(QPixmap(_fromUtf8(":/turnright_m.png")), QIcon.Normal, QIcon.Off)				

		self.action = QAction('Set as desktop background', self)
		self.actionPre = QAction('Previous', self)
		self.actionNext = QAction('Next', self)
		self.actionNext.setShortcut(_translate("MainWindow", "", None))
		self.actionDelete = QAction('Delete', self)
		self.actionTurnRight = QAction('Rotate clockwise', self)
		self.actionTurnLeft = QAction('Rotate Counterclockwise', self)
		self.actionZoomIn = QAction('Zoom In', self)
		self.actionZoomOut = QAction('Zoom Out', self)
		self.actionProperties = QAction('Properties', self)
		
		self.actionNext.setIcon(iconRight)
		self.actionDelete.setIcon(iconDelete)
		self.actionZoomIn.setIcon(iconZoomIn)
		self.actionZoomOut.setIcon(iconZoomOut)
		self.actionTurnRight.setIcon(iconTurnRight)
		self.actionTurnLeft.setIcon(iconTurnLeft)
		
		
		self.contextMenu.addAction(self.actionNext)		
		self.contextMenu.addAction(self.actionPre)
		self.contextMenu.addSeparator()
		self.contextMenu.addAction(self.actionZoomIn)
		self.contextMenu.addAction(self.actionZoomOut)
		self.contextMenu.addSeparator()
		self.contextMenu.addAction(self.actionDelete)
		self.contextMenu.addSeparator()
		self.contextMenu.addAction(self.action)
		self.contextMenu.addSeparator()
		self.contextMenu.addAction(self.actionTurnRight)
		self.contextMenu.addAction(self.actionTurnLeft)
		self.contextMenu.addSeparator()
		self.contextMenu.addAction(self.actionProperties)
				
		self.connect(self.action, SIGNAL("triggered()"), self.setBackground)
		self.connect(self.actionPre, SIGNAL("triggered()"), self.previous)
		self.connect(self.actionNext, SIGNAL("triggered()"), self.next)
		self.connect(self.actionDelete, SIGNAL("triggered()"), self.delete)
		self.connect(self.actionTurnLeft, SIGNAL("triggered()"), self.rotateL)
		self.connect(self.actionTurnRight, SIGNAL("triggered()"), self.rotateR)
		self.connect(self.actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
		self.connect(self.actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
		self.connect(self.actionProperties, SIGNAL("triggered()"), self.property)
		
	def rotateL(self):
		self.emit(SIGNAL("rotateL()"))	
		
	def rotateR(self):
		self.emit(SIGNAL("rotateR()"))
	
	def setBackground(self):
		self.emit(SIGNAL("setWallpaper()"))

	def contextMenuEvent(self, event):
		self.contextMenu.exec_(event.globalPos())

	def previous(self):
		self.emit(SIGNAL("previous()"))
		
	def next(self):
		self.emit(SIGNAL("next()"))

	def delete(self):
		self.emit(SIGNAL("delete()"))

	def wheelEvent(self, event):
		modifier = QApplication.keyboardModifiers()
		self.cursorPos = event.pos()
		if event.delta() >= 120 and modifier == Qt.ControlModifier:
			self.zoomIn()	
		elif event.delta() <= -120 and modifier == Qt.ControlModifier:
			self.zoomOut()
		elif event.delta() >= 120:
			self.previous()
		elif event.delta() <= -120:
			self.next()
		
	def mousePressEvent(self,event):  
		self.e = event.button()
		if event.button() == Qt.LeftButton:
			self.emit(SIGNAL("hand(int)"), 0)
			self.startPosition = event.pos()
		elif event.button() == Qt.MidButton:
			if not self.topLevelWidget().isFullScreen():
				self.emit(SIGNAL("fullscreen()"))
			else:
				self.topLevelWidget().emit(SIGNAL("quitfullscreen()"))

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.emit(SIGNAL("hand(int)"), 1)
			
	def mouseMoveEvent(self,event):  
		self.endPosition = event.pos()
		if self.e == Qt.LeftButton:
			self.emit(SIGNAL("drag(QPoint)"), self.endPosition - self.startPosition)

	def mouseDoubleClickEvent(self, event):
		if event.button() == Qt.LeftButton and not self.topLevelWidget().isFullScreen():
			self.emit(SIGNAL("open()"))

	def zoomIn(self):
		self.emit(SIGNAL("zoomin(QPoint)"), self.cursorPos)

	def zoomOut(self):
		self.emit(SIGNAL("zoomout(QPoint)"), self.cursorPos)	
	
	def property(self):
		self.emit(SIGNAL("properties()"))

	def dragEnterEvent(self, event):
		global fileType
		if len(event.mimeData().urls()):
			self.fileName = event.mimeData().urls()[0].toLocalFile()
			ext = QFileInfo(self.fileName).suffix()
			if "*." + ext.toUtf8().data().lower() in fileTypes:
				event.accept()
	
	def dropEvent(self, event):
		self.emit(SIGNAL("openfile(QString)"), self.fileName)
		
class about(QDialog):
	def __init__(self, parent=None):
		super(about, self).__init__(parent)
		self.setObjectName(_fromUtf8("about"))
		self.setWindowModality(Qt.ApplicationModal)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.resize(252, 184)
		self.setMinimumSize(QSize(252, 184))
		self.setMaximumSize(QSize(252, 184))
		self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Dialog)	
		self.setStyleSheet('font-family: thoma,tahoma;font-size: 11px;')
		self.frame = QFrame(self)
		self.frame.setGeometry(QRect(0, 0, 252, 30))
		self.frame.setMinimumSize(QSize(252, 30))
		self.frame.setMaximumSize(QSize(16777215, 30))
		self.frame.setFrameShape(QFrame.NoFrame)
		self.frame.setFrameShadow(QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.horizontalLayout = QHBoxLayout(self.frame)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
		self.label = QLabel(self.frame)
		self.label.setObjectName(_fromUtf8("label"))
		self.label.setScaledContents(True)
		self.label.setMaximumSize(16, 16)
		self.horizontalLayout.addWidget(self.label)
		self.label_1 = QLabel(self.frame)
		self.label_1.setMinimumSize(QSize(0, 20))
		self.label_1.setObjectName(_fromUtf8("label_1"))
		self.label_1.setContentsMargins(5, 0, 0, 0)
		self.horizontalLayout.addWidget(self.label_1)
		spacerItem = QSpacerItem(157, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.closeBt = PushButton(self.frame)
		self.closeBt.setMinimumSize(QSize(20, 25))
		self.closeBt.setMaximumSize(QSize(40, 16777215))
		self.closeBt.setObjectName(_fromUtf8("closeBt"))
		self.closeBt.loadPixmap(":/close.png")
		self.horizontalLayout.addWidget(self.closeBt, 0, Qt.AlignTop)
		self.setFont(QFont(_fromUtf8('Tahoma')))
		
		QMetaObject.connectSlotsByName(self)		
		self.connect(self.closeBt, SIGNAL("clicked()"), self.close)	
		self.setupUI()

	def setupUI(self):
		self.setTitleIcon(":/icon.png")
		self.setTitle("About")
		self.icon = QLabel(self)
		self.icon.setGeometry(QRect(20, 40, 70, 70))
		self.icon.setMinimumSize(QSize(70, 70))
		self.icon.setMaximumSize(QSize(70, 70))
		self.icon.setText(_fromUtf8(""))
		self.icon.setPixmap(QPixmap(_fromUtf8(":/icon.png")))
		self.icon.setScaledContents(True)
		self.icon.setObjectName(_fromUtf8("icon"))
		self.OK_Bt = QPushButton(self)
		self.OK_Bt.setGeometry(QRect(160, 145, 75, 23))
		self.OK_Bt.setObjectName(_fromUtf8("OK_Bt"))
		self.OK_Bt.setStyleSheet("QPushButton{border:1px solid lightgray;background:transparent}}"
			"QPushButton:hover{border-color:#A9A9A9;background:transparent}"
			"QPushButton:hover:pressed{border:1px solid lightgray;background:rgb(230,230,230)")
		self.label_version = QLabel(self)
		self.label_version.setGeometry(QRect(110, 40, 131, 20))
		font = QFont()
		font.setBold(True)
		self.label_version.setFont(font)
		self.label_version.setObjectName(_fromUtf8("label_version"))
		self.label_year = QLabel(self)
		self.label_year.setGeometry(QRect(110, 70, 121, 16))
		self.label_year.setObjectName(_fromUtf8("label_year"))
		self.label_author = QLabel(self)
		self.label_author.setGeometry(QRect(110, 96, 121, 20))
		self.label_author.setObjectName(_fromUtf8("label_author"))
		self.label_email = QLabel(self)
		self.label_email.setGeometry(QRect(110, 110, 141, 20))
		self.label_email.setObjectName(_fromUtf8("label_email"))
		self.OK_Bt.setText(_translate("about", "OK", None))
		self.label_version.setText(_translate("about", "Photo Viewer v1.0", None))
		self.label_year.setText(_translate("about", "PyQt4 application, 2014", None))
		self.label_author.setText(_translate("about", "Author: Andy Wen", None))
		self.label_email.setText(_translate("about", "Email: wn0112@gmail.com", None))
		self.connect(self.OK_Bt, SIGNAL("clicked()"), self.close)
		
		self.connect(self.OK_Bt, SIGNAL("clicked()"), self.close)
		
	def setTitleIcon(self, str):
		self.label.setPixmap(QPixmap(str))
		
	def setTitle(self, str):
		self.label_1.setText(str)

	def isInTitle(self, xPos, yPos):
		return yPos <= 30 and not (yPos <= 22 and (xPos >= self.closeBt.pos().x() and xPos <= self.closeBt.pos().x() + 47))	

	def setTheme(self, str):
		if str == 'blue':
			self.pixmap = QPixmap(":/blueTheme.png")
		elif str == 'red':
			self.pixmap = QPixmap(":/redTheme.png")
		elif str == 'orange':
			self.pixmap = QPixmap(":/orangeTheme.png")
		else:
			self.pixmap = QPixmap(":/transparentTheme.png")

	def paintEvent(self, event):
		self.painter = QPainter()
		self.painter.begin(self)
		self.painter.drawPixmap(self.frame.rect(), self.pixmap.copy(28, 2, 4, 30))
		self.painter.end()	

		linear2 = QLinearGradient(QPoint(self.rect().topLeft()), QPoint(self.rect().bottomLeft()))
		linear2.start()
		linear2.setColorAt(0, Qt.white)
		linear2.finalStop()
		
		self.painter2 = QPainter()
		self.painter2.begin(self)
		self.painter2.setPen(Qt.white)
		self.painter2.setBrush(linear2)
		self.painter2.drawRect(QRect(0, 30, self.width(), self.height() - 30));
		self.painter2.end()
		
		self.painter3 = QPainter()
		self.painter3.begin(self)
		self.painter3.setPen(Qt.gray)
		self.painter3.drawPolyline(QPointF(0, 0), QPointF(0, self.height() - 1), QPointF(self.width() - 1, self.height() - 1), QPointF(self.width() - 1, 0))
		self.painter3.drawPolyline(QPointF(0, 0), QPointF(self.width() - 1, 0))
		self.painter3.end()		

class help(about):
	def __init__(self, parent=None):
		super(help, self).__init__(parent)
		self.setupUI()
		
	def setupUI(self):
		self.frame.setGeometry(QRect(0, 0, 320, 30))
		self.setTitleIcon(":/icon.png")
		self.setTitle("Photo Viewer Help")
		self.setWhatsThis(_translate("Photo Viewer Help", "Photo Viewer Help", None))
		self.setWindowModality(Qt.ApplicationModal)
		self.setObjectName(_fromUtf8("Help"))
		self.resize(320, 340)
		self.setMinimumSize(QSize(320, 340))
		self.setMaximumSize(QSize(320, 340))
		self.textBrowser = QTextBrowser(self)
		self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
		self.textBrowser.setGeometry(QRect(5, 30, 310, 300))
		self.textBrowser.setFrameShape(QFrame.NoFrame)
		self.textBrowser.setHtml(_translate("Photo Viewer Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
			"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
			"p, li { white-space: pre-wrap; }\n"
			"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
			"<p align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt; font-weight:600; color:#00007f;\">Photo Viewer Help</span></p>\n"
			"<table border=\"1\" style=\" margin-top:10px; margin-bottom:10px; margin-left:5px; margin-right:5px;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\">\n"
			"<tr>\n"
			"<td width=\"100\" style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/right.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\">  or </span><img src=\":/wheeldown.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Next image.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/left.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\">  or </span><img src=\":/wheelup.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Previous image.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ctrl.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\">  + </span><img src=\":/wheelup.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Zoom in.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ctrl.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\">  + </span><img src=\":/wheeldown.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Zoom out.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/mouse_left.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\"> x 2</span></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Open image.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/del.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Delete image.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/mouse_scroll.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Fullscreen.</span></p></td></tr>\n"
			"<tr>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/esc.png\" style=\"vertical-align: middle;\" /><span style=\" font-size:10pt;\">  or </span><img src=\":/mouse_scroll.png\" style=\"vertical-align: middle;\" /></p></td>\n"
			"<td style=\" vertical-align:middle;\">\n"
			"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Quit from fullscreen mode.</span></p></td></tr></table></body></html>", None))	

class settings(about):
	def __init__(self, parent=None):
		super(settings, self).__init__(parent)
		self.setupUI()
	
	def setupUI(self):
		self.setObjectName(_fromUtf8("settings"))
		self.resize(400, 290)
		self.setMinimumSize(QSize(400, 290))
		self.setMaximumSize(QSize(400, 290))
		self.frame.setGeometry(QRect(0, 0, 400, 30))
		self.setTitle("Settings")
		self.setTitleIcon(":/icon.png")
		self.tabWidget = QTabWidget(self)
		self.tabWidget.setGeometry(QRect(10, 35, 382, 211))
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.setStyleSheet('font-family: thoma,tahoma;font-size: 11px;')
		self.tab = QWidget(self)
		self.tab.setObjectName(_fromUtf8("tab"))
		self.label_support = QLabel(self.tab)
		self.label_support.setGeometry(QRect(80, 10, 91, 16))
		self.label_support.setObjectName(_fromUtf8("label_support"))
		self.listWidget = QListWidget(self.tab)
		self.listWidget.setGeometry(QRect(80, 30, 81, 145))
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.pushButton = QPushButton(self.tab)
		self.pushButton.setGeometry(QRect(170, 70, 31, 21))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton.setStyleSheet("QPushButton{border:1px solid lightgray;background:transparent}}"
			"QPushButton:hover{border-color:#A9A9A9;background:transparent}"
			"QPushButton:hover:pressed{border:1px solid lightgray;background:rgb(230,230,230)")
		self.pushButton_2 = QPushButton(self.tab)
		self.pushButton_2.setGeometry(QRect(170, 100, 31, 21))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_2.setStyleSheet("QPushButton{border:1px solid lightgray;background:transparent}}"
			"QPushButton:hover{border-color:#A9A9A9;background:transparent}"
			"QPushButton:hover:pressed{border:1px solid lightgray;background:rgb(230,230,230)")
		self.label_register = QLabel(self.tab)
		self.label_register.setGeometry(QRect(210, 10, 91, 16))
		self.label_register.setObjectName(_fromUtf8("label_register"))
		self.listWidget_3 = QListWidget(self.tab)
		self.listWidget_3.setGeometry(QRect(210, 30, 81, 145))
		self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.pushButton_3 = QPushButton(self)
		self.pushButton_3.setGeometry(QRect(220, 250, 75, 23))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.pushButton_3.setStyleSheet("QPushButton{border:1px solid lightgray;background:transparent}}"
			"QPushButton:hover{border-color:#A9A9A9;background:transparent}"
			"QPushButton:hover:pressed{border:1px solid lightgray;background:rgb(230,230,230)")
		self.pushButton_4 = QPushButton(self)
		self.pushButton_4.setGeometry(QRect(316, 250, 75, 23))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.pushButton_4.setStyleSheet("QPushButton{border:1px solid lightgray;background:transparent}}"
			"QPushButton:hover{border-color:#A9A9A9;background:transparent}"
			"QPushButton:hover:pressed{border:1px solid lightgray;background:rgb(230,230,230)")
		self.retranslateUi()
		self.tabWidget.setCurrentIndex(0)
		QMetaObject.connectSlotsByName(self)
		
		for item in fileTypes:
			self.listWidget.addItem(item)
		
		
		self.connect(self.pushButton_3, SIGNAL(_fromUtf8("clicked()")), self.close)
		self.connect(self.pushButton_4, SIGNAL(_fromUtf8("clicked()")), self.close)
		self.connect(self.pushButton, SIGNAL(_fromUtf8("clicked()")), self.addItem)
		self.connect(self.pushButton_2, SIGNAL(_fromUtf8("clicked()")), self.removeItem)

	def retranslateUi(self):
		self.label_support.setText(_translate("settings", "Supported exts:", None))
		self.listWidget.setSortingEnabled(True)
		self.listWidget_3.setSortingEnabled(True)
		self.listWidget.setSelectionMode(3)
		self.listWidget_3.setSelectionMode(3)
		self.pushButton.setText(_translate("settings", "->", None))
		self.pushButton_2.setText(_translate("settings", "<-", None))
		self.label_register.setText(_translate("settings", "Registered exts:", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("settings", "File Association", None))
		self.pushButton_3.setText(_translate("settings", "OK", None))
		self.pushButton_4.setText(_translate("settings", "Cancel", None))
		
	def addItem(self):
		for item in self.listWidget.selectedItems():
			self.listWidget.takeItem(self.listWidget.row(item))
			self.listWidget_3.addItem(item)
			
	def removeItem(self):
		for item in self.listWidget_3.selectedItems():
			self.listWidget_3.takeItem(self.listWidget_3.row(item))
			self.listWidget.addItem(item)
			
class MyApplication(QApplication):
	
	def __init__(self, args):
		super(MyApplication, self).__init__(args)
	
	def GET_X_LPARAM(self, param):
		return param & 0xffff

	def GET_Y_LPARAM(self, param):
		return param >> 16
	
	def winEventFilter(self, msg):
		if msg.message == 0x84:
			form = self.activeWindow()
			if form:
				xPos = self.GET_X_LPARAM(msg.lParam) - form.frameGeometry().x()
				yPos = self.GET_Y_LPARAM(msg.lParam) - form.frameGeometry().y()
				self.desktop = QDesktopWidget()
				self.desktopSize = QDesktopWidget.availableGeometry(self.desktop).size()				
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isTopLeft') and form.isTopLeft(xPos, yPos):
					return True, 0xD
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isTopRight') and form.isTopRight(xPos, yPos):
					return True, 0xE			
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isBottomLeft') and form.isBottomLeft(xPos, yPos):
					return True, 0x10				
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isBottomRight') and form.isBottomRight(xPos, yPos):
					return True, 0x11				
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isLeft') and form.isLeft(xPos):
					return True, 0xA								
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isRight') and form.isRight(xPos):
					return True, 0xB								
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isTop') and form.isTop(yPos):
					return True, 0xC
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isBottom') and form.isBottom(yPos):
					return True, 0xF
				if not form.isFullScreen() and self.desktopSize != form.size() and hasattr(form, 'isInTitle') and form.isInTitle(xPos, yPos):
					return True, 0x2	
		
		elif msg.message == 0xA3:
			form = self.activeWindow()
			if form:
				form.showMax()

		return False, 0
		
if __name__ == '__main__':
	import sys
	app = MyApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	if len(sys.argv) > 1:
		ui.open(_fromUtf8(sys.argv[1]))
	sys.exit(app.exec_())
