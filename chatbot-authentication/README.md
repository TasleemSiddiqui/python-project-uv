# Chatbot Authentication with Chainlit and Gemini AI

A secure and interactive chatbot application built with Chainlit and Google's Gemini AI, featuring GitHub OAuth authentication.

## Features

- 🤖 Powered by Google's Gemini AI (gemini-2.0-flash model)
- 🔐 GitHub OAuth Authentication
- 💬 Interactive chat interface
- 📝 Persistent chat history
- 🚀 Fast response times with Gemini's flash model

## Prerequisites

- Python 3.x
- GitHub account (for OAuth)
- Google Cloud account with Gemini API access
- uv (Python package installer and resolver)

## Installation

1. Install uv (if not already installed):
```bash
pip install uv
```

2. Clone the repository:
```bash
git clone <repository-url>
cd chatbot-authentication
```

3. Initialize the project with uv:
```bash
uv venv
```

4. Create a `.env` file in the root directory and add your API keys:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Configuration

1. Set up GitHub OAuth:
   - Create a new OAuth application in your GitHub account
   - Configure the callback URL in your GitHub OAuth settings
   - Update the OAuth settings in `chainlit.yaml`

2. Configure Chainlit:
   - The application uses the default Chainlit configuration
   - Customize the UI and behavior in `chainlit.yaml`

## Environment Variables

The application requires the following environment variables to be set in your `.env` file:

```
# Google Gemini API Key
GEMINI_API_KEY=
OAUTH_GITHUB_CLIENT_ID=
OAUTH_GITHUB_CLIENT_SECRET=
CHAINLIT_AUTH_SECRET=
```

### Getting Your API Keys

1. **Gemini API Key**:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key and add it to your `.env` file

2. **Security Best Practices**:
   - Never commit your `.env` file to version control
   - Keep your API keys secure and rotate them periodically
   - Use different API keys for development and production environments

## Usage

1. Start the application:
```bash
chainlit run main.py
```

2. Open your browser and navigate to `http://localhost:8000`
3. Log in with your GitHub account
4. Start chatting with the AI assistant!

## Project Structure

```
chatbot-authentication/
├── main.py              # Main application code
├── chainlit.yaml        # Chainlit configuration
├── pyproject.toml       # Project dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## Security

- API keys are stored in environment variables
- OAuth authentication ensures secure access
- Chat history is maintained per session

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Created By

[Muhammad Tasleem](https://github.com/TasleemSiddiqui)

Last updated: February 2024
