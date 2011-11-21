"""
/***************************************************************************
SimpleSvg
A QGIS plugin
Create simple SVG from current view, editable with InkScape
                             -------------------
begin                : 2011-06-16
copyright            : (C) 2011 by Richard Duivenvoorde
email                : richard@duif.net 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_SimpleSvg import Ui_SimpleSvg

# create the dialog for SimpleSvg
class SimpleSvgDialog(QDialog):
  def __init__(self): 
    QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_SimpleSvg ()
    self.ui.setupUi(self)


  # see http://www.riverbankcomputing.com/Docs/PyQt4/pyqt4ref.html#connecting-signals-and-slots
  # without this magic, the on_btnOk_clicked will be called two times: one clicked() and one clicked(bool checked)
  @pyqtSignature("on_btnBrowse_clicked()")
  def on_btnBrowse_clicked(self):
    fileName = QFileDialog.getSaveFileName(self, "/home/richard/temp/svgtest.svg", "/home/richard/temp", "")
    # TODO do some checks to be sure there is no extension
    self.ui.txtFileName.setText(fileName)


  def getFilePath(self):
    return self.ui.txtFileName.text()
