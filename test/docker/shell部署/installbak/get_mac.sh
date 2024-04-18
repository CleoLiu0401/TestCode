#!/bin/bash
mac_addr=$(cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address)
if [ -z $mac_addr ];then
  echo "未获取到机器码，检查网络配置后再次执行本脚本"
fi
echo ${mac_addr} >> /test/mc_stack/MACHINECODE
