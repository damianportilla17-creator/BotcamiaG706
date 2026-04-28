from Chatbot.data import training_data
from Chatbot.model import build_and_train_model,load_model,predict_answer
def chat(model,vectorize,unique_answers):
    """Inicia el modo de conversacion"""
    print("\n 🤖 Chatbot listo. Escribe 'salir' para terminar. \n")
    while True:
        user = input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("bot: !Hasta pronto¡")
            break
        response = predict_answer(model,vectorize,unique_answers,user)
        print("Bot: ", response)

def main():
    model, vectorize, unique_answer = load_model()
    # Menu principal
    while True:
        print("\n== 🤖  MENU PRINCIPAL DEL CHATBOT ==")
        print("1️⃣    Chatear con el modelo")
        print("2️⃣    Reentrenar el modelo")
        print("3️⃣    Salir")
        opcion = input("\n Elige una opcion (1-3); ").strip()
        if opcion == "1":
            if model is None:
                print("\n ⚠️ No hay modelo entrenado. Entrenalo primero.")
            else:
                chat(model,vectorize,unique_answer)
        elif opcion == "2":
            print("\n 🔁 Reentrenar el modelo con los nuevos datos...")
            model,vectorize,unique_answer = build_and_train_model(training_data)
            print("✅ Modelo actualizado correctamente.")
        elif opcion == "3":
            print("\n 👋 ¡Hasta luego!")
            break
        else:
            print("\n ❌ Opcion no valida. Intenta nuevamente")
if __name__ == "__main__":
    main()