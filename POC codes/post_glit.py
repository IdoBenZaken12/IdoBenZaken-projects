import socket

SERVER_IP = "54.187.16.171"#the server ip 
SERVER_PORT = 1336#the server port 
LOGIN_MSG = '100#{gli&&er}{"user_name":"IdoBenZaken","password":"123456789","enable_push_notifications":true}##'
##send the login msg to the server 
CHECKSUM_MSG = '110#{gli&&er}1543##'#sent the checksum Authentication of the user to the server 
BLACK_BACKROUND = '550#{gli&&er}{"feed_owner_id":40995,"publisher_id":40995,"publisher_screen_name":"Ido ben zaken","publisher_avatar":"im5","background_color":"Black","date":"2024-06-14T17:43:49.671Z","content":"test","font_color":"black","id":-1}##'#the black background request to the server
WHITE_TEXT = '550#{gli&&er}{"feed_owner_id":40995,"publisher_id":40995,"publisher_screen_name":"Ido ben zaken","publisher_avatar":"im5","background_color":"White","date":"2024-06-14T17:43:49.671Z","content":"test","font_color":"White","id":-1}##'#the white text request to the server

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
        print("please make a choice:\n1 - Black backround\n2 - White text\n3 - custom ")#print menu to the user
        choice = int(input("enter your choice:"))#get the user choice 
    else:#if the checksum is not good
        print("checksum error close the connection")
        sock.close()#close the connection
    if choice == 1:#if the user choose black background
        sock.sendall(BLACK_BACKROUND.encode())#send the request to the server 
    elif choice == 2:#if the user choose white text option
        sock.sendall(WHITE_TEXT.encode())#send the request to the server 
    elif choice == 3:
        custom_choice = input(
            'make a choice:\n"background" - change the backround color\n"text" - change the text color\nenter your choice:')#print the menu to the user and get his choice 
        if custom_choice == "background":#if the user choose to change the background
            back_color = input("insert the color that you want: ")#get the color of the background
            msg = '550#{gli&&er}{"feed_owner_id":40995,"publisher_id":40995,"publisher_screen_name":"Ido ben zaken","publisher_avatar":"im5","background_color":"' + back_color + '","date":"2024-06-14T17:43:49.671Z","content":"test","font_color":"black","id":-1}##'#CREATE THE MSG TO THE SERVER 
            sock.sendall(msg.encode())#send the request to the server with the color that the user choose
        elif custom_choice == "text":#if the user choose to change the text color 
            text_color = input("insert the color that you want: ")#get the color of the text
            msg = '550#{gli&&er}{"feed_owner_id":40995,"publisher_id":40995,"publisher_screen_name":"Ido ben zaken","publisher_avatar":"im5","background_color":"White","date":"2024-06-14T17:43:49.671Z","content":"test","font_color":"' + text_color + '","id":-1}##'#create the request to the server
            sock.sendall(msg.encode())#send the request to the server with the new color of text 

finally:
    sock.close()#close the connection
