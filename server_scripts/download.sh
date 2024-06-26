#!/bin/bash

user_name=andrewhz  # Change username
local_prefix='/c/Users/electron/etrap'  # Change these to the desired prefix
server_prefix='etrap/data'



# No need to change below
help_info='>>> SYNTAX: "sh download.sh [-r] [filename]", use [-r] if downloading folder'

source_prefix=${server_prefix}
destination_prefix=${local_prefix}
copy_folder=false
while getopts "r" opt; do
	case ${opt} in 
		r)
			copy_folder=true
			;;
		\?)
			echo ${help_info}
			exit 0
			;;
	esac
done

if [ "$copy_folder" == "true" ]
then
	echo ">>> Downloading folder ${2} from SERVER:${source_prefix} to LOCAL:${destination_prefix}"
	scp -r ${user_name}@dtn.brc.berkeley.edu:${source_prefix}/${2} ${destination_prefix}
else
	echo ">>> Downloading file ${1} from SERVER:${source_prefix} to LOCAL:${destination_prefix}"
	scp ${user_name}@dtn.brc.berkeley.edu:${source_prefix}/${1} ${destination_prefix}
fi


