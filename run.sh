#! /bin/bash
echo "" > nba_and_warriors_config
echo "" > nba_only_config
echo "" > warriors_only_config

rm *out
ubuntu@ip-172-31-43-218:~/assignment2/all$ cat run.sh
#! /bin/bash

function run {
  python main.py

  if [ $? -eq 139 ]; then
    run
  fi
}

run
