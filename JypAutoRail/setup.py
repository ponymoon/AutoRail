import sys
import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'C:\Conda\Library\lib\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Conda\Library\lib\tk8.6'
build_exe_options = dict(
        includes = ["sys","io","datetime","re","os", "time","telegram","threading","PyQt5","tinydb"],
        include_files = ["lib/JypAutoRailLayOut.py","lib/AuthDialog.py","lib/RailAuto.py","src/click.wav","src/File_Logo.png","src/JARlogo.ico","src/Korail_logo.png","src/Rail_Logo.png","src/Srt_logo.png","src/start.wav"]
)

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "JypAutoRail",
        version = "1.0",
        description = "Parsing_macro",
        author = "Jyp",
        options = dict(build_exe = build_exe_options),
        executables = [Executable("JARmain.py", base=base)])
