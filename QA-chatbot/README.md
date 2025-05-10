# QA Chatbot

A conversational AI chatbot built using Chainlit and Google's Gemini AI model. This chatbot provides an interactive interface for users to ask questions and receive AI-powered responses.

## Features

- Interactive chat interface using Chainlit
- Powered by Google's Gemini 2.0 Flash model
- Real-time response generation
- Environment variable support for secure API key management

## Prerequisites

- Python 3.7+
- Google API key for Gemini AI
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd QA-chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the chatbot:
```bash
chainlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8000`

3. Start chatting with the AI!

## Project Structure

- `main.py`: Main application file containing the chatbot logic
- `.env`: Environment variables file (create this file and add your API key)
- `requirements.txt`: Project dependencies

## Dependencies

- chainlit
- google-generativeai
- python-dotenv

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Muhammad Tasleem](https://github.com/TasleemSiddiqui)

---
Made with ❤️ by [Muhammad Tasleem]
