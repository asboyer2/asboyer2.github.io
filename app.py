import os
import json
import inflect
from flask import Flask, render_template, send_from_directory
from datetime import date
 
grade = "senior"
school = "Wayland High School"

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age

birthday = date(2003, 9, 21)
p = inflect.engine()

age_string = p.number_to_words(calculateAge(birthday))

if age_string.startswith('eight'):
    age_string = "n " + age_string
else:
    age_string = " " + age_string

soon_posts = []

f = open('data/blog/posts.json')
posts = json.load(f)
for post in posts:
    if not posts[post]['live']:
        soon_posts.append(str(posts[post]['id']))

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html", age=age_string, grade=grade, school=school)

@app.route("/<page>")
def main_page(page):
    if os.path.exists(f'templates/{page}.html'):
        return render_template(f'{page}.html')
    else:
        return render_template("error.html")

@app.route("/press")
def press():
    return render_template("about/news.html")

# blogs

@app.route("/blog")
def blog():
    return render_template("blog/blog.html")

@app.route("/blog/<name>")
def blog_post(name):
    if name in soon_posts:
        return render_template("soon.html")
    elif os.path.exists(f'templates/blog/{name}.html'):
        return render_template(f"blog/{name}.html")
    else:
        # make error page
        return render_template("error.html")

# favorites

# music
@app.route("/music")
def music():
    return render_template("favorites/music/music.html")

@app.route("/music/<name>")
def music_path(name):
    if os.path.exists(f'templates/favorites/music/{name}.html'):
        return render_template(f"favorites/music/{name}.html")
    else:
        # make error page
        return render_template("error.html")


# movies
@app.route("/movies")
def movies():
    return render_template("favorites/movies/movies.html")

@app.route("/shows")
def shows():
    return render_template("favorites/shows/shows.html")

#SEO
@app.route("/robots.txt")
def se1():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def se2():
    return send_from_directory(app.root_path, "sitemap.xml")

@app.route("/data/movies.json")
def movies_json():
    f = open('data/favorites/films/movies.json')
    data = json.load(f)
    return data

@app.route("/data/music_all_time.json")
def music_json():
    f = open('data/favorites/music/music_all_time.json')
    data = json.load(f)
    return data

@app.route("/data/music_current.json")
def music_json_current_albums():
    f = open('data/favorites/music/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/music_current_songs.json")
def music_json_current_tracks():
    f = open('data/favorites/music/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/data/shows.json")
def load_shows():
    f = open('data/favorites/films/shows.json')
    data = json.load(f)
    return data

@app.route("/data/projects.json")
def load_projects():
    f = open('data/projects/index.json')
    data = json.load(f)
    return data

@app.route("/data/work.json")
def load_work():
    f = open('data/work/index.json')
    data = json.load(f)
    return data

@app.route("/data/skills.json")
def load_skills():
    f = open('data/about/services/services.json')
    data = json.load(f)
    return data

@app.route("/data/blog/posts.json")
def load_blog_posts():
    f = open('data/blog/posts.json')
    data = json.load(f)
    return data    

@app.route("/data/tools.json")
def load_tools():
    f = open('data/tools/index.json')
    data = json.load(f)
    return data  

@app.route("/data/midnight/specs.json")
def load_midnight_parts():
    f = open('data/midnight/parts.json')
    data = json.load(f)
    return data      

@app.route("/midnight")
def midnight_parts():
    return render_template("midnight/parts.html")

@app.route("/tools/midnight")
def midnight_parts_tools():
    return render_template("midnight/parts.html")

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/data/quotes.json")
def load_quotes():
    f = open('data/quotes/quotes.json')
    data = json.load(f)
    return data
#####################3/1/2021 music backup here#####################
@app.route("/data/archive/music/312021/music_current.json")
def load_music_current_312021():
    f = open('data/archive/music/312021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/312021/music_current_songs.json")
def load_music_current_songs_312021():
    f = open('data/archive/music/312021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/0")
def music_archive_312021():
    return render_template("archive/music/312021.html")

#####################7/1/2021 music backup here#####################

@app.route("/data/archive/music/712021/music_current.json")
def load_music_current_712021():
    f = open('data/archive/music/712021/music_current.json')
    data = json.load(f)
    return data
        
@app.route("/data/archive/music/712021/music_current_songs.json")
def load_music_current_songs_712021():
    f = open('data/archive/music/712021/music_current_songs.json')
    data = json.load(f)
    return data
        
@app.route("/archive/music/1")
def music_archive_712021():
    return render_template("archive/music/712021.html")


#####################8/25/2021 music backup here#####################

@app.route("/data/archive/music/8252021/music_current.json")
def load_music_current_8252021():
    f = open('data/archive/music/8252021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/8252021/music_current_songs.json")
def load_music_current_songs_8252021():
    f = open('data/archive/music/8252021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/2")
def music_archive_8252021():
    return render_template("archive/music/8252021.html")
    
#####################9/10/2021 music backup here#####################

@app.route("/data/archive/music/9102021/music_current.json")
def load_music_current_9102021():
    f = open('data/archive/music/9102021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/9102021/music_current_songs.json")
def load_music_current_songs_9102021():
    f = open('data/archive/music/9102021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/3")
def music_archive_9102021():
    return render_template("archive/music/9102021.html")
    
#####################9/16/2021 music backup here#####################

@app.route("/data/archive/music/9162021/music_current.json")
def load_music_current_9162021():
    f = open('data/archive/music/9162021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/9162021/music_current_songs.json")
def load_music_current_songs_9162021():
    f = open('data/archive/music/9162021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/4")
def music_archive_9162021():
    return render_template("archive/music/9162021.html")
    
#####################10/3/2021 music backup here#####################

@app.route("/data/archive/music/1032021/music_current.json")
def load_music_current_1032021():
    f = open('data/archive/music/1032021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/1032021/music_current_songs.json")
def load_music_current_songs_1032021():
    f = open('data/archive/music/1032021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/5")
def music_archive_1032021():
    return render_template("archive/music/1032021.html")
    
#####################10/12/2021 music backup here#####################

@app.route("/data/archive/music/10122021/music_current.json")
def load_music_current_10122021():
    f = open('data/archive/music/10122021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/10122021/music_current_songs.json")
def load_music_current_songs_10122021():
    f = open('data/archive/music/10122021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/6")
def music_archive_10122021():
    return render_template("archive/music/10122021.html")
    
#####################10/27/2021 music backup here#####################

@app.route("/data/archive/music/10272021/music_current.json")
def load_music_current_10272021():
    f = open('data/archive/music/10272021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/10272021/music_current_songs.json")
def load_music_current_songs_10272021():
    f = open('data/archive/music/10272021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/7")
def music_archive_10272021():
    return render_template("archive/music/10272021.html")
    
#####################2/4/2022 music backup here#####################

@app.route("/data/archive/music/242022/music_current.json")
def load_music_current_242022():
    f = open('data/archive/music/242022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/242022/music_current_songs.json")
def load_music_current_songs_242022():
    f = open('data/archive/music/242022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/8")
def music_archive_242022():
    return render_template("archive/music/242022.html")
    