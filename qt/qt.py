#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Desarrollado para LaSociedadPost
# Author: Leandro Inocencio aka Cesio (cesio.arg@gmail.com)

"""Funciones generales para el manejo de QT"""

import sys

from lasp.tactic.utils import ensure_module

try:    # Nuke < 11
    globals().update(ensure_module('PySide'))
    from PySide.QtCore import *
    from PySide.QtGui import *
except: # Nuke > 11
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    #from PySide2.QtWidgets import QApplication
    
from cStringIO import StringIO
import xml.etree.ElementTree as xml


def closeExistingWindows(self):  #TODO no funciona esto hace crashear al maya
    """Metodo que se hereda para cerrar ventanas existentes."""
    
    for qt in qApp.topLevelWidgets():
        try:
            if qt.__class__.__name__ == self.__class__.__name__:
                qt.ui.close()
                qt.close()
        except:
            pass


def load_ui(filepath, parent):
    """Carga un archivo .ui de QT y devuelve los objectos pythonizados de la UI
    
    :param str filepath: Ruta al archivo .ui
    
    :param QWidget parent: Widget padre
    
    :return: Un QWidget con toda su descendencia
    """
    try:    # Nuke < 11
        from PySide.QtUiTools import QUiLoader
    except: # Nuke > 11
        from PySide2.QtUiTools import QUiLoader
    

    uifile = QFile(filepath)
    uifile.open(QFile.ReadOnly)
    data = QUiLoader().load(uifile, parent)
    uifile.close()
    return data


class GetApp(object):
    """Contexto que nos da el *QApplication.instance()*
    
    :param bool close: Si es True cierra la UI cuando sale de contexto
    """
    
    def __init__(self, close=True):
        self.close = close
        self.is_instance = False
        
    def __enter__(self):
        self.is_instance = True
        self.app = QApplication.instance()
        if self.app:
            self.is_instance = True
        else:
             self.app = QApplication(sys.argv)
             self.is_instance = False
        
        return self.app
        
    def __exit__(self, *args):
        if not self.is_instance and self.close:
             sys.exit(self.app.exec_())
        else:
            self.app.exec_()


def loadUiType(uiFile):
    import pysideuic
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}
        
        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame
        
        #Fetch the base_class and form class based on their type in the xml from designer
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('%s'%widget_class)
    return form_class, base_class


def open_ui(filename, parent=None):    
    """Otra forma de cargar un archivo .ui de QT y devuelver los objectos pythonizados de la UI
    
    :param str filename: Ruta al archivo .ui
    
    :param QWidget parent: Widget padre
    
    :return: Un QWidget con toda su descendencia
    """
    
    ui_form, ui_base = loadUiType(filename)

    class ui(ui_form, ui_base):
        def __init__(self, parent=parent):
            super(ui, self).__init__(parent)
            self.setWindowFlags(Qt.Window)
            self.setAttribute(Qt.WA_DeleteOnClose)
            self.setupUi(self)

    return ui()
