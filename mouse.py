import win32api, time, os
import config  # Import settings from config.py

# Function to write logs in batches
def write_log_batch(log_entries, file_path):
    with open(file_path, "a") as log_file:
        log_file.writelines(log_entries)  # Use writelines for efficiency

# Check if the log file exists; if not, create it with a header
if not os.path.exists(config.LOG_FILE_PATH):
    with open(config.LOG_FILE_PATH, "w") as f:
        f.write("Timestamp, X, Y\n")  # Write the header

# Initialize the log entry buffer and last_position tracker
log_buffer = []
last_position = None  # Store the last position to track only changes

try:
    print("Tracking mouse position... Press Ctrl + C to stop.")
    
    # Start tracking
    while True:
        # Get the current mouse position
        mouse_pos = win32api.GetCursorPos()
        
        # Track only if the mouse position changes
        if mouse_pos != last_position:
            # Get the current time for logging
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # Create the log entry
            log_entry = f"{timestamp}, {mouse_pos[0]}, {mouse_pos[1]}\n"
            log_buffer.append(log_entry)
            
            # Print the current mouse position with timestamp (on position change)
            print(f"{timestamp} - Current mouse position: {mouse_pos}", end="\r")
            
            last_position = mouse_pos
        
        # Write log entries in batches (from config)
        if len(log_buffer) >= config.LOG_BATCH_SIZE:
            write_log_batch(log_buffer, config.LOG_FILE_PATH)
            log_buffer.clear()  # Clear the buffer after writing

        time.sleep(config.LOG_INTERVAL)  # Use logging interval from config

except KeyboardInterrupt:
    # On script exit, write any remaining log entries
    if log_buffer:
        write_log_batch(log_buffer, config.LOG_FILE_PATH)
    
    print("\nMouse tracking stopped. Log saved to:", config.LOG_FILE_PATH)

except Exception as e:
    print(f"An error occurred: {e}")
