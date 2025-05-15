from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime as dt
app = Flask(__name__)
time = dt.datetime.now()
formatted_time = time.strftime("%d/%m/%Y")
client = MongoClient("mongodb://localhost:27017/")
app.db = client.todo_db
collection = app.db.todos
todos = []
@app.route("/")
def todo_list():
    todos = [(data["todo"], data["date"]) for data in collection.find()]
    return render_template("todo_list.html", todos=todos, title="Todo - Home")

@app.route("/add", methods=["GET","POST"])
def todo_add():
    if request.method == "POST":
        new_todo = request.form.get("todo")
        collection.insert_one({"todo" : new_todo, "date" : formatted_time})
        all_data = [e for e in collection.find()]
        for data in all_data:
            todos.append((data["todo"], data["date"]))
    return render_template("todo_add.html",title="+ New Todo")


if __name__ == "__main__":
    app.run(debug=True)
