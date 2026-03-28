# 📄 PDF Summarizer

An AI-powered PDF summarizer built with Python (Flask) and Claude API. Drag & drop any PDF and get an instant structured summary.

---

## ✨ Features

- Drag & drop or browse to upload any PDF
- AI-generated summary with main topic, key points & conclusion
- Clean dark-themed UI
- Local Flask backend (no CORS issues)
- Your files are never stored

---

## 🖥️ Preview

```
[ Drop your PDF here ]
        ↓
[ ✦ Summarize PDF ]
        ↓
  ✦ Summary
  1. Main Topic
  2. Key Points
  3. Conclusion
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pdf-summarizer.git
cd pdf-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Anthropic API key

Open `server.py` and replace the placeholder:

```python
client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")
```

Get your API key at 👉 https://console.anthropic.com

### 4. Run the server

```bash
python server.py
```

You should see:
```
✅ PDF Summarizer server running at http://localhost:5000
```

### 5. Open the app

Open `pdf_summarizer.html` in your browser — no extra setup needed.

---

## 📁 Project Structure

```
pdf-summarizer/
├── server.py            # Flask backend
├── pdf_summarizer.html  # Frontend UI
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Layer    | Technology          |
|----------|---------------------|
| Frontend | HTML, CSS, JS       |
| Backend  | Python, Flask       |
| AI       | Claude (Anthropic)  |

---

## ⚙️ How It Works

1. User drops a PDF onto the page
2. The browser converts it to Base64 and sends it to the Flask server
3. Flask forwards it to the Claude API
4. Claude reads the PDF and returns a structured summary
5. The summary is displayed in the browser

---

## 📋 Requirements

- Python 3.8+
- An Anthropic API key (free tier available)
- Any modern browser

---
