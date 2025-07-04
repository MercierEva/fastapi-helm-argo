import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

# facultatif : pour exécuter localement sans uvicorn CLI
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

