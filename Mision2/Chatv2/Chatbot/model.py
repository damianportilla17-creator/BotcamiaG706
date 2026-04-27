import os # Trabaja con el sistema operativo
import pickle# Guarda y carga objetos de python en archivos
from sklearn.feature_extraction.text import CountVectorizer
# CountVectorizer convierte texto en un vector
from sklearn.naive_bayes import MultinomialNB
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR,"answers.pkl")

def build_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs] # Lista de preguntas
    answers = [a for _, a in train_pairs] #lista de respuestas
    vectorize = CountVectorizer()
    x = vectorize.fit_transform(questions)
    unique_answer = sorted(set(answers))
    answers_to_label ={a:i for i, a in  enumerate(unique_answer)}
    y = [answers_to_label[a] for a in answers]
    model = MultinomialNB()
    model.fit(x,y)
    # Crear carpeta para guardar el modelo si no exite 
    os.makedirs(MODEL_DIR,exit_ok=True)
    #Guardar los objetos entrenados 
    with open(MODEL_PATH,"wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH,"wb") as f:
        pickle.dump(vectorize,f)
    with open(ANSWERS_PATH,"wb") as f:
        pickle.dump(unique_answer,f)
    print("🆗 Modelo entrenado y guardado correctamente")
    return model, vectorize, unique_answer

def load_model():
    if(
        os.path.exists(MODEL_PATH)
        and os.path.exists(VECTORIZER_PATH)
        and os.path.exists(ANSWERS_PATH)
    ):
        with open(MODEL_DIR,"rb") as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH,"rb") as f:
            vectorize = pickle.load(f)
        with open(ANSWERS_PATH,"rb") as f:
            unique_answers = pickle.load(f)
        print("📁 Modelo cargando desde disco.")
        return model, vectorize, unique_answers
    else:
        print("⚠️ No hay modelo guardado. Será necesario entrenarlo")
        return None,None,None
    def predict_answer(model,vectorize,unique_answers,user_text):
        X = vectorize.transfor ([user_text])
        label = model.predict(x)[0]
        return unique_answers[label]
