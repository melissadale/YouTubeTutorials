# ATM: Auto Tune Models


 * https://atm.readthedocs.io/en/latest/introduction.html 
 * https://github.com/HDI-Project/ATM


**PRE-SETUP**

_For on Windows:_ 

 * Ubuntu bash on Windows: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#3
 
 * Conda for Window’s Ubuntu: https://www.cgranade.com/blog/2016/08/22/qutip-on-wsl.html 
 
 _optional:_
 
 * SQLite Viewer: https://sqlitebrowser.org/ 
 
 
 
**Files in this repo**

 * _atm_setup.sh_: This script will checkout coordinating versions of ATM and BTB, create a conda virtual environment, install packages in the requirments.txt and setup.py.
 
 
 * CookBook: _evaluate_run.py_: This python script demonstrates how to interact with the generated database once the evaluation portion is done. To use, create a directory inside the Scripts directory of ATM to store your own evaluation scripts and put file in there.  
 
 
 * CookBook: _sqlite_metrics.py_: This python script demonstrates how to collect the evaluation metrics for the best performing classifier. This example could be modified for other purposes in interacting with the generated db file. 
   


**_Helper Things:_**

- **RUN SCRIPT**: `source atm_setup.sh` 


- **Remove virtual environment**: `conda env remove -n atm_environment`
