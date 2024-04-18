#!/bin/bash
# 权限注册

usage() {
  echo "Usage:$0 [args]"
  echo "  all: means to register mc_ucenter mc_itsm mc_audit"
  echo "  portal: means to register mc_portal"
  echo "  ucenter: means to register mc_ucenter"
  echo "  itsm: means to register mc_itsm"
  echo "  iam: means to register mc_iam"
  echo "  audit: means to register mc_audit"
  echo "  storage: means to register mc_storage"
  echo "  cmdb: means to register mc_cmdb"
}

if [ -z "$1" ];then
  usage
  exit 0
fi
# php yii site/register iam
for arg in $*
do
  case $arg in
    all)
        echo "register all apps..."
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register iam
        ;;
    mns)
      echo "register mc_mns..."
      docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register iam
      ;;
    cmdb)
      echo "register mc_cmdb..."
      docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register iam
      ;;
    itsm)
      echo "register mc_itsm..."
      docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register iam
      ;;
    ucenter)
        echo "register mc_ucenter..."
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register iam
        ;;
    iam)
        echo "register mc_iam..."
        docker exec mc_php php /opt/mc_stack/backends/iam/yii site/register iam
        ;;
    audit)
        echo "register mc_audit..."
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register iam
        ;;
   storage)
        echo "register mc_storage..."
        docker exec mc_php php /opt/mc_stack/backends/storage/yii site/register iam
    ;;
   portal)
        echo "register mc_portal..."
        docker exec mc_php php /opt/mc_stack/backends/portal/yii site/register iam
    ;;
   ams)
        echo "register mc_ams..."
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register iam
    ;;
    *)
        echo "Error Params!!!"
        usage
        exit 1
        ;;
  esac
done


