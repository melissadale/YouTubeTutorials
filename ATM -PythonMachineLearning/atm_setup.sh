#!/bin/bash
mkdir ATM
cd ATM

conda create --name atm_environment python=3.5
source activate atm_environment

sudo apt install libmysqlclient-dev
sudo apt install sqlite3
mkdir ATM_code
cd ATM_code

echo "************************************************************"
echo "****   Cloning atm from GitHub"
echo "************************************************************"
git clone https://github.com/hdi-project/ATM.git .
git reset --hard 799468fc1daef41470be389c79898ba69bafd0bd

echo "****   adjusting requirements.txt"
rm requirements.txt

echo "boto>=2.48.0
joblib>=0.11
future>=0.16.0
mysqlclient>=1.2
numpy>=1.13.1
pandas>=0.22.0
pyyaml>=3.12
requests>=2.18.4
scikit-learn>=0.18.2
scipy>=0.19.1
sklearn-pandas>=1.5.0
sqlalchemy>=1.1.14">> requirements.txt

echo "************************************************************"
echo "****   Installing requirements for ATM"
echo "************************************************************"

pip install -r requirements.txt
python setup.py install

echo "****   SET UP BayTune/BTB"
mkdir BTB
cd BTB

git clone https://github.com/HDI-Project/BTB.git .
git reset --hard 0bf834b70cfa12bc32918fd574b266d73b2616c2

echo "****   Modifying gp.py"
cd btb/tuning

sed -e 's/GaussianProcess, //g' -i gp.py

echo "****   Install BTB"
cd ../..
python setup.py install

cd ..

echo "************************************************************"
echo "****   Copying helper scripts"
echo "************************************************************"

cp scripts/enter_data.py .
cp scripts/worker.py .

echo "************************************************************"
echo "****   All DONE!"
echo "****   Thank you for running Melissa's Script"
echo "****   Now make it so!"
echo "************************************************************"
