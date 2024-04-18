import logging
import json
from json import JSONDecodeError
from websocket import create_connection
logger = logging.getLogger(__name__)


class WebsocketUtil:

    def conn(self, uri, timeout=3):
        """
        连接web服务器
        :param uri: 服务的url
        :param timeout: 超时时间
        :return:
        """
        self.wss = create_connection(uri, timeout=timeout)

    def send(self, message):
        """
        发送请求数据体
        :param message: 待发送的数据信息
        :return:
        """
        if not isinstance(message, str):
            message = json.dumps(message)
        return self.wss.send(message)

    def load_json(self, base_str):
        """
        进行数据体的处理
        :param base_str: 待处理的数据体
        :return:
        """
        if isinstance(base_str, str):
            try:
                res = json.loads(base_str)
                return self.load_json(res)
            except JSONDecodeError:
                return base_str
        elif isinstance(base_str, list):
            res = []
            for i in base_str:
                res.append(self.load_json(i))
            return res
        elif isinstance(base_str, dict):
            for key, value in base_str.items():
                base_str[key] = self.load_json(value)
            return base_str
        return base_str

    def recv(self, timeout=3):
        """
        接收数据体信息，并调用数据体处理方法处理响应体
        :param timeout: 超时时间
        :return:
        """
        if isinstance(timeout, dict):
            timeout = timeout["timeout"]
        try:
            self.settimeout(timeout)
            recv_json = self.wss.recv()
            all_json_recv = self.load_json(recv_json)
            self._set_response(all_json_recv)
            return all_json_recv
        except WebSocketTimeoutException:
            logger.error(f"已经超过{timeout}秒没有接收数据啦")

    def settimeout(self, timeout):
        """
        设置超时时间
        :param timeout: 超时时间
        :return:
        """
        self.wss.settimeout(timeout)

    def recv_all(self, timeout=3):
        """
        接收多个数据体信息，并调用数据体处理方法处理响应体
        :param timeout: 超时时间
        :return:
        """
        if isinstance(timeout, dict):
            timeout = timeout["timeout"]
        recv_list = []
        while True:
            try:
                self.settimeout(timeout)
                recv_json = self.wss.recv()
                all_json_recv = self.load_json(recv_json)
                recv_list.append(all_json_recv)
                logger.info(f"all::::: {all_json_recv}")
            except WebSocketTimeoutException:
                logger.error(f"已经超过{timeout}秒没有接收数据啦")
                break
        self._set_response(recv_list)
        return recv_list

    def close(self):
        """
        关闭连接
        :return:
        """
        return self.wss.close()

    def _set_response(self, response):
        self.response = response

    def _get_response(self) -> list:
        return self.response
