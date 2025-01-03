# Melissa - Street Route Cloud API Python3

## Purpose
This code showcases the Melissa Street Route Cloud API using Python3.

Please feel free to copy or embed this code to your own project. Happy coding!

For the latest Melissa Street Route release notes, please visit: https://releasenotes.melissa.com/cloud-api/street-route/

For further documentation, please visit: https://docs.melissa.com/cloud-api/street-route/street-route-index.html

The console will ask the user for:

- StartLatitude
- StartLongitude
- EndLatitude
- EndLongitude

And return information of the coordinates such as:

- Results
- Units
- TransmissionResult
- TravelTime
- TotalDrivingDistance
- TransmissionReference

## Tested Environments
- Windows 10 64-bit Python 3.10.4, Powershell 5.1
- Ubuntu Linux 20.04.04 LTS 64-bit Python 3.10.4
- Street Route Cloud API Version 8.2.1.0

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Download this project
```
git clone https://github.com/MelissaData/StreetRoute-Python3
cd StreetRoute-Python3
```

## Windows

#### Install Python3
Before starting, make sure that Python3 has been correctly installed on your machine and your environment paths are configured. 

You can download Python here: 
https://www.python.org/downloads/

To set up your Path to correctly to use the python3 command, execute the following steps:
1) Run Powershell as an administrator 
2) Execute the command: 
`New-Item -ItemType SymbolicLink -Path "Link" -Target "Target"`

    where "Target" is the path to py.exe (by default this should be "C:\Windows\py.exe")\
    and "Link" is the path to py.exe, but "py.exe" is replaced with "python3.exe"\
    For Example:\
    `New-Item -ItemType SymbolicLink -Path "C:\Windows\python3.exe" -Target "C:\Windows\py.exe"`

If you are unsure, you can check by opening a command prompt window and typing the following:
`python3 --version`

![alt text](/screenshots/python_version.png)

#### Run Powershell Script
Parameters:
- -startlat: an input start latitude
- -startlong: an input start longitude
- -endlat: an input end latitude
- -endlong: an input end longitude
 	
  This is convenient when you want to get results for a specific request in one run instead of testing multiple records in interactive mode.  

- -license (optional): a license string to test the Cloud API

There are two modes:

- Interactive 

	The script will prompt the user for input(s), then use the provided input(s) to call the Cloud API. For example:
	```
	.\StreetRoutePython3.ps1
	```

- Command Line 

	You can pass a start latitude, start longitude, end latitude, end longitude, and license string into `-startlat`, `-startlong`, `-endlat`, `-endlong`, and `-license` parameters respectively to test the Cloud API. For example: 
	```
    .\StreetRoutePython3.ps1 -startlat "33.637520" -startlong "-117.606920" -endlat "33.649870" -endlong "-117.582960"
    .\StreetRoutePython3.ps1 -startlat "33.637520" -startlong "-117.606920" -endlat "33.649870" -endlong "-117.582960" -license "<your_license_string>"
    ```
	
This is the expected output from a successful setup for interactive mode:

![alt text](/screenshots/output.png)

## Linux

#### Install Python3
Before starting, check to see if you already have the Python3 already installed by entering this command:

`python3 --version`

If the Python3 is already installed, you should see it in the following list:

![alt text](/screenshots/python_version2.png)

As long as the above list contains version `3.xx.xx` (underlined in red), then you can skip to the next step. If your list does not contain version 3, or you get any kind of error message, then you will need to download and install Python3.

To download, run the following commands to add the Microsoft package signing key to your list of trusted keys and add the package repository.

```
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
```

Next, you can now run this command to install the Python3:

```
sudo apt-get update && \
  sudo apt-get install -y python3
```

Once all of this is done, you should be able to verify that the Python3 is installed with the `Python3 --version` command.

#### Run Bash Script
Parameters:
- --startlat: an input start latitude
- --startlong: an input start longitude
- --endlat: an input end latitude
- --endlong: an input end longitude

  This is convenient when you want to get results for a specific request in one run instead of testing multiple records in interactive mode.  

- --license (optional): a license string to test the Cloud API

There are two modes:

- Interactive 

	The script will prompt the user for input(s), then use the provided input(s) to call the Cloud API. For example:
	```
	./StreetRoutePython3.sh
	```

- Command Line 

	You can pass a start latitude, start longitude, end latitude, end longitude, and license string into `-startlat`, `-startlong`, `-endlat`, `-endlong`, and `-license` parameters respectively to test the Cloud API. For example: 
	```
    ./StreetRoutePython3.sh --startlat "33.637520" --startlong "-117.606920" --endlat "33.649870" --endlong "-117.582960"
    ./StreetRoutePython3.sh --startlat "33.637520" --startlong "-117.606920" --endlat "33.649870" --endlong "-117.582960" --license "<your_license_string>"
    ```

This is the expected output from a successful setup for interactive mode:

![alt text](/screenshots/output2.png)

## Result Codes
For details about the result codes please refer to https://docs.melissa.com/melissa/result-codes/result-codes-index.html

## Contact Us
For free technical support, please call us at 800-MELISSA ext. 4 (800-635-4772 ext. 4) or email us at tech@melissa.com.

To purchase this product, contact the Melissa sales department at 800-MELISSA ext. 3 (800-635-4772 ext. 3).
