import os
import requests
import schedule
import time
from datetime import datetime

# Access token for authentication
access_token = "ODA1MTI3MTMtMDExNS00ZmU3LTlhMzAtODhmOTEyODkxYzViZjNmNjQ5Y2UtOGFj_P0A1_3b73211d-14aa-400d-b1f6-2334f5901977"

def send_webex_message(room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }
    print(f"Sending message to room ID: {room_id}")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message:", response.json())
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def schedule_message(room_id, message, send_time):
    schedule_time = datetime.strptime(send_time, '%Y-%m-%d %H:%M:%S')
    schedule.every().day.at(schedule_time.strftime('%H:%M:%S')).do(send_webex_message, room_id=room_id, message=message)

# Example usage
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZWRjMmZkNjAtMTFkNS0xMWVmLWJlNjctZGIwMDQzNDRmNjM4'
message = 'Test message2'  # Replace with the actual message text
send_time = '2024-07-13 20:06:00'  # Format: YYYY-MM-DD HH:MM:SS
schedule_message(room_id, message, send_time)

while True:
    schedule.run_pending()
    time.sleep(1)







