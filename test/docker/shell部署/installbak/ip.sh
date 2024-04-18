#!/bin/bash

#替换ip
read -p "ip: " ip

sed -i "s/1.1.1.1/${ip}/g" configs/local/host.json
sed -i "s/1.1.1.1/${ip}/g" configs/local/php.json
