>[!TIP]
>Please know that due to this new release, the diversity of contributions may be limited to the scope of simply adding support to your own models<br>
>In the future, know that as more modifications come and go, contributions will diversify.

## Contributing
- **To contribute please follow the guidelines bellow**
  - **Fork this repository**
  - **Make changes as you wish and ensure code readability**
  - **Commit changes and perform a pull request**
  - **As the owner and manager of this repository I will read and review your changes and merge them**

## Details  
- **To contribute at this current time and new release follow the steps below**
  - **One of the ways to contribute is by adding support to your own models**
  - **To do so, follow the steps above and make changes to the file located in src/utils/Ollama_custom/Modelfile**
  - **Please perform research to the model you're adding and provide details about its pros and cons**
  - **If the model being added has strong logic gates such as those of qwen3.5 and deepseek-r1, copy the modelfile from deepseek-r1**
  - **After copying the modelfile change the FROM `llama3.2` / `deepseek-r1` to FROM `your_model_name`, afterwards save the file and exit**
  - **To handle the installation part simply edit the install.sh, head over to the if statement that does a check on the $clean variable, change the ollama rm `deepseek-r1 / llama3.2 / qwen3.5` to ollama rm `your_model_name`**
  - **To provide further clarity to the installation procedure change the base model name to `your_model_name` in this string `read -p "After creating the model: tarotui, would you like to delete the base model 'llama3.2', this would not affect anything in regards to the program (Y/N) " clean`, change `llama3.2` to `your_model_name`**
  - **Afterwards i will review changes and view the model you've added and analyze its pros and cons and add it to the table at the README.md**
