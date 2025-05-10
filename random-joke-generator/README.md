# Random Joke Generator

A simple and fun web application that generates random jokes using the Official Joke API. Built with Streamlit, this application provides an interactive interface to fetch and display jokes with a clean, modern design.

## Features

- Generate random jokes with a single click
- Clean and responsive user interface
- Real-time joke fetching from the Official Joke API
- Error handling for failed API requests

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/random-joke-generator.git
cd random-joke-generator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Click the "Generate Joke" button to get a random joke

## Project Structure

```
random-joke-generator/
├── main.py              # Main application file
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Dependencies

- streamlit: For creating the web interface
- requests: For making HTTP requests to the joke API

## API Reference

This project uses the [Official Joke API](https://official-joke-api.appspot.com/) to fetch random jokes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Built with ❤️ by [Muhammad Tasleem](https://github.com/TasleemSiddiqui)

## Acknowledgments

- [Official Joke API](https://official-joke-api.appspot.com/) for providing the joke data
- [Streamlit](https://streamlit.io/) for the web framework
