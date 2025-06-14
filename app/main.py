from fastapi import FastAPI
from .routes import user, auth

# Create the app
app = FastAPI(
    title="Login Setup using FastAPI",
    version="0.0.1",
)

# Include the user router
app.include_router(user.router)
app.include_router(auth.router)

# Root Route
@app.get("/")
def root(): 
    return {"message": "Hello World"}