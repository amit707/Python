# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:41:15 2017

@author: amits
"""

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
i=0
while i<5:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
    i+=1