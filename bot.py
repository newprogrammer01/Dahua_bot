from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ChatAdministratorRights, ChatPermissions
import os
from db import DB
import datetime
TOKEN=os.environ['TOKEN']
import json





def start(update:Update, context:CallbackContext):
    bot=context.bot
    user_id=update.message.from_user.id
    chat_id=update.message.chat_id
    first_name=update.message.from_user.first_name
    text=f'Assalomu alaykum {first_name}'
    if update.message.chat.type=='private':
         bot.send_message(chat_id=chat_id, text=text)
         text=f'Tilni tanlang'
         uzbek_tili=InlineKeyboardButton("Uzbek tili 🇺🇿", callback_data='uzbek_tili')
         rus_tili=InlineKeyboardButton('Rus tili 🇷🇺', callback_data='rus_tili')
         

         button=InlineKeyboardMarkup([[uzbek_tili, rus_tili]])
         bot.sendMessage(chat_id=chat_id, text=text, reply_markup=button)

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
    chat_id=update.message.chat_id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11380", caption="Oynali eshiklar uchun otpechatkalik zamok!!!\nNarxi: 230$ \nDomofonga ulash moduli aloxida 50$\n☎️+998333344442\n☎️+998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11491", caption="«Sam Smart Security Services» Jamoasidan uyingiz uchun ajoyib elektron eshik qulfi! 💪🏻\nKoʻrib turgan ushbu qulfingizni siz barmoq izi va maxsus karta orqali ochish imkoniyatiga egasiz asosiysi esa oʻzingiz istagan parolni oʻrnatib xavfsizligingizni toʻliq taʼminlashingiz mumkin! ✅\n\nNarxi:💰2.888.000\nModel:📌 Imou Smart Lock K2\nOnline konsultant: ↙️\n@Finansist786\nBatafsil ma’lumot uchun:\n☎️ +998906051221")
def tv_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11474", caption="Телевизор Artel 32 Led tv/n110$\nTel: +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11297", caption="Телевизор Artel 43 Led tv.")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11302", caption="Sam Smart Security services\nSandisk Cruzer Glide3️⃣🔤0️⃣\n🔤🔤🔤🔤🔤🔤🔤🔤\nPrice💲\n16GB - 4.8\n32GB - 5.3\n64GB - 7.5\n128GB - 11\nTEL: 33 334 44 42 ☎️")
   # bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11375")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11455")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11383")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11252')
