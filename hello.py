#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from telethon import TelegramClient

#import pdb
#-------------------------------------------------------------------------------
# git test 111
#-------------------------------------------------------------------------------
class MessagesSnapshot:
    
    def  __init__(self):
        self.first = {}
        self.second = {}
#-------------------------------------------------------------------------------
def load_dialogs():
    ids = []
    with open('dialog.config') as fin:
        for line in fin:
            words = line.split()
            ids.append(int(words[0]))
    return ids
#-------------------------------------------------------------------------------
def compare(messages_snapshot):
    # Новые сообщения
    difference = []
    
    for second_key, second_messages in messages_snapshot.second.items():
        if second_key in messages_snapshot.first:
            for s_message in second_messages:
                first_messages = messages_snapshot.first[second_key]
                par = False
                for f_message in first_messages:
                    if s_message == f_message:
                        par = True
                if par == False:
                    a = []
                    a.append(second_key)
                    a.append(s_message)
                    difference.append(a)
        else:
            for s_message in second_messages:
                a = []
                a.append(second_key)
                a.append(s_message)
                difference.append(a)

    # Выгрузка в БД
    for d1 in difference:
        print(d1)
    print('*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***')
#-------------------------------------------------------------------------------
async def main(messages_snapshot):
    # Параметры работы с Телеграм
    # Идентификаторы Телеграм каналов
    dialog_ids = load_dialogs()

    # Глубина запрашиваемых сообщений
    limit = 12

    #messages_snapshot.second = {}
    
    async for dialog in client.iter_dialogs():
         for identifier in dialog_ids:
             if dialog.id == identifier:
                 messages = await client.get_messages(dialog, limit)
                 messages_chain = []
                 for message in messages:
                    messages_chain.append(message.text)
                 messages_snapshot.second[dialog.id] = messages_chain
    
    # Cравнение first и second, нахождение новых в second
    # --- заполнение first --- заполнение second ---> ось времени
    compare(messages_snapshot)
    
    # Копирование second в first
    messages_snapshot.first = {}
    for k in messages_snapshot.second:
        messages_snapshot.first[k] = messages_snapshot.second[k]
    
    
                 # Заполнение хранилища second
                 #swallow(messages, dialog)
                #pdb.set_trace()
    # Cравнение first и second, нахождение новых в second
    # --- заполнение first --- заполнение second ---> ось времени
    #pdb.set_trace()
    #compare()
    #first = {}
    #for k in second:
    #    first[k] = second[k]
#-------------------------------------------------------------------------------
# Значения получаеммые при регистрации с my.telegram.org
api_id = 14882538
api_hash = '339e8b920c042f412ea424a96eada5dd'

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient('annot', api_id, api_hash)

# Сообщения
ms = MessagesSnapshot() 

while True:
    with client:
        client.loop.run_until_complete(main(ms))
    sleep(60)


#              print('->', dialog.name, 'has ID', dialog.id)
#             for message in messages:
#                 print('{', message.text, '}')
#             print('*\n')
#
#-------------------------------------------------------------------------------
#def swallow(messages, dialog):
#    print('<*** ', dialog.name, 'has ID', dialog.id, ' ***>')
#    for message in messages:
#        print('{', message.text, '}')
#    print('*\n')
#-------------------------------------------------------------------------------        
#         if dialog.id == -1001099860397: #  id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#             
#         if dialog.id == -1001050820672: # ТАСС id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#             
#         if dialog.id == -1001001872252: # ВЕСТИ id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#             
#         if dialog.id == -1001096463945: # НЕЗЫГАРЬ id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#             
#         if dialog.id == -1001134400443: # Reuters Russia id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#             
#         if dialog.id == -1001003921752: # BBC News | Русская служба id
#             messages = await client.get_messages(dialog, limit)
#             swallow(messages, dialog)
#
#'''
# Идентификаторы Телеграм каналов
#dialog_ids = [#-1001099860397, # РБК
#              -1001050820672, # ТАСС
#              #-1001001872252, # ВЕСТИ
#              #-1001096463945, # НЕЗЫГАРЬ
#              #-1001134400443, # Reuters Russia id
#              -1001003921752] # BBC News | Русская служба id
#
# Хранилища сообщений
#first
#second
#
# Новые сообщения
#difference = []
#
# Глубина запрашиваемых сообщений
#limit = 3
#'''
'''
#-------------------------------------------------------------------------------
def swallow():
    #a = {}
    #async for dialog in client.iter_dialogs():
        for identifier in dialog_ids:
            if dialog.id == identifier:
                messages = await client.get_messages(dialog, limit)
                messages_chain = []
                for message in messages:
                    messages_chain.append(message.text)
                a = {}
                a[dialog.id] = messages_chain
    pdb.set_trace()
    return a
#-------------------------------------------------------------------------------
def compare():
    # Новые сообщения
    difference = []
    for second_key, second_messages in second.items():
        if second_key in first:
            print('if second_key in first')
            for s_message in second_messages:
                first_messages = first[second_key]
                par = False
                for f_message in first_messages:
                    if s_message == f_message:
                        par = True
                if par == False:
                    a = []
                    a.append(second_key)
                    a.append(s_message)
                    difference.append(a)
        else:
            print('not found second_key in first')
            for s_message in second_messages:
                a = []
                a.append(second_key)
                a.append(s_message)
                difference.append(a)
'''     
