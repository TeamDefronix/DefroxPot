# This module is to run all honeypots from one script

from .mydesign import *

# To Avoid entering unwanted inputs

def get_numeric_choice():
    while True:
        user_choice = input("Choice >> ")

        # Check if numeric or not
        if not user_choice.isdigit() or int(user_choice) >= 4:
            print("Invalid Choice")
        else:
            return int(user_choice)


if __name__ == "__main__":

    green_text('-'*50)
    print("1. Web Honeypot \n2. Network Honeypot")
    green_text('-'*50)

    opt = get_numeric_choice()

    if opt == 1:
        # Auto assign system ip
        WebsiteTrap.app.run(host="0.0.0.0", port=80,threaded=True)

    elif opt == 2:

        print("1. FTP Honeypot \n2. SSH Honeypot")

        opt = get_numeric_choice()

        if opt == 1:
            FtpHoneypot.run_ftp_server()

        elif opt == 2:
            SSHhoneypot.start_ssh_server()
