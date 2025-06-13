# Clarifai Llama 3 Chat

A simple Python application that demonstrates how to use Clarifai's Llama 3 model through their Python SDK.

## 🚀 MLH GHW Clarifai Challenge 2025

This project was created as part of the MLH Global Hack Week 2025 Clarifai Challenge. It showcases how to integrate with Clarifai's API using their Python SDK with the Llama 3 model.

## 🛠️ Prerequisites

- Python 3.8+
- A Clarifai account (free tier available)
- A Clarifai Personal Access Token (PAT)

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/mlh-hello-clarifai.git
   cd mlh-hello-clarifai
   ```

2. **Set up a virtual environment**
   ```bash
   # On Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Get your Clarifai PAT from [Clarifai Security Settings](https://clarifai.com/settings/security)
   - Add your PAT to the `.env` file:
   ```
   CLARIFAI_PAT=your_personal_access_token_here
   ```

## 🎮 Usage

Run the interactive chat:
```bash
python clarifai_chat.py
```

You'll see a prompt where you can type your messages. Type 'quit' to exit the application.

## 🤖 Model Used

This project uses the Llama 3 2-3B Instruct model from Meta, available through Clarifai's platform:
- Model URL: `https://clarifai.com/meta/Llama-3/models/Llama-3_2-3B-Instruct`

## 📝 Notes

- The application uses the free tier of Clarifai's API
- Make sure to keep your `.env` file secure and never commit it to version control
- The `.gitignore` file is already configured to exclude sensitive files and virtual environment directories
python clarifai_chat.py
```

Or import and use the `chat_with_gpt4` function in your own code:

```python
from clarifai_chat import chat_with_gpt4

response = chat_with_gpt4(
    prompt="Tell me a joke about AI",
    system_message="You are a helpful assistant.",
    temperature=0.7,
    stream=False
)
print(response)
```

## 🔧 Configuration

- `CLARIFAI_PAT`: Your Clarifai Personal Access Token (required)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
