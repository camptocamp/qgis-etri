# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Wed Aug  4 20:22:31 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.group_params = QtGui.QGroupBox(self.centralwidget)
        self.group_params.setObjectName("group_params")
        self.gridLayout = QtGui.QGridLayout(self.group_params)
        self.gridLayout.setObjectName("gridLayout")
        self.Tab_params = QtGui.QTabWidget(self.group_params)
        self.Tab_params.setObjectName("Tab_params")
        self.tab_criterions = QtGui.QWidget()
        self.tab_criterions.setObjectName("tab_criterions")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_criterions)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_crit = QtGui.QTableWidget(self.tab_criterions)
        self.table_crit.setDragEnabled(False)
        self.table_crit.setAlternatingRowColors(False)
        self.table_crit.setShowGrid(False)
        self.table_crit.setCornerButtonEnabled(False)
        self.table_crit.setRowCount(0)
        self.table_crit.setObjectName("table_crit")
        self.table_crit.setColumnCount(3)
        self.table_crit.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_crit.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_crit.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_crit.setHorizontalHeaderItem(2, item)
        self.table_crit.horizontalHeader().setVisible(True)
        self.table_crit.horizontalHeader().setDefaultSectionSize(100)
        self.table_crit.horizontalHeader().setHighlightSections(False)
        self.table_crit.verticalHeader().setVisible(False)
        self.table_crit.verticalHeader().setHighlightSections(False)
        self.table_crit.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.table_crit, 0, 0, 1, 1)
        self.Tab_params.addTab(self.tab_criterions, "")
        self.tab_profiles = QtGui.QWidget()
        self.tab_profiles.setObjectName("tab_profiles")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_profiles)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.table_prof = QtGui.QTableWidget(self.tab_profiles)
        self.table_prof.setObjectName("table_prof")
        self.table_prof.setColumnCount(0)
        self.table_prof.setRowCount(0)
        self.gridLayout_5.addWidget(self.table_prof, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.tab_profiles)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.indiff_tab = QtGui.QWidget()
        self.indiff_tab.setObjectName("indiff_tab")
        self.gridLayout_3 = QtGui.QGridLayout(self.indiff_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.table_indiff = QtGui.QTableWidget(self.indiff_tab)
        self.table_indiff.setObjectName("table_indiff")
        self.table_indiff.setColumnCount(0)
        self.table_indiff.setRowCount(0)
        self.gridLayout_3.addWidget(self.table_indiff, 0, 1, 1, 1)
        self.tabWidget.addTab(self.indiff_tab, "")
        self.pref_tab = QtGui.QWidget()
        self.pref_tab.setObjectName("pref_tab")
        self.gridLayout_4 = QtGui.QGridLayout(self.pref_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.table_pref = QtGui.QTableWidget(self.pref_tab)
        self.table_pref.setObjectName("table_pref")
        self.table_pref.setColumnCount(0)
        self.table_pref.setRowCount(0)
        self.gridLayout_4.addWidget(self.table_pref, 0, 0, 1, 1)
        self.tabWidget.addTab(self.pref_tab, "")
        self.veto_tab = QtGui.QWidget()
        self.veto_tab.setObjectName("veto_tab")
        self.gridLayout_7 = QtGui.QGridLayout(self.veto_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.table_veto = QtGui.QTableWidget(self.veto_tab)
        self.table_veto.setObjectName("table_veto")
        self.table_veto.setColumnCount(0)
        self.table_veto.setRowCount(0)
        self.gridLayout_7.addWidget(self.table_veto, 0, 0, 1, 1)
        self.tabWidget.addTab(self.veto_tab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.Tab_params.addTab(self.tab_profiles, "")
        self.gridLayout.addWidget(self.Tab_params, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.group_params, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.group_options = QtGui.QGroupBox(self.centralwidget)
        self.group_options.setMaximumSize(QtCore.QSize(388, 16777215))
        self.group_options.setObjectName("group_options")
        self.formLayout = QtGui.QFormLayout(self.group_options)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.Badd_profile = QtGui.QCommandLinkButton(self.group_options)
        self.Badd_profile.setObjectName("Badd_profile")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Badd_profile)
        self.Bdel_profile = QtGui.QCommandLinkButton(self.group_options)
        self.Bdel_profile.setObjectName("Bdel_profile")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.Bdel_profile)
        self.verticalLayout_2.addWidget(self.group_options)
        self.group_electre = QtGui.QGroupBox(self.centralwidget)
        self.group_electre.setObjectName("group_electre")
        self.gridLayout_8 = QtGui.QGridLayout(self.group_electre)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Bgenerate = QtGui.QCommandLinkButton(self.group_electre)
        self.Bgenerate.setObjectName("Bgenerate")
        self.gridLayout_8.addWidget(self.Bgenerate, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.group_electre)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab_params.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.group_params.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.table_crit.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.table_crit.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_criterions), QtGui.QApplication.translate("MainWindow", "Criterions", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indiff_tab), QtGui.QApplication.translate("MainWindow", "Indifference", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pref_tab), QtGui.QApplication.translate("MainWindow", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.veto_tab), QtGui.QApplication.translate("MainWindow", "Veto", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_profiles), QtGui.QApplication.translate("MainWindow", "Profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.group_options.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.Badd_profile.setText(QtGui.QApplication.translate("MainWindow", "Add Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.Bdel_profile.setText(QtGui.QApplication.translate("MainWindow", "Del Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.group_electre.setTitle(QtGui.QApplication.translate("MainWindow", "Electre Tri", None, QtGui.QApplication.UnicodeUTF8))
        self.Bgenerate.setText(QtGui.QApplication.translate("MainWindow", "Generate Decision Map", None, QtGui.QApplication.UnicodeUTF8))

