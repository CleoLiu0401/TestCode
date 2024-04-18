#!/bin/bash

usage() {
  echo "Usage:$0 [args]"
  echo "  all: means to initialize all apps"
  echo "  portal: means to initialize mc_portal"
  echo "  ucenter: means to initialize mc_ucenter"
  echo "  itsm: means to initialize mc_itsm"
  echo "  iam: means to initialize mc_iam"
  echo "  audit: means to initialize mc_audit"
  echo "  storage: means to initialize mc_storage"
}

if [ -z "$1" ];then
  usage
  exit 0
fi

for arg in $*
do
  case $arg in
    all)
        echo "initialize all apps..."
        docker exec mc_php php /opt/mc_stack/backends/regcenter/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/portal/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/iam/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/storage/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/mns/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register iam
        docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register iam
        docker exec -it mc_php php /opt/mc_stack/backends/portal/yii site/refresh-application
        docker exec -it mc_php php /opt/mc_stack/backends/portal/yii site/refresh-panel
        ;;
    mns)
      echo "initialize mc_mns..."
      docker exec mc_php php /opt/mc_stack/backends/mns/yii site/init
      docker exec mc_php php /opt/mc_stack/backends/mns/yii site/register iam
      ;;
    cmdb)
      echo "initialize mc_cmdb..."
      docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/init
      docker exec mc_php php /opt/mc_stack/backends/cmdb/yii site/register iam
      ;;
    itsm)
      echo "initialize mc_itsm..."
      docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/init
      docker exec mc_php php /opt/mc_stack/backends/itsm/yii site/register iam
      ;;
    ucenter)
        echo "initialize mc_ucenter..."
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/ucenter/yii site/register iam
        ;;
    iam)
        echo "initialize mc_iam..."
        docker exec mc_php php /opt/mc_stack/backends/iam/yii site/init
        ;;
    audit)
         echo "initialize mc_audit..."
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/audit/yii site/register iam
        ;;
    ams)
         echo "initialize mc_ams..."
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/init
        docker exec mc_php php /opt/mc_stack/backends/ams/yii site/register iam
        ;;
   storage)
        echo "initialize mc_storage..."
        docker exec mc_php php /opt/mc_stack/backends/storage/yii site/init
    ;;
   portal)
        echo "initialize mc_portal..."
        docker exec mc_php php /opt/mc_stack/backends/portal/yii site/init
    ;;
  regcenter)
        echo "initialize mc_regcenter..."
        docker exec mc_php php /opt/mc_stack/backends/regcenter/yii site/init
    ;;
    *)
        echo "Error Params!!!"
        usage
        exit 1
        ;;
  esac
done
