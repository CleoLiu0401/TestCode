<?php
// mc_regcenter环境
return [
    // 配置api网关地址, 根据现场修改
    'apigateway' => '${mc_api_gateway_outside}',
    'apigatewayadmin' => '${mc_api_gateway_outsideadmin}',
    'apigatewayinside' => '${mc_api_gateway}',
    'apigatewayinsideadmin' => '${mc_api_gatewayadmin}',


    // redis的配置, 根据现场修改
    'redis' => [
        'mode' => '${regcenter_redis_mode}',
        'host' => 'tcp://${regcenter_redis_host}:${regcenter_redis_port}',
        'db'=> ${regcenter_redis_database},
        'password' => '${regcenter_redis_password}'
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];