import telebot

from RaspberryBot.constants import *


class ConsoleColor:
    __colors = {
        RED      : '\033[91m',
        BLUE     : '\033[94m',
        GREEN    : '\033[32m',
        END_COLOR: '\033[0m',
        BOLD     : '\033[1m'
    }

    def paint(self, text, text_color=GREEN, bot_message: telebot.TeleBot = None, cid: int = None,
              reply_keyboard: telebot.types=None):
        if text_color not in self.__colors:
            raise ConsoleColorError()
        print(self.__colors[text_color] + text + self.__colors[END_COLOR])
        if bot_message:
            if reply_keyboard:
                bot_message.send_message(cid, text, reply_markup=reply_keyboard)
            else:
                bot_message.send_message(cid, text)


class ConsoleColorError(Exception):
    def __init__(self, *args, **kargs):
        super(ConsoleColorError, self).__init__(args, kargs)

    def __str__(self):
        return "Error in colour." + super(ConsoleColorError, self).__str__()
