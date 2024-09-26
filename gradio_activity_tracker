import gradio as gr
import time
import subprocess

# Initialize variables
active_time = 0  # Tracks how long you've been using your Mac
max_time = 3600  # 1 hour in seconds (60 minutes x 60 seconds)
tracking = False  # Controls if the timer is running
lock_enabled = False  # Controls if locking is allowed

def check_meeting_running():
    """Checks if a meeting app like Zoom is running."""
    try:
        # Uses AppleScript to check if Zoom is running
        result = subprocess.run(["osascript", "-e", 'tell application "System Events" to (count of (every process whose name is "zoom.us")) > 0'], capture_output=True, text=True)
        # Returns if Zoom is running or not
        return "Zoom is running" if "true" in result.stdout else "No meeting detected"
    except Exception as e:
        return f"Error checking meeting status: {e}"

def start_tracking():
    """Starts the activity tracking."""
    global tracking, active_time
    tracking = True
    active_time = 0  # Reset the timer to zero
    return "Tracking started."

def stop_tracking():
    """Stops the activity tracking."""
    global tracking
    tracking = False
    return "Tracking stopped."

def reset_tracking():
    """Resets the timer back to zero."""
    global active_time
    active_time = 0
    return "Tracking reset."

def enable_lock():
    """Enables the locking feature."""
    global lock_enabled
    lock_enabled = True
    return "Lock feature enabled."

def disable_lock():
    """Disables the locking feature."""
    global lock_enabled
    lock_enabled = False
    return "Lock feature disabled."

def track_activity():
    """Tracks activity and locks screen if needed."""
    global active_time, tracking, lock_enabled
    if not tracking:
        return f"Not tracking. Time active: {active_time // 60} minutes."

    meeting_status = check_meeting_running()  # Check if Zoom is running
    if meeting_status == "No meeting detected":
        active_time += 60  # Add 1 minute to the active time
        if active_time >= max_time:
            if lock_enabled:
                # Lock the screen for 1 minute when 1 hour is reached
                subprocess.run(["osascript", "-e", 'do shell script "pmset displaysleepnow"'])
                active_time = 0  # Reset time after locking
                time.sleep(60)  # Wait 1 minute before allowing to unlock
                return "You've been active for an hour! Locking the screen for 1 minute."
            else:
                return "You've been active for an hour, but locking is disabled."
        return f"Active time: {active_time // 60} minutes."
    else:
        active_time = 0  # Reset time if you're in a meeting
        return "In a meeting. Not tracking active time."

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### MacBook Usage Tracker with Meeting Detection and Screen Locking")
    status = gr.Textbox(label="Status", value="Press start to begin tracking.", interactive=False)

    start_button = gr.Button("Start Tracking")
    start_button.click(fn=start_tracking, outputs=status)

    stop_button = gr.Button("Stop Tracking")
    stop_button.click(fn=stop_tracking, outputs=status)

    reset_button = gr.Button("Reset Tracking")
    reset_button.click(fn=reset_tracking, outputs=status)

    track_button = gr.Button("Track Now")
    track_button.click(fn=track_activity, outputs=status)

    enable_lock_button = gr.Button("Enable Lock Feature")
    enable_lock_button.click(fn=enable_lock, outputs=status)

    disable_lock_button = gr.Button("Disable Lock Feature")
    disable_lock_button.click(fn=disable_lock, outputs=status)

    meeting_status = gr.Textbox(label="Meeting Status", value="Checking...", interactive=False)
    track_button.click(fn=check_meeting_running, outputs=meeting_status)

# Launch the Gradio app
demo.launch()
