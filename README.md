# Python package tempelate scaffold
------

## Steps of usage

This folder is a template scaffold for those who are not familiar with software engineering. This structure is supposed to be used to publish packages in the context for either of Data Science or Machine learning to automate model deployment.
1. Clone the repo or fork it to your account, then navigate to the project folder `cd ML_app_scaffold`
2. Activate the virtualenv `dev` by running this command in the terminal `source dev/bin/activate`
3. Change `sub_pckage_1` to your package name
4. install all dependencies `pip install -rrequirements.txt`
5. Add your information to the `setup.py` file
6. Add train and test data to the datasets folder inside the package folder
7. Update the `MANIFEET.in` file to your package name
8. Navigate to the sub_package_1 folder then run `tox -r` to build the package

You should see:
 **commands succeeded congratulations :)**

9. You can add tests in the test folder in the dedicated package. However, you need to add the dependency in the `tox.ini` and `requirements.txt` files. for more details check out [tox documentation](https://tox.readthedocs.io/en/latest/examples.html)

10. In case you want to create a CI/CD pipeline, the demo folder includes a basic configuration file. You need to add enviromental variables to your project configuration at the project setting at circleci. 

11. In case you need to publish your model using `Gemfury.io`, you can use the script file `publish_model.sh` and of course add env variables to the project setting at the circleci. 
------

## Few things to consider

I structured the scaffold based on the OOP which seperate concerns of code. 
* `processing` folder conatains any scripts for data wrangeling, cleaning, or feature engineering. 
* `trained_model` folder contains any scripts dedicated to build model, tuning or any related scripts.
* `pipeline.py` file contains all the procedures that should be done using the `sklearn.pipeline` 
* `predict.py` file dedicated for getting out the predictions
* `train_pipeline.py` file dedicated to train the model, starting from downloading the dataset, split, apply pipeline...etc. 

You are free to just delete them and put all your scripts in just one file - personal preferences. 

** Please note that the `train_pipeline` is commented out until you download the dataset, fill the config file with the correct variables.** Otherwise, the `tox` command would fail because there are no variables to train. 

* The tests are not set yet on the scaffold - next step, pull requests are very welcome. 

## Output:

The resulted model is saved as a `.pkl` file versioned with the same version of the package. 


------
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)