from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .Honeypot_Project_final import main
from werkzeug.serving import make_server
import threading
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
server = None
t2 = None
# LOG_FILE_PATH = './honeypot/Honeypot_Project_final/var/web_honeypot.log'
def handle_logs(LOG_FILE_PATH):
    logs = []
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line:  # Ensure the line is not empty
                # print(line)
                logs.append(json.loads(line))
    return logs

@login_required
def dashboard(request):
    ip_addr=[]
    try:
        logs_web = handle_logs('./honeypot/Honeypot_Project_final/var/web_honeypot.log')
        for log in logs_web:
            if log['ip_addr'] not in ip_addr:
                ip_addr.append(log['ip_addr'])
        logs_net = handle_logs('./honeypot/Honeypot_Project_final/var/net_honeypot.log')
        for log in logs_net:
            try:
                if log['ip_address'] not in ip_addr:
                    ip_addr.append(log['ip_address'])
            except:
                pass
        logs_key = handle_logs('./honeypot/Honeypot_Project_final/var/key_logger.log')
        for log in logs_key:
            if log['ip_addr'] not in ip_addr:
                ip_addr.append(log['ip_addr'])
        return render(request,'dashboard.html',{"active":"dashboard","ip_addr":ip_addr})
    except:
        return render(request,'dashboard.html',{"active":"dashboard"})
flask_thread = None
flask_server = None
ftp_thread=None
ssh_thread=None
@csrf_exempt
def start_flask_server(request):
    global flask_thread, flask_server
    if request.method == 'POST':
        if flask_thread is None or not flask_thread.is_alive():
            def run_flask():
                global flask_server
                # from main import WebsiteTrap  # Import the Flask app inside the function
                flask_server = make_server('0.0.0.0', 5000, main.WebsiteTrap.app, threaded=True)
                flask_server.serve_forever()

            flask_thread = threading.Thread(target=run_flask)
            flask_thread.start()
            return JsonResponse({'status': 'started', 'ip': '0.0.0.0', 'port': '5000'})
        else:
            return JsonResponse({'status': 'already_running'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def stop_flask_server(request):
    global flask_thread, flask_server
    if request.method == 'POST':
        if flask_thread is not None and flask_thread.is_alive():
            flask_server.shutdown()  # Shutdown the server
            flask_thread.join()  # Wait for the thread to finish
            flask_thread = None
            flask_server = None
            return JsonResponse({'status': 'stopped'})
        else:
            return JsonResponse({'status': 'not_running'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def start_network_server(request):
    global ftp_thread, ssh_thread
    if request.method == 'POST':
        if ftp_thread is None or not ftp_thread.is_alive():
            ftp_thread = threading.Thread(target=main.FtpHoneypot.run_ftp_server)
            ftp_thread.start()

        if ssh_thread is None or not ssh_thread.is_alive():
            ssh_thread = threading.Thread(target=main.SSHhoneypot.start_ssh_server)
            ssh_thread.start()
            return JsonResponse({'status': 'started'})
        else:
            return JsonResponse({'status': 'already_running'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def stop_network_server(request):
    global ftp_thread, ssh_thread
    if request.method == 'POST':
        if ftp_thread is not None and ftp_thread.is_alive():
            main.FtpHoneypot.stop_ftp_server()
            # Code to stop the FTP server goes here
            ftp_thread.join()
            ftp_thread = None

        if ssh_thread is not None and ssh_thread.is_alive():
            main.SSHhoneypot.stop_ssh_server()
            # Code to stop the SSH server goes here
            ssh_thread.join()
            ssh_thread = None

        return JsonResponse({'status': 'stopped'})
    # return JsonResponse({'status': 'not_running'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def network_setup(request):
    global ftp_thread, ssh_thread
    # if request.method == 'POST':
    if (ftp_thread is not None and ftp_thread.is_alive()) or (ssh_thread is not None and ssh_thread.is_alive()):
        return JsonResponse({'status': 'running'})
    return JsonResponse({'status': 'stopped'})

    # return JsonResponse({'error': 'Invalid request method'}, status=400)

def server_setup(request):
    global flask_thread
    if flask_thread is not None and flask_thread.is_alive():
        return JsonResponse({'status': 'running'})
    else:
        return JsonResponse({'status': 'stopped'})
@login_required
def setup(request):
    return render(request,"setup.html",{"active":"setup"})
@login_required
def file_analysis(request):
    try:
        key_logs = handle_logs('./honeypot/Honeypot_Project_final/var/file_analysis.log')
        keys=[]
        for key_log in key_logs:
            for key in key_log.keys():
                if key not in keys:
                    keys.append(key)
        return render(request,"file.html",{"active":"details",'key_logs':key_logs,'keys':keys})
    except:
        return render(request,"file.html",{"active":"details"})
@login_required
def Keylogger(request):
    try:
        key_logs = handle_logs('./honeypot/Honeypot_Project_final/var/key_logger.log')
        # print(key_logs)
        keys=[]
        for key_log in key_logs:
            for key in key_log.keys():
                if key not in keys:
                    keys.append(key)
        # print(keys)
        return render(request,"Keylogger.html",{"active":"Keylogger",'key_logs':key_logs,'keys':keys})
    except:
        return render(request,"Keylogger.html",{"active":"Keylogger"})
@login_required
def network(request):
    try:
        key_logs = handle_logs('./honeypot/Honeypot_Project_final/var/net_honeypot.log')
        keys=[]
        for key_log in key_logs:
            for key in key_log.keys():
                if key not in keys:
                    keys.append(key)
        return render(request,"network.html",{"active":"network",'key_logs':key_logs,'keys':keys})
    except:
        return render(request,"network.html",{"active":"network"})
@login_required
def photo(request):
    try:
        key_logs = handle_logs('./honeypot/Honeypot_Project_final/var/photo_metadata.log')
        keys=[]
        for key_log in key_logs:
            for key in key_log.keys():
                if key not in keys:
                    keys.append(key)
        return render(request,"photo.html",{"active":"photo",'key_logs':key_logs,'keys':keys})
    except:
        return render(request,"photo.html",{"active":"photo"})
@login_required
def website(request):
    try:
        key_logs = handle_logs('./honeypot/Honeypot_Project_final/var/web_honeypot.log')
        keys=[]
        for key_log in key_logs:
            for key in key_log.keys():
                if key not in keys:
                    keys.append(key)
        return render(request,"website.html",{"active":"website",'key_logs':key_logs,'keys':keys})
    except:
        return render(request,"website.html",{"active":"website"})

def handlelogin(request):
    if request.method=="POST":
        Username=request.POST["loginusername"]
        Password=request.POST["loginpassword"]
        user=authenticate(username=Username,password=Password)
        if user is not None:
            login(request,user)
            # messages.success(request,"You are successfully logined!!")
            return redirect("dashboard")
        else:
            messages.error(request,"Username or Password is incorrect.")
            return redirect('handlelogin')
    return render(request,'login.html')
@login_required
def handlelogout(request):
    logout(request)
    messages.info(request,"Logged out Successfully!")
    return redirect('handlelogin')