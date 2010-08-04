#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

from Ui_mainwindow import Ui_MainWindow
from qgis_utils import *
from utils import *

COL_CRITERIONS = 2

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.table_crit.setColumnWidth(0, 235)
        self.table_crit.setColumnWidth(1, 60)
        self.table_crit.setColumnWidth(2, 50)

        self.load_data()

    def load_data(self):
        self.crit_layer = layer_load("/home/oso/tfe/qgis_data/france.shp", "criterions")
        criterions = layer_get_criterions(self.crit_layer)
        self.add_criterions(criterions)

        minmax = layer_get_minmax(self.crit_layer)
        self.crit_min = minmax[0]
        self.crit_max = minmax[1]

        self.add_profile(0)

    def get_row(self, table, index):
        ncols = table.columnCount()
        values = []
        for j in range(ncols):
            item = table.item(index,j)
            try:
                values.append(round(float(item.text()), 2))
            except:
                values.append(round(float(0, 2)))
        return values

    def set_row(self, table, index, vector):
        for j in range(len(vector)):
            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            item.setText(str(round(vector[j],2)))
            table.setItem(index, j, item)

    def add_profile(self, index):
        nprof = self.table_prof.rowCount()
        if index > nprof or index == -1:
            index = nprof

        # Profiles table
        self.table_prof.insertRow(index)

        if nprof == 0:
            abs = v_add(self.crit_max, self.crit_max)
            val = [x/2 for x in abs]
        else:
            val = self.get_row(self.table_prof, index-1)

        self.set_row(self.table_prof, index, val)

        # Thresholds table
        self.table_pref.insertRow(nprof)
        self.table_indiff.insertRow(nprof)
        self.table_veto.insertRow(nprof)
        for table in [self.table_pref, self.table_indiff, self.table_veto]:
            try:
                thresholds = self.get_row(table, index-1)
            except:
                thresholds = [0] * table.columnCount()
            self.set_row(table, index, thresholds)

    def add_criteria(self, crit):
        # Add row in criteria table
        nrow = self.table_crit.rowCount()
        self.table_crit.insertRow(nrow)

        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsTristate)
        self.table_crit.setItem(nrow, 0, item)

        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsTristate)
        self.table_crit.setItem(nrow, 1, item)

        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        item.setText("10.0")
        self.table_crit.setItem(nrow, 2, item)
        
        checkBox = QtGui.QCheckBox(self)
        checkBox.setCheckState(QtCore.Qt.Checked)
        checkBox.setText(QtGui.QApplication.translate("MainWindow", crit, None, QtGui.QApplication.UnicodeUTF8))
        self.table_crit.setCellWidget(nrow, 0, checkBox)

        signalMapper = QtCore.QSignalMapper(self)
        QtCore.QObject.connect(checkBox, QtCore.SIGNAL("stateChanged(int)"), signalMapper, QtCore.SLOT("map()"))
        signalMapper.setMapping(checkBox, nrow)
        QtCore.QObject.connect(signalMapper, QtCore.SIGNAL("mapped(int)"), self.on_criteria_stateChanged)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("Min")
        comboBox.addItem("Max")
        self.table_crit.setCellWidget(nrow, 1, comboBox)

        # Add column in profiles and thresholds table
        for table in [ self.table_prof, self.table_pref, self.table_indiff, self.table_veto ]:
            table.insertColumn(nrow)
            item = QtGui.QTableWidgetItem()
            table.setHorizontalHeaderItem(nrow, item)
            table.horizontalHeaderItem(nrow).setText(crit)

    def add_criterions(self, criterions):
        for crit in criterions:
            self.add_criteria(crit)

    def get_criterions_weights(self):
        nrows = self.table_crit.rowCount()
        W = []
        for i in range(nrows):
            w = self.table_crit.item(i,2) 
            W.append(round(float(w.text()), 2))

        return W

    def get_profiles(self): 
        print "coucou"
    
    def check_is_float(self, table, row, column):
        item = table.item(row, column)
        val = item.text()
        try:
            round(float(val), 2)
        except:
            item.setBackgroundColor(QtCore.Qt.red)
            return

        item.setBackgroundColor(QtCore.Qt.white)

    def check_profile_crit(self, row, column):
        item = self.table_prof.item(row, column)
        val = item.text()
        try:
            val = round(float(val), 2)
        except:
            item.setBackgroundColor(QtCore.Qt.red)
            return

        if val < self.crit_min[column] or val > self.crit_max[column]:
            item.setBackgroundColor(QtCore.Qt.red)
            return

        try:
            profile = self.get_row(self.table_prof, row-1)
            if profile[column] > val and profile[column] > self.crit_min[column] and profile[column] < self.crit_max[column]:
                item.setBackgroundColor(QtCore.Qt.red)
                return
            else:
                item2 = self.table_prof.item(row-1, column)
                item2.setBackgroundColor(QtCore.Qt.white)
        except:
            pass

        try:
            profile = self.get_row(self.table_prof, row+1)
            if profile[column] < val and profile[column] > self.crit_min[column] and profile[column] < self.crit_max[column]:
                item.setBackgroundColor(QtCore.Qt.red)
                return
            else:
                item2 = self.table_prof.item(row+1, column)
                item2.setBackgroundColor(QtCore.Qt.white)
        except:
            pass

        item.setBackgroundColor(QtCore.Qt.white)

    def goto_next_cell(self, table, c_row, c_col):
        nrows = table.rowCount()
        if c_row == nrows-1:
            table.setCurrentCell(0, c_col+1)
        else:
            table.setCurrentCell(c_row+1,c_col)

    def on_table_crit_cellChanged(self, row, column):
        if column == COL_CRITERIONS:
            self.check_is_float(self.table_crit, row, column)

        self.table_crit.setCurrentCell(row+1,column)

    def on_criteria_stateChanged(self, row):
        print "Row", row
        item = self.table_crit.cellWidget(row, 0)
        print "Checked:", item.isChecked()

    def on_Badd_profile_pressed(self):
        self.add_profile(-1)

    def on_table_prof_cellChanged(self, row, column):
        self.check_profile_crit(row, column)
        self.goto_next_cell(self.table_prof, row, column)

    def on_table_indiff_cellChanged(self, row, column):
        self.check_is_float(self.table_indiff, row, column)
        self.goto_next_cell(self.table_indiff, row, column)

    def on_table_pref_cellChanged(self, row, column):
        self.check_is_float(self.table_pref, row, column)
        self.goto_next_cell(self.table_pref, row, column)

    def on_table_veto_cellChanged(self, row, column):
        self.check_is_float(self.table_veto, row, column)
        self.goto_next_cell(self.table_veto, row, column)
