from flask import Flask, render_template, request
app = Flask(__name__)
todos = ["buy milk","hit the gym","wash clothes","prepare for lecture"]

@app.route("/")
def todo_list():
    return render_template("todo_list.html", todos=todos, title="Todo - Home")

@app.route("/add", methods=["GET","POST"])
def todo_add():
    if request.method == "POST":
        new_todo = request.form.get("todo")
        todos.append(new_todo)
    return render_template("todo_add.html",title="+ New Todo")


if __name__ == "__main__":
    app.run(debug=True)
