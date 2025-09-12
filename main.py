from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the Mini-RAG API!"}

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}