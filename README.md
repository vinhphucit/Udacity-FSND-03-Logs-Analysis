# Logs Analysis

This is the thirt project in FSND of Udacity. In this project, I used Python to get data from Postgres Database and print output.

### Enviroment Installation
Fistly, You have to make sure you already setup python, virtualbox and vagrant. Check all with bellow commands:

`python --version`  -> `Python 2.7.10`
`vagrant --version` -> `Vagrant 1.9.1`

If python hasn't installed you can download [here](https://www.python.org/downloads/)
If vagrant hasn't installed you can download [here](https://www.vagrantup.com/downloads.html)
If VirtualBox hasn't installed you can download [here](https://www.virtualbox.org/wiki/Downloads)

Download [FSND-Virtual-Machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository [here]https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

### Setup Project

1. Download [postgress data from here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
2. Unzip and put file newsdata.sql to the vagrant directory above and run these commands:
`vagrant up`
`vagrant ssh`
3. Restore data from newsdata.sql to Postgres Database 
`psql -d news -f newsdata.sql`

### Run Project
From Source Code Directory in Virtual Machine run this command
`python3 ./analysis_log.py`
