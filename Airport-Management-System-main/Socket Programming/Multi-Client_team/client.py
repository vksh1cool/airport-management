import socket
import csv
import string
import random


def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)
    print("\n[SERVER] Connected.")

    """ Displaying the menu and getting the option. """
    print("\n")
    operation = input("""************ Welcome to Airlines **************

            A: Ticket Details
            B: Booking tickets
            C: Ticket Cancellation
            Q: Disconnect     

            Please enter your choice: """)

    """ A. Ticket details wrt to PNR number. """
    if (operation == "A"):

        """ Sending filename to server. """
        client.send("ticket_details.txt".encode(FORMAT))
        print(f"\n[SERVER] Filename Received.")

        """ Opening a .csv file to write the data. """
        with open('ticket_details.csv', 'wb') as file:

            """ Writing data sent by the server to the file. """
            print("\n[SERVER] Data is being sent.")
            while True:
                data = client.recv(SIZE)
                if not data:
                    break
                file.write(data)

        """ Closing the file. """
        file.close()
        print(f"\n[SERVER] Process completed.")

        """ Closing the connection from the server. """
        client.close()
        print("\n[SERVER] Disconnected.")

        """ Getting PNR number from the user. """
        print("\n")
        print("\n")
        PNR = input("Enter your PNR number: ")

        """ Opening the csv file and creating iterative obj. """
        csv_file = open('ticket_details.csv')
        csv_obj = csv.reader(csv_file)

        """ Getting fields of the file. """
        fields = next(csv_obj)

        """ Printing the ticket Details. """
        print("\nYour ticket details are: ")
        print("[ " + ', '.join(field for field in fields) + "]")
        for row in csv_obj:
            if (row[0] == PNR):
                print(row)
        print("\n")

    """ B. Ticket Booking. """
    if (operation == "B"):
        """ Sending filename to server. """
        client.send("ticket_details.txt".encode(FORMAT))
        print(f"\n[SERVER] Filename Received.")

        """ Opening a .csv file to write the data. """
        with open('ticket_details.csv', 'wb') as file:

            """ Writing data sent by the server to the file. """
            print("\n[SERVER] Data is being sent.")
            while True:
                data = client.recv(SIZE)
                if not data:
                    break
                file.write(data)

        """ Closing the file. """
        file.close()
        print(f"\n[SERVER] Process completed.")

        """ Closing the connection from the server. """
        client.close()
        print("\n[SERVER] Disconnected.")

        """ Getting PNR number from the user. """
        print("\n")
        print("\n")
        rows = []
        name = input("Enter your name: ")
        des_from = input("\nEnter your SOURCE: ")
        des_to = input("\nEnter your DESTINATION: ")
        print(f"\n[SERVER] Ticket Confirmed.")
        print("\n")

    """ C. Ticket Cancellation wrt to PNR number. """
    if (operation == "C"):
        """ Sending filename to server. """
        client.send("ticket_details.txt".encode(FORMAT))
        print(f"\n[SERVER] Filename Received.")

        """ Opening a .csv file to write the data. """
        with open('ticket_details.csv', 'wb') as file:

            """ Writing data sent by the server to the file. """
            print("\n[SERVER] Data is being sent.")
            while True:
                data = client.recv(SIZE)
                if not data:
                    break
                file.write(data)

        """ Closing the file. """
        file.close()
        print(f"\n[SERVER] Process completed.")

        """ Closing the connection from the server. """
        client.close()
        print("\n[SERVER] Disconnected.")

        print("\n")
        print("\n")
        PNR = input("Enter your PNR number: ")
        lines = list()
        with open('ticket_details.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == PNR:
                        lines.remove(row)
        with open('ticket_details.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        print(f"\n[SERVER] Ticket Cancelled.")
        print("\n")

    """ Q. Disconnect"""
    if (operation == "Q"):
        """ Sending filename to server. """
        client.send("exit".encode(FORMAT))

        """ Closing the connection from the server. """
        client.close()
        print("\n[SERVER] Disconnected.\n")


if __name__ == "__main__":
    main()
