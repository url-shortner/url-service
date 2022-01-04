from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from . import schemas
from .utils import AddURL, getURLbyID

app = FastAPI()


@app.get("/url/{url_id}", response_model=schemas.URLGetResponse)
def getURL(url_id: str):  # type: ignore
    url = getURLbyID(url_id)
    if url is None:
        raise HTTPException(404, "URL NOT FOUND")
    return url


@app.post("/url", response_model=schemas.URL)
def addURL(target_url: schemas.URLAddRequest):  # type: ignore
    return AddURL(target_url.target_url)
