from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Hardcoded sensitive data (for testing Gitleaks detection)
app.secret_key = 'your_super_secret_key_123456'  # Hardcoded secret key
DATABASE_URL = 'mysql://admin:SuperSecretPass@localhost:3306/mydatabase'  # Hardcoded database credentials
AWS_ACCESS_KEY_ID = "AKIAXXXXXXXXXXXXXX"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Hardcoded AWS credentials

# Hardcoded user credentials for demonstration purposes
USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin@123'  # Hardcoded password
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
