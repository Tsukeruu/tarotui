# TAROTUI
A tarot reading experience in the terminal

> [!TIP]
> TAROTUI uses an ollama model with 2gb of storage, that model is specifically and originally `ollama3.2`.
> In the foreseeable future (yes i love using this word), options to choose custom models based on user preferences is going to be added to allocate different situations, such as not enough storage, etc

![Stars](https://img.shields.io/github/stars/Tsukeruu/tarotui?style=for-the-badge)
![License](https://img.shields.io/github/license/Tsukeruu/tarotui?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/Tsukeruu/tarotui?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/Tsukeruu/tarotui?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/Tsukeruu/tarotui?style=for-the-badge)

<img width="1200" height="800" alt="Image" src="https://github.com/user-attachments/assets/8679285a-d71e-4d98-a764-b15fab5ad695" />

- Sorry for the slow post request my internet is bunz :(

  
- **TAROTUI** is a tarot reading experience in the terminal built with python 🐍, questions are analyzed through ollama and card shuffling is done through the backend

## Installation

> [!CAUTION]
> For all universal linux distros, no specific distro package manager was used in the creation of this project, and thus requires python installed,
> This is a mere python program with no varying ux and incompatability of specific packages, making it available to systems with python installed

  <img width="1893" height="996" alt="Image" src="https://github.com/user-attachments/assets/d5b24e96-e8e9-4764-b868-845048440bdc" />
  
  ## Using the shell script

  - **To begin your first tarot reading experience run the install script in shell using the following command, please note that this command does not account for git cloning, it assumes you've already git cloned the repository, if you havent git cloned the repository then git clone it now and follow up on the install script**

  - **Please note that for the install, have python alongside pip installed to download the required libraries used to build this project**

  ```bash
  cd tarotui && chmod +x ./install.sh
  ./install.sh
  ```

  If you havent git cloned then proceed to do so here and run the command above ^^
  ```bash
  git clone https://github.com/Tsukeruu/tarotui
  ```

## Manually
- **For users who value security and do not trust shell scripts online, you may install it manually using the following set of commands**
- **First and foremost have python and pip installed, this section wont cover the installation for python as it requires covering for most distro package managers**

```bash
cd tarotui
pip install -r libraries.txt
````
The command above installs all the python libraries required ^

if you have not installed ollama then proceed to do so using the following command
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
After successfuly installing ollama proceed to build the tarotui model using the following command

```bash
cd tarotui
ollama create tarotui -f src/utils/Ollama_custom/Modelfile
```
**The command above installs ollama 3.2 if not installed, which takes 2 gbs of storage and builds the custom model using the Modelfile which includes the persona required for the reading**
