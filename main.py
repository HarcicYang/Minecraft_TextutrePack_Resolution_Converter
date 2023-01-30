import sys, zipfile, shutil, win32con, win32api, atexit, tzlocal, os
from PIL import Image, ImageFile
from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets

atexit.register(lambda: shutil.rmtree("./temp"))
localTimeZone = tzlocal.get_localzone()
ImageFile.LOAD_TRUNCATED_IMAGES = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 338)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(578, 338))
        MainWindow.setMaximumSize(QtCore.QSize(578, 338))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(20, 0, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: white;")
        self.Title.setObjectName("Title")
        self.Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.Title_2.setGeometry(QtCore.QRect(20, 50, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Title_2.setFont(font)
        self.Title_2.setStyleSheet("color: white;")
        self.Title_2.setObjectName("Title_2")
        self.Pack = QtWidgets.QLabel(self.centralwidget)
        self.Pack.setGeometry(QtCore.QRect(20, 80, 291, 81))
        self.Pack.setStyleSheet("QLabel {\n"
                                "    color: white;\n"
                                "    background-color: rgb(39, 39, 39);\n"
                                "    border: 0px;\n"
                                "    border-radius: 7px;\n"
                                "}")
        self.Pack.setText("")
        self.Pack.setObjectName("Pack")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.Resolution = QtWidgets.QLabel(self.centralwidget)
        self.Resolution.setGeometry(QtCore.QRect(330, 80, 231, 81))
        self.Resolution.setStyleSheet("QLabel {\n"
                                      "    color: white;\n"
                                      "    background-color: rgb(39, 39, 39);\n"
                                      "    border: 0px;\n"
                                      "    border-radius: 7px;\n"
                                      "}")
        self.Resolution.setText("")
        self.Resolution.setObjectName("Resolution")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.ResolutionText = QtWidgets.QLabel(self.centralwidget)
        self.ResolutionText.setGeometry(QtCore.QRect(350, 130, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ResolutionText.setFont(font)
        self.ResolutionText.setStyleSheet("color: white; background-color: rgb(39, 39, 39);")
        self.ResolutionText.setObjectName("ResolutionText")
        self.FileText = QtWidgets.QLabel(self.centralwidget)
        self.FileText.setGeometry(QtCore.QRect(350, 100, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.FileText.setFont(font)
        self.FileText.setStyleSheet("color: white; background-color: rgb(39, 39, 39);")
        self.FileText.setObjectName("FileText")
        self.FileNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FileNameInput.setGeometry(QtCore.QRect(400, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.FileNameInput.setFont(font)
        self.FileNameInput.setStyleSheet("QLineEdit {\n"
                                         "    border: 0px;\n"
                                         "    border-radius: 5px;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:hover {\n"
                                         "    border-top: 0px;\n"
                                         "    border-left: 0px;\n"
                                         "    border-right: 0px;\n"
                                         "    border-bottom: 2px solid rgb(56, 159, 255);\n"
                                         "}")
        self.FileNameInput.setObjectName("FileNameInput")
        self.PackName = QtWidgets.QLabel(self.centralwidget)
        self.PackName.setGeometry(QtCore.QRect(120, 90, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.PackName.setFont(font)
        self.PackName.setStyleSheet("QLabel {\n"
                                    "    color: white;\n"
                                    "    background-color: rgb(39, 39, 39);\n"
                                    "    border: 0px;\n"
                                    "    border-radius: 7px;\n"
                                    "}")
        self.PackName.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.PackName.setObjectName("PackName")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: white")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 230, 501, 16))
        self.progressBar.setStyleSheet("QProgressBar::chunk\n"
                                       "{\n"
                                       "border-radius:7px;\n"
                                       "background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #01FAFF,stop:1  #26B4FF);\n"
                                       "}\n"
                                       "QProgressBar#progressBar\n"
                                       "{\n"
                                       "height:12px;\n"
                                       "text-align:center;\n"
                                       "color:rgba(0,0,0,0);\n"
                                       "border-radius:7px;\n"
                                       "background: rgb(107, 107, 107);\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.ProgressBar = QtWidgets.QLabel(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(20, 200, 540, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ProgressBar.setFont(font)
        self.ProgressBar.setStyleSheet("QLabel {\n"
                                       "    color: white;\n"
                                       "    background-color: rgb(39, 39, 39);\n"
                                       "    border: 0px;\n"
                                       "    border-radius: 7px;\n"
                                       "}")
        self.ProgressBar.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ChooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseButton.setGeometry(QtCore.QRect(110, 170, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseButton.setFont(font)
        self.ChooseButton.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(35, 178, 255);\n"
                                        "    background-color: rgba(0,0,0,0);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(57, 120, 255);\n"
                                        "}")
        self.ChooseButton.setObjectName("ChooseButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    color: white;\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "    border: 0px;\n"
                                      "    border-radius: 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background: qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #01FAFF,stop:1  #26B4FF);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.Title.raise_()
        self.Title_2.raise_()
        self.Pack.raise_()
        self.label.raise_()
        self.Resolution.raise_()
        self.label_2.raise_()
        self.ResolutionText.raise_()
        self.FileText.raise_()
        self.FileNameInput.raise_()
        self.PackName.raise_()
        self.comboBox.raise_()
        self.ProgressBar.raise_()
        self.progressBar.raise_()
        self.ChooseButton.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 根据时区设置语言
        if localTimeZone == "Asia/Shanghai" or "Asia/Harbin" or "Asia/Chongqing" or "Asia/Urumqi" or "Asia/Kashgar":
            self.translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(self.translate("MainWindow", "Pak converter"))
            self.Title.setText(self.translate("MainWindow", "Resourcepacks resolution converter"))
            self.Title_2.setText(self.translate("MainWindow", "资源包分辨率修改 By HarcicYang"))
            self.label.setText(self.translate("MainWindow", "已选择的资源包"))
            self.label_2.setText(self.translate("MainWindow", "输出选项"))
            self.ResolutionText.setText(self.translate("MainWindow", "分辨率"))
            self.FileText.setText(self.translate("MainWindow", "文件名"))
            self.FileNameInput.setText(self.translate("MainWindow", "new.zip"))
            self.comboBox.setCurrentText(self.translate("MainWindow", "128x"))
            self.comboBox.setItemText(0, self.translate("MainWindow", "16x"))
            self.comboBox.setItemText(1, self.translate("MainWindow", "32x"))
            self.comboBox.setItemText(2, self.translate("MainWindow", "64x"))
            self.comboBox.setItemText(3, self.translate("MainWindow", "128x"))
            self.comboBox.setItemText(4, self.translate("MainWindow", "256x"))
            self.comboBox.setItemText(5, self.translate("MainWindow", "512x"))
            self.comboBox.setItemText(6, self.translate("MainWindow", "1024x"))
            self.comboBox.setItemText(7, self.translate("MainWindow", "2048x"))
            self.comboBox.setItemText(8, self.translate("MainWindow", "4096x"))
            self.ProgressBar.setText(self.translate("MainWindow", "    输出进度"))
            self.ChooseButton.setText(self.translate("MainWindow", "选择"))
            self.ChooseButton.clicked.connect(self.Open)
            self.pushButton.setText(self.translate("MainWindow", "开始"))
            self.pushButton.clicked.connect(self.Run)
        else:
            self.translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(self.translate("MainWindow", "Pak converter"))
            self.Title.setText(self.translate("MainWindow", "Resourcepacks resolution converter"))
            self.Title_2.setText(self.translate("MainWindow", "By HarcicYang"))
            self.label.setText(self.translate("MainWindow", "Chosen resource pack"))
            self.label_2.setText(self.translate("MainWindow", "Options"))
            self.ResolutionText.setText(self.translate("MainWindow", "Resolution"))
            self.FileText.setText(self.translate("MainWindow", "Output file name"))
            self.FileNameInput.setText(self.translate("MainWindow", "new.zip"))
            self.comboBox.setCurrentText(self.translate("MainWindow", "128x"))
            self.comboBox.setItemText(0, self.translate("MainWindow", "16x"))
            self.comboBox.setItemText(1, self.translate("MainWindow", "32x"))
            self.comboBox.setItemText(2, self.translate("MainWindow", "64x"))
            self.comboBox.setItemText(3, self.translate("MainWindow", "128x"))
            self.comboBox.setItemText(4, self.translate("MainWindow", "256x"))
            self.comboBox.setItemText(5, self.translate("MainWindow", "512x"))
            self.comboBox.setItemText(6, self.translate("MainWindow", "1024x"))
            self.comboBox.setItemText(7, self.translate("MainWindow", "2048x"))
            self.comboBox.setItemText(8, self.translate("MainWindow", "4096x"))
            self.ProgressBar.setText(self.translate("MainWindow", "    Progress"))
            self.ChooseButton.setText(self.translate("MainWindow", "Choose one"))
            self.ChooseButton.clicked.connect(self.Open)
            self.pushButton.setText(self.translate("MainWindow", "Start"))
            self.pushButton.clicked.connect(self.Run)

    def Open(self):  # 文件打开方法
        if localTimeZone == "Asia/Shanghai" or "Asia/Harbin" or "Asia/Chongqing" or "Asia/Urumqi" or "Asia/Kashgar":
            filePath = filedialog.askopenfilename(title="选择一个资源包", filetypes=(("资源包", "*.zip"),))
        else:
            filePath = filedialog.askopenfilename(title="Choose a resource pack",
                                                  filetypes=(("Resource pack", "*.zip"),))
        try:
            zip = zipfile.ZipFile(filePath)
            zipfile.ZipFile.extractall(zip, './temp/files/')
            zip.close()
            with open("./temp/files/pack.mcmeta", "r", errors="ignore") as f:
                f.read()
            self.PackImg = QtWidgets.QWidget(self.centralwidget)
            self.PackImg.setGeometry(QtCore.QRect(20, 80, 81, 81))
            self.PackImg.setAutoFillBackground(False)
            self.PackImg.setStyleSheet(
                "border: 0px; border-radius: 7px; border-image: url(" + "./temp/files/pack.png" + ");")
            self.PackImg.setObjectName("PackImg")
            self.PackImg.raise_()
            self.PackImg.show()
            for i in filePath.split("/"):
                name = i
            self.PackName.setText(self.translate("MainWindow", name))
        except:
            if localTimeZone == "Asia/Shanghai" or "Asia/Harbin" or "Asia/Chongqing" or "Asia/Urumqi" or "Asia/Kashgar":
                win32api.MessageBox(0,
                                    "您可能选择了一个不正确的资源包\n若您坚信您选择的资源包没有问题且此问题频繁出现，请前往GitHub仓库反馈",
                                    "提醒", win32con.MB_ICONERROR)
            else:
                win32api.MessageBox(0,
                                    "You might chose a bad resource pack.\n"
                                    "If you believe that you have chosen a normal resource pack "
                                    "and this problem appear again and again, "
                                    "please go to the GitHub repository to provide feedback.",
                                    "Notification", win32con.MB_ICONERROR)


    def Run(self):  # 运行
        self.OutPutFile = self.FileNameInput.text()
        OutPutOption = self.comboBox.currentText()
        if OutPutOption == "16x":  # 匹配材质分辨率
            width = 16
        elif OutPutOption == "32x":
            width = 32
        elif OutPutOption == "64x":
            width = 64
        elif OutPutOption == "128x":
            width = 128
        elif OutPutOption == "256x":
            width = 256
        elif OutPutOption == "512x":
            width = 512
        elif OutPutOption == "1024x":
            width = 1024
        elif OutPutOption == "2048x":
            width = 2048
        elif OutPutOption == "4096x":
            width = 4096
        TexturePath = "./temp/files/assets/minecraft/textures/"
        for i in os.listdir(TexturePath):  # 获取材质贴图
            if i == "models":
                continue
            else:
                ProcessPath = TexturePath + i + "/"
                print("ProcessPath#: " + ProcessPath)
                List = os.listdir(ProcessPath)
                ProcessList = []
                for j in List:
                    if ".png" in j:
                        if ".png." in j:
                            continue
                        ProcessList.append(ProcessPath + j)
                        print("ProcessPath#:" + ProcessPath + j)
                    else:
                        try:
                            TempList = os.listdir(ProcessPath + j)
                            for k in TempList:
                                if ".png" in k:
                                    if ".png." in k:
                                        continue
                                    ProcessList.append(ProcessPath + j + "/" + k)
                        except:
                            pass
                print("note: List finished")
                self.progressBar.setRange(0, len(ProcessList) + 20)
                ValueNow = 10
                self.progressBar.setValue(ValueNow)
                print("ProgressBar Update")
                for j in ProcessList:
                    print("processing: " + j)
                    img = Image.open(j)
                    if img.width != img.height:
                        height = (img.height / img.width) * width
                        img.resize((width, int(height))).save(j)
                        print("saved: " + j + "#" + str(width) + "x" + str(int(height)))
                        ValueNow += 1
                        self.progressBar.setValue(ValueNow)
                        print("ProgressBar Update")
                    elif img.width == img.height:
                        img.resize((width, width)).save(j)
                        print("saved: " + j + "#" + str(width) + "x" + str(width))
                        ValueNow += 1
                        self.progressBar.setValue(ValueNow)
                        print("ProgressBar Update")

        self.progressBar.setValue(ValueNow + 10)
        zip = zipfile.ZipFile(self.OutPutFile, "w", zipfile.ZIP_DEFLATED)  # 压缩输出文件
        for path, dirnames, filenames in os.walk("./temp/files/"):
            fpath = path.replace("./temp/files/", '')

            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        if localTimeZone == "Asia/Shanghai" or "Asia/Harbin" or "Asia/Chongqing" or "Asia/Urumqi" or "Asia/Kashgar":
            win32api.MessageBox(0, "完成，文件保存为" + os.getcwd() + self.OutPutFile, "提醒", win32con.MB_ICONASTERISK)
        else:
            win32api.MessageBox(0, "Finish! The file already saved to " + os.getcwd() + self.OutPutFile, "Notification", win32con.MB_ICONASTERISK)


from PyQt5.QtWidgets import QApplication, QMainWindow  # 加载Qt窗口

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
