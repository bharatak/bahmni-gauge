#!/usr/bin/env bash
nohup Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
mvn clean install
echo "Bahmni URL is $BAHMNI_GAUGE_APP_URL"
cd bahmni-gauge-default/ && mvn install -Denv=ci -Dtags=sanity1 -DBAHMNI_GAUGE_APP_URL=$BAHMNI_GAUGE_APP_URL