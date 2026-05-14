#!/usr/bin/sh

#An install script for tarotui

# ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
#  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
# ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀

#Usually my install scripts tend to be longer, however since this is a pure python project with no mixed languages, and just one external dependency (ollama), it tends to just be an installation
#Of the libraries and the building of an ollama model

clear

echo '''
▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
 ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
- The installation uses pip to install the required python libraries
- The installation installs ollama alongside building the custom model 
''' 

main() {
  echo "Installing the required python libraries"
  pip install -r libraries.txt
  if ! command -v "ollama" > /dev/null; then
    read -p "Would you like to install ollama and build the ollama model required for the reading? (Y/N) " ollamaPrompt
    if [[ "$ollamaPrompt" = "Y" || "$ollamaPrompt" = "y" ]]; then
      curl -fsSL https://ollama.com/install.sh | sh
      ollama create tarotui -f src/utils/Ollama_custom/Modelfile
    else
      continue
    fi
  else
    echo "OLLAMA ALREADY INSTALLED, PROCEEDING TO RUN TAROTUI..."
  fi
  read -p "Would you like to run tarotui? (Y/N) " runPrompt
  if [[ "$runPrompt" = "Y" || "$runPrompt" = "y" ]]; then
    python tarot.py
  else
    exit
  fi
}

main
