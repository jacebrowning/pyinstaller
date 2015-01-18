# -*- mode: python -*-
a = Analysis(['helloworld_tk.py'],
             pathex=['/Users/Browning/Programs/PyInstaller/sandbox'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='helloworld_tk',
          debug=True,
          strip=None,
          upx=False,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name='helloworld_tk')
app = BUNDLE(coll,
             name='helloworld_tk.app',
             icon=None)
