import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/answer', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Invalid request"}), 400

        prompt = data['prompt']
        if not isinstance(prompt, str) or len(prompt) > 1000:
            return jsonify({"error": "Invalid prompt"}), 400

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um profissional especialista em uma comunidade quilombola no interior de alagoas que foi parte do quilombo dos palmares antigamente hoje tem uma cultura de manofatura baseado na agricultura e herda muito da cultura alagoana com danças típicas como o reizado e seu dever é ajudar os professores a criar planos de aula."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        return jsonify({"response": response.choices[0].message.content}), 200

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=False)