from fastapi import FastAPI,  Depends, HTTPException
from pydantic import BaseModel
from db_conn import SessionLocal, get_db
import schemas
from schemas import TodoCreate, TodoResponse
from db_model import tododb, UserDB
from sqlalchemy.orm import Session
from auth import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# Creates a new database session, Automatically closes it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SignUP
@app.post("/signup")
def signup(user: schemas.usercreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)

    new_user = UserDB(
        username = user.username,
        password = hashed
    )
    
    db.add(new_user)
    db.commit()

    return {"Message": "User Created"}

# Login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2PasswordRequestForm gives you username and password
    db_user = db.query(UserDB).filter(UserDB.username == form_data.username).first()
    
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}



@app.get("/todos")
def read_todos(
    current_user: UserDB = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    todos_list = db.query(tododb).filter(tododb.user_id == current_user.id).all()
    return todos_list

# Create Todo
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, current_user: UserDB = Depends(get_current_user), db: Session = Depends(get_db)):
    new_todo = tododb(
        task = todo.task,
        is_done = todo.is_done,
        user_id = current_user.id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Get Todo By ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, current_user: UserDB = Depends(get_current_user), db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id, tododb.user_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# UPDATE - Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_update: TodoCreate, current_user: UserDB = Depends(get_current_user), db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id, tododb.user_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.task = todo_update.task
    todo.is_done = todo_update.is_done
    db.commit()
    db.refresh(todo)
    return todo

# DELETE - Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, current_user: UserDB = Depends(get_current_user), db: Session = Depends(get_db)):
    todo = db.query(tododb).filter(tododb.id == todo_id, tododb.user_id == current_user.id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"Message": "Deleted Successfully"}