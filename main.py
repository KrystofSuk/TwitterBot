#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys, getopt, time

historySearch = 10
ttl = 120
breakTime = 6000

hashtags = []

alreadyVisited = []

class Bot:
    def __init__(self, us, pswd):
        self.username = us   
        self.password = pswd
        self.bot = webdriver.Firefox()     

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')

        time.sleep(3)

        usernameField = bot.find_element_by_name('session[username_or_email]')
        passwordField = bot.find_element_by_name('session[password]')

        usernameField.clear()
        passwordField.clear()

        usernameField.send_keys(self.username)
        passwordField.send_keys(self.password)
        passwordField.send_keys(Keys.RETURN)
        
        time.sleep(3)

    def like(self):
        bot = self.bot
        while(True):
            time.sleep(3)
            tweetLinks = []
            hs = 0
            while(hs < len(hashtags)):
                bot.get('https://twitter.com/search?q='+hashtags[hs]+'&src=typd')
                time.sleep(ttl)
                for i in range(1,historySearch):
                    bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    time.sleep(ttl)
                    try:
                        l = [i.get_attribute('href')for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
                        for href in l:
                            if href not in tweetLinks and href not in alreadyVisited:
                                tweetLinks.append(href)
                                alreadyVisited.append(href)
                        time.sleep(ttl)
                    except Exception as ex:
                        print(ex)
                hs = hs + 1

            time.sleep(2)
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))
            print(filteredLinks)

            for link in filteredLinks:
                bot.get(link)
                time.sleep(ttl)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    print("I Liked:", link)
                    time.sleep(ttl)
                except Exception as ex:
                    bot.refresh()
                    print("I Couldn't Like:", link)
                    time.sleep(ttl*2)

            bot.get('https://twitter.com/search?q='+hashtags[0]+'&src=typd')
            print("Getting a break!")
            time.sleep(breakTime)

def main(argv):

    argo = Bot(argv[0], argv[1])
    i = 2
    print(len(argv))
    while(i < len(argv)):
        hashtags.append(argv[i])
        i = i + 1
    print("Starting Argo Bot")
    argo.login()
    argo.like()    
    

if __name__ == "__main__":
   main(sys.argv[1:])
