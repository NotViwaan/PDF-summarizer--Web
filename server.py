from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import anthropic
import base64
import os

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")

# Serve the frontend
@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        pdf_base64 = data.get("pdf")

        if not pdf_base64:
            return jsonify({"error": "No PDF provided"}), 400

        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "base64",
                                "media_type": "application/pdf",
                                "data": pdf_base64,
                            },
                        },
                        {
                            "type": "text",
                            "text": """Please provide a clear, well-structured summary of this PDF document. Include:
1. **Main Topic** — What is this document about?
2. **Key Points** — The most important ideas or findings (3–6 bullet points)
3. **Conclusion** — Main takeaway or purpose of the document

Keep the summary concise but informative."""
                        }
                    ],
                }
            ],
        )

        summary = message.content[0].text
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("✅ PDF Summarizer server running at http://localhost:5000")
    app.run(debug=True, port=5000)
