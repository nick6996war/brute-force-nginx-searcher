# -*- coding: utf-8 -*-

from distutils.log import error
import io
import os
import re
from collections import Counter
from alive_progress import alive_bar

import os

cmd = 'mode 202,42'
os.system(cmd)

logo="""
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
       ,@@&#&@@*                                                  ,@%             .@(%@      #@,     &%      /@        @&.      #@*    &@,            @@     .@/     #@,@#      @@     .@,  *@,     .@/ 
       @@,    @@                                                  @%             .@#  &@     #@,    *@(      /@       @@         (@   #@.    .....    @@     #@,    (@. ,@/     @@     %@.  *@&&&&&@&@/ 
       .@@@%@@@,                                                  @@.            @#.  .&&    #@*,,/@*        /@       #@.        &&   /@/        @/   @@,,,#@      *@,...*@*    @@,,,,.     *@,     .@/ 
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

# сюда будут складываться айпи адреса для дальнейшего пощета количества
ipList=[]
# счетчик файлов
counter = 0
wordpatern='r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"gm'
print("Hello")
filepath= input("Input file path: ")
# функция сбора путей к файла и записи их в файл ТК либо я не вьехал в питон либо он не дружит со сложной рекурсией
thisdir = os.getcwd()
with io.open("pathFile.txt", "w", encoding="utf-8", errors='ignore') as pathFile:
    for r, d, f in os.walk(filepath):  
        for file in f:
            filepath = os.path.join(r, file)
            counter += 1
            pathFile.write(os.path.join(r, file) + "\n")
pathFile.close()


# функция чтения путей по к файлам
print(f"All: {counter} files.")
with io.open("pathFile.txt", 'r', encoding='utf8', errors='ignore') as f:
    pathText = f.read().splitlines()
    with alive_bar(counter, dual_line=True, title='Alphabet') as bar:
        
        for path in pathText:
            bar.text = f'-> Reading file: {path}, please wait...'
            try:
                with io.open(path, 'r',encoding='utf8', errors='ignore') as dataF:
                    textfile = dataF.read().splitlines()
                dataF.close()
            

                for line in textfile:
                    ip = re.search(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", line)
                    if  ip != None:
                        if " 401 "in line:
                            ipList.append(ip.group(0))
            except:
                print('error:' + str(error) + '\n'+ path)
            bar()

c = Counter(ipList) 
answ =str(c).replace(',','\n')
answ = answ[9:]
answ = answ[:-2]
print(answ)
with io.open("exit.txt", "w", encoding="utf-8", errors='ignore') as exitFile:
    exitFile.write(answ)
print('output saved to file exit.txt')
