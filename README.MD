<h1 align="center">
  <img src="https://github.com/KernFerm/mouse-tracker-logger/blob/main/banner/Mouse_Tracking_Logger.png" alt="Mouse Tracking Logger" width="500" />
</h1>




# 🖱️ Mouse Tracking Logger

This Python script tracks the position of your mouse and logs the X and Y coordinates to a file. It's useful for proving legitimate mouse activity during gameplay or other tasks. The script is configurable, allowing you to adjust how frequently the mouse position is logged and how often the data is written to a file.

## Support the Project ⭐

If you find this project useful, please give it a star! Your support is appreciated and helps keep the project growing. 🌟

## 🚀 Features

- Tracks the mouse's X and Y coordinates in real-time.
- Logs the mouse position to a text file with timestamps.
- Configurable logging interval and batch size.
- Efficient performance using buffered logging to minimize disk I/O.

## 🛠️ Installation

1. Clone the repository:
  - make sure to make a folder on `Desktop` then `CD` it in `CMD.exe` then do the `Git Clone`.
  ```
  git clone https://github.com/kernferm/mouse-tracking-logger.git
  cd mouse-tracking-logger
  ```

## Install Dependencies
  - You can install the required dependencies using one of the following methods:

- **Option 1: Install using** `pip`
  ```
  pip install pywin32
  ```
- **Option 2: Install using** `requirements.txt`
  - If you have the `requirements.txt` file, you can install all dependencies at once:
  ```
  pip install -r requirements.txt
  ```
- **Option 3: Install using** `install.bat`
  - You can also use the `install.bat` file (if provided) to install the dependencies. Simply run the batch file:
  ```
  install.bat
  ```

### Run the Script

You can run the script using one of the following methods:

- **Option 1:** Run using Python directly
  ```
  python mouse.py
  ```
- **Option 2: Run using the** `main.bat` file
  - If you prefer, you can run the script by executing the `main.bat` file:
  ```
  main.bat
  ```

## ⚙️ Configuration

You can configure the behavior of the script using the `config.py` file. Here's a breakdown of the options:

- `LOG_INTERVAL`: Controls how often the mouse position is logged (in seconds). Lower values result in faster logging.
  - **Example:**
  ```
  LOG_INTERVAL = 0.05  # Log every 0.05 seconds
  ```
- `LOG_FILE_PATH`: Path to the file where mouse positions will be saved.
  - **Example:**
  ```
  LOG_FILE_PATH = "mouse_tracking_log.txt"
  ```
- `LOG_BATCH_SIZE`: Number of entries to buffer before writing to the log file. A higher batch size means fewer writes to the file, which can improve performance
  - **Example:**
  ```
  LOG_BATCH_SIZE = 20  # Write to the file after 20 entries
  ```

## 📂 File Structure

```
📂 File Structure
mouse-tracking-logger/
│
├── .github               # dependabot.yml 
├── banner/               # Directory for any banner or image files
├── .gitignore            # Files and directories to ignore in Git
├── CODE_OF_CONDUCT.md    # CODE_OF_CONDUCT documentation
├── SECURITY.md           # SECURITY documentation
├── README.md             # Project documentation
├── config.bat            # Configuration file to load the settings in a batch file for eaiser
           " save config.py when you change your settings , then relaunch. "
├── config.py             # Configuration settings
├── install.bat           # Batch file to install dependencies
├── main.bat              # Batch file to run the main script from in the directory folder
├── mouse.py              # Main script to track mouse movements
└── requirements.txt      # Python dependencies
```

## 🖥️ Usage

1. **Run the script:**
  ```
  python mouse.py
  ```

2. **Track your mouse**: The script will begin tracking your mouse position and logging it to `mouse_tracking_log.txt`. It will print the current mouse position on the screen.

3. **Stop tracking**: Press `Ctrl + C` to stop the script. The log file will be saved to the specified location.

## 📋 Example Log Output

  ```
  Timestamp, X, Y
2024-09-10 12:00:01, 500, 300
2024-09-10 12:00:01, 505, 320
2024-09-10 12:00:02, 510, 340
  ```

## ❓ FAQ

- **What is the best `LOG_INTERVAL`?**
  - For real-time tracking, a smaller interval (e.g., `0.01`) is best. For less frequent logging, use a larger value (e.g., `1.0`).
- **How do I improve performance?**
  ```
  Increase the `LOG_BATCH_SIZE` in the `config.py` file to reduce the number of times the log is written to disk.
  ```

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests! Contributions are welcome.

### Thank you for using Mouse Tracking Logger! If you have any questions or feedback, feel free to reach out.
