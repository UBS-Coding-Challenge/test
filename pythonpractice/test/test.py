import requests
from datetime import datetime, timedelta

# Define the base URL
url = "https://agent-api.green-ribbon.co.kr/api/v1/query-request/daily-agent-fee"

# Define the start and end dates
start_date = datetime.strptime('2024-09-01', '%Y-%m-%d')
end_date = datetime.strptime('2024-09-26', '%Y-%m-%d')

# Define the authorization token (replace 'your_token_here' with the actual token)
auth_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMjE1MjkzIiwiaWF0IjoxNzI3NDIxMDI5LCJleHAiOjE3MjgyODUwMjl9.S3UGWbcLUMJ4R9B4i-czCglCG5YCNDMirM-Em2alNi4c_iDFz5LvVvNCBvucSC09KWPfeNYl0HMaRyR0YQ0gCw'

# Define the headers, including authorization
headers = {
    'Authorization': f'Bearer {auth_token}',
    'X-USER-TYPE': 'ADMIN'
}

# Loop over each date from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Convert current date to string format required by the API
    target_date = current_date.strftime('%Y-%m-%d')
    
    # Prepare the query parameters
    params = {'targetDate': target_date}
    
    # Send the GET request with headers
    response = requests.get(url, headers=headers, params=params)
    
    # Print the target date and the response body
    # print(f"Date: {target_date}, Response: {response.json()}")  # Use response.json() if the response is in JSON format
    body = response.json()
    print(f"\n- 날짜: {target_date}")
    print(f"  * 단독병원: {body['totalUniqueHospitalFee']}")
    print(f"  * 중복병원: {body['totalDuplicateHospitalFee']}")
    print(f"  * 단독약국: {body['totalUniquePharmacyFee']}")
    print(f"  * 중복약국: {body['totalDuplicatePharmacyFee']}")
    print(f"  * 정액서류비용: {body['totalDocumentFee']}")

    # Move to the next day
    current_date += timedelta(days=1)
