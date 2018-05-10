#!/bin/sh
nohup Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
mvn clean install
echo "The env is $env"
# cd bahmni-gauge-default/ && mvn install -Denv=$ENV -Dtags=$TAGS