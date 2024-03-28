# OpenCV Human Detection with Telegram Alert

This project utilizes OpenCV and Python to create a real-time human detection system. It continuously monitors a video stream and sends alerts to the user via a Telegram bot whenever a human is detected.

## Features

- **Real-Time Video Stream Monitoring**: Utilizes OpenCV to monitor a video stream in real-time.
- **Human Detection**: Detects humans in the video stream using computer vision techniques.
- **Telegram Bot Integration**: Sends alerts and the video stream to the user via a Telegram bot.
- **Configurable Parameters**: Allows users to adjust various parameters such as sensitivity thresholds and video stream sources.

## Prerequisites

- Python 3.x
- OpenCV
- Telegram API Key
- Telegram Bot ID

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Karanxidhu/CCTV-telebot
2. Navigate to the project directory:
   ```bash
   cd CCTV-telebot
3. Make sure that you have openCV installed.

## Configuration

1. Obtain a Telegram API Key and Bot ID from the Telegram BotFather.
2. Update the `bot.py` file with your Telegram API Key and Bot ID.

## Usage

1. Run the main script:
   ```bash
   python bot.py
2. Sit back and let the system monitor the video stream. You will receive alerts via your Telegram bot whenever a human is detected.
## Contributions
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
