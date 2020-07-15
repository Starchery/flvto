# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 655)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"../../../Zafiro-icons/Zafiro-icons/apps/scalable/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAdd_Video = QAction(MainWindow)
        self.actionAdd_Video.setObjectName(u"actionAdd_Video")
        icon1 = QIcon()
        icon1.addFile(u"../../../Zafiro-icons/Zafiro-icons/categories/22/applications-multimedia.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Video.setIcon(icon1)
        self.actionAdd_Playlist = QAction(MainWindow)
        self.actionAdd_Playlist.setObjectName(u"actionAdd_Playlist")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionResume = QAction(MainWindow)
        self.actionResume.setObjectName(u"actionResume")
        icon2 = QIcon()
        icon2.addFile(u"../../../Zafiro-icons/Zafiro-icons/actions/22/media-playback-start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionResume.setIcon(icon2)
        self.actionPause = QAction(MainWindow)
        self.actionPause.setObjectName(u"actionPause")
        icon3 = QIcon()
        icon3.addFile(u"../../../Zafiro-icons/Zafiro-icons/actions/22/media-playback-pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPause.setIcon(icon3)
        self.actionResume_All = QAction(MainWindow)
        self.actionResume_All.setObjectName(u"actionResume_All")
        self.actionPause_All = QAction(MainWindow)
        self.actionPause_All.setObjectName(u"actionPause_All")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionShow = QAction(MainWindow)
        self.actionShow.setObjectName(u"actionShow")
        self.actionShow.setCheckable(True)
        self.actionNormal = QAction(MainWindow)
        self.actionNormal.setObjectName(u"actionNormal")
        self.actionNormal.setCheckable(True)
        self.actionVerbose = QAction(MainWindow)
        self.actionVerbose.setObjectName(u"actionVerbose")
        self.actionVerbose.setCheckable(True)
        self.actionWarning_Messages = QAction(MainWindow)
        self.actionWarning_Messages.setObjectName(u"actionWarning_Messages")
        self.actionWarning_Messages.setCheckable(True)
        self.actionCritical_Messages = QAction(MainWindow)
        self.actionCritical_Messages.setObjectName(u"actionCritical_Messages")
        self.actionCritical_Messages.setCheckable(True)
        self.actionStatistics = QAction(MainWindow)
        self.actionStatistics.setObjectName(u"actionStatistics")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon4 = QIcon()
        icon4.addFile(u"../../../Zafiro-icons/Zafiro-icons/apps/scalable/control-center2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon4)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        self.widgetVLayout = QVBoxLayout(self.widget)
        self.widgetVLayout.setObjectName(u"widgetVLayout")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.mainTab.setAcceptDrops(True)
        self.mainTabVLayout = QVBoxLayout(self.mainTab)
        self.mainTabVLayout.setObjectName(u"mainTabVLayout")
        self.mainVLayout = QVBoxLayout()
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainBannerHLayout = QHBoxLayout()
        self.mainBannerHLayout.setObjectName(u"mainBannerHLayout")
        self.mainBannerLogo = QLabel(self.mainTab)
        self.mainBannerLogo.setObjectName(u"mainBannerLogo")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBannerLogo.sizePolicy().hasHeightForWidth())
        self.mainBannerLogo.setSizePolicy(sizePolicy)
        self.mainBannerLogo.setPixmap(QPixmap(u"../../../Zafiro-icons/Zafiro-icons/apps/scalable/music.svg"))
        self.mainBannerLogo.setScaledContents(True)
        self.mainBannerLogo.setAlignment(Qt.AlignCenter)

        self.mainBannerHLayout.addWidget(self.mainBannerLogo)

        self.mainBannerTitle = QLabel(self.mainTab)
        self.mainBannerTitle.setObjectName(u"mainBannerTitle")
        sizePolicy.setHeightForWidth(self.mainBannerTitle.sizePolicy().hasHeightForWidth())
        self.mainBannerTitle.setSizePolicy(sizePolicy)
        self.mainBannerTitle.setAlignment(Qt.AlignCenter)

        self.mainBannerHLayout.addWidget(self.mainBannerTitle)


        self.mainVLayout.addLayout(self.mainBannerHLayout)

        self.mainFormVLayout = QVBoxLayout()
        self.mainFormVLayout.setObjectName(u"mainFormVLayout")
        self.mainFormFrame = QFrame(self.mainTab)
        self.mainFormFrame.setObjectName(u"mainFormFrame")
        self.mainFormFrame.setFrameShape(QFrame.Box)
        self.mainFormFrame.setFrameShadow(QFrame.Sunken)
        self.mainFormFrameLayout = QHBoxLayout(self.mainFormFrame)
        self.mainFormFrameLayout.setSpacing(9)
        self.mainFormFrameLayout.setObjectName(u"mainFormFrameLayout")
        self.mainFormFrameLayout.setContentsMargins(9, 9, 9, 9)
        self.mainFormInnerVLayout = QVBoxLayout()
        self.mainFormInnerVLayout.setObjectName(u"mainFormInnerVLayout")
        self.mainEnterUrlLabel = QLabel(self.mainFormFrame)
        self.mainEnterUrlLabel.setObjectName(u"mainEnterUrlLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.mainEnterUrlLabel.setFont(font1)
        self.mainEnterUrlLabel.setTextFormat(Qt.AutoText)
        self.mainEnterUrlLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.mainFormInnerVLayout.addWidget(self.mainEnterUrlLabel)

        self.mainUrlLine = QLineEdit(self.mainFormFrame)
        self.mainUrlLine.setObjectName(u"mainUrlLine")
        self.mainUrlLine.setFont(font1)

        self.mainFormInnerVLayout.addWidget(self.mainUrlLine)

        self.mainSaveToLabel = QLabel(self.mainFormFrame)
        self.mainSaveToLabel.setObjectName(u"mainSaveToLabel")
        self.mainSaveToLabel.setFont(font1)
        self.mainSaveToLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.mainFormInnerVLayout.addWidget(self.mainSaveToLabel)

        self.mainFormFileHLayout = QHBoxLayout()
        self.mainFormFileHLayout.setObjectName(u"mainFormFileHLayout")
        self.mainPathCombo = QComboBox(self.mainFormFrame)
        self.mainPathCombo.setObjectName(u"mainPathCombo")
        self.mainPathCombo.setFont(font1)

        self.mainFormFileHLayout.addWidget(self.mainPathCombo)

        self.mainPathBrowseBtn = QToolButton(self.mainFormFrame)
        self.mainPathBrowseBtn.setObjectName(u"mainPathBrowseBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainPathBrowseBtn.sizePolicy().hasHeightForWidth())
        self.mainPathBrowseBtn.setSizePolicy(sizePolicy1)
        self.mainPathBrowseBtn.setFont(font1)

        self.mainFormFileHLayout.addWidget(self.mainPathBrowseBtn)


        self.mainFormInnerVLayout.addLayout(self.mainFormFileHLayout)

        self.mainDownloadBtn = QPushButton(self.mainFormFrame)
        self.mainDownloadBtn.setObjectName(u"mainDownloadBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainDownloadBtn.sizePolicy().hasHeightForWidth())
        self.mainDownloadBtn.setSizePolicy(sizePolicy2)
        self.mainDownloadBtn.setFont(font1)

        self.mainFormInnerVLayout.addWidget(self.mainDownloadBtn)


        self.mainFormFrameLayout.addLayout(self.mainFormInnerVLayout)


        self.mainFormVLayout.addWidget(self.mainFormFrame)


        self.mainVLayout.addLayout(self.mainFormVLayout)


        self.mainTabVLayout.addLayout(self.mainVLayout)

        self.tabWidget.addTab(self.mainTab, icon, "")
        self.transfersTab = QWidget()
        self.transfersTab.setObjectName(u"transfersTab")
        self.transfersTabVLayout = QVBoxLayout(self.transfersTab)
        self.transfersTabVLayout.setObjectName(u"transfersTabVLayout")
        self.transfersVLayout = QVBoxLayout()
        self.transfersVLayout.setObjectName(u"transfersVLayout")
        self.transfersPanesHLayout = QHBoxLayout()
        self.transfersPanesHLayout.setObjectName(u"transfersPanesHLayout")
        self.transfersTreeHLayout = QHBoxLayout()
        self.transfersTreeHLayout.setObjectName(u"transfersTreeHLayout")
        self.transfersTreeList = QListWidget(self.transfersTab)
        self.transfersTreeList.setObjectName(u"transfersTreeList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.transfersTreeList.sizePolicy().hasHeightForWidth())
        self.transfersTreeList.setSizePolicy(sizePolicy3)

        self.transfersTreeHLayout.addWidget(self.transfersTreeList)


        self.transfersPanesHLayout.addLayout(self.transfersTreeHLayout)

        self.transfersListVLayout = QVBoxLayout()
        self.transfersListVLayout.setObjectName(u"transfersListVLayout")
        self.transfersListBtnsVLayout = QVBoxLayout()
        self.transfersListBtnsVLayout.setObjectName(u"transfersListBtnsVLayout")
        self.transfersListBtnsHLayout = QHBoxLayout()
        self.transfersListBtnsHLayout.setObjectName(u"transfersListBtnsHLayout")
        self.transfersAddBtn = QPushButton(self.transfersTab)
        self.transfersAddBtn.setObjectName(u"transfersAddBtn")

        self.transfersListBtnsHLayout.addWidget(self.transfersAddBtn)

        self.transfersRemoveBtn = QPushButton(self.transfersTab)
        self.transfersRemoveBtn.setObjectName(u"transfersRemoveBtn")

        self.transfersListBtnsHLayout.addWidget(self.transfersRemoveBtn)

        self.transfersPauseBtn = QPushButton(self.transfersTab)
        self.transfersPauseBtn.setObjectName(u"transfersPauseBtn")

        self.transfersListBtnsHLayout.addWidget(self.transfersPauseBtn)

        self.transfersStopBtn = QPushButton(self.transfersTab)
        self.transfersStopBtn.setObjectName(u"transfersStopBtn")

        self.transfersListBtnsHLayout.addWidget(self.transfersStopBtn)


        self.transfersListBtnsVLayout.addLayout(self.transfersListBtnsHLayout)


        self.transfersListVLayout.addLayout(self.transfersListBtnsVLayout)

        self.tableWidget = QTableWidget(self.transfersTab)
        self.tableWidget.setObjectName(u"tableWidget")

        self.transfersListVLayout.addWidget(self.tableWidget)


        self.transfersPanesHLayout.addLayout(self.transfersListVLayout)


        self.transfersVLayout.addLayout(self.transfersPanesHLayout)

        self.transfersInfoFrame = QFrame(self.transfersTab)
        self.transfersInfoFrame.setObjectName(u"transfersInfoFrame")
        self.transfersInfoFrame.setAutoFillBackground(True)
        self.transfersInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.transfersInfoVLayout = QVBoxLayout(self.transfersInfoFrame)
        self.transfersInfoVLayout.setObjectName(u"transfersInfoVLayout")
        self.transfersBarHLayout = QHBoxLayout()
        self.transfersBarHLayout.setObjectName(u"transfersBarHLayout")
        self.transfersBarLabel = QLabel(self.transfersInfoFrame)
        self.transfersBarLabel.setObjectName(u"transfersBarLabel")

        self.transfersBarHLayout.addWidget(self.transfersBarLabel)

        self.transfersBar = QProgressBar(self.transfersInfoFrame)
        self.transfersBar.setObjectName(u"transfersBar")
        self.transfersBar.setValue(0)

        self.transfersBarHLayout.addWidget(self.transfersBar)


        self.transfersInfoVLayout.addLayout(self.transfersBarHLayout)

        self.line = QFrame(self.transfersInfoFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.transfersInfoVLayout.addWidget(self.line)

        self.transfersInfoGBox = QGroupBox(self.transfersInfoFrame)
        self.transfersInfoGBox.setObjectName(u"transfersInfoGBox")
        self.transfersInfoGBoxLayout = QVBoxLayout(self.transfersInfoGBox)
        self.transfersInfoGBoxLayout.setObjectName(u"transfersInfoGBoxLayout")
        self.transfersInfoParagraph = QLabel(self.transfersInfoGBox)
        self.transfersInfoParagraph.setObjectName(u"transfersInfoParagraph")

        self.transfersInfoGBoxLayout.addWidget(self.transfersInfoParagraph)


        self.transfersInfoVLayout.addWidget(self.transfersInfoGBox)


        self.transfersVLayout.addWidget(self.transfersInfoFrame)


        self.transfersTabVLayout.addLayout(self.transfersVLayout)

        icon5 = QIcon()
        icon5.addFile(u"../../../Zafiro-icons/Zafiro-icons/panel/22-light/connect_established.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.transfersTab, icon5, "")

        self.widgetVLayout.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 735, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuLog = QMenu(self.menuView)
        self.menuLog.setObjectName(u"menuLog")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(32, 32))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.mainEnterUrlLabel.setBuddy(self.mainUrlLine)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionAdd_Video)
        self.menuFile.addAction(self.actionAdd_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionResume)
        self.menuEdit.addAction(self.actionPause)
        self.menuEdit.addAction(self.actionResume_All)
        self.menuEdit.addAction(self.actionPause_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menuView.addAction(self.actionStatistics)
        self.menuView.addAction(self.menuLog.menuAction())
        self.menuLog.addAction(self.actionShow)
        self.menuLog.addSeparator()
        self.menuLog.addAction(self.actionNormal)
        self.menuLog.addAction(self.actionVerbose)
        self.menuLog.addAction(self.actionWarning_Messages)
        self.menuLog.addAction(self.actionCritical_Messages)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionAdd_Video)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionResume)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.transfersRemoveBtn.clicked.connect(self.tableWidget.clearSelection)
        self.mainUrlLine.returnPressed.connect(self.mainDownloadBtn.click)
        self.tableWidget.cellActivated.connect(self.transfersBar.setValue)
        self.tableWidget.cellActivated.connect(self.transfersInfoGBox.update)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MPy3", None))
        self.actionAdd_Video.setText(QCoreApplication.translate("MainWindow", u"Add Video", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Video.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Playlist.setText(QCoreApplication.translate("MainWindow", u"Add Playlist", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Playlist.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionResume.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
#if QT_CONFIG(shortcut)
        self.actionResume.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
#if QT_CONFIG(shortcut)
        self.actionPause.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionResume_All.setText(QCoreApplication.translate("MainWindow", u"Resume All", None))
#if QT_CONFIG(shortcut)
        self.actionResume_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPause_All.setText(QCoreApplication.translate("MainWindow", u"Pause All", None))
#if QT_CONFIG(shortcut)
        self.actionPause_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionShow.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.actionNormal.setText(QCoreApplication.translate("MainWindow", u"Normal Messages", None))
        self.actionVerbose.setText(QCoreApplication.translate("MainWindow", u"Information Messages", None))
        self.actionWarning_Messages.setText(QCoreApplication.translate("MainWindow", u"Warning Messages", None))
        self.actionCritical_Messages.setText(QCoreApplication.translate("MainWindow", u"Critical Messages", None))
        self.actionStatistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.mainBannerLogo.setText("")
        self.mainBannerTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">MPy3</span></p><p><span style=\" font-size:large; font-weight:600;\">Video converter</span></p><p><span style=\" font-size:small; font-weight:600;\">Version 1.0</span></p></body></html>", None))
        self.mainEnterUrlLabel.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<head/>\n"
"<body>\n"
"	<p>\n"
"	<span style=\" font-size:12pt;\">Enter a video URL to convert</span>\n"
"	</p>\n"
"\n"
"	<p>\n"
"	<span style=\" font-style:italic; color:#5a5a5a;\">(example: https://www.youtube.com/watchv?fakevideourl)\n"
"	</span>\n"
"	</p>\n"
"</body>\n"
"</html>", None))
        self.mainSaveToLabel.setText(QCoreApplication.translate("MainWindow", u"Save to", None))
        self.mainPathBrowseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.mainDownloadBtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.transfersAddBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.transfersRemoveBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.transfersPauseBtn.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.transfersStopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.transfersBarLabel.setText(QCoreApplication.translate("MainWindow", u"Progress:", None))
        self.transfersInfoGBox.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.transfersInfoParagraph.setText(QCoreApplication.translate("MainWindow", u"Placeholder Text<br>Placeholder Text<br>Placeholder Text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transfersTab), QCoreApplication.translate("MainWindow", u"Transfers", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

