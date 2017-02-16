#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script allows you to read and write settings of an application.
There are the following settings:
- "CultureCode" - like 'ru-RU', obligatory.
- "Servers" - a list of servers, where each server is described by the following attributes:
    - "ID" - integer, unique, obligatory.
    - "ServerName" - string, obligatory.
    - "ServerPort" - integer, obligatory.
    - "UserName" - string, optional (if not specified, a user must enter it when runs the application).
    - "Password" - string, optional (if not specified, a user must enter it when runs the application).
"""

import os
import json


class Settings(object):
    """Read and write app settings using a JSON file"""
    def __init__(self, path):
        self.filePath = path
        self.__data = self.__read_file()
        self.__write_file()

    def __read_file(self):
        if os.path.exists(self.filePath):
            data = json.load(open(self.filePath, 'r'))
            return data
        else:
            return self.__create_default()

    @staticmethod
    def __create_default():
        data = {'CultureCode': 'ru-RU',
                'Servers': [
                    {1: {'ServerName': 'LOCALHOST', 'ServerPort': 1017,
                     'UserName': '', 'Password': ''}}
                ]}
        return data

    def __write_file(self):
        json.dump(self.__data, open(self.filePath, 'w'), indent=4)

    def get_settings(self):
        return self.__data

    def set_cultureCode(self, newCode):
        """"Only strings like 'ru' or 'ru-RU' are allowed"""
        newCode = str(newCode)
        if len(newCode) == 2 or len(newCode) == 5:
            self.__data['CultureCode'] = newCode
            self.__write_file()

    def edit_serverByID(self, serverID, serverName = None,
                        serverPort = None, userName = None, password = None):
        if isinstance(serverID, int):
            pass

"""ОСТАНОВИЛСЯ ЗДЕСЬ
В этом классе надо дописать, как обновить атрибуты сервера, не забыть возможность задавать имя и пароль юзера пустой строкой - смю isinstance('', type(None))

Дальше надо сделать методы для добавления и удаления серверов, а также получение текущей папки.

"""



mySettings = Settings(r'C:\Users\Alexey\Documents\GitHub\CGScripting\4. Text files\appSettings.config')


print mySettings.get_settings()

mySettings.set_cultureCode('en-US')

print mySettings.get_settings()



