[![Pipeline](https://github.com/url-shortner/url-service/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/url-shortner/url-service/actions/workflows/pipeline.yaml)
# URL Service
This service provides an interface for dealing with URL object. Redis is used as storage backend.

## URL Object
```
TYPE: JSON
FIELDS:
	url_id[str]: Unique short id of url object. Also used for routing.
	target_url[str]: Full target url to redirect to
	created_on[int]: Creation time in unix epoch
	expires_on[int]: Valid until
```

## Endpoints
| METHOD | ENDPOINT        |
|--------|-----------------|
| GET    | `/url/<url_id>` |
| POST   | `/url`          |
| DELETE | `/url`          |

## GET
Fetches URL Object if exists and also attaches aggragate analytics.
```
/url/<url_id>
```
### Example
Request
```
/url/abc123
```

Response
```json
{
    "url": {
        "url_id": "abc123",
        "target_url": "http://www.long-domain.com/very-long-indeed",
        "created_on": 1577985385,
        "expires_on": 1577995385,
    },

    "stats":{
        "total_visits": 1041,
        "failed_redirects": 9
    }

}
```

## POST
Creates a new URL object and returns full url. Duplicate URLs to unique mapping is permitted.
```
/url
```
### Example
Request
```
/url/abc123
```

Body:
```json
{
    "target_url": "http://www.long-domain.com/very-long-indeed"
}
```

Response
```json
{
    "url": {
        "url_id": "abc123",
        "target_url": "http://www.long-domain.com/very-long-indeed",
        "created_on": 1577985385,
        "expires_on": 1577995385,
    },
}
```