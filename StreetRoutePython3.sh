#!/bin/bash

# Name:    StreetRouteCloudAPI
# Purpose: Execute the StreetRouteCloudAPI program

######################### Constants ##########################

RED='\033[0;31m' #RED
NC='\033[0m' # No Color

######################### Parameters ##########################

startlat=""
startlong=""
endlat=""
endlong=""
license=""

while [ $# -gt 0 ] ; do
  case $1 in
    --startlat) 
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter \'startlat\'.${NC}\n"  
            exit 1
        fi 

        startlat="$2"
        shift
        ;;
    --startlong)  
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter \'startlong\'.${NC}\n"  
            exit 1
        fi 

        startlong="$2"
        shift
        ;;
    --endlat) 
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter \'endlat\'.${NC}\n"  
            exit 1
        fi 

        endlat="$2"
        shift
        ;;
    --endlong)         
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter \'endlong\'.${NC}\n"  
            exit 1
        fi 
        
        endlong="$2"
        shift
        ;;
    --license) 
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter \'license\'.${NC}\n"  
            exit 1
        fi 

        license="$2"
        shift 
        ;;
  esac
  shift
done

########################## Main ############################
printf "\n====================== Melissa Street Route Cloud API ======================\n"

# Get license (either from parameters or user input)
if [ -z "$license" ];
then
  printf "Please enter your license string: "
  read license
fi

# Check for License from Environment Variables 
if [ -z "$license" ];
then
  license=`echo $MD_LICENSE` 
fi

if [ -z "$license" ];
then
  printf "\nLicense String is invalid!\n"
  exit 1
fi

# Run project
if [ -z "$startlat" ] && [ -z "$startlong" ] && [ -z "$endlat" ] && [ -z "$endlong" ];
then
    python3 StreetRoutePython3.py --license $license 
else
    python3 StreetRoutePython3.py --license $license --startlat "$startlat" --startlong "$startlong" --endlat "$endlat" --endlong "$endlong" 
fi

