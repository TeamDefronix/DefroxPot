<div align="center"><p>
    <h1>DefroxPot</h1>
     <img style="filter: brightness(200%)" src="https://github.com/TeamDefronix/DefroxPot/assets/64286654/c8b70e39-59d1-4a4c-9ada-74b7dba0e923" width="50%"><br>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    <img src="https://forthebadge.com/images/badges/built-with-love.svg">
    <br><br>
    <a href="https://github.com/TeamDefronix/DefroxPot/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/TeamDefronix/DefroxPot?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/DefroxPot/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/TeamDefronix/DefroxPot?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/DefroxPot/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/TeamDefronix/DefroxPot?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/DefroxPot/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/TeamDefronix/DefroxPot?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/DefroxPot/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/TeamDefronix/DefroxPot?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/DefroxPot">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/TeamDefronix/DefroxPot?color=%23DDB6F2&label=SIZE&logo=codesandbox&style=for-the-badge&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=niteshlike123">
      <img alt="follow on Twitter" src="https://img.shields.io/twitter/follow/niteshlike123?style=for-the-badge&logo=twitter&color=8aadf3&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://discord.gg/defronix">
      <img alt="Discord" src="https://img.shields.io/discord/1072407436348112896?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
  </p>
  <p align="center">
    <img src="https://stars.medv.io/TeamDefronix/DefroxPot.svg", title="commits"/>
  </p>

<h1 align="left">Description</h1>

<p align="left">
     DefroxPot is a honeypot project designed to detect, monitor, and analyze malicious activity in a controlled environment. This project aims to provide cybersecurity enthusiasts and professionals with a powerful tool to study attack patterns, improve defensive strategies, and enhance security awareness.
</p>


---

**[<kbd> <br> Variants <br> </kbd>][Variants]** 
**[<kbd> <br> Install <br> </kbd>][Install]**
**[<kbd> <br> Dependencies <br> </kbd>][Dependencies]** 
**[<kbd> <br> Usage <br> </kbd>][Usage]** 
**[<kbd> <br> Screenshots <br> </kbd>][ScreenShots]** 
**[<kbd> <br> Contributors <br> </kbd>][Contributors]**

---

[Variants]: #Variants
[Install]: #Installation
[Dependencies]: #Dependencies
[Usage]: #Usage
[Screenshots]: #Screenshots
[Contributors]: #Contributors

</div>

# Variants

### Web Honeypot

The Web Honeypot simulates a vulnerable website to attract and analyze web-based attacks.

#### Features

**Web Logging**
- Records all HTTP requests and responses
- Logs IP addresses, session details, user agents, user IDs, and paths visited
- Captures keystrokes through the website

**File Analysis**
- Analyzes files uploaded by attackers to check for malicious content
- Extracts metadata from the uploaded files

**Dashboard**
- Provides a dashboard for real-time monitoring

### Network Honeypot

The Network Honeypot mimics a network environment to detect, log and analyze network-based attacks.

#### Features

**Network Logging**
- Captures and logs all network traffic
- Records IP addresses and authentication attempts via FTP or SSH services (whichever you run)

**Deceptive Environment**
- Creates a deceptive environment to trap attackers
- Simulates various network services to attract malicious activity

# Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/repo/HoneyGuard.git
    cd honeypot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the honeypot:**
      ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```
    **Note**: `python manage.py createsuperuser` is required to create for managing the DefroxPot tool

4. **Start the honeypot:**
   
    ```bash
    python manage.py runserver
    ```
   You will receive a URL with port 8000. Open this URL in your browser to access the admin panel.
   
# Dependencies
- Apart from what is in `requirements.txt` ExifTool is also required to extract metadata from images. You can visit the official website [https://exiftool.org]
- Virus total has been used to check malicious content if uploaded by an attacker [https://www.virustotal.com]

  **You can visit the following URLs to check software authenticity.**
  
  `exiftool.exe` (Windows): https://www.virustotal.com/gui/file/e9bfbb1ae99f3b5587f926393c3e9ccd86ad7e03a779a06f5e68601a6a85a714 <br>
  `exiftool` (Linux): https://www.virustotal.com/gui/file/4827ade560b85f0877c635fd7e32144e9196f4fa256cc504c42f8593cc79a32b
  
# Technology Stack

### Essential Python Libraries

`Django`: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.

`Flask`: A lightweight WSGI web application framework in Python.

`paramiko`: A library for making SSH2 connections.

`pyftpdlib`: A library for creating FTP servers.

`bcrypt`: Library for hashing passwords in a secure manner.

`blinker`: Provides support for creating signals and listening to them, often used in Flask applications.

`certifi`: Provides Mozilla’s CA Bundle, useful for SSL verification.

`cryptography`: Provides cryptographic recipes and primitives.

`itsdangerous`: Provides various helpers to pass trusted data to untrusted environments.

`pycparser`: A C parser and AST generator written in Python.

`PyNaCl`: Python binding to the Networking and Cryptography (NaCl) library.
 

# Usage
### Website
- Navigate to the `Setup` tab and launch the web setup. You will receive a URL with port 5000 that is intended to be accessed by an attacker.
- `File Analysis`, `Photo`, `Keylogger` and `Website` tabs belong to Web honeypot. You can navigate to check logs.

### Network
- Navigate to the `Setup` tab and launch the network setup. The `ssh` and `ftp` will be started that is intended to be accessed by an attacker.
- `Network` tabs belong to network honeypot. You can navigate to check logs.

# Screenshots
![d1](https://github.com/TeamDefronix/DefroxPot/assets/104693696/f9f2965d-37ec-4750-9287-673c2608b065)

![d2](https://github.com/TeamDefronix/DefroxPot/assets/104693696/5bfb2d44-6c8d-4da8-aaee-badb4b21b897)

![d3](https://github.com/TeamDefronix/DefroxPot/assets/104693696/09b4b4e5-5872-432e-a465-0f401e52c4c4)

![d4](https://github.com/TeamDefronix/DefroxPot/assets/104693696/0ea91eea-d965-42c4-81d1-4b440a0e2ab3)

![d5](https://github.com/TeamDefronix/DefroxPot/assets/104693696/804c461e-61f4-4850-827f-b787a80a3c55)

![d6](https://github.com/TeamDefronix/DefroxPot/assets/104693696/3abda9aa-d3ad-479f-8f11-f2ab5600b6f8)

![d7](https://github.com/TeamDefronix/DefroxPot/assets/104693696/7c5f1dd9-9a5c-4ea2-9690-c21777162665)

# Contacts

<p align="left">
<a href="https://github.com/TeamDefronix"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/Github.svg" width="64" height="64" alt="Github Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/> <a href="https://www.facebook.com/defronix"><img src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Facebook.svg" width="64" height="64" alt="Facebook Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/> <a href="https://twitter.com/teamdefronix"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/Twitter.svg" width="64" height="64" alt="Twitter Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
<a href="https://instagram.com/teamdefronix"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/Instagram.svg" width="64" height="64" alt="Instagram Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
<a href="https://whatsapp.com/channel/0029VaGltobEKyZ8eX8Ki82w"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/WhatsApp.svg" width="64" height="64" alt="WhatsApp Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
<a href="https://youtube.com/@defronix"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/Youtube.svg" width="64" height="64" alt="Youtube Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
<a href="https://www.linkedin.com/company/defronix/"><img src="https://github.com/gauravghongde/social-icons/raw/master/SVG/Color/LinkedIN.svg" width="64" height="64" alt="LinkedIN Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
</p>

# Support

<p><a href="https://www.buymeacoffee.com/metaxone" target="_blank"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Buymeacoffee" /></a></p><br><br><br>
<p><a href="https://paypal.me/niteshsinghhacker" target="_blank"> <img align="left" src="https://raw.githubusercontent.com/andreostrovsky/donate-with-paypal/master/blue.svg" height="70" width="210" alt="Donate with paypal" /></a></p><br><br><br>
<p><a href="https://tools.apgy.in/upi/Nitesh+Singh/niteshkumar5@ybl/" target="_blank"> <img align="left" style="border-radius:8px" src="https://user-images.githubusercontent.com/122822828/216837693-3480fcd2-b4fc-40ff-94f8-c5d7d4b82ad5.png" height="50" width="210" alt="Donate with paypal" /></a></p><br><br><br>
<p><a href="https://razorpay.me/@technicalnavigator" target="_blank"> <img align="left" src="https://user-images.githubusercontent.com/122822828/216838288-a946ef91-f215-4286-926f-afa71d0c3760.png" height="50" width="210" alt="Donate with paypal" /></a></p><br><be>
<br>
  
*This tool is currently a prototype and can be further improved. If you have more context or specific improvements in mind, We can tailor the further requirements to fit your needs*
<div align="center">
    <h1 id="Contributors">Thanks To All Contributors</h1>

<a href="https://github.com/TeamDefronix/DefroxPot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TeamDefronix/DefroxPot" />
</a>
</div>
