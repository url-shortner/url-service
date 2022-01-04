from pydantic import BaseSettings


class Config(BaseSettings):
    redis_host: str = "redis"
    es_host: str = "elasticsearch"
    es_port: int = 9200
    es_index: str = "redirect-log"
    ttl: int = 300000000  # 1 year


config = Config()
