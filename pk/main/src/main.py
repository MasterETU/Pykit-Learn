# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:13:25 2015

@author: bhavesh
"""

import sys
from PyQt4 import QtCore, QtGui
import pandas as pd
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import seaborn as sns

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

class Ui_TabWidget(QtGui.QTabWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, main_tab):
        main_tab.setObjectName(_fromUtf8("main_tab"))
        main_tab.resize(987, 737)
        self.upload_tab = QtGui.QWidget()
        self.upload_tab.setObjectName(_fromUtf8("upload_tab"))
        self.horizontalWidget = QtGui.QWidget(self.upload_tab)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 501, 51))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.openfile_btn = QtGui.QPushButton(self.horizontalWidget)
        self.openfile_btn.setObjectName(_fromUtf8("openfile_btn"))
        self.horizontalLayout.addWidget(self.openfile_btn)
        self.openurl_btn = QtGui.QPushButton(self.horizontalWidget)
        self.openurl_btn.setObjectName(_fromUtf8("openurl_btn"))
        self.horizontalLayout.addWidget(self.openurl_btn)
        self.generate_btn = QtGui.QPushButton(self.horizontalWidget)
        self.generate_btn.setObjectName(_fromUtf8("generate_btn"))
        self.horizontalLayout.addWidget(self.generate_btn)
        self.verticalLayoutWidget = QtGui.QWidget(self.upload_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 391, 621))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.datainfo_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.datainfo_label.setObjectName(_fromUtf8("datainfo_label"))
        self.verticalLayout.addWidget(self.datainfo_label)
        self.datainfotext = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.datainfotext.setObjectName(_fromUtf8("datainfotext"))
        self.verticalLayout.addWidget(self.datainfotext)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.upload_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 50, 541, 621))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dataplotter_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.dataplotter_label.setObjectName(_fromUtf8("dataplotter_label"))
        self.verticalLayout_2.addWidget(self.dataplotter_label)
        self.dataplottergraphics = QtGui.QGraphicsView(self.verticalLayoutWidget_2)
        self.dataplottergraphics.setObjectName(_fromUtf8("dataplottergraphics"))
        self.verticalLayout_2.addWidget(self.dataplottergraphics)
        self.progressBar = QtGui.QProgressBar(self.upload_tab)
        self.progressBar.setGeometry(QtCore.QRect(20, 683, 941, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        main_tab.addTab(self.upload_tab, _fromUtf8(""))
        self.preprocess_tab = QtGui.QWidget()
        self.preprocess_tab.setEnabled(True)
        self.preprocess_tab.setAutoFillBackground(False)
        self.preprocess_tab.setObjectName(_fromUtf8("preprocess_tab"))
        self.horizontalWidget_2 = QtGui.QWidget(self.preprocess_tab)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.preprocess_tab_2 = QtGui.QTabWidget(self.horizontalWidget_2)
        self.preprocess_tab_2.setObjectName(_fromUtf8("preprocess_tab_2"))
        self.normalize_tab = QtGui.QWidget()
        self.normalize_tab.setObjectName(_fromUtf8("normalize_tab"))
        self.preprocess_tab_2.addTab(self.normalize_tab, _fromUtf8(""))
        self.standardize_tab = QtGui.QWidget()
        self.standardize_tab.setObjectName(_fromUtf8("standardize_tab"))
        self.preprocess_tab_2.addTab(self.standardize_tab, _fromUtf8(""))
        self.binarize_tab = QtGui.QWidget()
        self.binarize_tab.setObjectName(_fromUtf8("binarize_tab"))
        self.preprocess_tab_2.addTab(self.binarize_tab, _fromUtf8(""))
        self.impute_tab = QtGui.QWidget()
        self.impute_tab.setObjectName(_fromUtf8("impute_tab"))
        self.preprocess_tab_2.addTab(self.impute_tab, _fromUtf8(""))
        self.noise_tab = QtGui.QWidget()
        self.noise_tab.setObjectName(_fromUtf8("noise_tab"))
        self.preprocess_tab_2.addTab(self.noise_tab, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.preprocess_tab_2)
        self.attr_label = QtGui.QLabel(self.preprocess_tab)
        self.attr_label.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.attr_label.setObjectName(_fromUtf8("attr_label"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.preprocess_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 421, 251))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.attr_checkbox1 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.attr_checkbox1.setObjectName(_fromUtf8("attr_checkbox1"))
        self.verticalLayout_3.addWidget(self.attr_checkbox1)
        self.attr_checkbox2 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.attr_checkbox2.setObjectName(_fromUtf8("attr_checkbox2"))
        self.verticalLayout_3.addWidget(self.attr_checkbox2)
        self.attr_checkbox3 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.attr_checkbox3.setObjectName(_fromUtf8("attr_checkbox3"))
        self.verticalLayout_3.addWidget(self.attr_checkbox3)
        self.attr_checkbox4 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.attr_checkbox4.setObjectName(_fromUtf8("attr_checkbox4"))
        self.verticalLayout_3.addWidget(self.attr_checkbox4)
        self.attr_checkbox5 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.attr_checkbox5.setObjectName(_fromUtf8("attr_checkbox5"))
        self.verticalLayout_3.addWidget(self.attr_checkbox5)
        self.remove_attr_btn = QtGui.QPushButton(self.preprocess_tab)
        self.remove_attr_btn.setGeometry(QtCore.QRect(10, 330, 419, 26))
        self.remove_attr_btn.setObjectName(_fromUtf8("remove_attr_btn"))
        main_tab.addTab(self.preprocess_tab, _fromUtf8(""))
        self.regression_tab = QtGui.QWidget()
        self.regression_tab.setObjectName(_fromUtf8("regression_tab"))
        self.horizontalWidget_4 = QtGui.QWidget(self.regression_tab)
        self.horizontalWidget_4.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalWidget_4.setObjectName(_fromUtf8("horizontalWidget_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.regression_tab_2 = QtGui.QTabWidget(self.horizontalWidget_4)
        self.regression_tab_2.setObjectName(_fromUtf8("regression_tab_2"))
        self.linearreg_tab = QtGui.QWidget()
        self.linearreg_tab.setObjectName(_fromUtf8("linearreg_tab"))
        self.regression_tab_2.addTab(self.linearreg_tab, _fromUtf8(""))
        self.polyreg_tab = QtGui.QWidget()
        self.polyreg_tab.setObjectName(_fromUtf8("polyreg_tab"))
        self.regression_tab_2.addTab(self.polyreg_tab, _fromUtf8(""))
        self.leastsqreg_tab = QtGui.QWidget()
        self.leastsqreg_tab.setObjectName(_fromUtf8("leastsqreg_tab"))
        self.regression_tab_2.addTab(self.leastsqreg_tab, _fromUtf8(""))
        self.logisticreg_tab = QtGui.QWidget()
        self.logisticreg_tab.setObjectName(_fromUtf8("logisticreg_tab"))
        self.regression_tab_2.addTab(self.logisticreg_tab, _fromUtf8(""))
        self.gdreg_tab = QtGui.QWidget()
        self.gdreg_tab.setObjectName(_fromUtf8("gdreg_tab"))
        self.regression_tab_2.addTab(self.gdreg_tab, _fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.regression_tab_2)
        main_tab.addTab(self.regression_tab, _fromUtf8(""))
        self.classify_tab = QtGui.QWidget()
        self.classify_tab.setObjectName(_fromUtf8("classify_tab"))
        self.horizontalWidget_3 = QtGui.QWidget(self.classify_tab)
        self.horizontalWidget_3.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalWidget_3.setObjectName(_fromUtf8("horizontalWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.classifymethods_tab = QtGui.QTabWidget(self.horizontalWidget_3)
        self.classifymethods_tab.setElideMode(QtCore.Qt.ElideNone)
        self.classifymethods_tab.setObjectName(_fromUtf8("classifymethods_tab"))
        self.dt_tab = QtGui.QWidget()
        self.dt_tab.setObjectName(_fromUtf8("dt_tab"))
        self.classifymethods_tab.addTab(self.dt_tab, _fromUtf8(""))
        self.ensemble_tab = QtGui.QWidget()
        self.ensemble_tab.setObjectName(_fromUtf8("ensemble_tab"))
        self.classifymethods_tab.addTab(self.ensemble_tab, _fromUtf8(""))
        self.nn_tab = QtGui.QWidget()
        self.nn_tab.setObjectName(_fromUtf8("nn_tab"))
        self.classifymethods_tab.addTab(self.nn_tab, _fromUtf8(""))
        self.svm_tab = QtGui.QWidget()
        self.svm_tab.setObjectName(_fromUtf8("svm_tab"))
        self.classifymethods_tab.addTab(self.svm_tab, _fromUtf8(""))
        self.bn_tab = QtGui.QWidget()
        self.bn_tab.setObjectName(_fromUtf8("bn_tab"))
        self.classifymethods_tab.addTab(self.bn_tab, _fromUtf8(""))
        self.knn_tab = QtGui.QWidget()
        self.knn_tab.setObjectName(_fromUtf8("knn_tab"))
        self.classifymethods_tab.addTab(self.knn_tab, _fromUtf8(""))
        self.otherclassify_tab = QtGui.QWidget()
        self.otherclassify_tab.setObjectName(_fromUtf8("otherclassify_tab"))
        self.classifymethods_tab.addTab(self.otherclassify_tab, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.classifymethods_tab)
        main_tab.addTab(self.classify_tab, _fromUtf8(""))
        self.cluster_tab = QtGui.QWidget()
        self.cluster_tab.setObjectName(_fromUtf8("cluster_tab"))
        self.horizontalWidget_5 = QtGui.QWidget(self.cluster_tab)
        self.horizontalWidget_5.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalWidget_5.setObjectName(_fromUtf8("horizontalWidget_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.clustermethod_tab = QtGui.QTabWidget(self.horizontalWidget_5)
        self.clustermethod_tab.setObjectName(_fromUtf8("clustermethod_tab"))
        self.kmeans_tab = QtGui.QWidget()
        self.kmeans_tab.setObjectName(_fromUtf8("kmeans_tab"))
        self.clustermethod_tab.addTab(self.kmeans_tab, _fromUtf8(""))
        self.em_tab = QtGui.QWidget()
        self.em_tab.setObjectName(_fromUtf8("em_tab"))
        self.clustermethod_tab.addTab(self.em_tab, _fromUtf8(""))
        self.propcluster_tab = QtGui.QWidget()
        self.propcluster_tab.setObjectName(_fromUtf8("propcluster_tab"))
        self.clustermethod_tab.addTab(self.propcluster_tab, _fromUtf8(""))
        self.spectralcluster_tab = QtGui.QWidget()
        self.spectralcluster_tab.setObjectName(_fromUtf8("spectralcluster_tab"))
        self.clustermethod_tab.addTab(self.spectralcluster_tab, _fromUtf8(""))
        self.aggcluster_tab = QtGui.QWidget()
        self.aggcluster_tab.setObjectName(_fromUtf8("aggcluster_tab"))
        self.clustermethod_tab.addTab(self.aggcluster_tab, _fromUtf8(""))
        self.dbscan_tab = QtGui.QWidget()
        self.dbscan_tab.setObjectName(_fromUtf8("dbscan_tab"))
        self.clustermethod_tab.addTab(self.dbscan_tab, _fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.clustermethod_tab)
        main_tab.addTab(self.cluster_tab, _fromUtf8(""))
        self.reduce_tab = QtGui.QWidget()
        self.reduce_tab.setObjectName(_fromUtf8("reduce_tab"))
        self.horizontalWidget_6 = QtGui.QWidget(self.reduce_tab)
        self.horizontalWidget_6.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalWidget_6.setObjectName(_fromUtf8("horizontalWidget_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.reducemethods_tab = QtGui.QTabWidget(self.horizontalWidget_6)
        self.reducemethods_tab.setObjectName(_fromUtf8("reducemethods_tab"))
        self.pca_tab = QtGui.QWidget()
        self.pca_tab.setObjectName(_fromUtf8("pca_tab"))
        self.reducemethods_tab.addTab(self.pca_tab, _fromUtf8(""))
        self.ica_tab = QtGui.QWidget()
        self.ica_tab.setObjectName(_fromUtf8("ica_tab"))
        self.reducemethods_tab.addTab(self.ica_tab, _fromUtf8(""))
        self.rpa_tab = QtGui.QWidget()
        self.rpa_tab.setObjectName(_fromUtf8("rpa_tab"))
        self.reducemethods_tab.addTab(self.rpa_tab, _fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.reducemethods_tab)
        main_tab.addTab(self.reduce_tab, _fromUtf8(""))
        self.visualize_tab = QtGui.QWidget()
        self.visualize_tab.setObjectName(_fromUtf8("visualize_tab"))
        main_tab.addTab(self.visualize_tab, _fromUtf8(""))
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName(_fromUtf8("other_tab"))
        main_tab.addTab(self.other_tab, _fromUtf8(""))

        self.retranslateUi(main_tab)
        main_tab.setCurrentIndex(0)
        self.preprocess_tab_2.setCurrentIndex(0)
        self.regression_tab_2.setCurrentIndex(0)
        self.classifymethods_tab.setCurrentIndex(0)
        self.clustermethod_tab.setCurrentIndex(0)
        self.reducemethods_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_tab)

    def retranslateUi(self, main_tab):
        main_tab.setWindowTitle(_translate("main_tab", "Scikit GUI", None))
        self.openfile_btn.setText(_translate("main_tab", "Open File", None))
        self.openurl_btn.setText(_translate("main_tab", "Open URL", None))
        self.generate_btn.setText(_translate("main_tab", "Generate", None))
        self.datainfo_label.setText(_translate("main_tab", "Dataset Information", None))
        self.dataplotter_label.setText(_translate("main_tab", "Dataset Plotter", None))
        main_tab.setTabText(main_tab.indexOf(self.upload_tab), _translate("main_tab", "Upload", None))
        self.preprocess_tab_2.setTabText(self.preprocess_tab_2.indexOf(self.normalize_tab), _translate("main_tab", "Normalize", None))
        self.preprocess_tab_2.setTabText(self.preprocess_tab_2.indexOf(self.standardize_tab), _translate("main_tab", "Standardize", None))
        self.preprocess_tab_2.setTabText(self.preprocess_tab_2.indexOf(self.binarize_tab), _translate("main_tab", "Binarize", None))
        self.preprocess_tab_2.setTabText(self.preprocess_tab_2.indexOf(self.impute_tab), _translate("main_tab", "Impute", None))
        self.preprocess_tab_2.setTabText(self.preprocess_tab_2.indexOf(self.noise_tab), _translate("main_tab", "Add Noise", None))
        self.attr_label.setText(_translate("main_tab", "Attributes", None))
        self.attr_checkbox1.setText(_translate("main_tab", "Attribute 1", None))
        self.attr_checkbox2.setText(_translate("main_tab", "Attribute 2", None))
        self.attr_checkbox3.setText(_translate("main_tab", "Attribute 3", None))
        self.attr_checkbox4.setText(_translate("main_tab", "Attribute 4", None))
        self.attr_checkbox5.setText(_translate("main_tab", "Attribute 5", None))
        self.remove_attr_btn.setText(_translate("main_tab", "Remove", None))
        main_tab.setTabText(main_tab.indexOf(self.preprocess_tab), _translate("main_tab", "Preprocess", None))
        self.regression_tab_2.setTabText(self.regression_tab_2.indexOf(self.linearreg_tab), _translate("main_tab", "Linear", None))
        self.regression_tab_2.setTabText(self.regression_tab_2.indexOf(self.polyreg_tab), _translate("main_tab", "Polynomial", None))
        self.regression_tab_2.setTabText(self.regression_tab_2.indexOf(self.leastsqreg_tab), _translate("main_tab", "Least Square", None))
        self.regression_tab_2.setTabText(self.regression_tab_2.indexOf(self.logisticreg_tab), _translate("main_tab", "Logistic", None))
        self.regression_tab_2.setTabText(self.regression_tab_2.indexOf(self.gdreg_tab), _translate("main_tab", "Gradient Descent", None))
        main_tab.setTabText(main_tab.indexOf(self.regression_tab), _translate("main_tab", "Regression", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.dt_tab), _translate("main_tab", "Decision Tree", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.ensemble_tab), _translate("main_tab", "Ensemble", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.nn_tab), _translate("main_tab", "Neural Networks", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.svm_tab), _translate("main_tab", "SVM", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.bn_tab), _translate("main_tab", "Bayes Nets", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.knn_tab), _translate("main_tab", "kNN", None))
        self.classifymethods_tab.setTabText(self.classifymethods_tab.indexOf(self.otherclassify_tab), _translate("main_tab", "Others", None))
        main_tab.setTabText(main_tab.indexOf(self.classify_tab), _translate("main_tab", "Classify", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.kmeans_tab), _translate("main_tab", "kMeans", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.em_tab), _translate("main_tab", "EM", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.propcluster_tab), _translate("main_tab", "Affinity Propogation", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.spectralcluster_tab), _translate("main_tab", "Spectral", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.aggcluster_tab), _translate("main_tab", "Agglomerative", None))
        self.clustermethod_tab.setTabText(self.clustermethod_tab.indexOf(self.dbscan_tab), _translate("main_tab", "DBSCAN", None))
        main_tab.setTabText(main_tab.indexOf(self.cluster_tab), _translate("main_tab", "Cluster", None))
        self.reducemethods_tab.setTabText(self.reducemethods_tab.indexOf(self.pca_tab), _translate("main_tab", "PCA", None))
        self.reducemethods_tab.setTabText(self.reducemethods_tab.indexOf(self.ica_tab), _translate("main_tab", "ICA", None))
        self.reducemethods_tab.setTabText(self.reducemethods_tab.indexOf(self.rpa_tab), _translate("main_tab", "Random Projection", None))
        main_tab.setTabText(main_tab.indexOf(self.reduce_tab), _translate("main_tab", "Reduce", None))
        main_tab.setTabText(main_tab.indexOf(self.visualize_tab), _translate("main_tab", "Visualize", None))
        main_tab.setTabText(main_tab.indexOf(self.other_tab), _translate("main_tab", "Other", None))

        # actions goes here
        self.openfile_btn.clicked.connect(self.openfile)

    # action functions goes here
    def openfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File','/',"Data files (*.csv)")
        fn = str(filename)
        if (fn):
            dataset = pd.read_csv(fn, sep=",")
            g = sns.PairGrid(dataset)
            g.map(plt.scatter)
            self.datainfotext.setText(str(dataset.describe))
            plt.show()  # --> uncomment this to show plot in the new window
        else:
            print 'File does not exist'


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_TabWidget()
    ex.show()
    sys.exit(app.exec_())