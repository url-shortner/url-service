import json
from typing import Any, Dict, Union

import redis as Redis

from . import schemas
from .config import config


def fetchURLbyID(url_id: str) -> Union[Dict[Any, Any], None]:
    redis = Redis.Redis(host=config.redis_host)
    data = redis.get(url_id)
    if data is None:
        return None
    data_decoded = json.loads(data)
    data_decoded["url_id"] = url_id
    return data_decoded


def addUrl(url: schemas.URL) -> bool:
    redis = Redis.Redis(host=config.redis_host)
    data = {
        "target_url": url.target_url,
        "created_on": url.created_on,
        "expires_on": url.expires_on,
    }
    redis.set(url.url_id, value=json.dumps(data))
    return True
