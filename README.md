# Langchain Intro

This project demonstrates how to use the Langchain library with OpenAI's language models to create a simple chat application using Streamlit.

## Prerequisites

- Python 3.7 or higher
- `pip` package manager
- OpenAI API key
- Langchain API key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/langchain-intro.git
    cd langchain-intro
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your question in the input field and get a response from the language model.

## Project Structure

- `app.py`: Main application file that sets up the Streamlit interface and handles user input.
- `llms.py`: Contains the implementation of the language model interaction.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: Environment file to store API keys (not included in the repository).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.