#git_setup.py

import subprocess
import os
import requests



python_dep_list = list()
python_dep_list.append("pyautogui")
python_dep_list.append("pyclick")
python_dep_list.append("opencv-python")


downloads_list = list()
downloads_list.append("https://github.com/git-for-windows/git/releases/download/v2.27.0.windows.1/Git-2.27.0-64-bit.exe")
downloads_list.append("https://updates.torguard.biz/Software/Windows/torguard-setup-latest.exe")
downloads_list.append("https://www.runescape.com/downloads/oldschool.msi")


#subprocess.call(download_command, shell = True)

def download_from_url():
	for _ in downloads_list:
		url = _
		r = requests.get(url, allow_redirects=True)
		download_name = _.split("/")[-1]
		open(download_name, 'wb').write(r.content)


download_from_url()

operating_folder = "C:/OSBOT"

git_command_1 = "git init"
git_command_2 = "git remote add upstream https://github.com/JoshCourt/OSRSBOTS"
git_command_3 = "git pull upstream master"

def make_operating_folder():
	try:
		os.mkdir(operating_folder)
	except Exception as E:
		print("Error during making operating folder : "+str(E))
	os.chdir(operating_folder)
	time.sleep(2)
	subprocess.call(git_command_1, shell=True)
	subprocess.call(git_command_2, shell=True)
	print("Waiting for input to singal logged into git.....")
	input()
	subprocess.call(git_command_3, shell=True)

def python_install_dependencies():
	for _ in python_dep_list:
		command = "python -m pip install "+str(_)
		subprocess.call(command, shell=True)

python_install_dependencies()
make_operating_folder()
#download_command = curl https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe
