import telebot
import google.generativeai as genai

# 1. TERA TOKEN AUR API KEY
BOT_TOKEN = "8819011127:AAFhSkNexT5-dOXLnPe_g_SrpGk89_Xxbws"
GEMINI_API_KEY = "AQ.Ab8RN6J920p9f36jSZzTfjgdCwiZPOTDRSPXzLGlWYfXikj9WQ"

# 2. AI DIMAAG SETUP
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(BOT_TOKEN)
BOT_NAME = "sasta babu"

# 3. CHAT ENGINE
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    text = message.text.lower()
    is_private = message.chat.type == 'private'
    
    if is_private or BOT_NAME in text:
        bot.send_chat_action(message.chat.id, 'typing') 
        clean_text = text.replace(BOT_NAME, "").strip()
        
        if clean_text == "":
            bot.reply_to(message, "Haan boss, Sasta Babu hazir hai! Kya haal hain?")
            return
            
        try:
            prompt = f"""
            Tu ek bohot smart, funny, aur desi Indian dost hai jiska naam 'Sasta Babu ✨' hai.
            Tera kaam user ke sawalon ka jawab ekdum natural aur dosti wale andaz me dena hai.
            Tu Hinglish (Hindi written in English alphabet) me baat karta hai.
            Tere jawab me attitude, emojis aur thoda humor hona chahiye.
            User ka sawal: {clean_text}
            """
            response = model.generate_content(prompt)
            bot.reply_to(message, response.text)
        except Exception as e:
            print(f"Error: {e}")
            bot.reply_to(message, "Bhai tera AI dimaag load nahi le pa raha. Shayad API Key galat hai, nayi (AIza... wali) key daal!")

print("🔥 Sasta Babu Render par zinda ho gaya hai!...")
bot.infinity_polling(skip_pending=True)
