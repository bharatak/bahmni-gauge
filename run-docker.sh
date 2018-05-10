#!/usr/bin/env bash
docker run -v /var/go/.m2:/root/.m2:rw -v /var/lib/go-agent/pipelines/Functional_Test_v91/bahmni-gauge:/gauge -i bharatak/docker-gauge-chromedriver:chromedriver-2.34 -- sh run.sh
