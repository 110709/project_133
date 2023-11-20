from flask import Flask, render_template

app = Flask(__name__)

# Sample data for family members
family_members = [
    {"name": "Avika", "age": 14, "picture": "static/me.jpg"},
    {"name": "Gyanesh", "age": 40, "picture": "static/father.jpg"},
    {"name": "Sapna", "age": 38, "picture": "static/mother.jpg"},
    {"name": "Saanvika", "age": 2, "picture": "static/sister.jpg"},
    
]

@app.route("/")
def index():
    return render_template("index.html", family_members=family_members)

@app.route("/member/<name>")
def member(name):
    member_data = next((member for member in family_members if member["name"] == name), None)
    if member_data:
        return render_template("member.html", member=member_data)
    else:
        return render_template("not_found.html")

if __name__ == "__main__":
    app.run(debug=True)
