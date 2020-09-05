# -*- coding: utf-8 -*-
import config
import telebot
import pyodbc
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handel_text(message):
        sti = open('1.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, "/menu")


@bot.message_handler(commands=['menu'])
def handle_text(message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('/Shot_Match')
        markup.row('/Full_Match', 'About')

        bot.send_message(message.chat.id, "menu", reply_markup=markup)


@bot.message_handler(commands=['Shot_Match'])
def handle_text(message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('Atletico_Madrid_S', 'Barcelona_S')
        markup.row('Dynamo_S', 'Inter_Milan_S')
        markup.row('Juventus_S', 'Karpati_S')
        markup.row('Lazio_S', 'Marseille_S')
        markup.row('Milan_S', 'Monako_S')
        markup.row('Olimpic_Lion_S', 'PSG_S')
        markup.row('Real_Madrid_S', 'Shahtar_S')
        markup.row('Valencia_S', 'Vorscla_S')

        bot.send_message(message.chat.id, "menu", reply_markup=markup)


@bot.message_handler(commands=['Full_Match'])
def handle_text(message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('Atletico_Madrid_F', 'Barcelona_F')
        markup.row('Dynamo_F', 'Inter_Milan_F')
        markup.row('Juventus_F', 'Karpati_F')
        markup.row('Lazio_F', 'Marseille_F')
        markup.row('Milan_F', 'Monako_F')
        markup.row('Olimpic_Lion_F', 'PSG_F')
        markup.row('Real_Madrid_F', 'Shahtar_F')
        markup.row('Valencia_F', 'Vorscla_F')

        bot.send_message(message.chat.id, "menu", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text == 'About':

            cursor = config.conn.cursor()
            cursor.execute('select * from  About')

            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.id) + "\t"+str(row.firstname)+"\t")

    
    if message.text == 'Atletico_Madrid_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Atletico_Madrid')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Barcelona_S':
            cursor = config.conn.cursor()
            cursor.execute( 'select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Barcelona')
            row = cursor.fetchone()
            if row:
            	bot.send_message(message.chat.id, str(row))

    if message.text == 'Dynamo_S':
            cursor = config.conn.cursor()
            cursor.execute(  'select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Dynamo')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Inter_Milan_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Inter_Milan')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Juventus_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Juventus')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Karpati_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Karpati')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Lazio_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Lazio')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Marseille_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Marseille')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Milan_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Milan')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Monako_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Monako')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Olimpic_Lion_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Olimpic_Lion')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'PSG_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from PSG')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Real_Madrid_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Real_Madrid')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Shahtar_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Shahtar')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Valencia_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Valencia')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    if message.text == 'Vorscla_S':
            cursor = config.conn.cursor()
            cursor.execute('select last(id),last(w_Country1), last(w_Team1),last(w_Num1),last(w_Num2),last(w_Team2),last(w_Country2) from Vorscla')
            row = cursor.fetchone()
            if row:
                bot.send_message(message.chat.id, str(row))

    

    if message.text == 'Atletico_Madrid_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from  Atletico_Madrid')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")


    if message.text == 'Barcelona_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Bercelona')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Dynamo_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Dynamo')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Inter_Milan_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Inter_Milan')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Juventus_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Juventus')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Karpati_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Karpati')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Lazio_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Lazio')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Marseille_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Merseille')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Milan_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Milan')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Monako_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Monako')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Olimpic_Lion_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Olimpic_Lion')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'PSG_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from  PSG')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Real_Madrid_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Real_Madrid')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Shahtar_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Shahtar')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")


    if message.text == 'Valencia_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Valencia')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

    if message.text == 'Vorscla_F':
            cursor = config.conn.cursor()
            cursor.execute('select * from Vorscla')
            while 1:
                    row = cursor.fetchone()
                    if not row:
                            break

                    bot.send_message(message.chat.id, str(row.w_Country1)+"\t"+str(row.w_Team1)+"\t"+str(row.w_Num1)+"\t"+str(row.w_Num2)+"\t"+str(row.w_Team2)+"\t"+str(row.w_Country2)+"\t")

bot.polling(none_stop=True)



