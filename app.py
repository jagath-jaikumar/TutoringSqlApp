import db
from db import packets
from db import process
from typing import Optional
import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


def session_generator():
    """Yields a dbm session for dependency injection"""
    session = db.get_session()
    try:
        yield session
    finally:
        session.commit()
        session.close()


@app.post("/create/simple_item")
def read_item(simple_object: packets.SimpleObject, session=Depends(session_generator)):
    process.persist_simple_table(simple_object, session)
    return {"status": "success"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000)
