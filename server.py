from flask import Flask, render_template
import random
import datetime
import requests
import json

GENDERIZE_API_ENDPOINT = "https://api.genderize.io?name="
AGIFY_API_ENDPOINT = "https://api.agify.io?name="
BLOG_API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
# name = "Cesar"
# response = requests.get(url=GENDERIZE_API_URL+name)
# response.raise_for_status
# gender = json.loads(response.content)
# print(gender["name"])
app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)  # We can pass python variables like num=random_number

@app.route("/guess/<name>")
def guess_name(name):
    genderize_response = requests.get(url=GENDERIZE_API_ENDPOINT+name)
    genderize_response.raise_for_status
    gender = json.loads(genderize_response.content)["gender"]
    agify_response = requests.get(url=AGIFY_API_ENDPOINT+name)
    agify_response.raise_for_status
    age = json.loads(agify_response.content)["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get(BLOG_API_ENDPOINT)
    response.raise_for_status
    all_post = response.json()
    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
