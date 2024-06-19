from flask import Flask, redirect, url_for, request, render_template
import json


app = Flask(__name__, template_folder="templates")

with open('Todos.json') as f:
    todos = json.load(f)

def DumpTodos():
    with open('Todos.json', 'w') as f:
        json.dump(todos, f)

@app.route('/')
def index():
    with open('Todos.json') as f:
        return render_template("index.html", todos=json.load(f))


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    todos.append({"todo": todo, "done": False})
    DumpTodos()
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo["todo"] = request.form["todo"]
        DumpTodos()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)




@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    DumpTodos()
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    DumpTodos()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
