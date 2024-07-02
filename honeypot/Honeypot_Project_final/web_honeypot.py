# WebsiteTrap
# This class represents a web trap for detecting and logging web-based attacks.

from .mydesign import *
from . import mydesign


class WebsiteTrap:

    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 2048 * 2048
    app.config['UPLOAD_PATH'] = f'{os.path.dirname(__file__)}\\uploads'

    # Close db

    @app.teardown_appcontext
    def close_db(error):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    @app.errorhandler(404)
    # Handle 404 content
    def page_not_found(error):
        # Render your custom 404 template
        return render_template('404.html'), 404

    # To generate unique session ids
    app.secret_key = '122k'

    # Login Page for the attacker to trap
    @app.route('/', methods=['GET', 'POST'])
    def login():
        try:
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                user_data = mydesign.check_credentials(username, password)

                if user_data:
                    # Set session data to indicate a new account
                    session['user_id'] = user_data[0]
                    session['new_account'] = False
                    return render_template('dashboard.html')
                else:
                    return render_template('incorrect_pass.html')
        except Exception as e:
            print(f"Error in login: {e}")
            return "Error occurred during login. Please try again."

        return mydesign.track_and_response(request, 'login.html')

    # Registration Page for the attacker to trap

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        try:
            if request.method == 'POST':
                # Get form data
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('password')

                # Check if the request contains a file
                if 'photo' in request.files:
                    photo = request.files['photo']

                    # Check if the file is allowed based on its extension
                    allowed_extensions = {'jpg', 'jpeg', 'png', 'pdf'}
                    if '.' in photo.filename and photo.filename.rsplit('.', 1)[1].lower() in allowed_extensions:
                        # Save the file with a unique name
                        username = request.form.get('username', 'unknown_user')
                        # filename = f"{username}_photo.{photo.filename.rsplit('.', 1)[1]}"
                        file_path = os.path.join(os.path.dirname(__file__), "uploads", photo.filename)
                        photo.save(file_path)
                        mydesign.file_analysis(filepath=file_path)
                        mydesign.meta_data_extract(file_path)

                        # mydesign.file_analysis(file_path)
                        # Set session data to indicate a new account
                        session['user_id'] = username
                        session['new_account'] = True

                        # Perform registration logic
                        mydesign.insert_credentials(username, email, password)
                        return render_template('registration_success.html')

                    else:
                        # Invalid file type
                        return 'Invalid file type. Please upload an image file.'
                else:
                    # No file found in the request
                    return 'No file found in the request.'
        except Exception as e:
            print(f"Error in registration: {e}")
            return "Error occurred during registration. Please try again."

        return mydesign.track_and_response(request, 'register.html')

    
    # Logout  user from the system
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        return render_template('login.html')
    
    # About
    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')

    # Keylogger set-up

    @app.route('/s', methods=['POST'])
    def keypress():

        json_logs = {
            "date": "",
            "timestamp": "",
            "ip_addr": "",
            "keystrokes": ""
        }
        
        # Taking keystrokes from attacker
        data = request.get_json()
        json_logs["date"] = datetime.now().strftime('%d/%m/%Y')
        json_logs["timestamp"] = datetime.now().strftime('%H:%M:%S')
        json_logs["ip_addr"] = request.remote_addr
        pressed_key = data.get('key')

        # Key to decrypt
        key = 'defronix'

        # To decrypt keystrokes
        json_logs['keystrokes'] = ''
        for i in range(len(pressed_key)):
            json_logs['keystrokes'] += chr(ord(pressed_key[i]) ^ ord(key[i % len(key)]))
            
        #Adding a space at the end of word received from keylogger

        json_logs['keystrokes'] += ' '
        #f=open(f'{os.path.dirname(__file__)}\\var\\key_logger.log','a')
        f = open(os.path.join(os.path.dirname(__file__), 'var', 'key_logger.log'), 'a')
        json.dump(json_logs, f, ensure_ascii=False)
        f.write("\n")
        f.close()

        return 'Keypress handled successfully'
    