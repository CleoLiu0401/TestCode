#!/bin/bash
# chkconfig: 23456 10 90 
# description: myservice ....

source /etc/profile
sleep 5

#start php
#/usr/local/php7.3/sbin/php-fpm -R
php-fpm -R

#start nginx
#/usr/local/nginx/sbin/nginx
nohup /usr/local/nginx/sbin/nginx > /dev/null 2>&1 &

#keep running
tail -f /dev/null
