#!/bin/sh

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
fi

echo $1 | festival --tts
