# SmartSeller AI 🛍️🤖

An open-source AI-powered product description generator built with Python, Ollama, and Qwen2.5.

## About the Project

SmartSeller AI helps small businesses, students, and online sellers create attractive product descriptions using artificial intelligence.

Instead of writing descriptions manually, users enter their product name, price, and special features. SmartSeller AI then generates a description using a locally running AI model.

## Features

- AI-generated product descriptions
- Simple command-line interface
- Supports product names, prices, and special features
- Uses the open-weight Qwen2.5 model
- Runs locally using Ollama
- No paid API key required
- Free and open-source Python code

## Technologies Used

- Python 3
- Ollama
- Qwen2.5 (0.5B)
- Requests library

## Installation

### Step 1: Install Python

Download Python from https://www.python.org/

### Step 2: Install Ollama

Download Ollama from https://ollama.com/download

### Step 3: Download the AI Model

Open Terminal and run:

```bash
ollama pull qwen2.5:0.5b
```

### Step 4: Download SmartSeller AI

Clone this repository:

```bash
git clone https://github.com/thebugbag/SmartSeller-AI.git
cd SmartSeller-AI
```

### Step 5: Install Python Dependencies

```bash
python3 -m pip install requests
```

### Step 6: Run SmartSeller AI

Make sure Ollama is running, then execute:

```bash
python3 app.py
```

## Example

**Input:**

Product: Handmade Lavender Candle

Price: Rs. 199

Special Feature: Handmade with natural lavender fragrance

**Output:**

SmartSeller AI generates a product description based on the details entered by the user.

The exact price is also displayed separately.

## Limitations

AI-generated descriptions may occasionally include incorrect or invented product details.

Users should review and verify descriptions before publishing them.

## Why Open Source?

SmartSeller AI demonstrates how open-source software and open-weight AI models can make useful AI tools accessible without expensive subscriptions.

Developers can study the code, suggest improvements, and contribute new features.

## Future Improvements

- Better description accuracy
- Multiple languages
- Different writing styles
- Web interface
- Product category selection

## License

This project is licensed under the MIT License.

## Created For

Hacktoberfest 2026 — DEV Community AI Challenge.
