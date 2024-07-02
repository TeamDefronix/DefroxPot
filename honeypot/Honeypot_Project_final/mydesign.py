# This module contains custom and organized functionalities for specific purposes.
# That is to design text, organized module to avoid re-import

import json
import time, subprocess,platform
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from datetime import datetime
import socket
import paramiko
import sqlite3
import requests
import os
from flask import Flask, make_response, render_template, request,  redirect, session, url_for, g
from .web_honeypot import WebsiteTrap
from werkzeug.utils import secure_filename
from .net_honeypot import FtpHoneypot, SSHhoneypot


# ANSI escape codes for text colors
# To print respective messages
ERROR = '\033[91m'
SUCCESS = '\033[92m'
INFO = '\033[93m'
WHITE = '\033[97m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# ANSI escape codes for text styles
# To style respective messages
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
STRIKETHROUGH = '\033[9m'

# Custom text designing functions


def color_style_text(color, text, style=''):
    print((color + style + text + RESET))


def red_text(text):
    print((ERROR + text + RESET))


def green_text(text):
    print((SUCCESS + text + RESET))


def yellow_text(text):
    print(INFO + text + RESET)


# To track, set cookie and return page

json_logs = {
    "ip_addr": "",
    "date": "",
    "timestamp": "",
    "user_id": "",
    "user_agent": "",
    "path_visited": "",
    "session": "",
}


def track_and_response(request, page):

    # Path related code

    curr_path = request.path
    # Read existing cookie or create a new one
    visited_paths = request.cookies.get('visited_paths', '').split(',')

    # Check for duplicate path
    if not curr_path in visited_paths:
        # Append the current path to the list
        visited_paths.append(curr_path)

    # Join the paths and set the cookie
    updated_path = ','.join(visited_paths)
    
    json_logs["ip_addr"] = request.remote_addr
    json_logs["date"] = datetime.now().strftime('%d/%m/%Y')
    json_logs["timestamp"] = datetime.now().strftime('%H:%M:%S')
    json_logs["user_agent"] = request.user_agent.string
    json_logs["path_visited"] = updated_path
    json_logs["session"] = request.cookies.get('session')
    json_logs["new_account"] = session.get('new_account')
    json_logs["user_id"] = session.get('user_id')

    response = make_response(render_template(
        page, visited_paths=visited_paths))

    # Setting cookie value
    response.set_cookie('path_visited', updated_path)

    # Log of site access by
    #f = open(f'{os.path.dirname(__file__)}\\var\\web_honeypot.log', 'a')
    f = open(os.path.join(os.path.dirname(__file__), 'var', 'web_honeypot.log'), 'a')
    json.dump(json_logs, f, ensure_ascii=False)

    f.write("\n")
    f.close()

    return response


# For logging in a file

#def log_capture(filepath, what_to_write):
 #with open(filepath, "a") as log_file:
  #      log_file.write(what_to_write)


# SQL lite3

# Database: users.db
db_con = sqlite3.connect('users.db')
cursor = db_con.cursor()

# Create new table 'users.db' if not there

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(15) UNIQUE, 
        email VARCHAR(100), 
        password VARCHAR(20))""")


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db')
    return g.db

# Searching in database

def check_credentials(username, password):
    db = get_db()
    cursor = db.cursor()

    sql_select = """
    SELECT username, password FROM users
    WHERE username = ? AND password = ?"""

    val_select = (username, password)
    cursor.execute(sql_select, val_select)
    user_data = cursor.fetchone()
    cursor.close()

    return user_data

# Inserting in database

def insert_credentials(username, email, password):
    db = get_db()
    cursor = db.cursor()

    sql_insert = """INSERT INTO users 
    (username, email, password) 
    VALUES (?, ?, ?)"""

    val_insert = (username, email, password)
    user_data = cursor.execute(sql_insert, val_insert)
    db.commit()
    cursor.close()

    return user_data


def file_analysis(filepath):
    
    if 'photo' in request.files:
        
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'

        params = {'apikey': 'd4a04142db71e29bc4993c4a49c19609bdb3b4747d4c0ffa710a5ea17e836cc0'}

        files = {'file':  open(filepath, 'rb')}

        response = requests.post(url, files=files, params=params)
        file_url=f"https://www.virustotal.com/api/v3/files/{(response.json())['sha1']}"
        headers = {
            "accept": "application/json",
            "x-apikey": "d4a04142db71e29bc4993c4a49c19609bdb3b4747d4c0ffa710a5ea17e836cc0",
            "content-type": "multipart/form-data"
        }
        response=requests.get(file_url, headers=headers)
        stats = response.json()['data']['attributes']
        print(stats)
        # Log analysis stats
       # f = open(f'{os.path.dirname(__file__)}\\var\\file_analysis.log', 'a')
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'file_analysis.log'), 'a')
        json.dump(stats, f, ensure_ascii=False)

        f.write("\n")
        f.close()
            

# To extract meta data from photo
            
def meta_data_extract(image_path):
    # Check the operating system
    current_os = platform.system()
    infoDict = {}
    
    # Set the path to the exiftool executable based on the operating system
    if current_os == "Windows":
        file_path = "exiftool(-k).exe"
    elif current_os == "Linux":
        file_path = "exiftool"
    else:
        print(f"Unsupported operating system: {current_os}")
        return
    file_path = os.path.join(os.path.dirname(__file__),file_path)
        
    
	
    try:
        # Execute the exiftool command
        process = subprocess.Popen([file_path, image_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        # Wait for the process to finish and collect output
        output, _ = process.communicate()

        # Parse the output to populate the metadata dictionary
        for tag in output.splitlines():
            line = tag.strip().split(':', 1)
            if len(line) == 2:
                infoDict[line[0].strip()] = line[1].strip()

        # Ensure the log directory exists
        log_dir = os.path.join(os.path.dirname(__file__), 'var')
        os.makedirs(log_dir, exist_ok=True)

        # Log the metadata
        log_path = os.path.join(log_dir, 'photo_metadata.log')
        with open(log_path, 'a') as f:
            json.dump(infoDict, f, ensure_ascii=False)
            f.write("\n")
        
        print("Metadata extraction and logging completed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
