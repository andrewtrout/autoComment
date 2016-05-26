from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import random
import os


browser = webdriver.PhantomJS(service_log_path=os.path.devnull)
browser.set_window_size(960,1170)


def login():

	MY_USER = raw_input("Input Username:")
	MY_PASSWORD = getpass("Input Password:")

	browser.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26next%3D%252F%26hl%3Den%26feature%3Dsign_in_button%26app%3Ddesktop&hl=en&passive=true#identifier')

	time.sleep(3)

	email = browser.find_element_by_css_selector('input[placeholder="Enter your email"]')
	email.send_keys(MY_USER, Keys.RETURN)
	time.sleep(2)

	pw = browser.find_element_by_css_selector('input[placeholder="Password"]')
	pw.send_keys(MY_PASSWORD, Keys.RETURN)
	print "logged in successfully!"
	time.sleep(1)



def troll():

	video = raw_input('Paste a Youtube video URL to troll here:')
	counter = 1
	max_comment = 100 #Number of comments to make
	comments = ["This is wack", "This video sucks", "What kind of potato did you use to shoot this?"] #Put your comments here


	if "youtube.com" not in video:

		print "This isn't a youtube video"

		troll()

	else:

		browser.get(video)

		time.sleep(8)

		browser.execute_script("window.scrollBy(0, 600);")

		while counter <= max_comment:

			comment = random.choice(comments)

			comment_box = browser.find_element_by_css_selector('.comment-simplebox-renderer-collapsed-content')
			comment_box.click()
			comment_here = browser.find_element_by_css_selector('.comment-simplebox-text')
			comment_here.send_keys(comment)
			browser.find_element_by_css_selector('.comment-simplebox-submit').click()


			print "%s Comment '%s'" % (counter, comment)
			counter+=1
			time.sleep(60*30) #Half hour 


login()
troll()







