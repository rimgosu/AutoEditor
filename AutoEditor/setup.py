from cx_Freeze import setup, Executable
 
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [],
                    excludes = [], 
                    includes = [])


import sys
base = None if sys.platform=='win32' else None

executables = [
    Executable('gui.py', base=base)
]
 
setup(
    name='pytool',
    version = '0.1',
    description = 'pytool @seonghun.chung',
    options = dict(build_exe = buildOptions),
    executables = executables
)