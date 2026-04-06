from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from db_conn import SessionLocal
from schemas import TodoCreate, TodoResponse
from db_model import tododb
from sqlalchemy.orm import Session

app = FastAPI()

# Creates a new database session, Automatically closes it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos") # get all todo lists
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(tododb).all()
    return todos

# Create Todo
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = tododb(
        task = todo.task,
        is_done = todo.is_done
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Get Todo By ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# UPDATE - Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_update: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.task = todo_update.task
    todo.is_done = todo_update.is_done
    db.commit()
    db.refresh(todo)
    return todo

# DELETE - Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"Message" : "Deleted Successfully"}