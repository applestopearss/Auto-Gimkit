from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.gimkit.com/play')

import time
from Answers import answers
from pynput.mouse import Button, Controller
import keyboard
mouse = Controller()
start = False
while not start:
	time.sleep(0.5)
	if keyboard.is_pressed("s"):
		start = True
	#print("not started")		
#print("started")


#print(question)
#print(ans1)
#print(ans2)
#print(ans3)
#print(ans4)

def answer_question(how_many=1):
	for i in range(how_many):
		time.sleep(1)
		res = driver.execute_script("return document.documentElement.outerHTML")
		soup = BeautifulSoup(res, 'lxml')
		question_and_answers = soup.find_all('span', {"class":"notranslate lang-en"})

		question = question_and_answers[0].text
		ans1 = question_and_answers[1].text
		ans2 = question_and_answers[2].text
		ans3 = question_and_answers[3].text
		ans4 = question_and_answers[4].text
		
		print(question)
		print(ans1)
		print(ans2)
		print(ans3)
		print(ans4)
		mouse.position = (0, 0)
		#time.sleep(1)
		# find the correct answer
		print(question)
		for i in answers:
			if i[0] == question:
				answer = i[1]
				
		print(answer)

		# Crop the original picture and turn the answers into strings, then check if it is correct
		correct_answer = 0
		
		if ans1 == answer:
			mouse.position = (50,500)
			correct_answer = 1
			

		elif ans2 == answer:
			mouse.position = (1200,500)
			correct_answer = 2
			

		if ans3 == answer:
			mouse.position = (50,800)
			correct_answer = 3
			

		if ans4 == answer:
			mouse.position = (1200, 800)
			correct_answer = 4
			
		#time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (1000,800)
		mouse.click(Button.left, 1)

		if correct_answer == 0:
			print('something broke')
			print(ans1)
			print(ans2)
			print(ans3)
			print(ans4)
			

def go_to_shop():
	mouse.position = (30, 110)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (30, 150)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def go_to_questions():
	mouse.position = (30, 110)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (30, 110)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def money_per_question():
	mouse.position = (500, 200)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def streak_bonus():
	mouse.position = (1000, 200)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def multiplier():
	mouse.position = (500, 800)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def buy_upgrade():
	mouse.position = (1000, 600)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (1000, 700)
	mouse.click(Button.left, 1)

def powerups():
	mouse.position = (950, 1000)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def upgrades():
	mouse.position = (800, 1000)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def mega_boost():
	mouse.position = (1850, 850)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (950, 750)
	mouse.click(Button.left, 1)

def discount():
	mouse.position = (1850, 650)
	mouse.click(Button.left, 1)

def use_powerup():
	mouse.position = (30, 110)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (250, 225)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def level_3():
	#levels are 385 x apart and 180 y apart
	mouse.position = (1000, 800)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
		

answer_question(6)
time.sleep(0.5)
go_to_shop()
streak_bonus()
buy_upgrade()
answer_question(5)
go_to_shop()
money_per_question()
level_3()
buy_upgrade()
answer_question(1)
go_to_shop()
powerups()
mega_boost()
answer_question(2)
go_to_shop()
upgrades()
streak_bonus()
level_3()
buy_upgrade()
answer_question(2)
go_to_shop()
multiplier()
level_3()
buy_upgrade()
answer_question(1)
go_to_shop()
powerups()
discount()
use_powerup()
go_to_questions()
answer_question(4)

while True:
	answer_question(500)


#driver.quit()