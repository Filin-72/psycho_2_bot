from keyboards import *
import random

bot = telebot.TeleBot('')


class answers_parents:
    def __init__(self, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.ans5 = ans5
        self.ans6 = ans6
        self.ans7 = ans7
        self.ans8 = ans8
        self.ans9 = ans9
        self.ans10 = ans10



class answers_oge:
    def __init__(self, ans1_oge, ans2_oge):
        self.ans1 = ans1_oge
        self.ans2 = ans2_oge



class answers_ege:
    def __init__(self, ans1_ege, ans2_ege, ans3_ege, ans4_ege,ans5_ege):
        self.ans1 = ans1_ege
        self.ans2 = ans2_ege
        self.ans3 = ans3_ege
        self.ans4 = ans4_ege
        self.ans5 = ans5_ege


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    start = bot.send_message(message.chat.id, 'Привет! Я твой школьный психологический помощник. '
                                              'В наше время каждому порой нужно получить ценный совет или просто выговориться тому, кто выслушает. '
                                              'Я ещё только учусь и могу не до конца понимать тебя, но я обещаю, что буду стараться! '
                                              'От тебя я прошу лишь честности перед собой, ну и передо мной. '
                                              'А сейчас выбери интересующую тебя тему!', reply_markup=keyboard1)
    bot.register_next_step_handler(start, get_attention)


@bot.message_handler(content_types=['photo', 'video', 'voice'])
def text_handler(message):
    chat_id = message.chat.id
    photo = bot.send_message(chat_id, 'Здорово, только вот я создан не для комментирования мультимедиа. '
                                      'Обратись ко мне с какой-то проблемой!')
    bot.register_next_step_handler(photo, start_handler)


@bot.message_handler(commands=['help'])
def help_handler(message):
    help = bot.send_message(message.chat.id, 'Совсем запутался уже? Что ж, тебе везёт - я всегда готов помочь! '
                                             'Если хочешь проработать какую-то тему, то выбери её по кнопкам в меню! '
                                             'Если бот завис/хочешь срочно вернуться в начало, то введи /start . '
                                             'Пожелания и вопросы можешь писать нам на почту: psychobot@inbox.ru ')
    bot.register_next_step_handler(help, start_handler)


def get_attention(message):
    if message.text.lower() == "снять стресс":
        start0 = bot.send_message(message.chat.id,
                                  'Сейчас мы с тобой будем снимать стресс. Учти, процедура это сложная. '
                                  'От тебя, как и прежде, мне нужны честность и усилия над собой. '
                                  'Тебе нужно будет хорошенько поработать и быть искренним, не '
                                  'пытаясь принизить свои хорошие качества. Если мы договорились,'
                                  'то жми кнопку ниже. И ещё кое-что: процедура не подразумевает '
                                  'резкой остановки. Если захочешь вернуться в начало, введи /start',
                                  reply_markup=keyboard4)
        bot.register_next_step_handler(start0, get_stress)
    elif message.text.lower() == "давление со стороны":
        start0 = bot.send_message(message.chat.id, 'Скажи, это давление со стороны родителей или учителей?',
                                  reply_markup=keyboard2)
        bot.register_next_step_handler(start0, get_attention_parents)
    elif message.text.lower() == "нехватка общения":
        start0 = bot.send_message(message.chat.id, 'Социализация в школе - это важный этап в развитии твоей психики, '
                                                   'поэтому, если тебя беспокоит твое положение в обществе, общение '
                                                   'с друзьями или одиночество, лучше решить проблему сейчас, '
                                                   'чем бороться с ее последствиями. Скажи, у тебя есть друзья или '
                                                   'хотя бы верный друг?', reply_markup=keyboard8)
        bot.register_next_step_handler(start0, get_friends)
    elif message.text.lower() == "нехватка времени":
        start0 = bot.send_message(message.chat.id,
                                  'Ох уж эта извечная проблема молодёжи. Всё куда-то спешим, всё заняты… '
                                  'Да ладно, понимаю прекрасно, на самом деле. '
                                  'Проблема со временем – одна из самых популярных в современном мире. '
                                  'Скажи, какие у тебя отношения с тайм-менеджментом?', reply_markup=keyboard7)
        bot.register_next_step_handler(start0, get_time)
    elif message.text.lower() == "экзамены":
        start0 = bot.send_message(message.chat.id, 'Какой экзамен тебя ожидает?', reply_markup=keyboard16)
        bot.register_next_step_handler(start0, get_exams)


def get_attention_parents(message):
    if message.text.lower() == "родители":
        start1 = bot.send_message(message.chat.id,
                                  'Хорошо, сейчас мы немножечко протестируем твои отношения с родителями. '
                                  'Будь, пожалуйста, предельно честен!', reply_markup=keyboard4)
        bot.register_next_step_handler(start1, get_attention_parents1)
    elif message.text.lower() == "учителя":
        start1 = bot.send_message(message.chat.id, 'Учителя любят портить жизнь, чего уж тут. '
                                                   'И любят нагнетать жути, когда этого не следует делать. '
                                                   'Все мы проходим через это - рано или поздно. '
                                                   'Знаешь, тут в случае, как и с тревогой, важно '
                                                   'уметь дистанцироваться. '
                                                   'Учителя - такие люди, которые могут сильно трепать нервы. '
                                                   'Не распыляйся на них и не иди на поводу эмоций. '
                                                   'Знаю, легко звучит, но сделать тяжело, и всё же постарайся!',
                                  reply_markup=keyboard4)
        bot.register_next_step_handler(start1, get_teacher)


def get_attention_parents1(message):
    start2 = bot.send_message(message.chat.id, 'Как ты сам считаешь, у тебя есть взаимопонимание с родителями?',
                              reply_markup=keyboard3)
    bot.register_next_step_handler(start2, get_attention_parents2)


def get_attention_parents2(message):
    start3 = bot.send_message(message.chat.id, 'Интересуешься ли ты работой своих родителей?', reply_markup=keyboard3)
    ans1 = message.text
    answers_parents.ans1 = ans1.lower()
    bot.register_next_step_handler(start3, get_attention_parents3)


def get_attention_parents3(message):
    start4 = bot.send_message(message.chat.id, 'Рассказываешь ли ты родителям о своих друзьях?', reply_markup=keyboard3)
    ans2 = message.text
    answers_parents.ans2 = ans2.lower()
    bot.register_next_step_handler(start4, get_attention_parents4)


def get_attention_parents4(message):
    start5 = bot.send_message(message.chat.id, 'Есть ли у тебя с родителями общие увлечения?', reply_markup=keyboard3)
    ans3 = message.text
    answers_parents.ans3 = ans3.lower()
    bot.register_next_step_handler(start5, get_attention_parents5)


def get_attention_parents5(message):
    start6 = bot.send_message(message.chat.id, 'Часто ли вы проводите время вместе?', reply_markup=keyboard3)
    ans4 = message.text
    answers_parents.ans4 = ans4.lower()
    bot.register_next_step_handler(start6, get_attention_parents6)


def get_attention_parents6(message):
    start7 = bot.send_message(message.chat.id, 'Есть ли у вас с родителями доверие?', reply_markup=keyboard3)
    ans5 = message.text
    answers_parents.ans5 = ans5.lower()
    bot.register_next_step_handler(start7, get_attention_parents7)


def get_attention_parents7(message):
    start8 = bot.send_message(message.chat.id, 'Готов ли ты помогать родителям по их просьбе?', reply_markup=keyboard3)
    ans6 = message.text
    answers_parents.ans6 = ans6.lower()
    bot.register_next_step_handler(start8, get_attention_parents8)


def get_attention_parents8(message):
    start9 = bot.send_message(message.chat.id, 'А помогут ли тебе родители по твоей просьбе, как думаешь?',
                              reply_markup=keyboard3)
    ans7 = message.text
    answers_parents.ans7 = ans7.lower()
    bot.register_next_step_handler(start9, get_attention_parents9)


def get_attention_parents9(message):
    start10 = bot.send_message(message.chat.id, 'Сможешь ли ты положиться на родителей, если будет сложная ситуация?',
                               reply_markup=keyboard3)
    ans8 = message.text
    answers_parents.ans8 = ans8.lower()
    bot.register_next_step_handler(start10, get_attention_parents10)


def get_attention_parents10(message):
    start11 = bot.send_message(message.chat.id, 'В твоих родителях больше хорошего, чем плохого?',
                               reply_markup=keyboard3)
    ans9 = message.text
    answers_parents.ans9 = ans9.lower()
    bot.register_next_step_handler(start11, counter)


def counter(message):
    end0 = bot.send_message(message.chat.id, 'Я провожу вычисления, секунду...', reply_markup=keyboard4)
    ans10 = message.text
    answers_parents.ans10 = ans10.lower()
    a = answers_parents.ans1
    b = answers_parents.ans2
    c = answers_parents.ans3
    d = answers_parents.ans4
    e = answers_parents.ans5
    f = answers_parents.ans6
    g = answers_parents.ans7
    h = answers_parents.ans8
    j = answers_parents.ans9
    k = answers_parents.ans10
    end = [a, b, c, d, e, f, g, h, j, k]
    global i
    i = 0
    for z in range(0, 10):
        if end[z] == "да":
            i += 1
        elif end[z] == "иногда":
            i = i + 0
        elif end[z] == "нет":
            i = i - 1
        else:
            i = i + 0
    bot.register_next_step_handler(end0, get_attention_end)


def get_attention_end(message):
    bot.send_message(message.chat.id, i)
    if i > 3:
        end1 = bot.send_message(message.chat.id, 'Вроде как ваши отношения смотрятся очень неплохо! '
                                                 'И всё-таки проблема есть. Нужно понимать, отношения с родителями - тяжёлая штука. '
                                                 'Обычно это комплекс из проблем, а не единичный случай. '
                                                 'И исправлять такое нужно с самого начала. '
                                                 'Самое сложное в этом во всём - сделать первый шаг. '
                                                 'Я понимаю, как это иногда сложно, но это лучше, чем потом сталкиваться '
                                                 'с этими проблемами и в будущем! Просто сядь спокойно и обсуди для начала '
                                                 'всё с ними. И помни, что ты всегда можешь позвонить по номеру 8-800-2000-122 '
                                                 '- бесплатно и анонимно!', reply_markup=keyboard4)
        bot.register_next_step_handler(end1, get_end)
    elif i >= -3:
        end1 = bot.send_message(message.chat.id, 'Я так понимаю, у вас примерно нейтральные отношения - это неплохо, '
                                                 'но ты должен понимать, что они в любой момент могут сломаться. Всё смотрится хрупко. '
                                                 'Пойми, родители беспокоятся за тебя, потому что переживают за твоё будущее. '
                                                 'Старайся наладить отношения с ними и тогда всё может и прийти в норму.',
                                reply_markup=keyboard4)
        bot.register_next_step_handler(end1, get_end)
    else:
        end1 = bot.send_message(message.chat.id, 'Проблема, видимо, действительно очень серьёзная. '
                                                 'Сочувствую. Не забывай, что ты всегда можешь рассказать, '
                                                 'что у тебя на душе в другой теме с помощью снятия стресса и тревожности. '
                                                 'Также советую, если ситуация будет совсем тяжёлой, позвонить по '
                                                 'номеру детской линии доверия: 8-800-2000-122 - бесплатно и анонимно!',
                                reply_markup=keyboard4)
        bot.register_next_step_handler(end1, get_end)


def get_end(message):
    end2 = bot.send_message(message.chat.id, 'Отношения с родителями - очень важная вещь, '
                                             'с которой нужно постоянно работать! Если бы у вас были бы идеальные '
                                             'отношения, то почти наверняка не было бы сложностей с давлением с '
                                             'их стороны. Налаживай отношения и, как бы грубо ни звучало, '
                                             'заставь их поверить в тебя через любовь и доброту! '
                                             'Сил тебе и терпения в этом деле!', reply_markup=keyboard5)
    bot.register_next_step_handler(end2, start_handler)


def get_teacher(message):
    end = bot.send_message(message.chat.id, 'Ты же знаешь, как оно бывает: в школьной комиссии давят на директора, '
                                            'директор кричит на учителя, а преподаватель вымещает свою злость на вас. '
                                            'Если твоя совесть чиста, то старайся не вестись на это. '
                                            'Если же ты в чём-то виноват, то постарайся искренне попросить прощения '
                                            'и закрыть эту тему и тогда, возможно, учитель пойдёт тебе навстречу!',
                           reply_markup=keyboard6)
    bot.register_next_step_handler(end, get_teacher_end)


def get_teacher_end(message):
    if message.text.lower() == "в начало!":
        end_end = bot.send_message(message.chat.id, 'Держись и удачи!', reply_markup=keyboard5)
        bot.register_next_step_handler(end_end, start_handler)
    else:
        end_end = bot.send_message(message.chat.id, 'Если есть тяжёлая и нерешаемая проблема, '
                                                    'обратись к взрослым или позвони на общероссийский телефон '
                                                    'доверия 8-800-2000-122, если по каким-то причинам не можешь '
                                                    'обсудить данную ситуацию с родителями. Это бесплатно и анонимно. '
                                                    'И помни, что если правда на твоей стороне, ты имеешь полное право '
                                                    'отстаивать свои чувства! ', reply_markup=keyboard5)
        bot.register_next_step_handler(end_end, start_handler)


def get_time(message):
    if message.text.lower() == "перепробовал большинство техник":
        time1 = bot.send_message(message.chat.id, 'Ох, вот это совсем тяжело. Вижу, передо мной эксперт '
                                                  'в области тайм-менеджмета. И если у тебя есть реальные '
                                                  'проблемы с ним, то это тяжко, конечно. Могу посоветовать '
                                                  'лишь попытаться перекладывать часть своих обязательств '
                                                  'на кого-то, если есть такая возможность или же полностью'
                                                  ' отказаться от чего-то, вычеркнув это на время из своей жизни. '
                                                  'Удачи и терпения тебе в этом!', reply_markup=keyboard5)
        bot.register_next_step_handler(time1, start_handler)
    elif message.text.lower() == "слежу за собой/планирую время":
        time1 = bot.send_message(message.chat.id, 'Может, стоит попробовать какую-то технику тайм-менеджмента? ',
                                 reply_markup=keyboard8)
        bot.register_next_step_handler(time1, get_time_profi1)
    else:
        time1 = bot.send_message(message.chat.id, 'Самое простое, что ты можешь сделать – это начать планировать '
                                                  'свой день. Расписывать, на что уйдёт сколько времени и в '
                                                  'зависимости от этого двигать своё расписание.',
                                 reply_markup=keyboard4)
        bot.register_next_step_handler(time1, get_new2)


def get_time_profi1(message):
    a = [
        'Правило 1-3-5: за день вы можете сделать только одну большую задачу, три средние и пять мелких. Всего — девять дел, не больше и не меньше.',
        'Принцип Паретто: 20% усилий дадут тебе 80% результата. А вот остальные 20% результата придут лишь с 80% усилий.',
        'Принцип Помодоро: берёте таймер и ставите его на 25 минут. После этого фокусируетесь на работе. Когда 25 минут истекут, вы отдыхаете 5 минут, а затем повторяете всё заново. Через четыре цикла вас ждёт большой перерыв на полчаса.',
        'Матрица Эйзенхауэра: матрица 2*2. Важно/Неважно, Срочно/Несрочно. Распределяем дела и делаем их по приоритету. ',
        'Метод Хронометраж: записываем постфактум то, что произошло. Выписываем абсолютно всё, как только идёт смена деятельности. В конце дня смотрим, на что ушло больше всего времени и корректируем.',
        'Метод трёх 8: 8 часов на сон, 8 часов на отдых, 8 часов на трудовую деятельность.',
        'Правило 4D: Делить свои задачи по группам. 4 группы – Do (делай), Delegate (делегируй), Delete (удаляй), Delay (отложи). По сути, альтернативный вариант Матрицы Эйзенхауэра.']
    b = random.choice(a)
    if message.text.lower() == 'да':
        time2 = bot.send_message(message.chat.id, b, reply_markup=keyboard4)
        bot.register_next_step_handler(time2, get_time_profi2)
    else:
        time2 = bot.send_message(message.chat.id, 'Эх, а ведь это мог быть твой последний шанс, хаха. '
                                                  'Надеюсь, полученных знаний тебе хватит! Не вешай нос! '
                                                  'Всё образуется со временем.', reply_markup=keyboard5)
        bot.register_next_step_handler(time2, start_handler)


def get_time_profi2(message):
    one_more = bot.send_message(message.chat.id, 'Хочешь получить ещё технику?', reply_markup=keyboard8)
    bot.register_next_step_handler(one_more, get_time_profi1)


def get_new2(message):
    new2 = bot.send_message(message.chat.id,
                            'Чтобы скорректировать расписание советуем попробовать метод «Хронометраж»: '
                            'записываем постфактум то, что произошло. Выписываем абсолютно всё, '
                            'как только идёт смена деятельности. В конце дня смотрим, на что ушло '
                            'больше всего времени и корректируем своё расписание на завтра, '
                            'основываясь на своём опыте.', reply_markup=keyboard9)
    bot.register_next_step_handler(new2, get_new3)


def get_new3(message):
    new3 = bot.send_message(message.chat.id, 'Тогда переходи по второй кнопке бота, чтобы узнать больше '
                                             'разных техник работы со временем ;)', reply_markup=keyboard5)
    bot.register_next_step_handler(new3, start_handler)


def get_stress(message):
    condition = bot.send_message(message.chat.id, 'Пожалуйста, опиши своё текущее состояние: ', reply_markup=keyboard10)
    bot.register_next_step_handler(condition, get_stress2)


def get_stress2(message):
    if message.text.lower() == 'подавленность' or message.text.lower() == 'тревога':
        user_condition = bot.send_message(message.chat.id, 'Хочешь поработать со своими мыслями? '
                                                           'Тогда первое, что тебе необходимо сделать - это понять, '
                                                           'что тебя тревожит. Да, с одной стороны может казаться, '
                                                           'что у твоего состояния нет причины, однако, скорее всего, '
                                                           'ты просто не замечаешь, как разворачиваются события. '
                                                           'Тревожность может появляться от вполне реальной опасности, '
                                                           'которая тебе угрожает, вследствие возникновения проблемы, '
                                                           'которую нужно решить или из-за наших собственных домыслов и догадок. '
                                                           'Какой вариант тебе сейчас ближе?', reply_markup=keyboard11)
        bot.register_next_step_handler(user_condition, get_problem)
    elif message.text.lower() == 'постоянная усталость':
        user_condition = bot.send_message(message.chat.id, 'А как у тебя со временем? Успеваешь решить всё задуманное?',
                                          reply_markup=keyboard12)
        bot.register_next_step_handler(user_condition, get_extra_time)
    else:
        user_condition = bot.send_message(message.chat.id,
                                          'Я могу предложить тебе несколько советов по борьбе с бессоницей,'
                                          'если тебе это нужно?', reply_markup=keyboard8)
        bot.register_next_step_handler(user_condition, get_sleep)


def get_problem(message):
    if message.text.lower() == 'мои мысли':
        things = bot.send_message(message.chat.id, 'Тогда ты понимаешь, что это в основном мысли в роде '
                                                   '"а что будет, если", как бы могло было быть по-другому и т.д. '
                                                   'Они просто тратят нашу энергию, ведь нельзя ничего знать наверняка. '
                                                   'Но в любом случае эти мысли крутятся вокруг конкретной причины, '
                                                   'какого-то страха. Какая причина тревожности у тебя? Напиши в чат: ')
        bot.register_next_step_handler(things, get_things)
    elif message.text.lower() == 'реальная опасность':
        danger = bot.send_message(message.chat.id, 'Если проблема зашла слишком далеко, не стоит пытаться '
                                                   'решить её самостоятельно. Это нормально - просить о помощи, '
                                                   'когда она действительно тебе нужна. Обратись к взрослым '
                                                   'или позвони на общероссийский телефон доверия 8-800-2000-122, '
                                                   'если по каким-то причинам не можешь обсудить данную '
                                                   'ситуацию с родителями. Это бесплатно и анонимно. Береги себя',
                                  reply_markup=keyboard5)
        bot.register_next_step_handler(danger, start_handler)
    else:
        problem = bot.send_message(message.chat.id, 'Даже если тебе нужно решить какую-то проблему, '
                                                    'тревожность здесь не помощник. Она отбирает у тебя '
                                                    'энергию на прокручивание одних и тех же мыслей в голове, '
                                                    'на создание возможных вариантов исхода событий. '
                                                    'Но есть и хорошие новости! Ты точно знаешь причину '
                                                    'своей тревоги. А это уже половина дела в её устранении. '
                                                    'Напиши свою причину в чат, это важно прописать и обозначить. '
                                                    'Опиши причину тревоги: ')
        bot.register_next_step_handler(problem, get_things)


def get_extra_time(message):
    if message.text.lower() == 'всё хорошо':
        extra_time = bot.send_message(message.chat.id, 'Ого, тогда что же тебе не даёт отдохнуть? Напиши мне об этом! ')
        bot.register_next_step_handler(extra_time, get_rest)
    else:
        extra_time = bot.send_message(message.chat.id, 'Ох уж эта извечная проблема молодёжи. '
                                                       'Всё куда-то спешим, всё заняты… '
                                                       'Да ладно, понимаю прекрасно, на самом деле. '
                                                       'Проблема со временем – одна из самых популярных в современном мире. '
                                                       'Скажи, какие у тебя отношения с тайм-менеджментом?',
                                      reply_markup=keyboard7)
        bot.register_next_step_handler(extra_time, get_time)


def get_rest(message):
    bot.send_message(message.chat.id, 'Хм, на самом деле, это довольно-таки частая проблема. '
                                      'Не ты первый, не ты последний, кто сталкивался с этим. '
                                      'Конечно же, тяжело, но попробуй посмотреть на это со стороны. '
                                      'Представь себя на месте наблюдателя. '
                                      'Подумай, что бы ты ему посоветовал и воспользуйся этим советом!',
                     reply_markup=keyboard13)
    bot.register_next_step_handler(message, get_rest2)


def get_rest2(message):
    if message.text.lower() == 'ок':
        ok = bot.send_message(message.chat.id, 'Рад был помочь, заходи ещё, когда потребуется!', reply_markup=keyboard5)
        bot.register_next_step_handler(ok, start_handler)
    else:
        not_ok = bot.send_message(message.chat.id, 'Попробуй посмотреть на свою проблему под другим углом. '
                                                   'Возможно, в нашем боте уже есть похожая тема, с помощью '
                                                   'которой ты сможешь проработать вопрос усталости. '
                                                   'Ведь нужно устранять причину, а не следствие. Мы всегда работаем с'
                                                   'источником проблемы. Попробуй поработать с тревогой. '
                                                   'Если же нет, то ты всегда можешь позвонить на общероссийский '
                                                   'телефон доверия 8-800-2000-122, если по каким-то '
                                                   'причинам не можешь обсудить данную ситуацию с близкими.',
                                  reply_markup=keyboard5)
        bot.register_next_step_handler(not_ok, start_handler)


def get_sleep(message):
    a = ['Послушать АСМР перед сном',
         'Выпить тёплого чаю',
         'Проветрить помещение до прохладной температуры',
         'Отказаться от экранов любых устройств минимум за час до сна',
         'Почитать занудную книгу',
         'Принять контрастный душ',
         'Поменять бельё на совершенно чистое, перевернуть матрас',
         'Помедитировать',
         'Рано встать на следующее утро, чтобы в следующий раз уж точно уснуть',
         'Ночная прогулка на свежем воздухе']
    b = random.choice(a)
    if message.text.lower() == 'да':
        sleep = bot.send_message(message.chat.id, b, reply_markup=keyboard4)
        bot.register_next_step_handler(sleep, get_sleep2)
    else:
        sleep = bot.send_message(message.chat.id, 'Что ж, надеюсь, полученных знаний тебе хватит! '
                                                  'Приятных тебе снов!', reply_markup=keyboard5)
        bot.register_next_step_handler(sleep, start_handler)


def get_sleep2(message):
    one_more = bot.send_message(message.chat.id, 'Хочешь получить ещё один совет?', reply_markup=keyboard8)
    bot.register_next_step_handler(one_more, get_sleep)


def get_things(message):
    good = bot.send_message(message.chat.id, 'Это могло быть непросто, но ты справился. '
                                             'Теперь, когда ты знаешь, когда и как может возникнуть тревога, '
                                             'важно от неё дистанцироваться. Можешь придумать тревоге имя, '
                                             'представить её в виде персонажа или дать ей смешное прозвище. '
                                             'Что угодно, что поможет тебе лучше идентифицировать тревожность '
                                             'и не воспринимать её как часть себя. Напиши имя или прозвище в чат: ')
    bot.register_next_step_handler(good, get_things2)


def get_things2(message):
    name = message.text
    good = bot.send_message(message.chat.id, 'Прекрасно! Теперь, когда ты заметишь, что ' + str(
        name) + ' начинает появляться, начинай отстранение. '
                'Представь, что ' + str(name) + ' это противный человек, '
                                                'который всё поучает и поучает, а ты ему говоришь: '
                                                '"Ой, ну всё, хватит! Ну как достал". '
                                                'Это поможет тебе понять, как дистанцироваться от тревоги. '
                                                'Продолжаем?', reply_markup=keyboard4)
    bot.register_next_step_handler(good, get_things3)


def get_things3(message):
    good = bot.send_message(message.chat.id, 'После выявления причины тревожности и дистанцирования от неё, '
                                             'тебе необходимо сделать её предсказуемой. Это не значит, '
                                             'что нужно постоянно ожидать новый стресс из-за чего-то. '
                                             'Но есть ситуации, в которых она точно появится. Когда это произойдёт, '
                                             'скажи ей что-то вроде "Тревога, ты очень предсказуемая" '
                                             'или "Тревога, ты мешаешь мне учиться новому".', reply_markup=keyboard4)
    bot.register_next_step_handler(good, get_things4)


def get_things4(message):
    good = bot.send_message(message.chat.id, 'Ну и последнее: практикуй некомфортные ситуации! '
                                             'Необходимо создать новый позитивный опыт реагирования на тревожные ситуации, '
                                             'а это возможно только с практикой. Если страшно идти сразу в какие-то '
                                             'реальные ситуации, можно попробовать ролевую игру с родителями, '
                                             'друзьями или твоим психологом. Главное - это не потакать тревоге, '
                                             'не идти у неё на поводу! Верю, что у тебя всё получится :)',
                            reply_markup=keyboard5)
    bot.register_next_step_handler(good, start_handler)


def get_friends(message):
    if message.text.lower() == 'нет':
        no = bot.send_message(message.chat.id, 'Скажи, у тебя когда-нибудь были друзья?', reply_markup=keyboard8)
        bot.register_next_step_handler(no, get_why)
    else:
        yes = bot.send_message(message.chat.id, 'Близкий друг, даже всего один – это уже прекрасно! '
                                                'Скажи, почему тебе не хватает общения? ', reply_markup=keyboard15)
        bot.register_next_step_handler(yes, get_friends2)


def get_why(message):
    if message.text.lower() == 'нет':
        no = bot.send_message(message.chat.id, 'Главное тебе сейчас не опускать руки! '
                                               'Скажи, как ты думаешь, почему у тебя сейчас нет друзей?',
                              reply_markup=keyboard14)
        bot.register_next_step_handler(no, get_why2)
    else:
        yes = bot.send_message(message.chat.id, 'Все мы меняемся со временем, поэтому смена круга общения '
                                                '- это нормально. Таких перемен не надо пугаться, они говорят '
                                                'лишь о том, что ты развиваешься и уже идешь на пути '
                                                'к чему-то новому. Друзья появятся, обязательно! Скажи, ты пробовал завести '
                                                'новых друзей?', reply_markup=keyboard8)
        bot.register_next_step_handler(yes, get_new_friends)


def get_new_friends(message):
    if message.text.lower() == 'да':
        yes = bot.send_message(message.chat.id, 'Это уже хорошо! Давай подумаем, в чём может быть проблема, что у тебя '
                                                'пока не получается ни с кем подружиться?', reply_markup=keyboard14)
        bot.register_next_step_handler(yes, get_why2)
    else:
        yes = bot.send_message(message.chat.id, 'Расскажи мне, пожалуйста, почему ты не пробовал найти новых друзей?',
                               reply_markup=keyboard14)
        bot.register_next_step_handler(yes, get_why2)


def get_why2(message):
    if message.text.lower() == 'не совпадают интересы':
        cause = bot.send_message(message.chat.id, 'Прежде всего определись, что для такое для тебя дружба. '
                                                  'Например, для меня дружба - это поддержка в трудную минуту. '
                                                  'Напиши мне свое определение? Для тебя дружба - это?..')
        bot.register_next_step_handler(cause, get_say)
    elif message.text.lower() == 'я слишком критичен':
        cause = bot.send_message(message.chat.id, 'Старайся видеть в людях больше хорошего и подчеркивать '
                                                  'это в разговоре. Когда ты говоришь человеку, что он молодец '
                                                  'или поступил правильно, он становится более открытм и, скорее всего, '
                                                  'испытает симпатию к тебе. Только осторожно - не перейди на лесть. '
                                                  'И постарайся понять, что идеальным быть ни у кого не получится, '
                                                  'даже у тебя, как бы это грустно ни звучало.', reply_markup=keyboard5)
        bot.register_next_step_handler(cause, start_handler)
    elif message.text.lower() == 'я навязчивый':
        cause = bot.send_message(message.chat.id, 'Чувство навязчивости возникает не на пустом месте. '
                                                  'Во-первых, постарайся понять, что навязчивость - это сильное '
                                                  'желание общаться и прими в себе это. Это нормально. Во-вторых, '
                                                  'нужно улучшить навык общения и научиться правильно '
                                                  'выражать свои мысли. Навязчивость, как правило, является '
                                                  'результатом неспособности правильно общаться с людьми, '
                                                  'из-за чего качество общения заменяется количеством попыток '
                                                  'его инициировать. Для начала попробуй больше читать '
                                                  'и наблюдать за характерами людей.', reply_markup=keyboard5)
        bot.register_next_step_handler(cause, start_handler)
    elif message.text.lower() == 'я чувствую себя неуверенно':
        cause = bot.send_message(message.chat.id, 'Такие ощущения знакомы многим, к счастью, это можно решить. '
                                                  'Разумеется, есть не коммуникабельные люди, закрытые интроверты… '
                                                  'однако, знаешь, в компании ребят всегда есть '
                                                  'какой-то открытый человек, который с радостью доверится '
                                                  'впустить к себе в общество «новичка». Тебе же нужно работать '
                                                  'над своей самоуверенностью. И сейчас мы с тобой это сделаем!',
                                 reply_markup=keyboard4)
        bot.register_next_step_handler(cause, get_scary)
    elif message.text.lower() == 'меня отвергают':
        cause = bot.send_message(message.chat.id, 'Мне жаль, если это и правда происходило часто. '
                                                  'Но, к сожалению, чаще отвергают тех, кто позволяет '
                                                  'себя отвергать. Постарайся не поддаваться на провокации и '
                                                  'не выдавать желаемых обидчику реакций. Будь выше, относись к '
                                                  'людям по-философски, знай себе цену.', reply_markup=keyboard5)
        bot.register_next_step_handler(cause, start_handler)
    elif message.text.lower() == 'я боюсь':
        cause = bot.send_message(message.chat.id, 'Такие ощущения знакомы многим, к счастью, это можно решить. '
                                                  'Разумеется, есть не коммуникабельные люди, закрытые интроверты… '
                                                  'однако, знаешь, в компании ребят всегда есть '
                                                  'какой-то открытый человек, который с радостью доверится '
                                                  'впустить к себе в общество «новичка». Тебе же нужно работать '
                                                  'над своей самоуверенностью. И сейчас мы с тобой это сделаем!',
                                 reply_markup=keyboard4)
        bot.register_next_step_handler(cause, get_scary)
    else:
        cause = bot.send_message(message.chat.id, 'Конечно, я не могу знать наверняка причины твоего отношения '
                                                  'к другим, но, знаешь, даже среди не очень умных и/или хороших '
                                                  'людей, есть преданные, в глубинах сердца которых скрыто, '
                                                  'возможно, такое же желание найти себе верного друга. '
                                                  'Не суди всех так строго и давай людям шанс. '
                                                  'Однако, если я ошибаюсь, и вокруг тебя собралось токсичное общество, '
                                                  'то эту уже тема для более глубокой проработки. Советую обратиться '
                                                  'к профессионалам. Знаешь, не все психологи плохие...',
                                 reply_markup=keyboard5)
        bot.register_next_step_handler(cause, start_handler)


def get_friends2(message):
    if message.text.lower() == 'друзья отдаляются':
        friend = bot.send_message(message.chat.id, 'Понимаю, это грустно. Ты хочешь вернуть общение?',
                                  reply_markup=keyboard8)
        bot.register_next_step_handler(friend, get_friends3)
    elif message.text.lower() == 'мы стали слишком разные':
        friend = bot.send_message(message.chat.id, 'Все мы меняемся со временем, поэтому смена круга общения '
                                                   '- это нормально. Таких перемен не надо пугаться, они говорят'
                                                   ' лишь о том, что ты развиваешься и уже идешь на пути'
                                                   ' к чему-то новому. Возможно, просто пришло время вам'
                                                   ' отпустить друг друга и развивать свои интересы вдали'
                                                   ' друг от друга. Это грустно, но если ты сам не хочешь'
                                                   ' уже что-то менять, то в глубине души понимаешь, что это так. '
                                                   'А если желание изменить всё есть, то не медли, действуй! Лучше всего'
                                                   'открыто поговорить и поставить все точки над Ё ',
                                  reply_markup=keyboard5)
        bot.register_next_step_handler(friend, start_handler)
    else:
        friend = bot.send_message(message.chat.id, 'Это чудесно! Молодец! Но в чём проблема? '
                                                   'Не получается завести новых друзей?', reply_markup=keyboard8)
        bot.register_next_step_handler(friend, get_new_talk)


def get_say(message):
    say = message.text
    oh = bot.send_message(message.chat.id,
                          'Отлично, у тебя есть понимание! И ты понимаешь, что дружба - ' + str(say).lower() +
                          'Теперь для себя реши, как ты хочешь дружить. Если для тебя важно проводить время вместе '
                          'за беседами ни о чем, то интересы здесь не столько важны, сколько схожесть характера. '
                          'А если всё-таки совпадение интересов важно, то попробуй поискать единомышленников '
                          'в тематических сообществах. Не волнуйся брать инициативу на себя и действуй!',
                          reply_markup=keyboard5)
    bot.register_next_step_handler(oh, start_handler)


def get_friends3(message):
    if message.text.lower() == 'да':
        yes = bot.send_message(message.chat.id, 'Пробовал ли ты поговорить с другом/друзьями?', reply_markup=keyboard8)
        bot.register_next_step_handler(yes, get_friends4)
    else:
        no = bot.send_message(message.chat.id, 'Посмотри на своих старых ещё раз. Если считаешь, что можешь без них - '
                                               'возможно, просто пришло время вам отпустить друг друга '
                                               'и развивать свои интересы вдали друг от друга. Это грустно, '
                                               'но если ты сам не хочешь уже что-то менять, то в '
                                               'глубине души понимаешь, что это так. Однако, если ты всё '
                                               'ещё чувствуешь, что вы нужны друг другу, лучше открыто всё обсудить!',
                              reply_markup=keyboard5)
        bot.register_next_step_handler(no, start_handler)


def get_friends4(message):
    if message.text.lower() == 'да':
        yes = bot.send_message(message.chat.id, 'Вот два возможных варианта: прямо спросить друга, '
                                                'действительно ли он потерял интерес к общению с тобой. '
                                                'Если ответ будет "нет", то попытаться вызвать его на '
                                                'откровенный разговор о том, что происходит. '
                                                'Если вразумительного ответа не будет, или он сразу '
                                                'скажет "да" - то переходи к следующему пункту – '
                                                'прекратить общение с этим человеком. Дружбу не может '
                                                'тянуть кто-то один, поэтому тут лучше разойтись.',
                               reply_markup=keyboard5)
        bot.register_next_step_handler(yes, start_handler)
    else:
        no = bot.send_message(message.chat.id, 'Попробуй узнать у друга, почему он отдалился, может, у него '
                                               'проблемы в жизни, и он много ресурса тратит на них. '
                                               'В таком случае предложи ему свою помощь и это еще больше укрепит '
                                               'вашу дружбу. В любом случае первое, что следует сделать - '
                                               'отрыто поговорить, выяснив проблему.', reply_markup=keyboard5)
        bot.register_next_step_handler(no, start_handler)


def get_new_talk(message):
    if message.text.lower() == 'да':
        yes = bot.send_message(message.chat.id, 'Ты пробуешь – это уже хорошо! Но, видимо, что-то пошло не так. '
                                                'Давай обсудим, почему друзья тебя не принимают?',
                               reply_markup=keyboard4)
        bot.register_next_step_handler(yes, get_friends5)
    else:
        no = bot.send_message(message.chat.id, 'Возможно, просто пришло время вам отпустить друг друга '
                                               'и развивать свои интересы вдали друг от друга. Это грустно, '
                                               'но если ты сам не хочешь уже что-то менять, то в '
                                               'глубине души понимаешь, что это так', reply_markup=keyboard5)
        bot.register_next_step_handler(no, start_handler)


def get_friends5(message):
    next = bot.send_message(message.chat.id, 'Итак, как ты думаешь, почему друзья тебя не принимают? В чём сложности?',
                            reply_markup=keyboard14)
    bot.register_next_step_handler(next, get_why2)


def get_scary(message):
    first = bot.send_message(message.chat.id, 'Напиши в диалог со мной хотя бы '
                                              '3 своих положительных качества одним '
                                              'сообщением через запятую.')
    bot.register_next_step_handler(first, get_scary2)


def get_scary2(message):
    good = str(message.text)
    b = good.count(',')
    if b > 1:
        ok = bot.send_message(message.chat.id, 'Почаще перечитывай этот список! '
                                               'А теперь как насчёт написать свои успехи?')
        bot.register_next_step_handler(ok, get_scary3)
    else:
        not_ok = bot.send_message(message.chat.id, 'Напиши не меньше 3 положительных качеств, я же просил! '
                                                   'Подумай хорошенько, хорошие качества есть у всех!)')
        bot.register_next_step_handler(not_ok, get_scary2)


def get_scary3(message):
    good = bot.send_message(message.chat.id, 'Ёу! Да тут у нас целый повод для гордости есть, '
                                             'а ты так сомневаешься в себе… Знаешь, самое сложное – это начать. '
                                             'Но стоит втянуться и ты со временем будешь чувствовать '
                                             'себя как рыба в воде!', reply_markup=keyboard5)
    bot.register_next_step_handler(good, start_handler)


def get_exams(message):
    if message.text.lower() == 'огэ':
        oge = bot.send_message(message.chat.id, 'Планируешь ли ты поступать в колледж?', reply_markup=keyboard8)
        bot.register_next_step_handler(oge, get_college)
    else:
        ege = bot.send_message(message.chat.id, 'Ох, это действительно тяжёлый вопрос. '
                                                'Ты наверняка беспокоишься, что твоя жизнь закончится в случае провала, '
                                                'как бы это ни звучало, но это не так. Жизнь продолжается. '
                                                'Не нужно думать, что всё кончено. Но давай продолжим, если хочешь!',
                               reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_ege)


def get_college(message):
    ans1_oge = message.text.lower()
    answers_oge.ans1 = ans1_oge
    oge = bot.send_message(message.chat.id, 'Испытываешь ли ты давление со стороны кого-то?', reply_markup=keyboard8)
    bot.register_next_step_handler(oge, get_college2)


def get_college2(message):
    if message.text.lower() == 'да':
        college = bot.send_message(message.chat.id, 'Скажи, это давление со стороны родителей или учителей?',
                                   reply_markup=keyboard2)
        bot.register_next_step_handler(college, get_attention_parents)
    else:
        college = bot.send_message(message.chat.id, 'Как ты думаешь, сможешь ли ты набрать проходные баллы? '
                                                    'Хотя бы по одному предмету', reply_markup=keyboard8)
        bot.register_next_step_handler(college, get_balls)


def get_balls(message):
    ans2_oge = message.text.lower()
    answers_oge.ans2 = ans2_oge
    if answers_oge.ans1 == 'да' and answers_oge.ans2 == 'нет':
        oge_end = bot.send_message(message.chat.id, 'Выпиши предметы, с которыми есть сложности. Проработай проблему '
                                                    'с ними - явно какие-то задания тебе уже удаются, посмотри, '
                                                    'где возникают сложности. И ни за что не переживай. '
                                                    'ОГЭ решает далеко не всё. Впереди много сложностей, '
                                                    'а ОГЭ сдать можно и без специальной подготовки, '
                                                    'если нет проблем со школьными знаниями. Это первая '
                                                    'твоя знаковая проверка, да, но ты почти наверняка её сдашь, '
                                                    'если не будешь нервничать и переживать! А если не получится '
                                                    'поступить в колледж, то ты всегда можешь остаться в школе!',
                                   reply_markup=keyboard4)
        bot.register_next_step_handler(oge_end, get_oge_end)
    elif answers_oge.ans1 == 'да' and answers_oge.ans2 == 'да':
        oge_end = bot.send_message(message.chat.id, 'Тебе следует понять, что чужие ожидания - чужие проблемы. '
                                                    'А твои переживания - это то, с чем ты можешь справиться сам! '
                                                    'Ты хорошо подготовился и точно наберёшь какие-то баллы. '
                                                    'Постарайся расслабиться и отпустить ситуацию. Нервы тебе '
                                                    'точно не помогут. Немного волноваться - нормально, но не стоит '
                                                    'впадать в панику! Никакого смысла в этом нет. А вот чтобы '
                                                    'гарантированно поступить в колледж, остаётся только работать'
                                                    'и ещё более усердно заниматься. Только ни за что не дави на себя!'
                                                    'На край, всегда остаётся вариант с тем, чтобы остаться в школе!',
                                   reply_markup=keyboard4)
        bot.register_next_step_handler(oge_end, get_oge_end)
    elif answers_oge.ans1 == 'нет' and answers_oge.ans2 == 'да':
        oge_end = bot.send_message(message.chat.id,
                                   'Успокойся! :) Ты хорошо подготовился и точно наберёшь проходные баллы. '
                                   'Коли ты планируешь продолжить обучение в школе то постарайся расслабиться '
                                   'и отпустить ситуацию. ОГЭ ты сдашь единожды в жизни и забудешь про него, '
                                   'как про не очень приятный сон. Никакого смысла в этом нет, '
                                   'если так подумать. Но если есть вещи, которые тебя действительно беспокоят, '
                                   'советую попробовать снять тревожность в другой ветке бота!', reply_markup=keyboard4)
        bot.register_next_step_handler(oge_end, get_oge_end)
    else:
        oge_end = bot.send_message(message.chat.id, 'Тогда остаётся только работать, работать и работать! '
                                                    'Выпиши предметы, с которыми есть сложности. Проработай проблему '
                                                    'с ними - явно какие-то задания тебе уже удаются, посмотри, '
                                                    'где возникают сложности. И ни за что не переживай. '
                                                    'ОГЭ решает далеко не всё. Впереди много сложностей, '
                                                    'а ОГЭ сдать можно и без специальной подготовки, '
                                                    'если нет проблем со школьными знаниями. Это первая твоя '
                                                    'знаковая проверка, да, но ты почти наверняка её сдашь, '
                                                    'если не будешь нервничать и переживать!', reply_markup=keyboard4)
        bot.register_next_step_handler(oge_end, get_oge_end)


def get_oge_end(message):
    oge_end = bot.send_message(message.chat.id, 'В конце концов, задай сам(а) себе вопрос: когда и кому было '
                                                'легко сдавать экзамены? Для того, чтобы успешно это сделать, '
                                                'всегда надо было кропотливо трудиться. Лишь редкие гении очень '
                                                'легко справлялись с любыми экзаменационными заданиями без подготовки. '
                                                'При этом невозможно утверждать, что они совсем не волновались. '
                                                'Ведь волнение перед экзаменами – это тоже нормально. Мы - люди. '
                                                'Эмоциональные существа. Небольшое волнение - это нормально, '
                                                'а вот панику нужно убирать и прорабатывать. '
                                                'И самое важное - начать!', reply_markup=keyboard5)
    bot.register_next_step_handler(oge_end, start_handler)


def get_ege(message):
    ege1 = bot.send_message(message.chat.id, 'Позволь полюбопытстовать: есть экзамены, в которых ты уверен? '
                                             'Хоть один...', reply_markup=keyboard8)
    bot.register_next_step_handler(ege1, get_ege2)


def get_ege2(message):
    ans1_ege = message.text.lower()
    answers_ege.ans1 = ans1_ege
    ege2 = bot.send_message(message.chat.id, 'Тебя волнует поступление в ВУЗ?', reply_markup=keyboard8)
    bot.register_next_step_handler(ege2, get_ege3)


def get_ege3(message):
    ans2_ege = message.text.lower()
    answers_ege.ans2 = ans2_ege
    ege3 = bot.send_message(message.chat.id, 'Ты боишься "потерять" 1 год жизни?', reply_markup=keyboard8)
    bot.register_next_step_handler(ege3, get_ege4)


def get_ege4(message):
    ans3_ege = message.text.lower()
    answers_ege.ans3 = ans3_ege
    ege4 = bot.send_message(message.chat.id, 'Тебя пугают видеокамеры и съёмка твоих действий?', reply_markup=keyboard8)
    bot.register_next_step_handler(ege4, get_ege5)


def get_ege5(message):
    ans4_ege = message.text.lower()
    answers_ege.ans4 = ans4_ege
    ege5 = bot.send_message(message.chat.id, 'Ощущаешь ли ты давление на тебя со стороны?', reply_markup=keyboard8)
    bot.register_next_step_handler(ege5, get_ege_end)


def get_ege_end(message):
    ans5_ege = message.text.lower()
    answers_ege.ans5 = ans5_ege
    if answers_ege.ans2 == 'да' and answers_ege.ans3 == 'да' and answers_ege.ans4 == 'да' and answers_ege.ans5 == 'да':
        ege = bot.send_message(message.chat.id, 'Да уж... 11 класс, всё понимаю, но аж столько нервов - это сильно! '
                                                'Но смотри, во-первых, тебе необходимо как следует подготовиться '
                                                'к экзаменам. В ЕГЭ очень много типичных и шаблонных заданий - сделай '
                                                'на них упор! Что касается итогов сдачи - мир не рухнет, если не выйдет '
                                                'поступить в унивреситет. Перед тобой всё равно будет много возможностей. '
                                                'Но если ты ощущаешь серьёзное давление на тебя, то советую перейти в '
                                                'другую тему бота и проработать этот вопрос.', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans2 == 'нет' and answers_ege.ans3 == 'нет' and answers_ege.ans4 == 'нет':
        ege = bot.send_message(message.chat.id, 'Так, я заинтригован и внимательно тебя слушаю... '
                                                'Обычно почти все переживают из-за поступления в ВУЗ или из-за '
                                                'потери года жизни в целом, а у тебя с этим вроде как нет проблем. '
                                                'Напиши нам на почту psychobot@inbox.ru, что тебя волнует. '
                                                'Мы ещё работаем над ботом, но это будет очень полезно для '
                                                'дальнейшего развития! Удачи тебе в дальнейшем!',
                               reply_markup=keyboard5)
        bot.register_next_step_handler(ege, start_handler)
    elif answers_ege.ans2 == 'да' and answers_ege.ans3 == 'да':
        ege = bot.send_message(message.chat.id, 'Как ты думаешь, неужели бабушкам и дедушкам было легко сдавать '
                                                'экзамены по всем изучаемым в школе предметам? Родителям могло '
                                                'повезти немного больше: экзамены уже можно было выбирать. '
                                                'Но после выпускных экзаменов надо было снова сдавать экзамены, '
                                                'только уже вступительные. В случае неудачи, люди теряли год, '
                                                'продолжали готовиться, чтобы повторить попытку в следующем году. '
                                                'А многие люди бросали и бросают университет. Можно ли утверждать, '
                                                'что все они потеряли год жизни? Не думаю...', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans1 == 'да' and answers_ege.ans4 == 'да':
        ege = bot.send_message(message.chat.id, 'Смотри, нас снимают на работе, в школе, на улице, в парикмахерской, '
                                                'на приёме у стоматолога и много где ещё. Мы перестали обращать на '
                                                'это внимание. Но когда вспоминаем про ЕГЭ, то почему-то '
                                                'начинаем возмущаться. Разве стоит это наших расшатанных нервов? '
                                                'Просто не нарушай правила и не рискуй тогда, когда не надо. '
                                                'Правда будет на твоей стороне в случае чего!', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans4 == 'да':
        ege = bot.send_message(message.chat.id, 'Страх видеокамер - это интересное, но распространённое свойство. '
                                                'Конечно, раньше на экзаменах на видеокамеру никого не снимали, '
                                                'но очень строго контролировали сдачу экзаменов члены '
                                                'экзаменационной комиссии, тщательно следившие за тем, чтобы никто '
                                                'не пользовался шпаргалками. И экзамены все люди тоже сдавали в '
                                                'непривычной для себя обстановке. Опять же, стоит себя спросить: '
                                                'так ли непривычно тебе находиться под объективом видеокамер? '
                                                'Увы, повсеместная видеосъёмка стала нормой современной жизни.',
                               reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans1 == 'да' or answers_ege.ans2 == 'да':
        ege = bot.send_message(message.chat.id,
                               'Неплохо сдать хоть один экзамен - уже повод для гордости, на самом деле! '
                               'По статистике каждый год минимум 7% учеников заваливают ЕГЭ. Уже неплохо, '
                               'что в их число ты не входишь. Дальше стоит наметить план подготовки! '
                               ' В ЕГЭ очень много типичных и шаблонных заданий - сделай '
                               'на них упор! Что касается итогов сдачи - мир не рухнет, если вдруг '
                               'не выйдет поступить в унивреситет. Перед тобой всё равно будет '
                               'много возможностей. Главное - верить в себя.', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans2 == 'нет' and answers_ege.ans3 == 'нет':
        ege = bot.send_message(message.chat.id, 'Главное - не паникуй. Подумай: может, тогда лучше выждать паузу, '
                                                'сдав экзамены через год? Знаешь, ничего глобально страшного '
                                                'не случится, если в этом году не получится. Не в этот год, '
                                                'так в следующий. Да и всегда есть возможность попробовать пересдать. '
                                                'Изучи список ВУЗов, подумай над возможным переездом. '
                                                'Помни, что варианты есть всегда и жизнь не кончается из-за '
                                                'одной неуспешной сдачи. Это не будет фатальной ошибкой!',
                               reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    elif answers_ege.ans5 == 'да':
        ege = bot.send_message(message.chat.id, 'Скажи, это давление со стороны родителей или учителей?',
                               reply_markup=keyboard2)
        bot.register_next_step_handler(ege, get_attention_parents)
    elif answers_ege.ans3 == 'да':
        ege = bot.send_message(message.chat.id,
                               'Ох, понимаю твоё волнение. Скажу тебе по секрету, я тоже этого очень боялся. '
                               'Однако жизнь не кончается, если не поступить в университет. '
                               'Не нужно думать, что если ты завалишь ЕГЭ - твоя жизнь будет окончена, '
                               'ведь это не так.', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)
    else:
        ege = bot.send_message(message.chat.id, 'Я в тебя верю в любом случае! И всегда тебя поддержу! Знаю, звучит '
                                                'предсказуемо, но порой именно таких слов нам не хватает. Ты имеешь право'
                                                'на абсолютно любое решение. И на любые чувства. Единственное, что '
                                                'стоит понимать - каждое твоё действие несёт последствия. Подумай '
                                                'хорошенько, что к чему может привести и дальше действуй, как '
                                                'посчитаешь нужным. Удачи!', reply_markup=keyboard4)
        bot.register_next_step_handler(ege, get_oge_end)


bot.polling()
