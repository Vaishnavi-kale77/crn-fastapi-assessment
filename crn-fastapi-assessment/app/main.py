from fastapi import FastAPI

app = FastAPI(title="CRN Product API")

@app.get("/")
def root():
    return {"message": "API is running successfully 🚀"}