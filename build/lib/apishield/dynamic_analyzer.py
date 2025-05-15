import requests
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def send_http_request(url, method, headers=None, data=None):
    """Send an HTTP request to the target API endpoint"""
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=data)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method")

        # Analyze Response
        status_code = response.status_code
        response_data = response.json() if response.status_code == 200 else response.text

        logging.info(f"HTTP Response Status: {status_code}")
        logging.info(f"Response Body: {json.dumps(response_data, indent=2)}")

        return status_code, response_data
    except Exception as e:
        logging.error(f"Error occurred while sending HTTP request: {e}")
        return None, str(e)

def dynamic_code_analyzer(url, method, headers=None, payload=None):
    """Analyze dynamic API code by sending HTTP requests"""
    
    # Perform HTTP request analysis
    status_code, response_data = send_http_request(url, method, headers, payload)
    
    return status_code, response_data

if __name__ == "__main__":
    # Example usage
    api_url = "http://localhost:8000/api/endpoint"
    api_method = "GET"
    api_headers = {"Content-Type": "application/json"}
    
    # Dynamic API analysis
    status, data = dynamic_code_analyzer(api_url, api_method, api_headers)
    logging.info(f"Dynamic API Analysis Result: {status}, {data}")

