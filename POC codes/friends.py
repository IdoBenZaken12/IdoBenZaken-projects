import socket

SERVER_IP = "54.187.16.171"
SERVER_PORT = 1336
LOGIN_MSG = '100#{gli&&er}{"user_name":"king098","password":"123456789","enable_push_notifications":true}##'
##send the login msg to the server
CHECKSUM_MSG = '110#{gli&&er}1063##'#sent the checksum Authentication of the user to the server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#you can use to find the id my last program ReplyInPrivetMode.py
try:
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    # Connecting to remote computer
    print("Sending login info.....")
    sock.sendall(LOGIN_MSG.encode())#sent the login info msg to the server
    response = sock.recv(1024).decode()#get the server respons
    if "105#" in response:#check if the accept is in the respons
        print("Sending the checksum - ")
        sock.sendall(CHECKSUM_MSG.encode())#sent to the server the user checksum
        response = sock.recv(1024).decode()#get the respons for the checksum
    else:#if the login dosent work
        print("login error close the connection")
        sock.close()#close the connection
    if "115#" in response:#if the checksum is good
        print("Authentication approved ")
        id = input("please enter the id of the user as is: ")
        print("sending request.....")
        req_msg = '410#{gli&&er}[42433,'+id+']##'
        sock.sendall(req_msg.encode())#sent to the server the friend request
        response = sock.recv(1024).decode()#get the respons for the user serch
    if "419#" not in response:#check if we dont got error
        accept_msg = '420#{gli&&er}[42433,'+id+']##'
        sock.sendall(accept_msg.encode())#sent to the server the accept
        response = sock.recv(1024).decode()#get the respons for the user serch
        print("the friend request was accepted")
    else:
        print("request error")



finally:
    print("Closing socket")
    sock.close()
