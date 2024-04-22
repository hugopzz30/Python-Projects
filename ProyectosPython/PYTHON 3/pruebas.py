import os.path, time
from pathlib import Path

"""
desktop = "C:\\Users\\hugop\\Documents\\prueba.txt"

with open(desktop, "w") as file:
    file.write("Hola")

"""

mastermind = "C:\\Users\\hugop\\OneDrive\\Documentos\\Curso Mastemind"

print("%s"%time.ctime(os.path.getmtime(mastermind)))
