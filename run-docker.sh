#!/bin/sh

docker run -v /var/go/.m2:/root/.m2:rw -v $PWD:/gauge -i bharatak/docker-gauge-chromedriver:chromedriver-2.34 -- sh run.sh $ENV
#Hack. The html-report executable is symlinked as a root user.  
#so, removing it so that the artifact is accessible from gocd server
rm -f bahmni-gauge-default/reports/html-report/html-report
