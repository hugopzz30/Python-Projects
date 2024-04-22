# Configurar la extension para poder crear un ejecutable

from distutils.core import setup
import py2exe
import glob
import os
import re
import sqlite3 # Conexion a una base de datos
from time import sleep
from random import randrange
from pathlib import Path # Libreria ruta home
import os.path, time

"""
setup(console = ["hackerscript.py"]) # console = Abre el ejecutable en la terminal
                                    # windows = Abre el ejecutable en una ventana

"""

setup(zipfile = None,
      options = {'py2exe': {"bundle files": 1}},
      console = ["convirtiendo_a_exe.py"])

"""Nos permite crear un archivo zip
      para mantener todos los archivos del ejecutable en poco espacio"""