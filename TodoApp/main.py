from fastapi import FastAPI
from models import Base
from database import engine, SessionLocal
from routers import auth, todos, admin, users

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


# Debugging: Print all routes
for route in app.routes:
    print(f"Route: {route.path} - {route.name}")
