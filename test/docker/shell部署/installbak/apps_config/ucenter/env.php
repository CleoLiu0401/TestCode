<?php
// mc_ucenter环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${ucenter_nginx_host}:21308/ucenter',

    // 后端入口
    'backend_url' => 'http://${ucenter_nginx_host}:21320',

    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${ucenter_neo4j_host}',
        'port' => '${ucenter_neo4j_port}',
        'username' => '${ucenter_neo4j_username}',
        'password' => '${ucenter_neo4j_password}',
    ],
    // mysql的配置, 根据现场修改
    'mysql' => [
        'masters' => [['dsn'=> 'mysql:host=${ucenter_mysql_host};port=${ucenter_mysql_port};dbname=${ucenter_mysql_dbname}']],
        'username' => '${ucenter_mysql_username}',
        'password' => '${ucenter_mysql_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${ucenter_redis_mode}',
        'host' => 'tcp://${ucenter_redis_host}:${ucenter_redis_port}',
        'db'=> ${ucenter_redis_database},
        'password' => '${ucenter_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];