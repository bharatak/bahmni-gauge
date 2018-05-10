#!/usr/bin/env bash
cd deployables/downloaded_rpms/rpms && sudo yum install -y bahmni-openmrs && sudo yum install -y bahmni-implementer-interface-* &&sudo yum install -y bahmni-emr-* && sudo yum install -y bahmni-web-* && cd ../../..
sudo service openmrs start
sleep 2m
sudo sed -i 's|##SSLCertificateChainFile /etc/pki/tls/certs/server-chain.crt|SSLCertificateChainFile /etc/bahmni-certs/chained.pem|g' /opt/bahmni-web/etc/ssl.conf
sudo sed -i 's|SSLCertificateKeyFile /etc/pki/tls/private/localhost.key|SSLCertificateKeyFile /etc/bahmni-certs/domain.key|g' /opt/bahmni-web/etc/ssl.conf
sudo sed -i 's|SSLCertificateFile /etc/pki/tls/certs/localhost.crt|SSLCertificateFile /etc/bahmni-certs/cert.crt|g' /opt/bahmni-web/etc/ssl.conf
sudo service httpd restart
sudo service openmrs restart