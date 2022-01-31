import sys
import socket
from sys import argv



def checkMSG(string):
    userMSG = string
    b = b""
    while b != userMSG:
        b += sock.recv(3333)

        if b == userMSG:
            break

        if userMSG.find(b) != 0:
            b = b""


def sendMSG(filename, sock):
    try:
        fp = open(filename, "rb")

    except FileNotFoundError:
        print(f"{filename} not found, try again.")
        quit()

    else:
        while True:
            chunk = fp.read(10000)
            if chunk:
                sock.send(chunk)
            else:
                fp.close()
                break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if (len(argv) != 4):
    print("Incorrect parameter entered")
    sys.exit(1)

pname, hostname, port, filename = argv

if int(port) < 3333 or int(port) > 65535:
    print("Incorrect port. Stay within parameters")
    quit(1)

sock.settimeout(10)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10101)

try:
    sock.connect((hostname, int((port))))

    checkMSG(b"accio\r\n")

    sock.send(b"confirm-accio\r\n")

    checkMSG(b"accio\r\n")

    sock.send(b"confirm-accio-again\r\n")

    response = sock.send(b"\r\n")

    sendMSG(filename, sock)
    sock.close()

except socket.error:
    print("Runtime Error")
    sys.stderr.write("ERROR: ")
    sys.exit(1)

sys.exit(0)










