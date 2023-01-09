# -*- coding: utf-8 -*-

from distutils.log import error
import io
import os
import re
from collections import Counter
from alive_progress import alive_bar
import datetime as dt
import os
import json
import gzip

cmd = 'mode 202,42'
os.system(cmd)

logo = """
                                                                       ,#&@@&(,           /@@@@@@.                %@@@@@%#@@@@@@@@@@@@@@@@@#.          (@@@@@@@@@@@@@@@@@@@&    (@@@@@@@@@@@@@@%*
          ./(/.                                                  .%%,            *&#        (#   ,@             %(   *&    ,@.                *@,        .&*              .@     .@.              .#%
        (@@(,(@@(                                              ##    .#@&(//#&@(.  ,@.        ##   ,&.        ##   *&         *///////////(&#   .@          ////////////////       *///////////&&,   *%
        @@*   *@@                                            (#   *@,            *(             ##   *&     ##   *&.                         #*  *#                                               %*  .%
         %@@@@@%                                            %*  .@                                %(   *& (#   ,@.                           #/  ,#                                               .&   &
              *@,                                          .%   @                                   &/   *   .@          ..............,.,*&%    @     ..................,..                      #/  .%
                @(                                         (*  *%                                     &*   .&,           &                    .&,      @.                  @             ,,,,,*(&/   ,&
                 #&                                        ,#  .&                                   *&    @,             &@@@@@@@@@@@@@@@@@&.   *&     @@@@@@@@@@@@@@@@@@@@&              (#       /&
                  *@/%@@@@@@%*                              &,  ,&                                ,@.  .&,                                   %,  /(                                        .&   .@
                 #@@@@@@@@@@@@@@%                            %*   %(                            ,&    %*                                     ((  .%                                          ((   %*
  #@@@%        /@@@@#        (@@@@(                           .&,   .#@(                      ,&.   &*                                     *@,   @.                                            @   ,&
.@*   ,@*.    ,@@@@            &@@@/                             (&*       ,%#.             .&.   %/                          &.               ##         ##               @                    %*   @.
 &@, ,@@      #@@@(            ,@@@%      #@@@@&                     .%@@@&&@@@#.         .@&&&&&(                            &&&&&&&&&&&&@@@/         *@&&&&&&&&&&&&&&&&&%&                     *@&&%@(
              ,@@@@            &@@@/.,*/#@@,   @&
               *@@@@%        #@@@@/       %@@@@@.
                 (@@@@@@@@@@@@@@#
                 ,@&,#&@@@@&#,
               #@/                                                  .&@@@@@(       ,@@       (@@@@@@@/   #@@@@@@@@@,     #@@@@@&.        (@@@@@&.     @@@@@@@@,       #@#       @@@@@@@&.   *@,     .@/
       #&@@*                                                  ,@%             .@(%@      #@,     &%      /@        @&.      #@*    &@,            @@     .@/     #@,@#      @@     .@,  *@,     .@/
       ,@@&
       #  &@     #@,    *@(      /@       @@         (@   #@.    .....    @@     #@,    (@. ,@/     @@     %@.  *@&&&&&@&@/
       @@,    @@                                                  @%             .@
       #.  .&&    #@*,,/@*        /@       #@.        &&   /@/        @/   @@,,,#@      *@,...*@*    @@,,,,.     *@,     .@/
       .@@@%@@@,                                                  @@.            @
                                                                   (@&,   *@(   @%      @%   #@,    @#       /@        ,@@*     %@(    .@@/.  ,%@/    @@    *@,   *@,     ,@,   @@          *@,     .@/
                                                                     (@&,*@(    @%      @%   #@,    @#       /@          ,@@,%@(        .@@ ,%@/      @@    *@,   *@,     ,@,   @@          *@,     .@/
    __               __          ____                                    _                                         __                      ___  ____
   / /_  _______  __/ /____     / __/___  _____________     ____  ____ _(_)___  _  __   ________  ____ ___________/ /_  ___  _____   _   _<  / / __ \\
  / __ \/ ___/ / / / __/ _ \   / /_/ __ \/ ___/ ___/ _ \   / __ \/ __ `/ / __ \| |/_/  / ___/ _ \/ __ `/ ___/ ___/ __ \/ _ \/ ___/  | | / / / / / / /
 / /_/ / /  / /_/ / /_/  __/  / __/ /_/ / /  / /__/  __/  / / / / /_/ / / / / />  <   (__  )  __/ /_/ / /  / /__/ / / /  __/ /      | |/ / /_/ /_/ /
/_.___/_/   \__,_/\__/\___/  /_/  \____/_/   \___/\___/  /_/ /_/\__, /_/_/ /_/_/|_|  /____/\___/\__,_/_/   \___/_/ /_/\___/_/       |___/_/(_)____/
                                                              /____/
"""
print(logo)