def router_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11146", caption="ПРИБЫЛ НОВЫЙ Роутеры 4G\nцена 56 $\n☎️ +998906051221\n☎️ +998333344442")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11379", caption="4G роутер с SIM-картой.\n🔸Модель: ЦПС 903\n🔸 IMEI зарегистрирован.\n⚡️ СУПЕР цены\n1 штук 35\n10 штук 30\n30 штук 28\n☎️+998333344442\n☎️+998906051221")
def monitor_rus(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11319")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11298")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11293')
def kameralar_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11291", caption="Sam smart security services\n🚀 IP камера Full-Color с двойной подсветкой это инновационный продукт в сфере видеонаблюдения. \nВ данной камере собраны самые необходимые функции для полноценной безопасности вашего окружения.\n🧠 Аналитика с помощью ИИ, \n🕺🏼умное обнаружение движения,\n 🅿️ протекция периметра, полноцветное изображение ночью - все это доступно в одном устройстве. \n💸Наличие карты памяти сэкономит ваши расходы, \n🔊а микрофон даст возможность просмотреть видео со звуком.")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11290', caption="Sam Smart Security services\n⚡️ Представляем лучшую полноцветную камеру видеонаблюдения с разрешением 5 МП! Благодаря качеству видео высокой четкости вы сможете запечатлеть каждую деталь и цвет с невероятной точностью. Независимо от того, охраняете ли вы свой дом или бизнес, эта камера идеально подходит для любых нужд наблюдения.\n🚀 Благодаря передовой технологии ночного видения вы сможете легко контролировать свою собственность 24 часа в сутки 7 дней в неделю.\n🌃 Попрощайтесь с размытыми или искаженными изображениями и поприветствуйте кристально чистые кадры, которые помогут вам, быть в курсе любой ситуации. Защитите то, что для вас важнее всего, с помощью 5-мегапиксельной Full-Color камеры видеонаблюдения. \n🔻 Закажите сейчас и испытайте новый уровень безопасности и спокойствия!\n\n___\n\nБезопаснее общество, качественнее жизнь")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11567", caption="Мы устанавливаем камеры видео-наблюдения быстро и  качественно 💯\nМонтаж 💻✅ \nУстановка 🛠✅\nПожарная сигнализация 🖲✅\nУстановка по всем городам и районам Республики Каракалпакстан\n𝙰𝚍𝚖𝚒𝚗☛ @Finansist786\n👇 Для связи\n +998333344442\n+998906051221")
def gps_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11476", caption="Сэм Смарт Секьюрити\n📌🚖Самые удобные аспекты установки GPS навигатора в автомобиль.\n\n- 1-недельное отслеживание пробега автомобиля и расчет пробега.\n— Наличие компьютерных и мобильных приложений для мониторинга.\n- Очень удобно контролировать, когда автомобиль продается или сдается в аренду нацией. (можно удалить программным обеспечением машины)\n- Очень удобно получать отчет по всем машинам для государственных и корпоративных машин.\n— Наличие постоянного сервисного центра GPS.\n- Установка и обучение бесплатно.\nПо дополнительным вопросам:\n☎️ +998906051221\n☎️ +998333344442")  
def qulf_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11491", caption="Отличный электронный дверной замок для вашего дома от Sam Smart Security Services! 💪🏻\nВы можете открыть этот замок с помощью отпечатка пальца и специальной карты, и, самое главное, установить пароль по вашему выбору и оставаться в безопасности! ✅\nЦена: 💰2 888 000\nНомер модели: 📌 Умный замок Imou K2\n\n\nОнлайн-консультант: ↙️\n@financier786\nДля дополнительной информации:\n☎️ +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11380', caption="Замок для стеклянных дверей!!!\nЦена: 230 долларов США\nМодуль подключения домофона - $50 отдельно\n☎️+998333344442\n☎️+998906051221")
def tv_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11561", caption="ST3108S – неуправляемый коммутатор ( ХАБ )  Netis Systems, (https://wifimag.ru/cat/netis/) имеющий 8 Fast Ethernet портов 10/100 Мбит с автосогласованием скорости соединения. Идеален для использования в малых и средних офисах.\n\n\n☎️ +998902814746")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11545", caption="TL-SG1024D представляет собой доступное и высокопроизводительное устройство, предназначенное для усовершенствования вашей сети до гигабитных скоростей. Все 24 порта поддерживают функцию авто-MDI/MDIX - больше не нужно думать о типе кабеля, просто подключите кабель к устройству, и оно будет работать. Более того, применение инновационной ⚠️энергосберегающей технологии позволит сберегать до 25% потребляемой электроэнергии, а 80% упаковочного материала может быть повторно переработано,♻️  \nблагодаря чему устройство представляет собой экологичное решение для вашей сети.✅")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11539", caption="Принтер для маркировки PT-E550WVP с расширенным набором функций для электриков | Brother\n\nОсновные характеристики\n• Печать с ПК и смартфона\n• Выделенные кнопки для распространенных электрических маркировок\n• Большой дисплей с подсветкой\n• Автоматическая обрезка и полуобрезка ленты\n• Комплект включает в себя кассету, литий-ионный аккумулятор, адаптер переменного тока и кейс для переноски\n• Печать на лентах шириной 3,5; 6, 9, 12, 18 и 24 мм, том числе и на термоусадочных трубках\nОписание\nВ электрических системах надежная маркировка имеет решающее значение и P-touch E550WVP с кейсом для переноски специально разработан, чтобы сделать вашу работу легче. Возможность подключения к компьютеру значительно упрощает работу. Wi-Fi позволяет печатать с вашего смартфона быстро и легко.\n\n☎️+998902814746")
    bot.sendPhoto(chat_id=chat_id, photo='https://t.me/samsmart_uz/11474', caption="Телевизор Artel 32 Led tv\n110$\nTel: +998906051221")
    bot.sendPhoto(chat_id=chat_id, photo="https://t.me/samsmart_uz/11297", caption="Телевизор Artel 43 Led tv.")
def aloqa_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Telifon raqamimiz 📞', callback_data='tel_uz')],
        #[InlineKeyboardButton(text="Locatsiyamiz 📍", url="")],
        #[InlineKeyboardButton(text="Bizning manzilimiz", callback_data="")]
        [InlineKeyboardButton(text='Telegram kanalimiz 👥', url="https://t.me/samsmart_uz")]
        #[InlineKeyboardButton(text="Instagram profilimiz", url="")]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text="Xurmatli mijoz biz bilan bog'lanish uchun quyidagilardan birini tanlang")
def aloqa_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="наш номер телефона 📞", callback_data='tel_rus')],
        # [InlineKeyboardButton(text="", url="")],
        # [InlineKeyboardButton(text="", callback_data="")],
        # [InlineKeyboardButton(text="", url="" )],
        # [InlineKeyboardButton(text="", url="")]

    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text="Уважаемый клиент, пожалуйста, выберите один из вариантов ниже, чтобы связаться с нами.")


