from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ChatAdministratorRights, ChatPermissions
import os
from db import DB
import datetime
TOKEN=os.environ['TOKEN']





def start(update:Update, context:CallbackContext):
    bot=context.bot
    user_id=update.message.from_user.id
    chat_id=update.message.chat_id
    first_name=update.message.from_user.first_name
    #last_name=update.message.from_user.last_name
    text=f'Assalomu alaykum {first_name}'
    db=DB('db.json')
   # db.starting(user_id)
    db.save()

    if update.message.chat.type=='private':
         bot.send_message(chat_id=chat_id, text=text)
         text=f'Tilni tanlang'
         uzbek_tili=InlineKeyboardButton("Uzbek tili 🇺🇿", callback_data='uzbek_tili')
         rus_tili=InlineKeyboardButton('Rus tili 🇷🇺', callback_data='rus_tili')
         #tojik_tili=InlineKeyboardButton('Tojik tili 🇹🇯', callback_data='tojik_tili')
         button=InlineKeyboardMarkup([[uzbek_tili, rus_tili]])
         bot.sendMessage(chat_id=chat_id, text=text, reply_markup=button)
def query(update: Update, context: CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=query.data
    bot=context.bot
    
    

    if data=='uzbek_tili':
       # bot.send_contact(chat_id=chat_id, phone_number="+998904776646", first_name='sooft_admin')
         keyboard=ReplyKeyboardMarkup([
            ['Routerlar 🌐', 'Monitorlar 🖥', "Kameralar 📸"],
            ['🚖 Mashinaga GPS navigator', 'Elektron eshik qulfi 🔐'],
            ['Televizorlar va boshqa mahsulotlar'],
            ['Asosiy Menuga qaytish ⬅️']
         ], resize_keyboard=True)
         text="Xurmatli mijoz siz bu bot orqali uzingizni qiziqtirgan savollarga javob topishingiz mumkin!"
         bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)
    else:
        keyboard=ReplyKeyboardMarkup([
            ['Роутеры 🌐', 'Мониторы 🖥', 'Камеры 📸'],
            ['🚖 Автомобильный GPS навигатор', "Электронный замок 🔐"],
            ["Телевизоры и другие товары"],
            ['Вернуться в главное меню ⬅️']


        ], resize_keyboard=True)
        text="Уважаемый клиент, вы можете найти ответы на свои вопросы через этого бота!"   
        bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)  
    return 'OK'    
