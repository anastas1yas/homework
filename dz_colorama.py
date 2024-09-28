import colorama
from colorama import Fore, Back, Style, init
init()
#init(autoreset=True) #метод для автоматического сброса цвета или стиля после каждой строки
#init(autoreset=False) #метод для того, чтобы цвета и стили НЕ сбрасывались автоматически
color = colorama

print(Fore.CYAN + "white text") # устанавливает цвет текста (помимо голубого цвета есть также 7 других)
print(Fore.RESET + "reset text") # возвращает первоначальный цвет
print(Back.RED + "black back") # делает цветной фон
print(Back.RESET + "reset back") # возвращает исходный фон
print(Style.BRIGHT + "bright style text") # делает текст ярче
print(Style.DIM + "dim style text") # делает текст приглушенным
print(Style.NORMAL + "normal style text") # делает текст стандартным
print(Style.RESET_ALL + "reset all style text") # удаляет все поставленные стили текста
print(Fore.BLACK + Back.GREEN + Style.DIM + "Hello world!" + Style.RESET_ALL) # использование сразу нескольких атрибутов
