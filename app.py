from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    input_lang = data.get("input_lang", "en")
    target_lang = data.get("target_lang", "")

    try:
        translator = Translator()
        translated_text = translator.translate(text, src=input_lang, dest=target_lang).text
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
