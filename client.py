import sys
import socket
from sys import argv

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def checkMSG(string):
    userMSG = ""
    b = b""
    while b != userMSG:
        b += sock.recv(3333)

        if b == userMSG:
            break

        if userMSG.find(b) != 0:
            b = b""


def sendMSG(fname, sock):
    try:
        fp = open(fname, "rb")

    except FileNotFoundError:
        print(f"{fname} not found, try again.")
        quit()

    else:
        while True:
            msg = fp.read(10000)
            if msg:
                sock.send(msg)
            else:
                fp.close()
                break

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

    sock.send()

    sock.send(b"confirm-accio\r\n")

    checkMSG(b"accio\r\n")

    sock.send(b"confirm-accio-again\r\n")

    response = sock.send(b"\r\n")

    sendMSG(filename, sock)
    sock.close()

except socket.error:
    sys.stderr.write("ERROR: ")
    sys.exit(1)




