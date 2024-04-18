#!/bin/bash
#获取当前目录
__current_dir=$(
  cd "$(dirname "$0")"
  pwd
)

###记录日志
function log() {
  message="[MC Log]: $1 "
  echo -e "${message}" 2>&1 | tee -a ${__current_dir}/install.log
}

###异常抛出
function error(){
  RED_COLOR='\E[1;31m'   #红
  RES='\E[0m'
  message="${RED_COLOR}[MC Error]: $1${RES} "
  echo -e "${message}" 2>&1 | tee -a ${__current_dir}/install.log
  exit 1;
}

#获取本地IP
__local_ip=$(hostname -I|cut -d" " -f 1)

###检查环境
# 检查 SELinux 的状态，并关闭
if [ "getenforce" != "Disabled" ];
  then
    setenforce 0
    sed -i 's/^SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
    log "关闭Selinux防火墙"
fi

#关闭防火墙
systemctl stop firewalld
log "关闭firewall防火墙"

#检查系统内核版本
Main_version=`uname -r |awk -F'.' '{print $1}'`
Minor_version=`uname -r |awk -F'.' '{print $2}'`
Patch_version=`uname -r |awk -F'.' '{print $3}'|awk -F'-' '{print $1}'`
Release_version=`uname -r |awk -F'-' '{print $2}'|awk -F'.' '{print $1}'`
if [[ ${Main_version} -lt 3 ]];
  then
    error "内核版本小于3.10.0-1160，无法安装运行MC，请升级系统内核高于此版本"
elif [[ ${Main_version} -eq 3 && ${Minor_version} -lt 10 ]];
  then
    error "内核版本小于3.10.0-1160，无法安装运行MC，请升级系统内核高于此版本"
elif [[ ${Main_version} -eq 3 && ${Minor_version} -eq 10 && ${Patch_version} -eq 0 && ${Release_version} -lt 1160 ]];
  then
    error "内核版本小于3.10.0-1160，无法安装运行MC，请升级系统内核高于此版本"
fi

