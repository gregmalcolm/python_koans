#!/bin/sh

function contemplate(){
  python3 -B contemplate_koans.py
}

if [ -z $2 ]; then
  SLEEP_S=5
else
  SLEEP_S=$2
fi

while true; do
  contemplate

  case $1 in
    help|h)
      clear
      echo "This script will contemplate the phython koans"
      echo "usage: `basename $0` (mode)"
      echo
      echo "Optional modes:"
      echo "\tkeeptesting (seconds)\t - Contemplate forever with a configurable delay"
      echo "\tkeepasking \t\t - Asks you to contemplate over and over until you had enough"
      echo
      exit
      ;;
    keepasking)
      if [ "$1" == "keepasking"  ]; then
        read -p "Keep testing? [y/n] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]];then
          break
        fi
      fi
      ;;
    keeptesting)
      sleep $SLEEP_S
      continue
      ;;
    *)
      exit
      ;;
    esac
done

