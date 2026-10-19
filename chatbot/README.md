# HR Chatbot Assistant

A simple Streamlit chatbot that answers HR-related questions using the OpenAI API.

## Prerequisites

- Python 3.10 or later
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

### 1. Go to the project folder

```powershell
cd chatbot
```

### 2. Create a virtual environment

A virtual environment keeps this app’s packages separate from your global Python install.

**Windows (PowerShell):**

```powershell
py -m venv .venv
```

**macOS / Linux:**

```bash
python3 -m venv .venv
```

This creates a `.venv` folder inside `chatbot`.

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run this once, then try again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

When it is active, your prompt usually starts with `(.venv)`.

To leave the virtual environment later:

```powershell
deactivate
```

### 4. Install dependencies

With the virtual environment activated:

```powershell
pip install -r requirements.txt
```

### 5. Add your OpenAI API key

Create a `.env` file in the `chatbot` folder:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not commit this file. It is already listed in `.gitignore`.

## Run the app

From the `chatbot` folder, with the virtual environment activated:

```powershell
py -m streamlit run app.py
```

Then open the URL shown in the terminal (usually [http://localhost:8501](http://localhost:8501)).

## Quick reference

| Step | Windows PowerShell |
|------|--------------------|
| Create venv | `py -m venv .venv` |
| Activate venv | `.\.venv\Scripts\Activate.ps1` |
| Install packages | `pip install -r requirements.txt` |
| Run app | `py -m streamlit run app.py` |
| Deactivate venv | `deactivate` |

## Usage

- Type an HR-related question in the chat input.
- The assistant replies using OpenAI (`gpt-4.1`).
- Non-HR questions are declined by the system prompt.
