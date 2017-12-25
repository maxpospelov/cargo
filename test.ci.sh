#!/bin/bash
set -e

docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml up -d test_web
docker-compose -f docker-compose.test.yml run test_prepare migrate
docker-compose -f docker-compose.test.yml run test_prepare superuser
docker-compose -f docker-compose.test.yml run test_prepare migrate
docker-compose -f docker-compose.test.yml run behave
docker-compose -f docker-compose.test.yml run test_prepare flush
docker-compose -f docker-compose.test.yml stop
docker-compose -f docker-compose.test.yml rm -fv

