import socket
import csv
from _thread import *

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def new_client(conn, addr):
    """ Getting Filename from Client. """
    filename = conn.recv(SIZE).decode(FORMAT)

    if filename != "exit":
        print(f"\n[CLIENT] Filename sent.")
        """ Opening the file. """
        file = open("data/" + filename, 'rb')
        line = file.read(1024)

        """ Reading the file and sending it. """
        print("\n[CLIENT] Receiving the data.")
        while (line):
            conn.send(line)
            line = file.read(1024)

        """ Closing the file"""
        file.close()
        print("\n[CLIENT] Data received.")

        """ Closing the connection from the client. """
        conn.close()
        print(f"\n[DISCONNECTED] {addr} disconnected.")

    else:
        """ Closing the connection from the client. """
        conn.close()
        print(f"\n[DISCONNECTED] {addr} disconnected.")


def main():
    """ To check how many clients are connected to the server. """
    No_of_Clients = 0

    """ Staring a TCP socket. """
    print("\n[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    try:
        server.bind(ADDR)
    except socket.error as error:
        """ Error message."""
        print("Error has occured! Please try again " + str(error))

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen(5)
    print("\n[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the clients. """
        conn, addr = server.accept()
        print(f"\n[NEW CONNECTION] {addr} connected.")

        """ Creating new threads to process multiple clients. """
        start_new_thread(new_client, (conn, addr))

        """ To print No of clients connected to server. """
        # No_of_Clients += 1
        # print("\n!!!!!! Clients Details !!!!!! ")
        # print("Clients online : " + str(No_of_Clients))


if __name__ == "__main__":
    main()
