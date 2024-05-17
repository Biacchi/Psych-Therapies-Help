from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.form

    # Define weights for different symptoms
    weights = {
        'anxiety': int(answers['anxiety']),
        'depression': int(answers['depression']),
        'stress': int(answers['stress']),
        'trauma': int(answers['trauma']),
        'relationship': int(answers['relationship']),
        'self_esteem': int(answers['self_esteem']),
        'anger': int(answers['anger']),
        'mood_swings': int(answers['mood_swings']),
        'grief': int(answers['grief']),
        'obsessions': int(answers['obsessions'])
    }

    # Initialize scores for each therapy type
    therapy_scores = {
        'CBT': 0,
        'DBT': 0,
        'ACT': 0,
        'Psychodynamic': 0,
        'ABA': 0,
        'Systemic': 0,
        'Humanistic': 0,
        'MBCT': 0
    }

    # Define the logic for scoring
    therapy_logic = {
        'CBT': ['anxiety', 'depression', 'obsessions'],
        'DBT': ['stress', 'relationship', 'mood_swings', 'anger'],
        'ACT': ['trauma', 'self_esteem', 'grief'],
        'Psychodynamic': ['self_esteem', 'relationship'],
        'ABA': ['obsessions', 'anger'],
        'Systemic': ['relationship'],
        'Humanistic': ['self_esteem', 'grief'],
        'MBCT': ['stress', 'anxiety', 'depression']
    }

    # Calculate scores for each therapy type
    for therapy, symptoms in therapy_logic.items():
        therapy_scores[therapy] = sum(weights[symptom] for symptom in symptoms)

    # Determine the best therapy based on the highest score
    recommended_therapy = max(therapy_scores, key=therapy_scores.get)

    return render_template('result.html', recommended_therapy=recommended_therapy)

if __name__ == '__main__':
    app.run(debug=True)
