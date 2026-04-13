# 🚀 FastAPI Backend Series (6 Sessions)

This project documents my journey of learning and building a complete backend using **FastAPI** across 6 structured sessions.
The focus was to move from basics to a **secure, production-style backend system**.

---

## 📅 What I Built (Session-wise)

### 🔹 Session 1 — Setup + First API + Basic CRUD

* Set up FastAPI project and environment
* Ran server using Uvicorn
* Created first API endpoint
* Built a basic Todo system (in-memory)
* Implemented:

  * `GET /todos`
  * `POST /todos`
* Tested APIs using Swagger (`/docs`)

---

### 🔹 Session 2 — Path Params + Validation (Pydantic)

* Introduced dynamic routes (`/todos/{id}`)
* Implemented:

  * Get single todo
  * Delete todo
* Added structured request validation using Pydantic
* Created input and response schemas
* Improved API reliability and data handling

---

### 🔹 Session 3 — Database Integration (SQLite + SQLAlchemy)

* Replaced in-memory storage with SQLite
* Used SQLAlchemy ORM
* Created database models
* Enabled persistent data storage (survives restart)

---

### 🔹 Session 4 — Clean Architecture & Dependency Injection

* Refactored project into modular structure:

  * `models.py`
  * `schemas.py`
  * `crud.py`
  * `database.py`
* Implemented Dependency Injection for DB sessions
* Separated concerns for scalability and maintainability

---

### 🔹 Session 5 — Authentication (User Identity)

* Implemented user system:

  * Signup & Login
* Added password hashing (bcrypt)
* Generated JWT tokens for authentication
* Verified user identity for protected routes

---

### 🔹 Session 6 — Authorization (User-Specific Access)

* Linked todos to users using `user_id`
* Implemented data ownership
* Restricted access so users only see their own todos
* Secured DELETE and other operations with ownership checks

---

## 🔐 Key Features

* FastAPI-based REST API
* Pydantic validation
* SQLAlchemy ORM
* JWT Authentication
* Authorization with user-specific data access
* Clean and modular project structure

---

## 🧠 What I Learned

* Building REST APIs using FastAPI
* Structuring backend projects for scalability
* Implementing authentication vs authorization
* Managing database integration with ORM
* Deploying a backend application


---

## 📌 Conclusion

This project helped me move from:

> “Basic API understanding”

to:

> **Designing and deploying a secure backend system**

---

⭐ Feel free to explore
