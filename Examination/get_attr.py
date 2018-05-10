#!/usr/bin/env python  
# coding=utf-8  
voice_message = {}
voice_message['type'] = 'voice'
voice_message['content'] = 'music'
text_message = {}
text_message['type'] = 'text'
text_message['content'] = 'word'

class Handler(object):
    """docstring for Chain"""
    def __init__(self):
        pass
        
    def text_handler(self,message):
        print(message['content'])

    def voice_handler(self,message):
        print(message['content'])

    def handler(self,arg):
        return getattr(self,arg['type']+'_handler')(arg)

random_handler = Handler()
random_handler.handler(text_message)
random_handler.handler(voice_message)