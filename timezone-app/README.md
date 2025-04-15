# Time Zone Application

A Streamlit-based web application that helps users track and convert times across different time zones.

## Features

- **Multi-timezone Display**: View current time in multiple time zones simultaneously
- **Time Conversion**: Convert time between any two time zones
- **User-friendly Interface**: Simple and intuitive UI with dropdown selections
- **Real-time Updates**: Automatically updates to show current times

## Supported Time Zones

The application supports the following time zones:
- UTC
- Asia/Karachi
- America/New_York
- Europe/London
- Asia/Tokyo
- Australia/Sydney
- America/Los_Angeles
- Europe/Berlin
- Asia/Dubai
- Asia/Kolkata

## Requirements

- Python 3.7+
- Streamlit
- zoneinfo (built-in with Python 3.9+)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd timezone-app
```

2. Install the required packages:
```bash
pip install streamlit
```

## Usage

1. Run the application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the application:
   - Select multiple time zones to view their current times
   - Use the time conversion feature to convert time between different zones
   - The application automatically updates to show current times

## Features in Detail

### Multi-timezone Display
- Select multiple time zones from the dropdown menu
- View current time in each selected time zone
- Times are displayed in 12-hour format with AM/PM

### Time Conversion
- Enter a specific time
- Select source and target time zones
- Click "Convert Time" to see the converted time
- Results are displayed in 12-hour format with AM/PM

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
