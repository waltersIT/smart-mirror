# Smart Mirror

A simple smart mirror application built using Python and Tkinter. It displays the current time, weather, and top news headlines in a sleek, full-screen interface.

## Features

- **Time Display**: Shows the current time in a large, easy-to-read format.
- **Weather Updates**: Fetches and displays the latest weather conditions for Baltimore (or any city of your choice).
- **News Headlines**: Retrieves and displays the latest top headlines from The Wall Street Journal.
- **Full-Screen Mode**: Runs in full-screen mode by default, with the option to exit or re-enter as needed.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- `requests` (for weather updates)
- `newsapi-python` (for news headlines)
- `tkinter` (usually included with Python)

### Setup

1. Clone or download this repository:
   ```sh
   git clone https://github.com/yourusername/Smart-Mirror.git
   cd Smart-Mirror
   ```

2. Install the required dependencies:
   ```sh
   pip install requests newsapi-python
   ```

3. **Set up API keys**:
   - Open `weather.py` and replace `"YOUR API KEY"` with your OpenWeather API key.
   - Open `news.py` and replace `"YOUR API KEY"` with your NewsAPI key.

## Usage

Run the application using:

```sh
python Smart-Mirror.py
```

### Full-Screen Controls

- Press **F** to enter full-screen mode.
- Press **ESC** to exit full-screen mode.

## File Structure

- `Smart-Mirror.py` - Main application logic using Tkinter.
- `weather.py` - Fetches current weather data.
- `news.py` - Fetches the latest news headlines.

## Notes

- The weather updates every 45 minutes to avoid excessive API requests.
- The application defaults to displaying weather for **Baltimore**, but you can change this in `weather.py`.

## Future Improvements

- Add voice control support.
- Include additional news sources.
- Display additional widgets (e.g., calendar, traffic updates).

## License

This project is open-source. Feel free to modify and improve it!
