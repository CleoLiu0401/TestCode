#!/bin/bash
compose_filepath=$MC_RESOURCE_PATH/install/compose/compose_files
if [  $# -lt 1 ]; then
     echo "Usage: $0 {start|stop|restart|status}" >&2
     exit 1
fi

if [ ! -f "$compose_filepath" ]; then
	echo "未检测到compose文件，请切换到正确目录执行"
	exit 1
fi

start() {
    #docker-compose $(cat compose_files) -p mcstack up -d  >/dev/null 2>&1 &
    docker-compose $(cat $compose_filepath) -p mcstack start 2>&1 | tee -a ${__current_dir}/run.log
}

stop() {
    docker-compose $(cat $compose_filepath) -p mcstack stop 2>&1 | tee -a ${__current_dir}/run.log
}

restart() {
    docker-compose $(cat $compose_filepath) -p mcstack restart 2>&1 | tee -a ${__current_dir}/run.log
}

status() {
    docker-compose $(cat $compose_filepath) -p mcstack ps |grep -v 'migra' 2>&1 | tee -a ${__current_dir}/run.log
}

case $1 in
  (start)
     start
     ;;
  (stop)
     stop
     ;;
  (restart)
     restart
     ;;
  (status)
     status
     ;;
  (*)
     echo "Error command"
     echo "$usage"
     ;;
esac