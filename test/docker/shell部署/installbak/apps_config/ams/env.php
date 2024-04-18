<?php
// mc_ams环境
// 本文件自动生成
// 创建时间:2022-10-11 01:20:39
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${ams_nginx_host}:21308/ams',

    // 后端入口
    'backend_url' => 'http://${ams_nginx_host}:21324',

    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${ams_neo4j_host}',
        'port' => '${ams_neo4j_port}',
        'username' => '${ams_neo4j_username}',
        'password' => '${ams_neo4j_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${ams_redis_mode}',
        'host' => 'tcp://${ams_redis_host}:${ams_redis_port}',
        'db'=> ${ams_redis_database},
        'password' => '${ams_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];