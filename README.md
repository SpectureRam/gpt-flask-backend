# GPT Flask Backend

## Description

This repository contains the backend service for a GPT-based chatbot application, implemented using Flask and LangChain. The service provides an API endpoint that receives user queries and responds with generated text using the Google Gemini model.

## Features

- **Flask Framework**: Lightweight web framework to handle HTTP requests and responses.
- **LangChain Integration**: Utilizes LangChain's `ChatGoogleGenerativeAI` to interface with Google's Gemini model for natural language processing.
- **Chat History Management**: Maintains chat history to provide context-aware responses.
- **API Endpoint**: `/api/chat` - Accepts POST requests with user queries and returns generated responses.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gpt-flask-backend.git
    ```
2. Navigate to the project directory:
    ```bash
    cd gpt-flask-backend
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables for API keys and configuration. Create a `.env` file and add:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```
5. Run the Flask server:
    ```bash
    python app.py
    ```

## Deployment

- **Recommended Platforms**: Render, Heroku, or similar cloud services.
- **Deployment Instructions**: Follow the respective platform's documentation for deploying a Flask application.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