# счетчики
counter = 0

print("Hello")
filepath = input("Input file path: ")
# radioData = input("Do yo want set time interval? yes/no: ")

# if radioData == 'yes': radioData = 1
# else: radioData= 0

# fileMass =[]
ipsBrutMass = []
ipsOvertimeMass = []
loginOvertimrMass = []
overLoginMass = {}

# def getdatefrom():
#     try:
#         dayFrom = int(input("Enter the day from: "))
#         monthFrom = int(input("Enter the month from: "))
#         yearFrom = int(input("Enter the year from: "))
#         global dateFrom
#         dateFrom =dt.datetime(yearFrom,monthFrom,dayFrom)
#     except:
#         print('error: uncorect date \n' + str(error)+'\n')
#         getdatefrom()
# def getdatebefore():
#     try:
#         dayBefore = int(input("Enter the day Before: "))
#         monthBefore = int(input("Enter the month Before: "))
#         yearBefore = int(input("Enter the year Before: "))
#         global dateBefore
#         dateBefore = dt.datetime(yearBefore, monthBefore, dayBefore)
#     except:
#         print('error: uncorect date \n' + str(error)+'\n')
#         getdatebefore()

# if radioData == 1: getdatefrom(), getdatebefore()

# def getPath(path):
#     thisdir = os.getcwd()
#     for r, d, f in os.walk(path):
#         for file in f:
#             filepathFull = os.path.join(r, file)
#             if os.path.splitext(file)[1] in fileTypes:
#                 zip = zipfile.ZipFile(filepathFull)
#                 print (zip.namelist())

#             else:
#                 counter += 1
#                 fileMass.append(filepathFull)


def BRUTE_FFORCE(line):
    ip = re.search(
        r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", line)
    if ip != None and " 401 " in line:
        ipsBrutMass.append(ip.group(0))


def OVERTIME(line, hourFrom, hourBefore):
    if hourFrom == None:
        hourFrom = 8
    if hourBefore == None:
        hourBefore = 20
    time = re.search(r":\d{2}:\d{2}:\d{2}", line)
    if time:
        time = time.group(0)
        time = dt.datetime.strptime(time, ':%H:%M:%S')
        timeFrom = dt.datetime.strptime(str(hourFrom), '%H')
        timeBefore = dt.datetime.strptime(str(hourBefore), '%H')
        if timeBefore <= time or time <= timeFrom:
            ip = re.search(
                r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", line)
            if ip != None and " 200 " in line:
                ipsOvertimeMass.append(ip.group(0))
            lineMass = line.split(' ')
            login = lineMass[2]
            loginOvertimrMass.append(login)


def OVER_LOGIN(line):
    ip = re.search(
        r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", line)
    lineMass = line.split(' ')
    login = lineMass[2]
    #overLoginMass.append(login)


def UNGZ(filepathFull):
    exitData = ''
    with gzip.open(filepathFull, 'rb') as f:
        fileContent = f.read()
        fileContent = str(fileContent)
        fileContent = fileContent[2:]
        fileContent = fileContent[:-1]
        fileContent = fileContent.replace('\\n', '\n')
        exitData += fileContent
    return exitData


thisdir = os.getcwd()
for r, d, f in os.walk(filepath):
    for file in f:
        filepathFull = os.path.join(r, file)
        if os.path.splitext(file)[1] == '.gz':
            fileData = UNGZ(filepathFull)
            fileData = fileData.splitlines()
            for line in fileData:
                OVER_LOGIN(line)
                OVERTIME(line, None, None)
                BRUTE_FFORCE(line)
        else:
            counter += 1
            with io.open(filepathFull, 'r', encoding='utf8', errors='ignore') as dataF:
                textfile = dataF.read().splitlines()
            dataF.close()
            for line in textfile:
                OVER_LOGIN(line)
                OVERTIME(line, None, None)
                BRUTE_FFORCE(line)


a = Counter(ipsBrutMass) 
answ =str(a).replace(',','\n')
answ = answ[9:]
answ = answ[:-2]
print('err logins')
print(answ+"\n")


b = Counter(ipsOvertimeMass) 
answ =str(b).replace(',','\n')
answ = answ[9:]
answ = answ[:-2]
print("top ips work from 20 to 8")
print(answ+"\n")

c = Counter(loginOvertimrMass) 
answ =str(c).replace(',','\n')
answ = answ[9:]
answ = answ[:-2]
print("top logins work from 20 to 8")
print(answ+"\n")