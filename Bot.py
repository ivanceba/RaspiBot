import os
import time

from RaspberryBot.Color import ConsoleColor
from RaspberryBot.constants import *


class Bot:
    __bot = telebot.TeleBot(TOKEN)
    __user_step = {}
    __known_users = []
    __color_manager = ConsoleColor()

    def __init__(self):
        self.__color_manager.paint("Starting bot...", GREEN)
        self.__bot.set_update_listener(_listener)

        @self.__bot.message_handler(commands=['start'])
        def command_start(m):
            cid = m.chat.id

            self.__bot.send_message(cid, WELCOME_TEXT.format(m.chat.first_name))
            time.sleep(1)
            command_help(m)

        @self.__bot.message_handler(commands=['ayuda'])
        def command_help(m) -> None:
            cid = m.chat.id
            help_text = HELP_TEXT
            for key in COMMANDS:
                help_text += "/" + key + ": " + COMMANDS[key] + "\n"
            self.__bot.send_message(cid, help_text)

        @self.__bot.message_handler(commands=['exec'])
        def command_exec(m) -> None:
            cid = m.chat.id
            if cid in PRIVILEGE_USERS:
                self.__bot.send_message(cid, EXECUTING_TEXT + m.text[len("/exec"):])
                self.__bot.send_chat_action(cid, BOT_TYPING_KEYWORD)
                time.sleep(2)
                f = os.popen(m.text[len('/exec'):])
                result = f.read()
                self.__bot.send_message(cid, RESULT_TEXT + result)
            else:
                self.__color_manager.paint(PERM_DENIED_TEXT, RED, self.__bot, cid)

        @self.__bot.message_handler(commands=['raspUpdate'])
        def rasp_update_command(m) -> None:
            cid = m.chat.id
            os.system(LINUX_UPDATER_COMMAND)
            self.__color_manager.paint(SYS_UPDATED_TEXT, GREEN, self.__bot, cid)

        @self.__bot.message_handler(func=lambda message: self.__get_user_step(message.chat.id) is MAIN_PAGE)
        def main_menu(m):
            cid = m.chat.id
            text = m.text

            if text == RASPI_INFO_KEYWORD:
                self.__bot.send_message(cid, RPINFO_TEXT, reply_markup=INFO_MENU)
                self.__user_step[cid] = 1
            else:
                command_help(m)

        @self.__bot.message_handler(func=lambda message: self.__get_user_step(message.chat.id) is RASPI_INFO_PAGE)
        def info_opt(m):
            cid = m.chat.id
            txt = m.text

            if txt == TEMP:
                temp_file = open(TEMP_FILE)
                cpu_temp = temp_file.read()
                temp_file.close()
                cpu_temp = round(float(cpu_temp) / 1000)
                gpu_temp = os.popen(LINUX_TEMPERATURE_GPU_COMMAND).read().split("=")[1][:-3]

                title = TITLE_TEXT.format(TEMP_TEXT)
                text = INFO_TEXT_TEMP % (cpu_temp, gpu_temp)
            elif txt == HD:
                disk_spaces = _disk_space()
                text = INFO_TEXT % (disk_spaces[0], disk_spaces[1], disk_spaces[2])
                title = TITLE_TEXT.format(HD_TEXT)
            elif txt == RAM:
                ram_space = _ram_info()
                text = INFO_TEXT % (ram_space[0], ram_space[1], ram_space[2])
                title = TITLE_TEXT.format(RAM_TEXT)
            elif txt == CPU:
                title = TITLE_TEXT.format(CPU_TEXT)
                text = SERV404
                # cpu = os.popen('mpstat | grep -A 5 "%idle" | tail -n 1 | awk -F ". ". \'{print 100 - $
                # 12}\'a').read()
                # bot.send_message(cid, "  [i]   Usado: %s" % cpu)
                # print(Color.GREEN + " [i] Usado: %s" % cpu + Color.ENDC)
            elif txt == BACK:
                self.__user_step[cid] = MAIN_PAGE
                self.__bot.send_message(cid, MAIN_MENU_TEXT, reply_markup=telebot.types.ReplyKeyboardRemove())
                return
            else:
                command_help(m)
                return
            self.__color_manager.paint(title, BLUE, self.__bot, cid)
            self.__color_manager.paint(text, GREEN, self.__bot, cid)

    def start(self):
        self.__color_manager.paint("Bot started...", GREEN)
        self.__bot.polling()

    def __get_user_step(self, uid: int) -> int:
        if uid not in self.__user_step:
            self.__known_users.append(uid)
            self.__user_step[uid] = MAIN_PAGE
            self.__color_manager.paint(CONS_NEW_USER, RED)
        return self.__user_step[uid]


def _listener(messages) -> None:
    for m in messages:
        if m.content_type == 'text':
            print("[" + str(m.chat.id) + "] " + str(m.chat.first_name) + ": " + m.text)


def _disk_space():
    p = os.popen(LINUX_HD_COMMAND)
    i = 0
    while True:
        i += 1
        line = p.readline()
        if i is 2:
            return line.split()[1:5]


def _ram_info():
    p = os.popen(LINUX_RAM_COMMAND)
    i = 0
    while True:
        i += 1
        line = p.readline()
        if i is 2:
            return line.split()[1:4]
