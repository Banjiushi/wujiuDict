import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'D:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Python36\tcl\tk8.6'

include_files = [
    r'E:\spider\env-spider\Scripts\tcl86t.dll',
    r'E:\spider\env-spider\Scripts\tk86t.dll',
]

build_exe_options = {'packages':['os', 'tkinter'], 'include_files':include_files}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'wujiu',
    version = '0.1',
    description = 'wujiu fanyi',
    options = {'build_exe':build_exe_options},
    executables = [Executable('wujiuDict.py',base=base)]
)