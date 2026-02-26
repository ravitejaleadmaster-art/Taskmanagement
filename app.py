from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

app = FastAPI()






@app.get("/db-check")
def check_db_connection(db: Session = Depends(get_db)):
    try:
        # Attempt a simple query to verify the connection
        db.execute(text("SELECT 1"))
        return {"status": "database is connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.get("/")
def read_root():
    return "Task Manager API running"

@app.get("/health")
def health_check():
    return {"status": "ok"}