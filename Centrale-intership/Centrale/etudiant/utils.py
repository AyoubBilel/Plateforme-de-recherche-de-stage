# chatbot/utils.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key="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"

def chat_with_gpt(sector, message, question_num):
    if question_num == 0:
        system_message = f"Vous êtes un entraîneur virtuel spécialisé dans la préparation des étudiants pour des entretiens de stage dans le secteur {sector}. Vous poserez des questions une par une et donnerez un retour constructif sur les réponses. Si une réponse est hors sujet, indiquez-le clairement et demandez une nouvelle réponse. Si une réponse est intéressante, demandez des détails supplémentaires."
        introduction_message = f"Bonjour ! Je suis votre entraîneur virtuel et je vais vous aider à vous préparer pour vos entretiens dans le secteur {sector}. Nous allons commencer par une série de questions pour simuler un entretien réel. Soyez prêt à répondre honnêtement et de manière détaillée. Commençons !"
        first_question = "Pouvez-vous me parler de vous et de votre parcours académique et professionnel ?"
        return introduction_message, first_question  # Retourner le message d'introduction et la première question
    else:
        system_message = f"Continuez l'entretien dans le secteur {sector}. Posez la question suivante et donnez un retour constructif sur la réponse précédente. Si une réponse est hors sujet, indiquez-le clairement et demandez une nouvelle réponse. Si une réponse est intéressante, demandez des détails supplémentaires."
        user_message = f"Réponse de l'étudiant: {message}"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150  # Ajuster selon vos besoins
        )
        return None, response.choices[0].message.content



import openai
import re

def generate_feedback_and_grade(list_question_reponse):
    feedback_message = "Voici un feedback sur vos réponses :\n\n"
    positive_feedback = "Félicitations pour les réponses suivantes, qui étaient pertinentes et bien formulées :\n"
    improvement_feedback = "Pour les réponses suivantes, voici quelques suggestions pour vous améliorer :\n"
    encouragement_message = "\nContinuez à vous entraîner afin de vous améliorer. Bon courage pour vos futurs entretiens !"
    
    total_score = 0
    max_score = 20
    criteria_points = {
        "pertinence": 5,
        "clarity": 5,
        "knowledge": 5,
        "structure": 5
    }

    system_messages = []

    for i in range(len(list_question_reponse['reponse'])):
        question = list_question_reponse['question'][i]
        user_response = list_question_reponse['reponse'][i]
        
        # Message système pour l'analyse de la réponse
        system_message = {
            "role": "system",
            "content": f"Veuillez analyser ma réponse suivante en fonction de la question posée et fournir un retour détaillé selon les critères suivants : pertinence (5 points), clarté (5 points), connaissance du sujet (5 points) et structure de la réponse (5 points). \n\nQuestion : {question} \n\nRéponse : {user_response} \n\nMerci de fournir une évaluation pour chaque critère et une note globale sur 20."
        }
        system_messages.append(system_message)

    # Appel à l'API OpenAI pour obtenir le feedback
    feedback_responses = openai.ChatCompletion.create(
        model="gpt-4",
        messages=system_messages,
        max_tokens=150 * len(system_messages)  # Ajuster selon vos besoins
    ).choices

    for i, feedback in enumerate(feedback_responses):
        feedback_text = feedback.message.content
        
        # Analyse du feedback pour déterminer les points
        scores = re.findall(r'\b(\d{1,2})\b', feedback_text)
        if scores and len(scores) == 4:
            scores = list(map(int, scores))
            score = sum(scores) / len(scores)
        else:
            score = 0

        total_score += score
           
        improvement_feedback += f"\n Question {i + 1}: {feedback_text}\n"

    # Calcul de la note finale
    final_score = (total_score * max_score) / (len(list_question_reponse['reponse']) * max(criteria_points.values()))
    grade_message = f"\nVotre note finale est : {final_score:.2f}/20"

    return[ feedback_message , positive_feedback , improvement_feedback , encouragement_message , grade_message]
