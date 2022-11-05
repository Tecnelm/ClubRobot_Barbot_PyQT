# Python software for BARBOT 2022

This is the repo for BARBOT 2022 GUI in python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

`git clone https://gitlab.com/barbot-2020/barbotQt.git`

### Prerequisites

* Python3

### Deployment

 This project has been deployed with dietpi OS, based on debian bulleyes for thinker board, so please download it from [here](https://dietpi.com/downloads/images/DietPi_ASUSTB-ARMv7-Bullseye.7z)
1.   Flash the .img downloaded into the SD card (windows use rufus, linux `dd` ⚠️**WARNING you can destroy your drive verify 2 times your arguments** 
2.  Run the thinker board **ℹ️ ID=root pass=dietpi**
3.  Do initial configuration (follow instruction on screen, like configuration of Wi-Fi or stuff like that)
4. Install requirement (refer section below)
5. Clone this repository and go inside `git clone https://gitlab.com/barbot-2020/barbotQt.git`
6. `pip3 install -r Requirement.txt`(you may need to remove PySide2)
7. `echo '#!/bin/sh'>start.sh && echo 'python3 Main.py' >>start.sh && chmod +x ./start.sh`
8. Edit configuration like serial port, screen size 
9. Plug an arduino 
10. execute `startx /bin/sh ./start.sh `(must be sudo)
11. setup autostart with dietpi-config

#### Requirement pakage
----
Please install following package with :
```bash 
sudo apt update && apt upgrade -y
sudo apt install -y \
	git \
	python3 \
	python3-pip \
	python3-PySide2* \
	lxqt \
	xinit \
	xorg 
```
---
### Development 
Please follow instruction above. 
[**PLEASE work in VENV python**](https://docs.python.org/fr/3/tutorial/venv.html)
 

## Project Infos

Game of the BARBOT 2022.

## Built With

* [Python3](https://www.python.org/) - Python
* [VsCode](https://code.visualstudio.com/) - Visual Studio Code

## Authors

* **Clément Garrigues** - *Initial work and development* - [Tecnelm](https://gitlab.com/Tecnelm)
* **Matthieu Jouin** - *Initial work and development*  - [2t1h](https://gitlab.com/2t1h)
* **Sophie Dreano** - *Drawing and Ideas* - [soso_drn_](https://www.instagram.com/soso_drn_/)
* **Paulin Navas** - *Rules* - [@HeinekenKatana](https://twitter.com/HeinekenKatana)

## License

Blank

## Acknowledgments

* Deel free to modify any thing in this document if you find it pertinent !
# ClubRobot_Barbot_PyQT_2022
