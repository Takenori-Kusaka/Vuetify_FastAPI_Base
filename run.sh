#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/frontend
npm run build
cd ../
python3 -m pipenv run start
