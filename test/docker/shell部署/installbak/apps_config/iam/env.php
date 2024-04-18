<?php
// mc_iam环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${iam_nginx_host}:21308/iam',

    // 后端入口
    'backend_url' => 'http://${iam_nginx_host}:21319',

    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${iam_neo4j_host}',
        'port' => '${iam_neo4j_port}',
        'username' => '${iam_neo4j_username}',
        'password' => '${iam_neo4j_password}',
    ],
    // mysql的配置, 根据现场修改
    'mysql' => [
        'masters' => [['dsn'=> 'mysql:host=${iam_mysql_host};port=${iam_mysql_port};dbname=${iam_mysql_dbname}']],
        'username' => '${iam_mysql_username}',
        'password' => '${iam_mysql_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${iam_redis_mode}',
        'host' => 'tcp://${iam_redis_host}:${iam_redis_port}',
        'db'=> ${iam_redis_database},
        'password' => '${iam_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];