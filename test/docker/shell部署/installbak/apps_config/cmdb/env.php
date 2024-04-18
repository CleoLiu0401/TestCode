<?php
// mc_cmdb环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${cmdb_nginx_host}:21308/cmdb',

    // 后端入口
    'backend_url' => 'http://${cmdb_nginx_host}:21323',

    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${cmdb_neo4j_host}',
        'port' => '${cmdb_neo4j_port}',
        'username' => '${cmdb_neo4j_username}',
        'password' => '${cmdb_neo4j_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${cmdb_redis_mode}',
        'host' => 'tcp://${cmdb_redis_host}:${cmdb_redis_port}',
        'db'=> ${cmdb_redis_database},
        'password' => '${cmdb_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];