from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Contract & Tax Compliance API running!"}
