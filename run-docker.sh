#!/usr/bin/env bash

docker run -v /var/go/.m2:/root/.m2:rw -v $PWD:/gauge -i bharatak/docker-gauge-chromedriver:chromedriver-2.34 -- sh run.sh
rm -f bahmni-gauge-default/reports/html-report/html-report
