# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/synth_widget.ui'
#
# Created: Wed Jun 15 14:15:00 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(715, 505)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.frame_controls = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy)
        self.frame_controls.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_controls.setObjectName(_fromUtf8("frame_controls"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_controls)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtGui.QFrame(self.frame_controls)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.dial_volume = QtGui.QDial(self.frame)
        self.dial_volume.setMaximum(100)
        self.dial_volume.setProperty(_fromUtf8("value"), 99)
        self.dial_volume.setNotchTarget(10.0)
        self.dial_volume.setNotchesVisible(True)
        self.dial_volume.setObjectName(_fromUtf8("dial_volume"))
        self.gridLayout_2.addWidget(self.dial_volume, 1, 2, 1, 1)
        self.spin_volume = QtGui.QDoubleSpinBox(self.frame)
        self.spin_volume.setMaximum(100.0)
        self.spin_volume.setSingleStep(100.0)
        self.spin_volume.setProperty(_fromUtf8("value"), 100.0)
        self.spin_volume.setObjectName(_fromUtf8("spin_volume"))
        self.gridLayout_2.addWidget(self.spin_volume, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 3, 1, 1)
        self.dial_pan = QtGui.QDial(self.frame)
        self.dial_pan.setMinimum(-20)
        self.dial_pan.setMaximum(20)
        self.dial_pan.setNotchTarget(10.0)
        self.dial_pan.setNotchesVisible(True)
        self.dial_pan.setObjectName(_fromUtf8("dial_pan"))
        self.gridLayout_2.addWidget(self.dial_pan, 1, 3, 1, 1)
        self.spin_pan = QtGui.QDoubleSpinBox(self.frame)
        self.spin_pan.setMinimum(-1000.0)
        self.spin_pan.setMaximum(1000.0)
        self.spin_pan.setProperty(_fromUtf8("value"), 0.0)
        self.spin_pan.setObjectName(_fromUtf8("spin_pan"))
        self.gridLayout_2.addWidget(self.spin_pan, 2, 3, 1, 1)
        self.dial_decay = QtGui.QDial(self.frame)
        self.dial_decay.setMaximum(500)
        self.dial_decay.setProperty(_fromUtf8("value"), 5)
        self.dial_decay.setNotchTarget(50.0)
        self.dial_decay.setNotchesVisible(True)
        self.dial_decay.setObjectName(_fromUtf8("dial_decay"))
        self.gridLayout_2.addWidget(self.dial_decay, 1, 1, 1, 1)
        self.dial_attack = QtGui.QDial(self.frame)
        self.dial_attack.setMaximum(500)
        self.dial_attack.setNotchTarget(50.0)
        self.dial_attack.setNotchesVisible(True)
        self.dial_attack.setObjectName(_fromUtf8("dial_attack"))
        self.gridLayout_2.addWidget(self.dial_attack, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.spin_attack = QtGui.QSpinBox(self.frame)
        self.spin_attack.setMaximum(100000)
        self.spin_attack.setObjectName(_fromUtf8("spin_attack"))
        self.gridLayout_2.addWidget(self.spin_attack, 2, 0, 1, 1)
        self.spin_decay = QtGui.QSpinBox(self.frame)
        self.spin_decay.setMaximum(100000)
        self.spin_decay.setProperty(_fromUtf8("value"), 5)
        self.spin_decay.setObjectName(_fromUtf8("spin_decay"))
        self.gridLayout_2.addWidget(self.spin_decay, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 3)
        self.label_4 = QtGui.QLabel(self.frame_controls)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)
        self.edit_duration = QtGui.QLineEdit(self.frame_controls)
        self.edit_duration.setObjectName(_fromUtf8("edit_duration"))
        self.gridLayout_3.addWidget(self.edit_duration, 6, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.frame_controls)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)
        self.spin_length = QtGui.QSpinBox(self.frame_controls)
        self.spin_length.setMaximum(100000000)
        self.spin_length.setProperty(_fromUtf8("value"), 100)
        self.spin_length.setObjectName(_fromUtf8("spin_length"))
        self.gridLayout_3.addWidget(self.spin_length, 5, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.frame_controls)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_freq = QtGui.QLineEdit(self.frame_controls)
        self.edit_freq.setObjectName(_fromUtf8("edit_freq"))
        self.gridLayout_3.addWidget(self.edit_freq, 1, 1, 1, 1)
        self.widget = QtGui.QWidget(self.frame_controls)
        self.widget.setStyleSheet(_fromUtf8("background-color: #729fcf;\n"
"color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/synth.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_9 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 3)
        self.frame_3 = QtGui.QFrame(self.frame_controls)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_4.setMargin(4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_4.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 0, 3, 1, 1)
        self.button_sine = QtGui.QPushButton(self.frame_3)
        self.button_sine.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sine.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sine.setIcon(icon)
        self.button_sine.setIconSize(QtCore.QSize(64, 64))
        self.button_sine.setCheckable(True)
        self.button_sine.setChecked(True)
        self.button_sine.setFlat(True)
        self.button_sine.setObjectName(_fromUtf8("button_sine"))
        self.gridLayout_4.addWidget(self.button_sine, 1, 0, 1, 1)
        self.button_saw = QtGui.QPushButton(self.frame_3)
        self.button_saw.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/saw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_saw.setIcon(icon1)
        self.button_saw.setIconSize(QtCore.QSize(64, 64))
        self.button_saw.setCheckable(True)
        self.button_saw.setFlat(True)
        self.button_saw.setObjectName(_fromUtf8("button_saw"))
        self.gridLayout_4.addWidget(self.button_saw, 1, 1, 1, 1)
        self.button_square = QtGui.QPushButton(self.frame_3)
        self.button_square.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/square.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_square.setIcon(icon2)
        self.button_square.setIconSize(QtCore.QSize(64, 64))
        self.button_square.setCheckable(True)
        self.button_square.setFlat(True)
        self.button_square.setObjectName(_fromUtf8("button_square"))
        self.gridLayout_4.addWidget(self.button_square, 1, 2, 1, 1)
        self.button_white_noise = QtGui.QPushButton(self.frame_3)
        self.button_white_noise.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/white_noise.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_white_noise.setIcon(icon3)
        self.button_white_noise.setIconSize(QtCore.QSize(64, 64))
        self.button_white_noise.setCheckable(True)
        self.button_white_noise.setFlat(True)
        self.button_white_noise.setObjectName(_fromUtf8("button_white_noise"))
        self.gridLayout_4.addWidget(self.button_white_noise, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.frame_controls, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.frame_notification = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_notification.sizePolicy().hasHeightForWidth())
        self.frame_notification.setSizePolicy(sizePolicy)
        self.frame_notification.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_notification.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_notification.setObjectName(_fromUtf8("frame_notification"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_notification)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget_2 = QtGui.QWidget(self.frame_notification)
        self.widget_2.setStyleSheet(_fromUtf8("background-color: #729fcf;\n"
"color: rgb(255, 255, 255);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(5)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/about_large.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_15 = QtGui.QLabel(self.widget_2)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_2.addWidget(self.label_15)
        self.button_script = QtGui.QPushButton(self.widget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_script.setIcon(icon4)
        self.button_script.setObjectName(_fromUtf8("button_script"))
        self.horizontalLayout_2.addWidget(self.button_script)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.frame_notification, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_volume.setToolTip(QtGui.QApplication.translate("Form", "Set the volume of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_volume.setToolTip(QtGui.QApplication.translate("Form", "Set the volume of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_volume.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pan</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_pan.setToolTip(QtGui.QApplication.translate("Form", "Set the panning (left-right) of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_pan.setToolTip(QtGui.QApplication.translate("Form", "Set the panning (left-right) of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_decay.setToolTip(QtGui.QApplication.translate("Form", "Set the decay (\"fade out\") of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_attack.setToolTip(QtGui.QApplication.translate("Form", "Set the attack (\"fade in\") of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Decay", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_attack.setToolTip(QtGui.QApplication.translate("Form", "Set the attack (\"fade in\") of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_attack.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_decay.setToolTip(QtGui.QApplication.translate("Form", "Set the decay (\"fade out\") of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_decay.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_duration.setToolTip(QtGui.QApplication.translate("Form", "Set the duration of the synth item. Expecting a duration in ms, \'sound\' (to wait until the sound is finished playing), \'keypress\', \'mouseclick\', or a variable (e.g., \'[synth_dur]\').", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_duration.setText(QtGui.QApplication.translate("Form", "sound", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_length.setToolTip(QtGui.QApplication.translate("Form", "Set the length of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_length.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Frequency</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">In hertz (Hz) or by note, like \'A1\'</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_freq.setToolTip(QtGui.QApplication.translate("Form", "The frequence of the sound. Expecting a numeric value (frequency in Hertz) a note (like \'C#2\' and \'A1\') or a variable (like \'[freq]\')", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_freq.setText(QtGui.QApplication.translate("Form", "A1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Synth controls", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Sine wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Sawtooth wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Square wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "White noise", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sine.setToolTip(QtGui.QApplication.translate("Form", "Generate a sine wav", None, QtGui.QApplication.UnicodeUTF8))
        self.button_saw.setToolTip(QtGui.QApplication.translate("Form", "Generate a sawtooth wave", None, QtGui.QApplication.UnicodeUTF8))
        self.button_square.setToolTip(QtGui.QApplication.translate("Form", "Generate a square wave", None, QtGui.QApplication.UnicodeUTF8))
        self.button_white_noise.setToolTip(QtGui.QApplication.translate("Form", "Generate white noise", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "One of the controls is defined using variables and therefore the controls are disabled. Use the script editor to edit the synth.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_script.setToolTip(QtGui.QApplication.translate("Form", "Edit the script to see the definition", None, QtGui.QApplication.UnicodeUTF8))
        self.button_script.setText(QtGui.QApplication.translate("Form", "Edit script", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