def chanel_photo(update: Update, context: CallbackContext):
    bot = context.bot
    db=open('admins.json').read()
    admins=json.loads(db)
    admins=admins['admins']
    chat_id=update.message.chat_id
    if str(chat_id) in admins:


        photo = update.message.photo

        file_id = photo[0].file_id
        with open("chanel.json") as f:
         data = json.loads(f.read())
         
         for url in data["chanel_urls"]:
            bot.sendPhoto(url, file_id)
        with open('db.json') as f:
            data=json.loads(f.read())
            for url in data['users']:
                bot.sendPhoto(url, file_id)

            

def query(update: Update, context: CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=query.data
    bot=context.bot
    
    

    if data=='uzbek_tili':
         keyboard=ReplyKeyboardMarkup([
            ['Routerlar 🌐', 'Monitorlar 🖥', "Kameralar 📸"],
            ['🚖 Mashinaga GPS navigator', 'Elektron eshik qulfi 🔐'],
            ['Televizorlar va boshqa mahsulotlar 🖥',"Biz bilan bog'lanish ☎️"],
            ['Bot haqida 🤖','Asosiy Menuga qaytish ⬅️']
           
        
         ], resize_keyboard=True)
         text="Xurmatli mijoz siz bu bot orqali uzingizni qiziqtirgan savollarga javob topishingiz mumkin!"
         bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)
    elif data=='rus_tili':
        keyboard=ReplyKeyboardMarkup([
            ['Роутеры 🌐', 'Мониторы 🖥', 'Камеры 📸'],
            ['🚖 Автомобильный GPS навигатор', "Электронный замок 🔐"],
            ["Телевизоры и другие товары 🖥", "связаться с нами ☎️"],
            ["О боте 🤖",'Вернуться в главное меню ⬅️']
         ], resize_keyboard=True)
        

        text="Уважаемый клиент, вы можете найти ответы на свои вопросы через этого бота!"   
        bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)  
    elif data=='tel_uz':
        bot.sendContact(chat_id=chat_id, phone_number='+998333344442', first_name="Жахонгир Хайдаров")
    elif data=="tel_rus":
        bot.sendContact(chat_id=chat_id, phone_number='+998333344442', first_name="Жахонгир Хайдаров")
    
    

    return 'OK'   
def bot_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat_id
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text="Har xil turdagi telegram botlar yasatish uchun  @TATU103 murojat qilishingiz mumkin")
    bot.sendContact(chat_id=chat_id, phone_number='+998906560727', first_name='Jasurbek Pirnazarov')
def bot_rus(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text="Вы можете обратиться к @TATU103 для создания различных типов ботов для телеграмм.")
    bot.sendContact(chat_id=chat_id, phone_number='+998906560727', first_name="Jasurbek Pirnazarov")



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
dp.add_handler(MessageHandler(Filters.text('Televizorlar va boshqa mahsulotlar 🖥'), tv_uz))
dp.add_handler(MessageHandler(Filters.text("Вернуться в главное меню ⬅️"), start))
dp.add_handler(MessageHandler(Filters.text("Роутеры 🌐"), router_rus))
dp.add_handler(MessageHandler(Filters.text('Мониторы 🖥'), monitor_rus))
dp.add_handler(MessageHandler(Filters.text('Камеры 📸'), kameralar_rus))
dp.add_handler(MessageHandler(Filters.text('🚖 Автомобильный GPS навигатор'), gps_rus))
dp.add_handler(MessageHandler(Filters.text("Электронный замок 🔐"), qulf_rus))
dp.add_handler(MessageHandler(Filters.text("Телевизоры и другие товары 🖥"),tv_rus))
dp.add_handler(MessageHandler(Filters.text("Biz bilan bog'lanish ☎️"), aloqa_uz))
dp.add_handler(MessageHandler(Filters.text("связаться с нами ☎️"), aloqa_rus))
dp.add_handler(MessageHandler(Filters.text('Bot haqida 🤖'), bot_uz))
dp.add_handler(MessageHandler(Filters.text("О боте 🤖"), bot_rus))
dp.add_handler(MessageHandler(Filters.photo, chanel_photo))



updater.start_polling()
updater.idle()

