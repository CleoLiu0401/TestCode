<?php
// mc_itsm环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${itsm_nginx_host}:21308/itsm',

    // 后端入口
    'backend_url' => 'http://${itsm_nginx_host}:21322',

    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${itsm_neo4j_host}',
        'port' => '${itsm_neo4j_port}',
        'username' => '${itsm_neo4j_username}',
        'password' => '${itsm_neo4j_password}',
    ],
    // mysql的配置, 根据现场修改
    'mysql' => [
        'masters' => [['dsn'=> 'mysql:host=${itsm_mysql_host};port=${itsm_mysql_port};dbname=${itsm_mysql_dbname}']],
        'username' => '${itsm_mysql_username}',
        'password' => '${itsm_mysql_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${itsm_redis_mode}',
        'host' => 'tcp://${itsm_redis_host}:${itsm_redis_port}',
        'db'=> ${itsm_redis_database},
        'password' => '${itsm_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];