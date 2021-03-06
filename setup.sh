#!/bin/sh
if ! which python3 &> /dev/null; then
	echo "You do not have python3 in your path"
else
	cd "$(dirname "$0")"
	python3 -m venv venv
	source ./venv/bin/activate
	python3 -m pip install -r requirements.txt
fi