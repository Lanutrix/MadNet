import cx_Freeze
import os
import sys
import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\MyProgram')

name, _ = winreg.QueryValueEx(key, 'Name')
description, _ = winreg.QueryValueEx(key, 'Description')
version, _ = winreg.QueryValueEx(key, 'Version')

included_modules = ['os', 'sys']

build_exe_options = {
'include_msvcr': True,
'includes': included_modules
}

executable = cx_Freeze.Executable(
script='my_script.py',
targetName='my_script.exe',
base='Win32GUI',
icon='my_icon.ico'
)

build = cx_Freeze.Build(
executable=executable,
build_exe_options=build_exe_options
)

cx_Freeze.setup(
name=name,
version=version,
description=description,
options={'build': build},
executables=executable
)