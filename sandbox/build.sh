#!/bin/sh

pyinstaller helloworld.py --noconfirm --clean --noupx --debug 2>&1 | tee helloworld.build.log

pyinstaller helloworld_tk.py --noconfirm --clean --noupx --debug --windowed 2>&1 | tee helloworld_tk.build.log
