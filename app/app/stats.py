from typing import Any, Dict, Union


def getStatsById(url_id: str) -> Union[Dict[Any, Any], None]:
    return {
        "url_id": "ABC123",
        "total_visits": 104,
        "failed_redirects": 10,
        "successful_redirects": 91,
    }
