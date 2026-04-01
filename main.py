from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/todos") # get all todo lists
def get_todo():
    return todos

@app.get("/todos/{todo_id}") # get todo, id vice
def dfs(todo_id:int):
    for to in todos:
        if to["id"] == todo_id:
            return to

@app.post("/todos") # make a todo
def sub_todo(item: str):
    todo = {
        "id" : len(todos) + 1,
        "task" : item
    }
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}") # delete a todo
def dlt_todo(todo_id: int):
    for to in todos:
        if to["id"] == todo_id:
            todos.remove(to)
            return {"Message" : "Removed"}