# TAROTUI
A tarot reading experience in the terminal

> [!TIP]
> TAROTUI in the master branch uses an ollama model with approximately 2-3gb of storage, that model is specifically and originally `ollama3.2`.<br>
> In the foreseeable future (yes i love using this word), options to choose custom models based on user preferences is going to be added to allocate different situations, such as not enough storage, etc. <br>
> Please know that qwen3.5:4b and deepseek-r1 support is added by switching to the qwen3.5 / deepseek-r1 branch and rebuilding the model through ```ollama create tarotui -f src/utils/Ollama_custom/Modelfile```

- All currently supported models are listed below

| Model         | Size (in gb)              | Status                            | Pros | Cons                                                                 |
| :------------ | :-------------------------| :-------------------------------- |:-----------------------------------------|:---------------------------------|
| DEEPSEEK-R1   | 5gb                       | Available at `deepseek-r1 `branch |Enhanced logic gate and detailed responses| Longer time for a `POST` request |
| llama3.2      | 2-3 gb                    | Available at `master` branch      |Shorter time for a response, creative and quick| Less logic gate and reasoning and does not **implicitly** follow the Modelfile|
| qwen3.5:4b    | 3.4 gb                    | Available at `qwen3.5` bramch     |Detailed responses and improved logic gate in comparison to llama3.2| Extremely longer time for a `POST` request and is slower|

For contributions in regards to model availability please read [Contributing.md](CONTRIBUTING.md)

![Stars](https://img.shields.io/github/stars/Tsukeruu/tarotui?style=for-the-badge)
![License](https://img.shields.io/github/license/Tsukeruu/tarotui?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/Tsukeruu/tarotui?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/Tsukeruu/tarotui?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/Tsukeruu/tarotui?style=for-the-badge)

<img width="1200" height="800" alt="Image" src="https://github.com/user-attachments/assets/e4a310a5-bad0-425d-b20c-63681a1653f7" />

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
**The command above installs either ollama 3.2 / deepseek / qwen3.5 if not installed, which depends on your current branch, for further information head to the start of the README, disk space / usage may vary from model to model, and builds the custom model using the Modelfile which includes the persona required for the reading**


## License

[MIT](LICENSE)
