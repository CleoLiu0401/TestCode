<?php
// mc_audit环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${audit_nginx_host}:21308/audit',

    // 后端入口
    'backend_url' => 'http://${audit_nginx_host}:21318',

    // es数据库配置, 根据现场修改
    'elasticsearch' => [
        'hosts' => ['${audit_es_hosts}'],
        'master' => '${audit_es_master}',
        'username' => '${audit_es_username}',
        'password' => '${audit_es_password}',
        'shards' => '${audit_es_shards}',
        'replicas' => '${audit_es_replicas}',
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];