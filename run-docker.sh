#!/usr/bin/env bash

BASEDIR=${dirname $0}
echo "The base directory is $BASEDIR"

docker run -v /var/go/.m2:/root/.m2:rw -v $BASEDIR/bahmni-gauge:/gauge -i bharatak/docker-gauge-chromedriver:chromedriver-2.34 -- sh run.sh
