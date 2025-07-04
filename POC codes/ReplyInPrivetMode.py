import socket

SERVER_IP = "54.187.16.171"
SERVER_PORT = 1336
LOGIN_MSG = '100#{gli&&er}{"user_name":"IdoBenZaken","password":"123456789","enable_push_notifications":true}##'
CHECKSUM_MSG = '110#{gli&&er}1543##'


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        content = input("please enter the msg that you want to send to the privet user: ")
        privet_msg = '650#{gli&&er}{"glit_id":44225,"user_id":40995,"user_screen_name":"Ido ben zaken","id":-1,"content":"'+content+'","date":"2024-06-17T11:25:05.841Z"}##'
        sock.sendall(privet_msg.encode())#sent to the server the user name
        response = sock.recv(1024).decode()#get the respons for the user serch '+content+'
    if "655#" in response:
        print("the message has been sent check the app ")

    #the privet account is username - tomer123 password - 123456789
finally:
    print("Closing socket")
    sock.close()
