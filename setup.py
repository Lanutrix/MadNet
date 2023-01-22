from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'win32gui'

executables = [
    Executable('D:\\BackDoorBot\\crmain.py', base=base)
]

setup(name='j',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
