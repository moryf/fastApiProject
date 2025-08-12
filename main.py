from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    # For now, we'll just return the ID we captured
    return {"user_id": user_id, "name": "Jane Doe", "email": "jane.doe@example.com"}