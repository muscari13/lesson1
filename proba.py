import os
import sys


print("proba.py")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добропожаловать в мир python!")

answer = ''
while answer != 'Q':
	answer = input("Давайте поработаем? (Y/N/Q?)")
	if answer == 'Y':
		print("1. Вывести список файлов?")
		print("2. Вывести информацию о системе?")
		answer2 = int(input("Выбери номер ответа!"))
		if answer2 == 1:
				print(os.listdir())
		elif answer2 == 2:
				print("Платформа системы:", sys.platform)
				print("Текущая директория:", os.getcwd())
				print("Текущий пользователь:", os.getlogin())
		else:
				pass
	elif answer == 'N':
		print("До свидания!")
	else:
		print("Неизвестный выбор")

