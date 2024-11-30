from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simple HTML template for login page
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Home page after login
home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h2>Welcome, {{ username }}!</h2>
    <p>You have successfully logged in.</p>
</body>
</html>
"""

# Route for login page
@app.route("/")
def login():
    return render_template_string(login_page)

# Route for login handling
@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    # Replace with actual authentication logic
    if username == "admin" and password == "password":
        return render_template_string(home_page, username=username)
    else:
        return "<h2>Invalid username or password. Try again.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
