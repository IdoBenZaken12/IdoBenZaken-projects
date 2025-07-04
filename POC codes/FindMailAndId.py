import socket

SERVER_IP = "54.187.16.171"
SERVER_PORT = 1336
LOGIN_MSG = '100#{gli&&er}{"user_name":"IdoBenZaken","password":"123456789","enable_push_notifications":true}##'
##send the login msg to the server
CHECKSUM_MSG = '110#{gli&&er}1543##'  # sent the checksum Authentication of the user to the server
OPTION_ONE = 1
OPTION_TWO = 2
ADD_TO_START_ID = 4
MINUS_TO_END_ID = 2
ADD_TO_START_MAIL = 6
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    # Connecting to remote computer
    print("Sending login info.....")
    sock.sendall(LOGIN_MSG.encode())  # sent the login info msg to the server
    response = sock.recv(1024).decode()  # get the server respons
    if "105#" in response:  # check if the accept is in the respons
        print("Sending the checksum - ")
        sock.sendall(CHECKSUM_MSG.encode())  # sent to the server the user checksum
        response = sock.recv(1024).decode()  # get the respons for the checksum
    else:  # if the login dosent work
        print("login error close the connection")
        sock.close()  # close the connection
    if "115#" in response:  # if the checksum is good
        print("Authentication approved ")
        name = input("please enter the name of the user as is: ")
        msg = '300#{gli&&er}{"search_type":"SIMPLE","search_entry":"' + name + '"}##'
        sock.sendall(msg.encode())  # sent to the server the user name
        response = sock.recv(1024).decode()  # get the respons for the user serch
        print(response)
        print("please make a choice:\n1 - get the user Id\n2 - get the user mail\n")  # print menu to the user
        choice = int(input("enter your choice:"))  # get the user choice
        name_index = response.index('"screen_name":"' + name + '"')
        response = response[name_index:]
    if choice == OPTION_ONE:
        start_index = response.index('id')  # get the index of the id parameter
        start_index += ADD_TO_START_ID  # add to the index to be the start of the id
        end_index = response.index("mail")  # get the index of the after parameter
        end_index -= MINUS_TO_END_ID  # minus to the index to be the end of the id
        print("the id of " + name + " is " + response[start_index:end_index])  # print the id
    elif choice == OPTION_TWO:
        start_index = response.index('mail')  # get the index of the mail parameter
        start_index += ADD_TO_START_MAIL  # add to the index to be the start of the mail with the "
        end_index = response.index('"}')  # get the index of the end of the mail
        print("the mail of " + name + " is " + response[start_index:end_index])  # print the mail



finally:
    print("Closing socket")
    sock.close()
