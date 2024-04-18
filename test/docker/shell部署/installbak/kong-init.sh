!#/bin/bash
set -e

psql -v ON_ERROR_STOP=1 -U kong kong <<-EOSQL
    CREATE DATABASE kong_inside;
EOSQL
