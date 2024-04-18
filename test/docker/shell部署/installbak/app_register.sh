#!/bin/bash
# 应用注册

usage() {
  echo "Usage:$0 [args]"
  echo "  all: means to register all apps"
  echo "  portal: means to register mc_portal"
  echo "  ucenter: means to register mc_ucenter"
  echo "  itsm: means to register mc_itsm"
  echo "  iam: means to register mc_iam"
  echo "  audit: means to register mc_audit"
  echo "  storage: means to register mc_storage"
  echo "  cmdb: means to register mc_cmdb"
  echo "  ams: means to register mc_ams"
}

if [ -z "$1" ];then
  usage
  exit 0
fi
# php yii site/register app
for arg in $*
do
  case $arg in
    all)
        echo "register all apps..."
        docker exec mc_php php /opt/mc_stack/backends/portal/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/iam/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/storage/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register app
        docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register app
        ;;
    mns)
      echo "register mc_mns..."
      docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register app
      ;;
    ams)
      echo "register mc_ams..."
      docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register app
      ;;
    cmdb)
      echo "register mc_cmdb..."
      docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register app
      ;;
    itsm)
      echo "register mc_itsm..."
      docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register app
      ;;
    ucenter)
        echo "register mc_ucenter..."
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register app
        ;;
    iam)
        echo "register mc_iam..."
        docker exec mc_php php /opt/mc_stack/backends/iam/yii site/register app
        ;;
    audit)
        echo "register mc_audit..."
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register app
        ;;
   storage)
        echo "register mc_storage..."
        docker exec mc_php php /opt/mc_stack/backends/storage/yii site/register app
    ;;
   portal)
        echo "register mc_portal..."
        docker exec mc_php php /opt/mc_stack/backends/portal/yii site/register app
    ;;
    *)
        echo "Error Params!!!"
        usage
        exit 1
        ;;
  esac
done