#离线or在线
while read -p "1.选择在线安装或离线安装？[1-在线，2-离线]" __choice; do
  if [ $__choice -ge 1 -a $__choice -le 2 ]; then
    case "$__choice" in
      1)
        #git
        if which git >/dev/null; then
          log "检测到 Git 已安装，跳过安装步骤"
        else
          yum -y install git
          log "...在线安装 git"
        fi
        #docker
        if which docker >/dev/null; then
          log "检测到 Docker 已安装，跳过安装步骤"
          log "启动 Docker "
          service docker start 2>&1 | tee -a ${__current_dir}/install.log
        else
          log "... 在线安装 docker"
          cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
          rm -rf /etc/yum.repos.d/*.repo
          mv /etc/yum.repos.d/CentOS-Base.repo.bak /etc/yum.repos.d/CentOS-Base.repo
          yum -y update
          curl -fsSL https://get.docker.com -o get-docker.sh 2>&1 | tee -a ${__current_dir}/install.log
          sudo sh get-docker.sh --mirror Aliyun 2>&1 | tee -a ${__current_dir}/install.log
          log "... 启动 docker"
          service docker start 2>&1 | tee -a ${__current_dir}/install.log
          systemctl enable docker.service
        fi
        #docker-compose
        if which docker-compose >/dev/null; then
          log "检测到 Docker Compose 已安装，跳过安装步骤"
        else
          log "... 在线安装 docker-compose"
          curl -L https://get.daocloud.io/docker/compose/releases/download/2.4.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose 2>&1 | tee -a ${__current_dir}/install.log
          chmod +x /usr/local/bin/docker-compose
          ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
        fi
        ;;
      2) 
        #docker
        if which docker >/dev/null; then
          log "检测到 Docker 已安装"
        else
          error "Docker 未正常安装，请先安装 Docker 后再次执行本脚本"
        fi
        #docker-compose
        if which docker-compose >/dev/null; then
          log "检测到 Docker Compose 已安装"
        else
          error "Docker Compose未正常安装，请先安装 Docker Compose V2.4.1后再次执行本脚本"
        fi
        ;;
    esac
    break
  else
    echo "输入错误请重新输入"
  fi
done

####开始安装
log "开始安装MC"
###获取资源包存放路径
read -p "请输入资源包存放路径（绝对路径），不输入默认为当前路径：" MC_RESOURCE_PATH
if [ ! -n "$MC_RESOURCE_PATH" ];then
  MC_RESOURCE_PATH=${__current_dir}
fi
log "资源包存放路径为 ${MC_RESOURCE_PATH}"

###指定安装目录
read -p "请输入安装目录（绝对路径），不输入默认为当前路径：" MC_INSTALL_PATH
if [ ! -n "$MC_INSTALL_PATH" ];then
  MC_INSTALL_PATH=${__current_dir}
fi
cd ${MC_INSTALL_PATH}
mkdir mc_stack/
log "安装路径为 ${MC_INSTALL_PATH}/mc_stack"

###判断获取资源包并解压
cd ${MC_RESOURCE_PATH}
log "获取资源包并解压"

while read -p "2.选择在线安装或离线安装？[1-在线，2-离线]" __choice; do
  if [ $__choice -ge 1 -a $__choice -le 2 ]; then
    case "$__choice" in
      1)
        git_url=git@code.aliyun.com
        read -p "请输入docker私有仓库公网IP:" MC_REMOTE_IP
        images_url=$MC_REMOTE_IP:5000/v2/_catalog
        #检测Git
        for i in {1..3}
        do
          log "检测 ${git_url} ... ${i} "
          curl -m 5 -kIs ${git_url} >/dev/null
          if [ $? != 0 ];then
            log "第${i}次结果：failed"
            success="false"
            break
          else
            success="true"
            log "检测成功"
          fi
        done
        if [ ${success} == "false" ];then
          error "git地址连接失败，请切换为离线安装"
          break
        fi

        #检测镜像仓库地址
        for i in {1..3}
        do
          log "检测 ${images_url} ... ${i} "
          curl -m 5 -kIs http://${images_url} >/dev/null
          if [ $? != 0 ];then
            log "第${i}次结果：failed"
            success="false"
            break
          else
            success="true"
            log "检测成功"
          fi
        done
        if [ ${success} == "false" ];then
          error "镜像仓库地址连接失败，请切换为离线安装"
          break
        fi

        #配置docker私有仓库
        cat /dev/null > /etc/docker/daemon.json
        cat > /etc/docker/daemon.json <<-'EOF'
        { 
          "insecure-registries":["1.1.1.1:5000"]
  
        }
        EOF
        sed -i "s/1.1.1.1/${MC_REMOTE_IP}/g" /etc/docker/daemon.json
        #重新加载daemon并重启docker
        sudo systemctl daemon-reload && sudo systemctl restart docker &> /dev/null

        #获取映射文件目录
        log "获取volume"
        git clone --depth 1 --branch master ${git_url}:mc-backend/docker_volume.git ${MC_INSTALL_PATH}/mc_stack
        
        #获取项目代码
        log "获取项目代码"
        mkdir ${MC_INSTALL_PATH}/mc_stack/frontends
        mkdir ${MC_INSTALL_PATH}/mc_stack/backends
        for app in $(ls apps);
          do
            if [ -d ${app} ];then
              git clone --depth 1 --branch master ${git_url}:${app}-devops/frontend.git ${MC_INSTALL_PATH}/mc_stack/frontends
              git clone --depth 1 --branch master ${git_url}:${app}-devops/backend.git ${MC_INSTALL_PATH}/mc_stack/backends      
            fi
          done
        ;;
      2) 
        #解压镜像
        MC_REMOTE_IP=192.168.1.238
        images_package=$(ls -p | grep "images.tar")
        if [ ! -f "$images_package" ]; then
          error "未检测到镜像包，请上传镜像包到${MC_RESOURCE_PATH}目录下后再次执行本脚本"
        else
          tar -zxvf ${images_package}
        #加载镜像
          for image in $(ls docker_images);
            do
              log "加载镜像images/$image"
              docker load -i docker_images/$image 2>&1 | tee -a ${__current_dir}/install.log  
            done
        fi
        
        #解压项目代码
        project_package=$(ls -p | grep "project" | grep "tar")
        if [ ! -f "$project_package" ]; then
          error "未检测到代码包，请上传代码包到${MC_RESOURCE_PATH}目录下后再次执行本脚本"
        else
          mkdir ${MC_INSTALL_PATH}/mc_stack/frontends
          mkdir ${MC_INSTALL_PATH}/mc_stack/backends
          tar -zxvf ${project_package}
          for app in $(ls project_packages);
            do
              if [ -d project_packages/$app ];then
                cp project_packages/${app}/frontend/* ${MC_INSTALL_PATH}/mc_stack/frontends
                cp project_packages/${app}/backend/* ${MC_INSTALL_PATH}/mc_stack/backends      
              fi
            done
          for fronapp in $(ls ${MC_INSTALL_PATH}/mc_stack/frontends);
            do
              if [ -f ${MC_INSTALL_PATH}/mc_stack/frontends/$fronapp ];then
                tar -zxvf ${MC_INSTALL_PATH}/mc_stack/frontends/${fronapp} -C ${MC_INSTALL_PATH}/mc_stack/frontends
                rm -rf ${MC_INSTALL_PATH}/mc_stack/frontends/${fronapp}
              fi
            done
          for backapp in $(ls ${MC_INSTALL_PATH}/mc_stack/backends);
            do
              if [ -f ${MC_INSTALL_PATH}/mc_stack/backends/$backapp ];then
                tar -zxvf ${MC_INSTALL_PATH}/mc_stack/backends/${backapp} -C ${MC_INSTALL_PATH}/mc_stack/backends
                rm -rf ${MC_INSTALL_PATH}/mc_stack/backends/${backapp}
              fi
            done
        fi

        #映射文件及结构
        volume_package=$(ls -p | grep "volume" |grep "tar")
        if [ ! -f "$volume_package" ]; then
          error "未检测到映射包，请上传映射包到${MC_RESOURCE_PATH}目录下后再次执行本脚本"
        else
          #mkdir  ${MC_INSTALL_PATH}/mc_stack/docker_volume
          tar -zxvf ${volume_package} -C ${MC_INSTALL_PATH}/mc_stack
        fi

        #rm -rf *.tar.gz，升级时删除
        ;;
    esac
    break
  else
    echo "输入错误请重新输入"
  fi
done

###修改配置，后期可优化成可交互式
# 将配置信息存储到安装目录的环境变量配置文件中
echo '' >> ${MC_RESOURCE_PATH}/compose/.env
sed -i "s|^MC_INSTALL_PATH=.*|MC_INSTALL_PATH=${MC_INSTALL_PATH}|g" ${MC_RESOURCE_PATH}/mc.conf
echo "MC_INSTALL_PATH=${MC_INSTALL_PATH}" > ~/.mcrc
sed -i "s|^MC_RESOURCE_PATH=.*|MC_RESOURCE_PATH=${MC_RESOURCE_PATH}|g" ${MC_RESOURCE_PATH}/mc.conf
sed -i "s|^MC_RESOURCE_PATH=.*|${MC_RESOURCE_PATH}|g" ${MC_RESOURCE_PATH}/docker_run.sh
sed -i "s|^MC_HOST_IP=.*|MC_HOST_IP=${__local_ip}|g" ${MC_RESOURCE_PATH}/mc.conf
sed -i "s|^MC_REMOTE_IP=.*|MC_REMOTE_IP=${MC_REMOTE_IP}|g" ${MC_RESOURCE_PATH}/mc.conf
sed -i "s/1.1.1.1/${__local_ip}/g" ${MC_RESOURCE_PATH}/mc.conf
cp -f ${MC_RESOURCE_PATH}/mc.conf ${MC_INSTALL_PATH}/mc_stack/docker_volume/install.conf.example
# 通过加载环境变量的方式保留已修改的配置项，仅添加新增的配置项
if [ -e ${MC_RESOURCE_PATH}/compose/.env ];then
  rm -rf ${MC_RESOURCE_PATH}/compose/.env
fi
cat ${MC_RESOURCE_PATH}/mc.conf |grep -vE '^$|#' >>${MC_RESOURCE_PATH}/compose/.env

#修改前端配置
log "修改配置"
for front_app in $(ls ${MC_INSTALL_PATH}/mc_stack/frontends);
  do
    if [ -d ${MC_INSTALL_PATH}/mc_stack/frontends/$front_app ];then
      cp -f ${MC_RESOURCE_PATH}/install/apps_config/config.json ${MC_INSTALL_PATH}/mc_stack/frontends/${front_app}/assets/config.json
      sed -i "s/1.1.1.1/${__local_ip}/g" ${MC_INSTALL_PATH}/mc_stack/frontends/${front_app}/assets/config.json
    fi
  done
log "前端配置修改完成"

#修改后端配置
declare -A map
OLD_IFS=$IFS
IFS=$'\n' # 定义分割符
for common_env in `cat ${MC_RESOURCE_PATH}/mc.conf |grep -vE '^$|#'`
{
    #字符串截取：从左至右第一个'='之前的内容
   # echo ${x%%=*}
    #字符串截取：从左至右第一个'='之后的内容
   # echo ${x#*=}  
    map[${common_env%%=*}]="${common_env#*=}"
}

for common_key in ${!map[*]};do
 sed -i "s|\${$common_key}|${map[$common_key]}|g" ${MC_RESOURCE_PATH}/install/apps_config/app_env
done

for back_app in $(ls apps_config);
  do
    if [ -d apps_config/$back_app ];then
      cp -f ${MC_RESOURCE_PATH}/apps_config/${back_app}/nginx.conf ${MC_INSTALL_PATH}/mc_stack/docker_volume/web_server/conf/nginxs/${back_app}_nginx.conf
      cp -f ${MC_RESOURCE_PATH}/apps_config/${back_app}/dependencies.php ${MC_INSTALL_PATH}/mc_stack/backends/${back_app}/config/dependencies.php
      cp -f ${MC_RESOURCE_PATH}/apps_config/${back_app}/env.php ${MC_INSTALL_PATH}/mc_stack/backends/${back_app}/config/env.php
      unset map && declare -A map
      for config_item in `cat ${MC_RESOURCE_PATH}/apps_config/app_env |grep -vE '^$|#|]$'`
      { 
        map[${config_item%%=*}]="${config_item#*=}"
      }

      for config_key in ${!map[*]};do
        sed -i "s|\${$config_key}|${map[$config_key]}|g" ${MC_INSTALL_PATH}/mc_stack/docker_volume/web_server/conf/nginxs/${back_app}_nginx.conf
        sed -i "s|\${$config_key}|${map[$config_key]}|g" ${MC_INSTALL_PATH}/mc_stack/backends/${back_app}/config/dependencies.php
        sed -i "s|\${$config_key}|${map[$config_key]}|g" ${MC_INSTALL_PATH}/mc_stack/backends/${back_app}/config/env.php
      done
    fi
  done

for dbname in `cat ${MC_RESOURCE_PATH}/apps_config/app_env |grep 'mysql_dbname'`;do
  echo "CREATE DATABASE IF NOT EXISTS ${dbname#*=} CHARSET=UTF8MB4;" >> ${MC_INSTALL_PATH}/mc_stack/docker_volume/data-init/mysql-init.sql
done

sed -i "s/1.1.1.1/${__local_ip}/g" ${MC_INSTALL_PATH}/mc_stack/docker_volume/web_server/conf/nginx.conf
log "后端配置修改完成"

###首次启动
#获取机器码
log "获取机器码"
mac_addr=$(cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address)
if [ -z $mac_addr ];then
  log "未获取到机器码，检查网络配置后执行get_mac.sh脚本"
fi
echo ${mac_addr} > ${MC_INSTALL_PATH}/mc_stack/MACHINECODE

#启动服务
IFS=$OLD_IFS
if [ -e ${MC_RESOURCE_PATH}/compose/compose_files ];then
  rm -rf ${MC_RESOURCE_PATH}/compose/compose_files
fi
echo -n '' >> ${MC_RESOURCE_PATH}/compose/compose_files
for file in $(ls ${MC_RESOURCE_PATH}/compose );
  do
    if [ "${file##*.}"x = "yml"x ];then
      echo -n ' -f ' ${MC_RESOURCE_PATH}/compose/${file} >> ${MC_RESOURCE_PATH}/compose/compose_files
    fi 
  done
log "启动容器"
compose_filepath=$MC_RESOURCE_PATH/compose/compose_files
docker-compose $(cat $compose_filepath) -p mcstack up -d  

#验证容器启动
if [ -z $(docker-compose $(cat $compose_filepath) -p mcstack ps |grep -v 'migra'|grep -i exit) ];
  then 
    log "服务容器启动成功"
else 
  error "$(docker-compose $(cat $compose_filepath) -p mcstack ps |grep -i exit|grep -v "migra"|awk -F' ' '{print $1}') 服务容器启动失败，请检查相关文件后重试"
fi

#初始化
log "容器内服务完全启动后方可开始初始化基础数据，过程较长需等待3分钟左右"
sleep 180
log "初始化数据"
chmod +x init.sh
sh init.sh all

#验证MC各应用部署成功
for back_app in $(ls ${MC_INSTALL_PATH}/mc_stack/backends);
  do
    if [ -d ${MC_INSTALL_PATH}/mc_stack/backends/${back_app} ] && [ ${back_app} != "regcenter" ];then
      pre_url=$(cat ${MC_INSTALL_PATH}/mc_stack/backends/${back_app}/config/env.php |awk -F'backend_url' '{print $2}' |grep -v '^$' | sed "s/'//g" |awk -F'=> ' '{print $2}' |awk -F',' '{print $1}')
      app_url=${pre_url}/${back_app}/api/index/site/info
      for i in {1..3}
      do
        log "检测 ${back_app}服务 ... ${i} "
        #todo 检测200
        body=$(curl -m 5 -ks "${app_url}")
        successStr='"status":0'
        if [[ $body != *$successStr* ]] ; then
          log "第${i}次结果：failed"
          success="false"
          break
        else
          success="true"
          log "${back_app}服务启动成功"
          break
        fi
      done
      if [ ${success} == "false" ];then
        error "${back_app}服务启动失败，请检查并修改对应配置后再次执行本脚本"
        break
      fi      
    fi
  done

#消息引擎
log "启动消息引擎"
chmod +x ${MC_INSTALL_PATH}/mc_stack/backends/mns/console/messenger
sh ${MC_INSTALL_PATH}/mc_stack/backends/mns/console/messenger.sh start
if [ "sh ${MC_INSTALL_PATH}/mc_stack/backends/mns/console/messenger.sh check |grep running 2> /dev/null)" != "" ];
  then
    log "消息引擎启动成功"
else
  log "消息引擎启动失败，请稍后检查配置并在${MC_INSTALL_PATH}/mc_stack/backends/mns/console目录下执行sh messenger.sh start命令"
fi

###部署完成
echo -e "======================= 安装完成 =======================\n" 2>&1 | tee -a ${__current_dir}/install.log
echo -e "机器码为${mac_addr}，请将该机器码复制并提供给商务人员获取license\n" 2>&1 | tee -a ${__current_dir}/install.log
echo -e "请通过以下方式访问:\n URL: http://${__local_ip}:21308\n 用户名: admin\n 初始密码: MC-Stack@123" 2>&1 | tee -a ${__current_dir}/install.log
echo -e "您可以使用命令 'sh docker_run.sh status' 检查服务运行情况.\n" 2>&1 | tee -a ${__current_dir}/install.log
