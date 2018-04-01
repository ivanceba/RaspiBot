"""
@Author Ivan Ceballos Vega

"""
import telebot

TOKEN = "TELEBOT_GIVEN_TOKEN"

RED = "red"
BLUE = "blue"
GREEN = "green"
END_COLOR = "endc"
BOLD = "bold"

COMMANDS = {
    'start': 'Arranca el bot',
    'ayuda': 'Comandos disponibles',
    'exec' : 'Ejecuta un comando'
}

MAIN_PAGE = 0
RASPI_INFO_PAGE = 1

PRIVILEGE_USERS = [206388682]

RASPI_INFO_KEYWORD = "RPinfo"
BOT_TYPING_KEYWORD = "TYPING"

TEMP = "TEMP"
HD = "HD"
RAM = "RAM"
CPU = "CPU"
BACK = "BACK"

INFO_MENU = telebot.types.ReplyKeyboardMarkup()
INFO_MENU.add(TEMP, HD)
INFO_MENU.add(RAM, CPU)
INFO_MENU.add(BACK)

TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"
LINUX_UPDATER_COMMAND = "bash /home/ivan/updater.sh"
LINUX_TEMPERATURE_GPU_COMMAND = "sudo /opt/vc/bin/vcgencmd measure_temp"
LINUX_RAM_COMMAND = "free -h"
LINUX_HD_COMMAND = "df -h /"

TITLE_TEXT = "[+] {}:"
INFO_TEXT = """\
\t[i]\tTotal: %s
\t[i]\tUsado: %s
\t[i]\tDisponible: %s 
"""

INFO_TEXT_TEMP = """\
\t[i]\tCPU: %s
\t[i]\tGPU: %s
"""

MAIN_MENU_TEXT = "Menú principal"
RPINFO_TEXT = "Información disponible:"
RAM_TEXT = "MEMORIA RAM"
CPU_TEXT = CPU
HD_TEXT = "DISCO DURO"
TEMP_TEXT = "TEMPERATURAS"
SYS_UPDATED_TEXT = "**SYSTEM UPDATED**"
PERM_DENIED_TEXT = "Permission denied"
RESULT_TEXT = "Resultado: "
EXECUTING_TEXT = "Ejecutando: "
HELP_TEXT = "Comandos disponibles:\n"
WELCOME_TEXT = "Bienvenido al gestor, {}!"

CONS_NEW_USER = "[!] New user!"

SERV404 = "Unavailable service"
