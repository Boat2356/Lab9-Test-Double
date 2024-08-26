from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response():
    mock_response = Response()
    mock_response.status_code = 200
    
    #{'base': 'THB', 'result': {'KRW': 38.69}}
    mock_response.raw = BytesIO(b'{"base": "THB", "result": {"KRW": 38.69}}')
    return mock_response
