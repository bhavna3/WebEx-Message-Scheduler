# WebEx-Message-Scheduler
This project automates sending scheduled messages to a WebEx room using Python. It uses the schedule library to handle the scheduling and the WebEx API to send the messages.

## Prerequisites

- Python 3.x
- `requests` library: Install using `pip install requests`
- `schedule` library: Install using `pip install schedule`

## Setup

 **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/webex-message-scheduler.git
   cd webex-message-scheduler

   Install Dependencies
```

## Example usage
room_id = 'YOUR_ROOM_ID'
message = 'Test message'  # Replace with the actual message text
send_time = '2024-07-13 20:06:00'  # Format: YYYY-MM-DD HH:MM:SS
schedule_message(room_id, message, send_time)

## License
This project is licensed under the MIT License.
