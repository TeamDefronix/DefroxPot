from .mydesign import *
from . import mydesign

# FTP Honeypot
# This class represents an FTP honeypot
# for detecting and logging FTP connection attempts.

server=None
ssh_server=None
class FtpHoneypot(FTPHandler):

    def on_connect(self):
        # Log connection attempt
        log_entry = {
            "ip_address": self.remote_ip,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "message": "Connection established"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_login(self, username):
        # Log login attempt
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "message": "Login attempt"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()
        

    def on_login_failed(self, username):
        # Log failed login attempt
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "message": "Failed login attempt"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_logout(self, username):
        # Log logout
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "message": "Logout"
        }
        
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_version(self, version):
        # Log version information
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "version": version,
            "message": "Version information"
        }
        
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_auth(self, username):
        # Log authentication
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "message": "Authentication successful"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_auth_failed(self, username):
        # Log failed authentication
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "message": "Authentication failed"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def on_disconnect(self):
        # Log disconnection
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "ip_address": self.remote_ip,
            "message": "Connection closed"
        }
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()
    def run_ftp_server():
        global server
        authorizer = DummyAuthorizer()
        # Add an anonymous user with no permissions

        filepath = os.path.join(os.path.dirname(__file__), 'home')

        authorizer.add_anonymous(filepath, perm="")
        authorizer.add_user(username="incog", password="pass",
                            homedir=filepath, perm="elradfm")

        handler = FtpHoneypot
        handler.authorizer = authorizer

        server = FTPServer(("0.0.0.0", 21), handler)
        server.serve_forever()
        # server.close_all
    def stop_ftp_server():
        global server
        print("Stopping FTP server...")
        # if server:
        server.close_all()
        print("FTP server stopped")


# SSH Honeypot
# This class represents an SSH honeypot
# for detecting and logging SSH connection attempts.

class SSHhoneypot(paramiko.ServerInterface):

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

    def check_channel_shell_request(self, channel):
        return True

    def check_auth_password(self, username, password):
        if username == "incog" and password == "pass":
            return paramiko.AUTH_SUCCESSFUL
        else:
            return paramiko.AUTH_FAILED

    def log_event(self, message):
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "message": message
        }
        
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'net_honeypot.log'), 'a')
        json.dump(log_entry, f, ensure_ascii=False)

        f.write("\n")
        f.close()

    def start_ssh_server():
        global ssh_server
        ssh_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssh_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ssh_server.bind(('127.0.0.1', 22))
        ssh_server.listen(5)
        print("SSH server listening on port 22")

        while True:
            client, addr = ssh_server.accept()
            print(f"Connection from {addr}")

            transport = paramiko.Transport(client)
            server_key = paramiko.RSAKey.from_private_key_file(filename=os.path.join(os.path.dirname(__file__), 'id_rsa'), password="pass")
            transport.add_server_key(server_key)

            # Disable strict host key checking
            transport.setDaemon(1)

            ssh = SSHhoneypot()
            transport.start_server(server=ssh)

            channel = transport.accept(20)
            if channel is None:
                print("SSH negotiation failed.")
                client.close()
                continue

            print("Authenticated!")

            # Set event handlers
            if channel.recv_ready():
                channel.set_combine_stderr(True)
                channel.setblocking(0)
                channel.recv_ready().register(ssh.on_output_ready)

            try:
                while True:
                    if channel.recv_ready():
                        command = channel.recv(1024).decode('utf-8').strip()
                        # Log the command
                        ssh.log_event(f"Executed command: {command}")
            except Exception as e:
                print(f"Error executing command: {e}")
            finally:
                channel.close()
                client.close()
    def stop_ssh_server():
        global ssh_server
        ssh_server.close()
