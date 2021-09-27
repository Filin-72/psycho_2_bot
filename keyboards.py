import telebot

keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard1.add('Снять стресс', 'Нехватка общения', 'Экзамены', 'Давление со стороны', 'Нехватка времени')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2.add('Родители', 'Учителя')

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard3.add('Да', 'Нет', 'Иногда')

keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard4.row('Дальше!')

keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard5.row('В начало!')

keyboard6 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard6.add('В начало!', 'С учителями всё плохо!')

keyboard7 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard7.add('Перепробовал большинство техник', 'Слежу за собой/планирую время', 'Только начинаю')

keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard8.row('Да', 'Нет')

keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard9.row('Звучит неплохо, но если не поможет?')

keyboard10 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard10.add('Подавленность', 'Тревога', 'Постоянная усталость', 'Бессоница')

keyboard11 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard11.add('Реальная опасность', 'Важная проблема', 'Мои мысли')

keyboard12 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard12.row('Всё хорошо', 'Всё плохо')

keyboard13 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard13.row('Ок', 'Не помогает!')

keyboard14 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard14.add('Не совпадают интересы', 'Я слишком критичен', 'Я навязчивый', 'Я чувствую себя неуверенно',
               'Меня отвергают', 'Я намного лучше других', 'Я боюсь')

keyboard15 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard15.add('Друзья отдаляются', 'Мы стали слишком разные', 'Я хочу новых друзей')

keyboard16 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard16.row('ОГЭ', 'ЕГЭ')