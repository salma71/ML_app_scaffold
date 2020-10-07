# Python package tempelate scaffold
------

## Steps of usage

This folder is a template scaffold for those who are not familiar with software engineering. This structure is supposed to be used to publish packages in the context for either of Data Science or Machine learning to automate model deployment.
1. Clone the repo or fork it to your account, then navigate to the project folder `cd ML_app_scaffold`
2. Activate the virtualenv `dev` by running this command in the terminal `source dev/bin/activate`
3. Change `sub_pckage_1` to your package name
4. Add your information to the `setup.py` file
5. Add train and test data to the datasets folder inside the package folder
6. Update the `MANIFEET.in` file to your package name
7. Navigate to the sub_package_1 folder then run `tox -r` to build the package

You should see:
 **commands succeeded congratulations :)**

8. You can add tests in the test folder in the dedicated package. However, you need to add the dependency in the `tox.ini` and `requirements.txt` files. for more details check out [tox documentation](https://tox.readthedocs.io/en/latest/examples.html)

------

## Few things to consider

I structured the scaffold based on the OOP which seperate concerns of code. 
* `processing` folder conatains any scripts for data wrangeling, cleaning, or feature engineering. 
* `trained_model` folder contains any scripts dedicated to build model, tuning or any related scripts.
* `pipeline.py` file contains all the procedures that should be done using the `sklearn.pipeline` 
* `predict.py` file dedicated for getting out the predictions
* `train_pipeline.py` file dedicated to train the model, starting from downloading the dataset, split, apply pipeline...etc. 

You are free to just delete them and put all your scripts in just one file - personal preferences. 

------
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)