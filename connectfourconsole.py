# Author: Angel Armendariz, Darren Cruz, Spencer Price
# Emails: angelarmendariz@csu.fullerton.edu, darrencruz@csu.fullerton.edu, spencerprice@csu.fullerton.edu

'''
This module contains the ConnectFour console which runs the game.
'''

import connectfourGUI

def main():
    game = connectfourGUI.ConnectFourApp().run()

if __name__ == '__main__':
    main()
