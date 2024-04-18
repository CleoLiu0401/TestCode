import socket
import yaml

with open("../config/tcp_config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
host = data.get("host")
port = data.get("port")
s = socket.socket()
s.connect((host, port))
print(s.recv(1024).decode())
s.close()
