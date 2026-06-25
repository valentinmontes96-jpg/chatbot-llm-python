import os
import google.generativeai as genai

#Configurar la API KEY 
API_KEY = "AQ.Ab8RN6IpfIuKe3foi6ut2AXZglRAgSscPQOVAhcOnSlUo1xz8A"
genai.configure(api_key=API_KEY)

#Definir el System Prompt 
instrucciones_sistema = (
    "Eres un tutor experto en programación de sistemas. "
    "Responde siempre en español. Tus respuestas deben ser  "
    "directas y cordiales. Si te preguntan algo que no sea de tecnología "
    "o programación, indica amablemente que tu enfoque es exclusivamente técnico."
)

#Configurar el modelo y sus parámetros
modelo = genai.GenerativeModel(
    model_name='gemini-2.5-flash', 
    system_instruction=instrucciones_sistema
)


chat = modelo.start_chat(history=[])


while True:
    
    entrada_usuario = input("\n Usuario: ")

    
    if entrada_usuario.lower() in ['salir', 'exit', 'quit']:
        print("\n Asistente: ¡Hasta luego! Éxitos con tu código.")
        break

    try:
        
        respuesta = chat.send_message(entrada_usuario)
        
        
        print(f" Asistente: {respuesta.text}")
        
    except Exception as e:
        print(f"\n Error al comunicarse con la API: {e}")