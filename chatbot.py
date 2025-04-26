

import time

def chat():
    print("Salom! Men oddiy chatbotman. Savolingizni bering.")
    
    while True:
        user_input = input(">>> ").lower()

        if 'exit' in user_input:
            print("Hayr! Yana ko‘rishguncha!")
            break
        elif 'salom' in user_input or 'hi' in user_input:
            print("Salom! Sizni ko‘rib xursandman!")
        elif 'isming nima' in user_input or 'isming' in user_input:
            print("Mening ismim ChatBot 1.0!")
        elif 'yaxshisanmi' in user_input or 'yaxshi' in user_input:
            print("Rahmat, yaxshi! Sizchi?")
        elif 'bugun qanday ob-havo' in user_input:
            print("Kechirasiz, men hozirgi ob-havo haqida ma'lumot bera olmayman.")
        elif 'vaqtni ayt' in user_input or 'soat' in user_input:
            current_time = time.strftime("%H:%M:%S")
            print(f"Hozirgi vaqt: {current_time}")
        elif 'yoshingni ayt' in user_input or 'yoshing' in user_input:
            print("Men robotman, yoshim yo'q!")
        elif 'hayr' in user_input or 'xayr' in user_input:
            print("Hayr! Yana ko‘rishguncha!")
        else:
            print("Kechirasiz, bu savolga javob bera olmayman.")

chat()

