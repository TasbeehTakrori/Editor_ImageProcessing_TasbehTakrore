import io
import math
from unittest import result

import cv2
import imutils
import numpy
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1249, 950)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(True)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(190, 190, 190);")
        Dialog.setSizeGripEnabled(False)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(-10, 0, 1261, 151))
        self.lineEdit.setStyleSheet("background-color: rgb(4, 190, 106);\n"
"border-bottom-color: rgb(4, 190, 106);\n"
"border-color: rgb(4, 190, 106);\n"
"background-color: rgb(58, 99, 81);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 431, 101))
        self.label.setStyleSheet("background-color: rgb(58, 99, 81);\n"
"font: 8pt \"Pristina\";")
        self.label.setObjectName("label")
        self.openimage = QtWidgets.QPushButton(Dialog)
        self.openimage.setGeometry(QtCore.QRect(1100, 810, 71, 41))
        self.openimage.setStyleSheet("background-color: rgb(228, 130, 87);")
        self.openimage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon\\export (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openimage.setIcon(icon)
        self.openimage.setObjectName("openimage")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-140, 20, 341, 121))
        self.label_2.setStyleSheet("background-color: rgb(58, 99, 81);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Icon\\graphic-designer (2).png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(1080, 140, 171, 751))
        self.lineEdit_2.setStyleSheet("\n"
"background-color: rgb(57, 50, 50);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.saveimage = QtWidgets.QPushButton(Dialog)
        self.saveimage.setGeometry(QtCore.QRect(1170, 810, 71, 41))
        self.saveimage.setStyleSheet("background-color: rgb(228, 130, 87);")
        self.saveimage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon\\import (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveimage.setIcon(icon1)
        self.saveimage.setObjectName("saveimage")
        self.contrastSlider = QtWidgets.QSlider(Dialog)
        self.contrastSlider.setGeometry(QtCore.QRect(1180, 160, 61, 261))
        self.contrastSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.contrastSlider.setMouseTracking(True)
        self.contrastSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.contrastSlider.setAcceptDrops(False)
        self.contrastSlider.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.contrastSlider.setMaximum(30)
        self.contrastSlider.setPageStep(2)
        self.contrastSlider.setProperty("value", 15)
        self.contrastSlider.setSliderPosition(15)
        self.contrastSlider.setOrientation(QtCore.Qt.Vertical)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.contrastSlider.setTickInterval(6)
        self.contrastSlider.setObjectName("contrastSlider")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(1180, 420, 61, 31))
        self.label_5.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.label_5.setObjectName("label_5")
        self.brightnessSlider_2 = QtWidgets.QSlider(Dialog)
        self.brightnessSlider_2.setGeometry(QtCore.QRect(1110, 160, 61, 261))
        self.brightnessSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.brightnessSlider_2.setMouseTracking(True)
        self.brightnessSlider_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.brightnessSlider_2.setAcceptDrops(False)
        self.brightnessSlider_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.brightnessSlider_2.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.brightnessSlider_2.setMaximum(30)
        self.brightnessSlider_2.setSingleStep(2)
        self.brightnessSlider_2.setPageStep(2)
        self.brightnessSlider_2.setProperty("value", 15)
        self.brightnessSlider_2.setSliderPosition(15)
        self.brightnessSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.brightnessSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.brightnessSlider_2.setTickInterval(4)
        self.brightnessSlider_2.setObjectName("brightnessSlider_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(1110, 420, 61, 31))
        self.label_6.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.label_6.setObjectName("label_6")
        self.autobright = QtWidgets.QPushButton(Dialog)
        self.autobright.setGeometry(QtCore.QRect(1100, 510, 141, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon\\sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autobright.setIcon(icon2)
        self.autobright.setCheckable(False)
        self.autobright.setObjectName("autobright")
        self.thresholding = QtWidgets.QPushButton(Dialog)
        self.thresholding.setGeometry (QtCore.QRect(1100, 550, 141, 41))
        self.thresholding.setTabletTracking(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon\\yin-yang-symbol-variant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thresholding.setIcon(icon3)
        self.thresholding.setShortcut("")
        self.thresholding.setCheckable(False)
        self.thresholding.setObjectName("thresholding")
        self.autocontrast = QtWidgets.QPushButton(Dialog)
        self.autocontrast.setGeometry(QtCore.QRect(1100, 470, 141, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.autocontrast.setFont(font)
        self.autocontrast.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon\\contrast-circle-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autocontrast.setIcon(icon4)
        self.autocontrast.setCheckable(False)
        self.autocontrast.setChecked(False)
        self.autocontrast.setAutoRepeat(False)
        self.autocontrast.setAutoExclusive(False)
        self.autocontrast.setObjectName("autocontrast")
        self.iconmajic = QtWidgets.QLabel(Dialog)
        self.iconmajic.setGeometry(QtCore.QRect(920, 650, 321, 121))
        self.iconmajic.setStyleSheet("background-color: rgb(57, 50, 50);")
        self.iconmajic.setText("")
        self.iconmajic.setPixmap(QtGui.QPixmap("Icon\\hat (2).png"))
        self.iconmajic.setObjectName("iconmajic")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 150, 1091, 721))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setStyleSheet("background-color: rgb(242, 237, 215);")
        self.lineEdit_3.setCursorPosition(0)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.buttonmagic = QtWidgets.QPushButton(Dialog)
        self.buttonmagic.setGeometry(QtCore.QRect(1120, 770, 101, 21))
        self.buttonmagic.setStyleSheet("background-color: rgb(252, 255, 184);")
        self.buttonmagic.setObjectName("buttonmagic")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(540, 170, 501, 681))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.thresholding_2 = QtWidgets.QPushButton(Dialog)
        self.thresholding_2.setGeometry(QtCore.QRect(1100, 590, 141, 41))
        self.thresholding_2.setTabletTracking(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon\\stacked-files.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thresholding_2.setIcon(icon5)
        self.thresholding_2.setShortcut("")
        self.thresholding_2.setCheckable(False)
        self.thresholding_2.setObjectName("thresholding_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 501, 681))
        self.label_7.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(420, 100, 631, 41))
        self.label_8.setStyleSheet("font: 9pt \"Tempus Sans ITC\";\n"
"background-color: rgb(58, 99, 81);")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 879, 1261, 51))
        self.label_3.setStyleSheet("background-color: rgb(228, 130, 87);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(0, 860, 1251, 21))
        self.label_9.setStyleSheet("background-color: rgb(57, 50, 50);\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(0, 930, 1251, 21))
        self.label_10.setStyleSheet("background-color: rgb(57, 50, 50);\n"
"background-color: rgb(58, 99, 81);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(140, 890, 921, 31))
        self.label_11.setStyleSheet("background-color: rgb(228, 130, 87);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.openimage.raise_()
        self.saveimage.raise_()
        self.contrastSlider.raise_()
        self.label_5.raise_()
        self.brightnessSlider_2.raise_()
        self.label_6.raise_()
        self.autobright.raise_()
        self.thresholding.raise_()
        self.autocontrast.raise_()
        self.iconmajic.raise_()
        self.lineEdit_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.buttonmagic.raise_()
        self.label_4.raise_()
        self.thresholding_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_2.setBuddy(self.lineEdit)
        self.label_5.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.lineEdit_3)

        self.retranslateUi(Dialog)
        self.brightnessSlider_2.valueChanged['int'].connect(self.brightness_value)
        self.contrastSlider.valueChanged['int'].connect(self.contrast_value)
        self.autocontrast.clicked.connect(self.autocont)
        self.autobright.clicked.connect(self.autobri)
        self.thresholding_2.clicked.connect(self.bitplanfun) ##bit blane, not thre..
        self.thresholding.clicked.connect(self.thresholdingFun)
        self.buttonmagic.clicked.connect(self.maj)
        self.openimage.clicked.connect(self.label_4.clear)
        self.saveimage.clicked.connect(self.savePhoto)
        self.openimage.clicked.connect(self.loadImage)
        self.saveimage.clicked.connect(self.label_7.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.file_name = None  # Will hold the image address location
        self.tmp = None  # Will hold the temporary image for display

        self.image = None
        self.isemageexist =0


        self.brightness_value_now = 15  # Updated brightness value
        self.contrast_value_now = 15  # Updated contrast value
        self.flage =0

    def loadImage(self):


            self.file_name = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
            self.image = cv2.imread(self.file_name, 0)

            if (self.file_name):
                self.isemageexist = 1

                print(self.image.shape)
                self.setPhoto(self.image)

                _translate = QtCore.QCoreApplication.translate
                self.label_11.setText(_translate("Dialog",
                                                 "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">...</span></p></body></html>"))
            else:
                pass
    def setPhoto(self, image):

                self.tmp = image
                image = imutils.resize(image, width=500)
                frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                self.label_7.setPixmap(QtGui.QPixmap.fromImage(image))
                self.label_4.setPixmap(QtGui.QPixmap.fromImage(image))

    def setPhoto2(self, image):
                self.tmp = image
                image = imutils.resize(image, width=500)
                frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                self.label_4.setPixmap(QtGui.QPixmap.fromImage(image))

    def brightness_value(self, value):

        if (self.isemageexist== 0):
            self.setMessage(1)
        else:
            print("value")
            self.brightness_value_now = value
            print('Brightness: ', value)
            self.change()
        print("hi2")

    def changeBrightness(self):
        print("change brhight")
        if (self.brightness_value_now == 15):
            gval = 1
        elif (self.brightness_value_now > 15):
            gval = 1-(( self.brightness_value_now-15) / 15)
        else:
            gval = 1 + ((15-self.brightness_value_now ) / 15)

        gamma_point_four = np.array(255 * (self.image / 255) ** gval, dtype='uint8')
        self.tmp =  gamma_point_four


    def change(self):
        self.changeBrightness()
        des = self.contfun()
        self.setPhoto2(des)

    def contrast_value(self, value):
        if (self.isemageexist== 0):
            self.setMessage(1)
        else:
         self.contrast_value_now = value
         print('contrast: ', value)
         self.change()

    def contfun(self):
        print("change cont")

        nalph= (self.contrast_value_now-15)/15
        alpha=1+ nalph
        norm_img2  = cv2.convertScaleAbs(self.tmp, alpha= alpha, beta=0)
        return norm_img2

    def autobri(self):
     if (self.isemageexist == 0):
            self.setMessage(1)
     else:

         # compute gamma = log(mid*255)/log(mean)
         mid = 0.5
         mean = np.mean(self.image)
         gamma = math.log(mid * 255) / math.log(mean)
         print(gamma)

         # do gamma correction
         img_gamma = np.power(self.image, gamma).clip(0, 255).astype(np.uint8)
         self.setPhoto2(img_gamma)


    def bitplanfun(self):
     if (self.isemageexist == 0):
            self.setMessage(1)
     else:
        self.setMessage(4)

        a1 = []
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                a1.append(np.binary_repr(self.image[i][j], width=8))  # width = no. of bits

        eight_bit_img = (np.array([int(i[0]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0],self.image.shape[1])
        #cv2.imshow("eight_bit_img", eight_bit_img )
        seven_bit_img = (np.array([int(i[1]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
        #cv2.imshow("seven_bit_img", seven_bit_img)
        six_bit_img = (np.array([int(i[2]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
       # cv2.imshow("six_bit_img", six_bit_img)
        five_bit_img = (np.array([int(i[3]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
        #cv2.imshow("five_bit_img", five_bit_img)
        four_bit_img = (np.array([int(i[4]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
       # cv2.imshow("four_bit_img", four_bit_img)
        three_bit_img = (np.array([int(i[5]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
        #cv2.imshow("three_bit_img", three_bit_img )
        two_bit_img = (np.array([int(i[6]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
      #  cv2.imshow("two_bit_img", two_bit_img)
        one_bit_img = (np.array([int(i[7]) for i in a1], dtype=np.uint8) * 255).reshape(self.image.shape[0], self.image.shape[1])
       # cv2.imshow("one_bit_img", one_bit_img)

        concat1 = np.concatenate((eight_bit_img, seven_bit_img,six_bit_img,five_bit_img), axis=1)
        concat2 = np.concatenate((four_bit_img , three_bit_img,two_bit_img ,one_bit_img), axis=1)
        concat3 = np.concatenate((concat1, concat2), axis =0)
        self.setPhoto2(concat3)

        #cv2.imshow("cocat", concat3)
        self.setMessage(2)

        print("End ya Tasbeeeha")

    def maj(self):

        if (self.isemageexist == 0):
            self.setMessage(1)
        else:
          kernel = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

          dst = cv2.filter2D(self.tmp, -1, kernel)
          self.setPhoto2(dst)

    def autocont(self):
     if (self.isemageexist == 0):
            self.setMessage(1)
     else:
         cl1= cv2.equalizeHist(self.image)
         self.setPhoto2(cl1)


    def thresholdingFun(self):
        if (self.isemageexist == 0):
            self.setMessage(1)
        else:
         ret,th3 = cv2.threshold(self.tmp,127,255,cv2.THRESH_BINARY)
         self.setPhoto2(th3)


    def savePhoto(self):

        if(self.isemageexist == 1):
         if(self.file_name):

            filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
            cv2.imwrite(filename, self.tmp)
            self.setMessage(3)
         else:
             print("no file")
             pass
        else:
            pass


    def setMessage(self, f):
        _translate = QtCore.QCoreApplication.translate
        if(f==1):
          self.label_11.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">You must upload an image first! You can use the orange button on the right. </span></p></body></html>"))
        elif (f==2):
            self.label_11.setText(_translate("Dialog",
                                             "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">These images are arranged from left to right, from the eighth bit plane to the first bit plane. Save the image to see it better! </span></p></body></html>"))
        elif (f==3):
            self.label_11.setText(_translate("Dialog",
                                             "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\"> Good job! Image saved successfully. You can upload another image to edit it | يبدو عملُك رائعًا!  </span></p></body></html>"))

        elif (f==4):
            self.label_11.setText(_translate("Dialog",
                                             "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\"> Don't worry if the image is delayed, good work may take an extra time. ^_& </span></p></body></html>"))

    #########################################################
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tasbeh_Editor"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#f2edd7;\">Tasbeh Editor</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">contrast</p></body></html>"))
        self.label_6.setText(
            _translate("Dialog", "<html><head/><body><p align=\"center\">brightness</p></body></html>"))
        self.autobright.setWhatsThis(
            _translate("Dialog", "<html><head/><body><p>automatic</p><p>brightness</p></body></html>"))
        self.autobright.setText(_translate("Dialog", "   automatic\n"
                                                     "   brightness"))
        self.thresholding.setWhatsThis(_translate("Dialog",
                                                  "<html><head/><body><p><span style=\" font-size:12pt; vertical-align:super;\">black&amp;white</span></p></body></html>"))
        self.thresholding.setText(_translate("Dialog", " black\n"
                                                       " white"))
        self.autocontrast.setText(_translate("Dialog", "   automatic\n"
                                                       "   contrast"))
        self.buttonmagic.setText(_translate("Dialog", "Additional effects"))
        self.thresholding_2.setWhatsThis(_translate("Dialog",
                                                    "<html><head/><body><p><span style=\" font-size:12pt; vertical-align:super;\">black&amp;white</span></p></body></html>"))
        self.thresholding_2.setText(_translate("Dialog", " bit planes"))
        self.label_8.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:12pt; color:#f2edd7;\">&quot;Some people look for a beautiful place, others make the place beautiful&quot;.</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">► Notes:</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
