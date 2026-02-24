import os
import datetime



def chatbot():
    print("Merhaba! Ben basit bir chat botum. Çikmak için 'çik' yazabilirsin.")
    while True:
        user_input = input("Sen: ").lower()
        
        if user_input == "çik":
            print("Chat bot: Görüşmek üzere!")
            break
        elif "merhaba" in user_input:
            print("Chat bot: Merhaba! Nasilsin?")
        elif "nasılsın" in user_input:
            print("Chat bot: Ben iyiyim, sen nasilsin?")
        elif "adın ne" in user_input:
            print("Chat bot: Benim adim ChatBot.")
        elif "nerelisin" in user_input:
            print("Chat bot: Python dünyasindan geliyorum!")
        elif "senin görevin ne" in user_input:
            print("Chat bot: Benim görevim, belirlenen sorulara cevap vermek ve sohbet etmektir.")
        elif "tarih" in user_input:
            today = datetime.date.today()
            print(f"Chat bot: Bugünün tarihi {today}.")
        elif "saat" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chat bot: Şu an saat {now}.")
        elif "kullanıcı" in user_input:
            user = os.getlogin()
            print(f"Chat bot: Senin kullanici adin: {user}")
        elif "dizin" in user_input:
            cwd = os.getcwd()
            print(f"Chat bot: Şu anki dizin: {cwd}")
        elif "işletim sistemi" in user_input:
            print(f"Chat bot: İşletim sistemi: {os.name}")
        elif "şuan hangi şehirdeyiz" in user_input:
            print(f"Chat bot: Türkiye nin isparta ilinin Uluborlu  ilçesindeyiz")
        elif "hangi takimi tutuyorsun" in user_input:
            print(f"Chat bot: Kütahya  spor takmini tutuyorum")
        
        else:
            print("Chat bot: Bunu anlayamadim, başka bir şey söylemek ister misin?")
        



chatbot()
os.system("cls")