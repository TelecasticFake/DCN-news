from flask import Flask, render_template_string, request, redirect, url_for, render_template
import mysql.connector as msql 
from mysql.connector import Error, IntegrityError
import requests

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
            font-size: 24px;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .input-field:focus {
            border-color: #007bff;
            outline: none;
        }
        .login-btn {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .login-btn:hover {
            background-color: #0056b3;
       
        }
    </style>
</head>
<body>

    <div class="login-container">
        <h2>Login</h2>
        <form action="/login" method="POST">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" class="input-field" required>

            <label for="password">Password</label>
            <input type="password" id="password" name="password" class="input-field" required>

            <button type="submit" class="login-btn">Login</button>
        </form>
        
        <div class="viewer">
        <form action="/signup_page">
            <input type="submit" value="Go to signup" />
        </form>
        </div>
    </div>

</body>
</html>
"""
signup_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
            font-size: 24px;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .input-field:focus {
            border-color: #007bff;
            outline: none;
        }
        .login-btn {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .login-btn:hover {
            background-color: #0056b3;
      
    </style>
</head>
<body>

    <div class="login-container">
        <h2>Sign up</h2>
        <form action="/signup" method="POST">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" class="input-field" required>

            <label for="password">Password</label>
            <input type="password" id="password" name="password" class="input-field" required>

            <button type="submit" class="login-btn">Sign up</button>
        </form>
        
        <div class="viewer">
        <form action="/">
            <input type="submit" value="Go to login" />
        </form>
        </div>
    </div>

</body>
</html>
"""

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

success_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h2>Welcome, {{ username }}!</h2>
        <p>You are successfully logged in.</p>
        <h1>DCN NEWS</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/world">World</a></li>
                <li><a href="/politics">Politics</a></li>
                <li><a href="/sports">Sports</a></li>
                <li><a href="/entertainment">Entertainment</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <div class="container">
        <h1>Welcome to DCN News</h1>
        <div class="row content">
            {% for article in articles %}
                <div class="col-md-4 mb-4">
                    <div class="card" style="width: 18rem;">
                        <img src="{{ article.urlToImage }}" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">{{ article.title }}</h5>
                            <p class="card-text">{{ article.description }}</p>
                            <a href="{{ article.url }}" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
</body>
</html>
"""

failure_page = """
<!DOCTYPE html>
<html>
<head>
    <title>{{process}} Failed</title>
</head>
<body>
    <h2>{{process}} Failed</h2>
    <p>{{error_msg}}</p>
</body>
</html>
"""

styles= """""
body {
  background-image: url('images/logo.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: rgba(0, 0, 0, 0.7);
  color: rgb(197, 0, 0);
  padding: 1rem;
  text-align: center;
}

h1 {
font-family: Lobster, cursive; /* stylish font */
font-weight: bold; /* bold text */
color:rgb(197, 0, 0); /* red color */


}

.navbar{
background-color: rgb(197, 0, 0);;
}
nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 1rem;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

.card {
height: 600px;
}
header {
  animation: fadeIn 2s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}


nav ul {
  animation: slideIn 2s;
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

a:hover {
  font-weight: bold;
  color:rgb(197, 0, 0);
  background-color: #333;
  padding: 10px;
  border-radius: 10px;
  transition: all 0.5s;
}
nav ul li a:not(:hover) {
  color: #fff;
  padding: 0;
  border-radius: 0;
  transition: all 0.3s;
}

.navbar.bg-body-tertiary {
  background-color: rgba(255, 0, 0, 0.5); /* translucent red background */
}

.pagination-btn {
background-color: rgb(197, 0, 0); /* matching the red theme */
color: white;
border: none;
padding: 10px 20px;
border-radius: 5px;
font-size: 16px;
cursor: pointer;
transition: background-color 0.3s ease, transform 0.3s ease;
}

.pagination-btn:hover {
background-color: rgba(197, 0, 0, 0.8); /* darker on hover */
transform: scale(1.05); /* slight grow on hover */
}

.pagination-btn:active {
transform: scale(0.95); /* shrink on click */
}"""


@app.route("/")
def login():
    return render_template_string(login_page)

@app.route("/signup_page")
def signup():
    return render_template_string(signup_page)

@app.route("/login", methods=["POST"])
def handle_login():
    process="Login"
    username = request.form["username"]
    password = request.form["password"]
    error_msg="Invalid username or password. Please try again."
    
    conn = msql.connect(host="localhost", user="root", password="root", database="dnc_news")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logintable WHERE loginusername = %s AND loginpassword = %s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        fetch_news()
        articles = get_news()  # Fetch news articles
        return render_template_string(success_page, username=username, articles=articles)
    else:
        return render_template_string(failure_page, process=process, error_msg=error_msg)

@app.route("/signup", methods=["POST"])
def handle_signup():
    process="Sign up"
    username = request.form["username"]
    password = request.form["password"]

    try:
        conn = msql.connect(host="localhost", user="root", password="root", database="dnc_news")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM logintable;")
        count = cursor.fetchone()[0]
        newid = count + 1

        cursor.execute(
            "INSERT INTO logintable (loginid, loginusername, loginpassword) VALUES (%s, %s, %s);",
            (newid, username, password)
        )
        conn.commit()
    except IntegrityError as e:
        duplicate_msg="This username is already in use. Please try a new one."
        return render_template_string(failure_page, process=process, error_msg=duplicate_msg)
    except msql.Error as e:
        error_msg="Following error has occurred:{e} \n Please contact the developers"
        return render_template_string(failure_page, process=process, error_msg=error_msg)
    finally:
        conn.close()
    articles = get_news()  # Fetch news articles
    return render_template_string(success_page, username=username, articles=articles)

@app.route("/politics") 
def politics():
    print("Rendering politics template...")
    return render_template("politics.html")

@app.route("/world")
def world():
    print("Rendering world template...")
    return render_template("world.html")

@app.route("/sports")
def sports():
    print("Rendering sports template...")
    return render_template("sports.html")

@app.route("/entertainment")
def entertainment():
    print("Rendering entertainment template...")
    return render_template("entertainment.html")

@app.route("/fetch_news")
def fetch_news():
    api_key = "934719473fce4176804d2174d4c529dc"
    url = f"https://newsapi.org/v2/everything?q=Breaking News&apiKey={api_key}"
    
    response = requests.get(url)
    articles = response.json().get("articles", [])

    conn = msql.connect(host="localhost", user="root", password="root", database="dnc_news")
    cursor = conn.cursor()
    cursor.execute(
        "DROP TABLE IF EXISTS news_articles;"
    )
    cursor.execute("CREATE TABLE news_articles (DataNo int primary key, title varchar(200), description long varchar, url long varchar, urlToImage long varchar, category varchar(20));")
    count=0
    for article in articles:
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        category = "General"  # You can modify this based on your needs
        count = count + 1
        cursor.execute(
            "INSERT INTO news_articles (DataNo, title, description, url, urlToImage, category) VALUES (%s, %s, %s, %s, %s, %s)",
            (count, title, description, url, urlToImage, category)
        )

    conn.commit()
    conn.close()

    return "News articles fetched and stored successfully!"


def get_news():
    try:
        # Connect to the database
        conn = msql.connect(host="localhost", user="root", password="root", database="dnc_news")
        cursor = conn.cursor()

        # Execute a query to select all articles from the news_articles table
        cursor.execute("SELECT * FROM news_articles;")
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Create a list to hold the articles
        articles = []
        
        # Iterate through the rows and create a dictionary for each article
        for row in rows:
            article = {
                "title": row[1],
                "description": row[2],
                "url": row[3],
                "urlToImage": row[4],
                "category": row[5]
            }
            articles.append(article)

        return articles  # Return the list of articles

    except msql.Error as e:
        print(f"Error: {e}")
        return []  # Return an empty list in case of an error

    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)
