from pydantic import BaseModel


class URL(BaseModel):
    url_id: str
    target_url: str
    created_on: int
    expires_on: int


class Stats(BaseModel):
    total_visits: int
    failed_redirects: int
    successful_redirects: int


class ResponseBase(BaseModel):
    url: URL


class URLAddResponse(ResponseBase):
    pass


class URLGetResponse(ResponseBase):
    stats: Stats


class URLAddRequest(BaseModel):
    target_url: str