def router_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11379", caption="4G router sim kartali\n🔸Model: CPF 903\n🔸IMEI ro’yhatidan o’tgan.\n⚡️ Narxlar SUPPER\n1dona 35\n10 dona   30\n30 dona 28\n☎️+998333344442\n☎️+998906051221" ) 
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11146", caption="Yangi 4G ROUTER keldi\nNarxi: 56$\n☎️ +998906051221\n☎️ +998333344442")
def monitor_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11508", caption="Sam Smart Security Servicesdan\nDahua monitor 27\nЦена: 180$\nTel:+998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11298")
def kameralar_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11489", caption="«Sam Smart Security Services» jamoasi signalizatsiya qurilmasiga ega super kamerani taqdim etadi! 😇\nKamera modeli:👇🏻\n✅ HFW3449T1P-AS-PV\nUshbu kamerani siz bizning doʻkonlarimizdan eng qulay narxlarda topasiz! 💪🏻\nKamera uxlab qolgan qo'riqchilarga qaraganda ancha yaxshiroq! 😆\nBiz bilan bog‘laning va ko‘proq ma’lumotga ega bo‘ling:\n☎️ +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11481', caption="Har bir ota-ona o'z farzandini bolalar bog'chasida yoki enaga bilan qoldirayotib, u haqida tashvishlanadi! 🤔\n«Sam Smart Security services» jamoasi farzandingiz nazorati uchun sizlarga ajoyib kamerani taqdim etadi! 😎\nNarxi: 400.000 soʻm\nModel: ✅ CUE2 Imou\nHoziroq do'konimizga tashrif buyuring yoki bizga murojaat qilib ushbu kameraga eng qulay narxda ega bo'lishga shoshiling! 👌🏻\nOnline konsultant: ↙️\n@Finansist786\nBatafsil ma’lumot uchun:\n☎️ +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11487", caption="«Sam Smart Security Services» Mijozlari uchun navbatdagi Full color kamerani taqdim etadi! 😎\nHa albatta yoriq tasvir sari yuqori aniqlikni aynan bizda koʻrasiz! ✅\nKamera modeli: 👉🏻 HFW 2439 SP-SA-LED  \nNarxi:💰766.000 soʻm\n«Sam Smart Security Services» Kechayu kunduz samarali va aniq tasvirga olish imkoniyatiga ega boʻlgan kameralarni sizga taqdim etib kelishdan toʻxtamaydi, va albatta hamyonbop narxlar ham shu oʻrinda turadi! 👌🏻\nBatafsil ma’lumot uchun:\n☎️ +998906051221")
def gps_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11477", caption="Sam Smart Security servicesdan\n📌🚖Mashinaga GPS navigator o'rnatishning eng qulay taraflari.\n— Mashinaning 1 xafta mobaynida yurgan joylarini saqlab borishi va masofa km larini xisoblashi.\n— Kuzatish uchun kompyuter va mobil ilovalari borligi.\n— Mashinani nasiya savdoga yoki ijaraga berganda, nazorat qilish uchun juda qulay. (dastur orqali mashinani o'chirib qo'yish mumkin)\n— Davlat va korxona mashinalari uchun barcha mashinalarni hisobotini olishda juda qulay.\n— GPS bo'yicha doimiy service markaz borligi.\n— O'rnatish va o'rgatish ishlari bepul.\nQo'shimcha savollar uchun:\n☎️ +998906051221\n☎️ +998333344442")
def qulf_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11380", caption="Oynali eshiklar uchun otpechatkalik zamok!!!\nNarxi: 230$ \nDomofonga ulash moduli aloxida 50$\n☎️+998333344442\n☎️+998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11491", caption="«Sam Smart Security Services» Jamoasidan uyingiz uchun ajoyib elektron eshik qulfi! 💪🏻\nKoʻrib turgan ushbu qulfingizni siz barmoq izi va maxsus karta orqali ochish imkoniyatiga egasiz asosiysi esa oʻzingiz istagan parolni oʻrnatib xavfsizligingizni toʻliq taʼminlashingiz mumkin! ✅\n\nNarxi:💰2.888.000\nModel:📌 Imou Smart Lock K2\nOnline konsultant: ↙️\n@Finansist786\nBatafsil ma’lumot uchun:\n☎️ +998906051221")
def tv_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11474", caption="Телевизор Artel 32 Led tv/n110$\nTel: +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11297", caption="Телевизор Artel 43 Led tv.")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11302", caption="Sam Smart Security services\nSandisk Cruzer Glide3️⃣🔤0️⃣\n🔤🔤🔤🔤🔤🔤🔤🔤\nPrice💲\n16GB - 4.8\n32GB - 5.3\n64GB - 7.5\n128GB - 11\nTEL: 33 334 44 42 ☎️")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11375")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11455")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11383")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11252')
def router_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11146", caption="ПРИБЫЛ НОВЫЙ Роутеры 4G\nцена 56 $\n☎️ +998906051221\n☎️ +998333344442")

    
    
   






updater=Updater(token=TOKEN)

dp=updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text('Asosiy Menuga qaytish ⬅️'), start))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
dp.add_handler(MessageHandler(Filters.text('Routerlar 🌐'), router_uz))
dp.add_handler(MessageHandler(Filters.text('Monitorlar 🖥'), monitor_uz))
dp.add_handler(MessageHandler(Filters.text("Kameralar 📸"), kameralar_uz))
dp.add_handler(MessageHandler(Filters.text('🚖 Mashinaga GPS navigator'), gps_uz))
dp.add_handler(MessageHandler(Filters.text('Elektron eshik qulfi 🔐'), qulf_uz))
dp.add_handler(MessageHandler(Filters.text('Televizorlar va boshqa mahsulotlar'), tv_uz))
dp.add_handler(MessageHandler(Filters.text("Роутеры 🌐"), router_rus))

updater.start_polling()
updater.idle()

