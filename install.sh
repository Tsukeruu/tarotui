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
  if ! command -v "ollama"; then
     read -p "Ollama was not detected in your system, would you like to download and install it now? (Y/N) " installOllama
     if [[ "$installOllama" = "Y" || "$installOllama" = "y" ]]; then
        curl -fsSL https://ollama.com/install.sh | sh
     else 
       exit
     fi
  else 
    continue
  fi

  read -p "Would you also like to build the ollama model required for the reading? (Y/N) " ollamaPrompt
  if [[ "$ollamaPrompt" = "Y" || "$ollamaPrompt" = "y" ]]; then 
    ollama create tarotui -f src/utils/Ollama_custom/Modelfile
    read -p "After creating the model: tarotui, would you like to delete the base model 'llama3.2', this would not affect anything in regards to the program" clean
    if [[ "$clean" = "Y" || "$clean" = "y" ]]; then
      ollama rm llama3.2
    else 
      continue
    fi
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
