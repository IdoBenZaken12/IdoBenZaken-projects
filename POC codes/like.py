import socket
#the liked user is joyha for checking 
SERVER_IP = "54.187.16.171"#the server ip 
SERVER_PORT = 1336#the server port 
LOGIN_MSG = '100#{gli&&er}{"user_name":"IdoBenZaken","password":"123456789","enable_push_notifications":true}##'#send the login msg to the server 
CHECKSUM_MSG = '110#{gli&&er}1543##'#sent the checksum Authentication of the user to the server 
LIKE_MSG = '710#{gli&&er}{"glit_id":43536,"user_id":40995,"user_screen_name":"Ido ben zaken","id":-1}##'#the like msg to the joyha user 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connecting to remote computer
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)

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
        print("sending the likes to the id 42569")
        for i in range(1,6):#the loop that sending 5 likes to joyha in id 42569
            sock.sendall(LIKE_MSG.encode())#sent the request
            response = sock.recv(1024).decode()
            print("the " + str(i) + " like was sent")
    else:
        print("checksum error close the connection")#if the checksum is not good
        sock.close()#close the connection 

finally:
    sock.close()
