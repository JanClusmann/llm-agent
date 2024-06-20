
# LLM-Agent Project

## Description

This project involves running a web-based application using the Large Language Model (LLM) agent. Follow the instructions below to set up and run the application.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Virtualenv

## Installation and Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/KatherLab/llm-agent.git
    cd llm-agent
   git checkout exp_trail_evaluations
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Ensure the virtual environment is activated** (if not already active)

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

2. **Run the application**

    ```sh
    python te_webui/app.py
    ```

## Usage

After running the above command, the web application should be accessible in your web browser. Open your browser and navigate to the URL provided in the terminal.

## Troubleshooting

If you encounter any issues, ensure that all prerequisites are installed and the virtual environment is activated. Additionally, ensure all dependencies are correctly installed from `llm-agent/requirements.txt`.
