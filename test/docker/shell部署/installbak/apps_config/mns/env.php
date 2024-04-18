<?php
// mc_mns环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${mns_nginx_host}:21308/mns',

    // 后端入口
    'backend_url' => 'http://${mns_nginx_host}:21325',

    // mysql的配置, 根据现场修改
    'mysql' => [
        'masters' => [['dsn'=> 'mysql:host=${mns_mysql_host};port=${mns_mysql_port};dbname=${mns_mysql_dbname}']],
        'username' => '${mns_mysql_username}',
        'password' => '${mns_mysql_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${mns_redis_mode}',
        'host' => 'tcp://${mns_redis_host}:${mns_redis_port}',
        'db'=> ${mns_redis_database},
        'password' => '${mns_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];