<?php
// mc_storage环境
return [

    // 配置注册中心地址, 根据现场修改
    'regcenter' => 'http://${regcenter_nginx_host}:21316',

     // 前端入口
    'frontend_url' => 'http://${storage_nginx_host}:21308/storage',

    // 后端入口
    'backend_url' => 'http://${storage_nginx_host}:21317',

    // 路径配置
    'path' => [
        // 所在主机地址
        'host' => '${storage_local_addr}',
        // 文件存储方式
        'driver' => 'local',
        // 数据存储的文件夹
        'dirs' => ['img', 'text', 'excel', 'doc', 'zip', 'voice', 'video'],
    ],
    //存储方式设置
    'driver' => [
         'local' => [
             // 数据存储路径
             'data' => '/opt/mc_stack/data',
             // url配置
             'url' => '/storage/data',
             // 类名
             'class' => 'api\client\LocalFileClient'
         ],
         'fastdfs' => [
              // 数据存储路径
              'data' => '/opt/mc_stack/fastdfs_data/data',
              // url配置
              'url' => '/storage/fastdfs',
              // fastdfs分组名称
              'class' => 'api\client\FastdfsFileClient',
              // 类名
              'group' => 'group1'
         ]
    ],
    'xj_domain' => 'http://dev.xj.hsip.gov.cn',
];