<?php
// mc_portal环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${portal_nginx_host}:21308/portal',

    // 后端入口
    'backend_url' => 'http://${portal_nginx_host}:21321',

    // mc系统信息配置(选配), 可以在系统设置里修改
    'system' => [
        'name' => '智能运维中台',
        'logo_file' => '',
        'customer_zh' => 'xxx公司',
        'customer_en' => 'xxxCompany',
    ],
    // 图库配置, 根据现场修改
    'neo4j' => [
        'host' => '${portal_neo4j_host}',
        'port' => '${portal_neo4j_port}',
        'username' => '${portal_neo4j_username}',
        'password' => '${portal_neo4j_password}',
    ],
    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${portal_redis_mode}',
        'host' => 'tcp://${portal_redis_host}:${portal_redis_port}',
        'db'=> ${portal_redis_database},
        'password' => '${portal_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];