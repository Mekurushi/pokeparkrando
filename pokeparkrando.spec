block_cipher = None

import os
import re
import glob
def build_datas_recursive(paths):
  datas = []

  for path in paths:
    for filename in glob.iglob(path, recursive=True):
      dest_dirname = os.path.dirname(filename)
      if dest_dirname == "":
        dest_dirname = "."

      data_entry = (filename, dest_dirname)
      datas.append(data_entry)
      print(data_entry)

  return datas
a = Analysis(['pokeparkrando.py'],  # Your main script
             pathex=[],
             binaries=[],
             datas=build_datas_recursive([
              'asm/*/*.txt',
              'asm/*/patch_diffs/*.txt',
              'assets/**/*',

              ]),
             hiddenimports=[
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pokeparkrando',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          runtime_tmpdir=None,
          icon="assets/icon.ico",)