#!/usr/bin/sh

#An install script for tarotui

# ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
#  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
# ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀

#Usually my install scripts tend to be longer, however since this is a pure python project with no mixed languages, it tends to just be an installation
#Of the libraries

main() {
  pip install -r libraries.txt
  read -p "Would you like to run tarotui? (Y/N) " prompt
  if [[ "$prompt" = "Y" || "$prompt" = "y" ]]; then
    python tarot.py
  else
    exit
  fi
}

main
