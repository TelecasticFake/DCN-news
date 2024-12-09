from flask import Flask, render_template_string, request, redirect, url_for
import mysql.connector as msql 

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
        .forgot-password {
            text-align: center;
            margin-top: 10px;
        }
        .forgot-password a {
            color: #007bff;
            text-decoration: none;
        }
        .forgot-password a:hover {
            text-decoration: underline;
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
        }
        .forgot-password {
            text-align: center;
            margin-top: 10px;
        }
        .forgot-password a {
            color: #007bff;
            text-decoration: none;
        }
        .forgot-password a:hover {
            text-decoration: underline;
        }
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
        <form action="/login_page">
            <input type="submit" value="Go to login" />
        </form>
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
<body>
    <h2>Welcome, {{ username }}!</h2>
    <p>You are successfully logged in.</p>
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>DCN News</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <header>
    <h1>DCN NEWS</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="world.html">World</a></li>
        <li><a href="politics.html">Politics</a></li>
        <li><a href="sports.html">Sports</a></li>
        <li><a href="entertainment.html">Entertainment</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  <body>
    <nav class="navbar">
      <div class="container-fluid">
        <a class="navbar-brand"></a>
        <form class="d-flex" role="search">
          <input
            id="searchInput"
            class="form-control me-2"
            type="search"
            placeholder="Sea"
            aria-label="Search"
          />
          <button id="search" class="btn btn-outline-success" type="submit">
            Search
          </button>
        </form>
      </div>
    </nav>
    <div class="container">
      <h1>Welcome to DCN News (<span id="resultCount"></span> Results)</h1>
      <div class="row content">
        <div class="card my-4 mx-2" style="width: 18rem">
          <img src="..." class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-around">
        <button class="btn pagination-btn">< Previous Page</button>
        <button class="btn pagination-btn">Next Page ></button>
      </div>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <script>
      const search = document.getElementById("search");
      const searchInput = document.getElementById("searchInput");
      const resultCount = document.getElementById("resultCount");

      const fetchNews = async (page, q) => {
        console.log("Fetching news...");
        var url =
          "https://newsapi.org/v2/everything?" +
          "q=" +
          q +
          "&pageSize=21&" +
          "page=" +
          page +
          "&sortBy=popularity&" +
          "apiKey=934719473fce4176804d2174d4c529dc";

        var req = new Request(url);

        let a = await fetch(req);
        let response = await a.json();
        console.log(response);
        let str = "";
        resultCount.innerHTML = response.totalResults;
        for (let item of response.articles) {
          str += `<div class="col-md-4 mb-4">
      <div class="card" style="width: 18rem;">
        <img src="${item.urlToImage}" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">${item.title}</h5>
          <p class="card-text">
            ${item.description}
          </p>
          <a href=${item.url}="btn btn-primary pagination-btn">Go somewhere</a>

        </div>
      </div>
    </div>`;
        }
        document.querySelector(".content").innerHTML = str;
      };
      fetchNews(1, "Breaking News");
      search.addEventListener("click", (e) => {
        e.preventDefault();
        let query = searchInput.value;
        fetchNews(1, query);
      });
    </script>
  </body>
</html>
</body>
</html>
"""


failure_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Failed</title>
</head>
<body>
    <h2>Login Failed</h2>
    <p>Invalid username or password. Please try again.</p>
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
    username = request.form["username"]
    password = request.form["password"]

    
    conn = msql.connect(host="localhost", user="root", password="root", database="dnc")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logintable WHERE loginusername = %s AND loginpassword = %s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template_string(success_page, username=username)
    else:
        return render_template_string(failure_page)

@app.route("/signup", methods=["POST"])
def handle_signup():
    username = request.form["username"]
    password = request.form["password"]

    
    conn = msql.connect(host="localhost", user="root", password="root", database="dnc")
    cursor = conn.cursor()
    cursor.execute("Count(*) from logintable;")
    count=cursor.fetchone()
    newid=count+1
    cursor.execute("INSERT INTO logintable (loginid, loginusername, loginpassword) VALUES(%s, %s, %s);", (newid, username, password))
    cursor.commit()
    conn.close()
    return render_template_string(success_page, username=username)

if __name__ == "__main__":
    app.run(debug=True)
