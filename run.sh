#!/usr/bin/env bash
nohup Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
mvn clean install
cd bahmni-gauge-default/ && mvn install -Denv=ci -Dtags=sanity1