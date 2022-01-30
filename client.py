import socket
import sys

PORT = 65432
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

program_name = sys.argv[0]
HOST = sys.argv[1]
PORT = int(sys.argv[2])
fileName = sys.argv[3]


@staticmethod
def connectTcp(host: str, port: int, fileName: str):  # task 6
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, port))
            return True
    except:
        return False
