#!/bin/sh

./dist/helloworld/helloworld 2>&1 | tee helloworld.run.log

./dist/helloworld_tk/helloworld_tk 2>&1 | tee helloworld_tk.run.log
