import PIL
from PIL import ImageGrab, Image, ImageOps
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

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

def answer_question(how_many=1):
	for i in range(how_many):
		time.sleep(1)
		mouse.position = (0, 0)
		sourceImg = ImageGrab.grab()
		# take a screenshot and process the question
		question = sourceImg.crop([620,230,1300,340])
		question = image_to_string(question)

		#question.show()
		#ans1.show()
		#ans2.show()
		#ans3.show()
		#ans4.show()
		#old code
		#question = ImageGrab.grab([640,230,1280,340])
		#ans1 = ImageGrab.grab([320,580,640,620])
		#ans2 = ImageGrab.grab([1280,580,1600,620])
		#ans3 = ImageGrab.grab([320,870,640,910])
		#ans4 = ImageGrab.grab([1280,870,1600,910])
		# find the correct answer
		print(question)
		for i in answers:
			if i[0] == question:
				answer = i[1]
				break
		print(answer)

		# Crop the original picture and turn the answers into strings, then check if it is correct
		correct_answer = 0
		for i in range(1):
			ans1 = sourceImg.crop([320,580,640,620])
			ans1 = image_to_string(ans1)
			if ans1 == answer or ans1 == '':
				mouse.position = (50,500)
				correct_answer = 1
				break

			ans2 = sourceImg.crop([1280,580,1600,620])
			ans2 = image_to_string(ans2)
			if ans2 == answer or ans2 == '':
				mouse.position = (1200,500)
				correct_answer = 2
				break

			ans3 = sourceImg.crop([320,870,640,920])
			#ans3 = ImageOps.invert(ans3)
			#ans3.show()
			ans3 = image_to_string(ans3)
			print(ans3)
			if ans3 == answer or ans3 == '':
				mouse.position = (50,800)
				correct_answer = 3
				break

			ans4 = sourceImg.crop([1280,870,1600,920])
			ans4 = image_to_string(ans4)
			if ans4 == answer or ans4 == '':
				mouse.position = (1200, 800)
				correct_answer = 4
				break
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
			break

def go_to_shop():
	mouse.position = (30, 110)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (30, 150)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def money_per_question():
	mouse.position = (1500, 200)
	mouse.click(Button.left, 1)
	time.sleep(0.5)

def streak_bonus():
	mouse.position = (1000, 200)
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

def mega_boost():
	mouse.position = (1850, 850)
	mouse.click(Button.left, 1)
	

answer_question(6)
time.sleep(0.5)
go_to_shop()
streak_bonus()
buy_upgrade()
answer_question(5)
go_to_shop()
money_per_question()
mouse.position = (1000, 800)
mouse.click(Button.left, 1)
time.sleep(0.5)
buy_upgrade()
answer_question(1)
powerups()
mega_boost()
