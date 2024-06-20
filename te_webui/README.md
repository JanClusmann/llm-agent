
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

## Finishing Up

After you have finished evaluating and testing the application, consider pushing your changes or any improvements back to the repository. Follow these steps:

1. **Add your changes**

    ```sh
    git add .
    ```

2. **Commit your changes**

    ```sh
    git commit -m "Your descriptive commit message"
    ```

3. **Push your changes**

    ```sh
    git push origin exp_trail_evaluations
    ```


If you are not a contributor to the repository, consider forking the repository and submitting a pull request with your changes.


## Usage

After running the above command, the web application should be accessible in your web browser. Open your browser and navigate to the URL provided in the terminal.

## Troubleshooting

If you encounter any issues, ensure that all prerequisites are installed and the virtual environment is activated. Additionally, ensure all dependencies are correctly installed from `llm-agent/requirements.txt`.
