import hashlib
import time
from secrets import token_bytes
from typing import Union

from . import redis, schemas, stats
from .config import config


def getURLbyID(url_id: str) -> Union[schemas.URLGetResponse, None]:
    url = redis.fetchURLbyID(url_id)
    # No url found
    if url is None:
        return None
    stat = stats.getStatsById(url_id)
    # Unable to fetch stats
    # TODO: Rework response if cant fetch stats instead of returning None
    if stat is None:
        return None
    url_s = schemas.URL(**url)
    stat_s = schemas.Stats(**stat)
    return schemas.URLGetResponse(url=url_s, stats=stat_s)


def AddURL(target_url: str) -> Union[schemas.URL, None]:
    # TODO: Validate URL
    url_id = generateID(target_url)
    creation_time = int(time.time())
    URL = schemas.URL(
        url_id=url_id,
        target_url=target_url,
        created_on=creation_time,
        expires_on=creation_time + config.ttl,
    )

    # TODO: check if url_id exists before adding
    store = redis.addUrl(URL)
    if not store:
        return None
    return URL


def generateID(target_url: str) -> str:
    url_id = hashlib.md5()
    url_id.update(target_url.encode())
    url_id.update(token_bytes(32))
    return url_id.hexdigest()[27:]
