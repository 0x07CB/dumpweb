#!/bin/bash
function installing(){
	echo "Install in progress..."
	sudo cp dumpweb.py /usr/bin/dumpweb && sudo chmod a+x /usr/bin/dumpweb
	dumpweb --help
}

if [ -e "/usr/bin/dumpweb" ]
then
	if [ $# -eq 1 ]
	then
		if [ "$1" == "-f" ]
		then
			installing
		else
			echo -e "Bad args."
			exit 2
		fi
	else
		echo -e "Is installed, For Overwrite use the flag (-f)."
		exit 2
	fi

else
	installing
	exit 0
fi
