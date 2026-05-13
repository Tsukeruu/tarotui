#!/usr/bin/sh

#An install script for tarotui

# ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
#  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
# ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀

#Usually my install scripts tend to be longer, however since this is a pure python project with no mixed languages, and just one external dependency (ollama), it tends to just be an installation
#Of the libraries and the building of an ollama model

main() {
  pip install -r libraries.txt
  read -p "Would you like to build the ollama model required for the reading? (Y/N)" ollamaPrompt
  if [[ "$ollamaPrompt" = "Y" || "$ollamaPrompt" = "y" ]]; then
    ollama create tarotui -f src/utils/Ollama_custom/Modelfile
  else
    continue
  fi
  read -p "Would you like to run tarotui? (Y/N) " runPrompt
  if [[ "$runPrompt" = "Y" || "$runPrompt" = "y" ]]; then
    python tarot.py
  else
    exit
  fi
}

main
