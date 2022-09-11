##Python Logging:
##==============
It is highly recommended to store complete application flow and exception information to a file. This process of writing data to the file is called logging.
Advantages:
-We can use log files while performing debugging.
-We can generate utilization reports like number of requests per day etc

#How many logging levels are there in Python : 6 in total
1. CRITICAL(50): Represents a very serious problem that needs high attention like Complete Application Failure.
2. ERROR(40): Represents a serious error. Some part of the application not working properly.
3. WARNING(30): Represents a warning message, some caution needed. It is alert to the programmer.
4. INFO(20): Represents a message with some important information.
5. DEBUG(10): Represents a message with debugging information.
6. NOTSET(0): Represents that level is not set.

--------------------------------------------------------------------------------------
##To implement logging with a demo program:
-We should know which file to write.
-Which logging level messages to write?
ex: logging.basicConfig(filename='log.txt',level=logging.WARNING) ##level=logging.WARNING means logs equal to WARNING and higher i.e. critical and error are captured in log.txt.
-|||ly the functions for other logging levels are:
    logging.critical(message)
    logging.error(message)
    logging.warning(message)
    logging.info(message)
    logging.debug(message)
-Even if log.txt is available or not we don't have to worry, the code line "logging.basicConfig(filename='log.txt',level=logging.WARNING)" will take care of it.
-By default appending will happen to log.txt file.
-If all levels of data needs to be printed to log.txt then we need to specify logging.DEBUG :)
-********We can also use 'level=30' instead of 'level=logging.WARNING'.
log_path >> "C:\Users\91961\PycharmProjects\pythonProject\Web\log.txt"

##Example1: To create a log file and write warning and higher level messages to it?
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
##We can specify log.txt/error.log/server.log etc... not an issue.
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message

##We're re-executing, then the data will be appended:
##Output:

##Example2:
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG) ##******
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message
DEBUG:root:This debug message

##Example3:
import logging
logging.basicConfig(filename='log.txt',level=20) ##******
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message

-------------------------------------------------------------------------------------

##How to configure log file in over writing mode?
-We do by using filemode='w'
    'a' ==> Append (This is default mode)
    'w' ==> Overwrite

##Example:
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG,filemode='w')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message
DEBUG:root:This debug message

##Example1: The default values for basicConfig??
Default Values:
    filemode = 'a'
    level = 'warning'
    filename = 'If no filename mentioned,by default the messages will be printed to console'

import logging
logging.basicConfig(filename='log.txt')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
CRITICAL:root:This is critical message (Next three lines got appended)
ERROR:root:This is error message
WARNING:root:This is warning message

##Example2:
import logging
logging.basicConfig()
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
##Below data is printed onto console
logging Demo
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message

---------------------------------------------------------------------------------
##Steps to format log messages:

-The meaning of 'root' in the output is called as logger 'CRITICAL:root:This is critical message'
Default Syntax for Logs : 'levelname:loggername:message'
-logging.basicCOnfig(format='%(levelname)s') ##This will only print the level name and meaning of 's' is string type
-logging.basicConfig(format='%(levelname)s:%(message)s') ##This will print the level name & message and meaning of 's' is string type
-logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s') ##This will print the level name,loggername & message and meaning of 's' is string type
-logging.basicConfig(format='%(levelname)s:%(name)s:%(process)d:%(message)s') ##This will print the level name,loggername,processid & message and meaning of 's' is string type and 'd' is int type.

Refer >> '''https://docs.python.org/3/library/logging.html#loggeradapter-objects''' To understand possible arguments to pass.

##Example:
import logging
logging.basicConfig(format='%(levelname)s')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL
ERROR
WARNING
logging Demo

##Example2:
import logging
logging.basicConfig(format='%(levelname)s:%(message)s')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
logging Demo
CRITICAL:This is critical message
ERROR:This is error message
WARNING:This is warning message

##Example3:
import logging
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
logging Demo

##Example4:
import logging
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s:%(module)s:%(lineno)s') ##lineno prints the source line for which message got triggered and module prints file name.
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message:Udemy:4
ERROR:root:This is error message:Udemy:5
WARNING:root:This is warning message:Udemy:6
logging Demo

-----------------------------------------------------------------------------

##How to add timestamp and date to log messages??

##Example:
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s') ##asctime prints IST time
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
2022-09-07 22:01:57,570:CRITICAL:This is critical message
2022-09-07 22:01:57,570:ERROR:This is error message
2022-09-07 22:01:57,570:WARNING:This is warning message

##Example1:
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
logging Demo
07/09/2022 10:08:09 PM:CRITICAL:This is critical message
07/09/2022 10:08:09 PM:ERROR:This is error message
07/09/2022 10:08:09 PM:WARNING:This is warning message

##Example2:
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
logging Demo
07/09/2022 22:10:54:CRITICAL:This is critical message
07/09/2022 22:10:54:ERROR:This is error message
07/09/2022 22:10:54:WARNING:This is warning message

Refer > 'https://docs.python.org/3/library/time.html#time.strftime' for more arguments to use.

----------------------------------------------------------------------------------------

##How to add exception information to the logfile and demo program.

##Example1:
try:
    x=int(input('Enter FIrst Number: '))
    y=int(input('Enter Second Number: '))
    print('The result: ',x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with zero')
except ValueError as msg:
    print('Provide int values only')

##Output:
Enter FIrst Number: r
Provide int values only

Enter FIrst Number: 3
Enter Second Number: 0
Cannot divide with zero

##Example2: Let's implement logging
import logging
logging.basicConfig(filename='mylog18072019.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
logging.info('A new request came')
try:
    x=int(input('Enter First Number: '))
    y=int(input('Enter Second Number: '))
    print('The result: ',x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('Provide int values only')
    logging.exception(msg)
logging.info('A request process completed')

##Output:
##Below messages are written to a file
07/09/2022 22:43:43:INFO:A new request came
07/09/2022 22:43:53:INFO:A request process completed
07/09/2022 22:43:55:INFO:A new request came
07/09/2022 22:43:59:ERROR:division by zero
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 10, in <module>
    print('The result: ',x/y)
ZeroDivisionError: division by zero
07/09/2022 22:43:59:INFO:A request process completed
07/09/2022 22:44:02:INFO:A new request came
07/09/2022 22:44:05:ERROR:invalid literal for int() with base 10: 'def'
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 8, in <module>
    x=int(input('Enter First Number: '))
ValueError: invalid literal for int() with base 10: 'def'
07/09/2022 22:44:05:INFO:A request process completed

-------------------------------------------------------------------------------------

##Problems with Root Logger:

##Example1:
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG,filemode='w')
logging.basicConfig(filename='abc.txt',level=logging.ERROR,filemode='w') ##We're trying to override the config by writing to a new file and with updated logging level, unfortunately this won't work due to root logger in previous step has already finalized everything ;P
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message
DEBUG:root:This debug message

##Example2:
#test.py : Through this I want to perform file handler, i.e. to write message to file
import logging
import module1 ##This led to a different story ;P, data is displayed to console
logging.basicConfig(filename='test.log',level=logging.DEBUG)
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

#module1.py : Through this I want to perform console handler, i.e. to write message to console
import logging
logging.basicConfig()
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
##The messages are printed onto the console and it is limited warninglog level:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message

##Example3:
#test.py : Through this I want to perform file handler, i.e. to write message to file
import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG) ##Henge Naavu ;P
import module1 
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

#module1.py : Through this I want to perform console handler, i.e. to write message to console
import logging
logging.basicConfig()
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This debug message')

##Output:
##Both messages are printed onto the a file and it is printing from debug log  level:
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message
DEBUG:root:This debug message
CRITICAL:root:This is critical message
ERROR:root:This is error message
WARNING:root:This is warning message
INFO:root:This is info message
DEBUG:root:This debug message

##Note: Problems with root logger:
-Once we set basic configuration then that configuration is final and we cannot change.
-We can use either file handler or console handler but not both simultaneously.
-It is not possible to configure logger with different configurations at different levels.
-We cannot specify multiple log files for multiple modules/classes/methods.
-To make sure that console messages are printed on console and messages mentioned to write into file are written onto the file is not possible.
-To make console module to print from error level and file handler to print from warning level is not possible.
-For different function different logging.
-No Boss, nothing doing, not possible.
-To overcome such issues, we need to opt for custom logging.

--------------------------------------------------------------------------------------

##How to define and use customized logger:
-For this we need to create three objects:
    1. Logger : This is whole & soul logger, responsible for implementing customisable logging.
    2. Handler : Helps to write into file, send via mail or print to console.
        -Stream Handler : To write onto console
        -File Handler : To write onto file
        -SMTP Handler : To send via email
        -HTTP Handler : To send to webserver by using http protocol
    3. Formatter : Responsible to format log message.
    
##ImpStep : Post implementing/Creating objects then we need to associate Formatter with Handler and Handler with Logger, our customizable logger is ready.

1. Create logger object & set level:
    logger=logging.getLogger('demologger') ##Created custom logger
    logger.setLevel(logging.WARNING) ##By default in custom logger logging level is NOTSET, i.e. it will print all levels
2. Create Handler Object & set Level:
    consoleHandler=logging.StreamHandler()
    consoleHandler.setLevel(logging.WARNING) ##By default it takes log level same as logger or we can give our own
    ##or
    fileHandler=logging.FileHandler('abc.log',mode='w')
    fileHandler.setLevel(logging.ERROR) ##By default it takes log level same as logger or we can give our own
3.  Create Formatter Object:
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
4. Set Formatter to Handler:
    consoleHandler.setFormatter(formatter)
    ##or
    fileHandler.setFormatter(formatter)
5. Add Handler to Logger:
    logger.addHandler(consoleHandler)
    ##or
    logger.addHandler(fileHandler)
6. Write log messages by logger object:
    logger.critical(message)
    logger.error(message)
    logger.warning(message)
    logger.info(message)
    logger.debug(message)
    
---------------------------------------------------------------------------------------

##Write a program to define and use custom logger with console handler?

##Example1:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
consoleHandler=logging.StreamHandler() ##To display on the console
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
consoleHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(consoleHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
08/09/2022 21:38:48:CRITICAL:demologger:It is critical message
08/09/2022 21:38:48:ERROR:demologger:It is error message
08/09/2022 21:38:48:WARNING:demologger:It is warning message
08/09/2022 21:38:48:INFO:demologger:It is info message
08/09/2022 21:38:48:DEBUG:demologger:It is debug message

##Example2:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
consoleHandler=logging.StreamHandler() ##To display on the console
consoleHandler.setLevel(logging.ERROR) ##************We can control logging level even at console handler.
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
consoleHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(consoleHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
08/09/2022 21:47:39:CRITICAL:demologger:It is critical message
08/09/2022 21:47:39:ERROR:demologger:It is error message

##Example3:
##Write a program to define and use custom logger with file handler:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
fileHandler=logging.FileHandler('custtest.log',mode='w') ##To write to a file
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##The output is written to a file "C:\Users\91961\PycharmProjects\pythonProject\Web"
08/09/2022 21:53:25:CRITICAL:demologger:It is critical message
08/09/2022 21:53:25:ERROR:demologger:It is error message
08/09/2022 21:53:25:WARNING:demologger:It is warning message
08/09/2022 21:53:25:INFO:demologger:It is info message
08/09/2022 21:53:25:DEBUG:demologger:It is debug message

##Example4:
##Write a program to define and use custom logger with file handler:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
fileHandler=logging.FileHandler('custtest.log',mode='w') ##To write to a file
fileHandler.setLevel(logging.ERROR) ##************We can control logging level even at file handler as well.
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##The output is written to a file "C:\Users\91961\PycharmProjects\pythonProject\Web"
08/09/2022 21:53:25:CRITICAL:demologger:It is critical message
08/09/2022 21:53:25:ERROR:demologger:It is error message

---------------------------------------------------------------------------------------

##Write a program to define and use customlogger with both console and file handlers:

##Example1:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
consoleHandler=logging.StreamHandler() ##To display on the console
fileHandler=logging.FileHandler('abc.log',mode='w') ##To write to a file
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
consoleHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.addHandler(consoleHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##Logging is written onto console:
08/09/2022 22:08:51:CRITICAL:demologger:It is critical message
08/09/2022 22:08:51:ERROR:demologger:It is error message
08/09/2022 22:08:51:WARNING:demologger:It is warning message
08/09/2022 22:08:51:INFO:demologger:It is info message
08/09/2022 22:08:51:DEBUG:demologger:It is debug message
##Logging is written to a file:
08/09/2022 22:08:51:CRITICAL:demologger:It is critical message
08/09/2022 22:08:51:ERROR:demologger:It is error message
08/09/2022 22:08:51:WARNING:demologger:It is warning message
08/09/2022 22:08:51:INFO:demologger:It is info message
08/09/2022 22:08:51:DEBUG:demologger:It is debug message

##Example2:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
consoleHandler=logging.StreamHandler() ##To display on the console
fileHandler=logging.FileHandler('abc.log',mode='w') ##To write to a file
fileHandler.setLevel(logging.DEBUG) ##Diff logging level for file
consoleHandler.setLevel(logging.ERROR) ##Diff logging level for console
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
consoleHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.addHandler(consoleHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##Logging is written onto console:
08/09/2022 22:08:51:CRITICAL:demologger:It is critical message
08/09/2022 22:08:51:ERROR:demologger:It is error message
##Logging is written to a file:
08/09/2022 22:08:51:CRITICAL:demologger:It is critical message
08/09/2022 22:08:51:ERROR:demologger:It is error message
08/09/2022 22:08:51:WARNING:demologger:It is warning message
08/09/2022 22:08:51:INFO:demologger:It is info message
08/09/2022 22:08:51:DEBUG:demologger:It is debug message

##Example3:
import logging
logger=logging.getLogger('demologger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
consoleHandler=logging.StreamHandler() ##To display on the console
fileHandler=logging.FileHandler('abc.log',mode='w') ##To write to a file
fileHandler.setLevel(logging.DEBUG) ##Diff logging level for file
consoleHandler.setLevel(logging.ERROR) ##Diff logging level for console
formatter1=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
formatter2=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
fileHandler.setFormatter(formatter1) ##Associate formatter to handler
consoleHandler.setFormatter(formatter2) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.addHandler(consoleHandler) ##To add handler to logger
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##Logging is written onto console:
CRITICAL:demologger:It is critical message
ERROR:demologger:It is error message
##Logging is written to a file:
08/09/2022 22:08:51:CRITICAL:demologger:It is critical message
08/09/2022 22:08:51:ERROR:demologger:It is error message
08/09/2022 22:08:51:WARNING:demologger:It is warning message
08/09/2022 22:08:51:INFO:demologger:It is info message
08/09/2022 22:08:51:DEBUG:demologger:It is debug message

----------------------------------------------------------------------------------

##Write a program to define and use custom logger with different modules and with different log files:
##Example1:
##test.py
import logging
import student
logger=logging.getLogger('testlogger') ##Created custom logger
logger.setLevel(logging.DEBUG) ##Setting logginfg level
fileHandler=logging.FileHandler('test.log',mode='a') ##To write to a file
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.critical('It is critical message from test module')
logger.error('It is error message from test module')
logger.warning('It is warning message from test module')
logger.info('It is info message from test module')
logger.debug('It is debug message from test module')

##student.py
import logging
logger=logging.getLogger('studentlogger')
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler('student.log',mode='w') ##To write to a file
logger.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
fileHandler.setFormatter(formatter) ##Associate formatter to handler
logger.addHandler(fileHandler) ##To add handler to logger
logger.critical('It is critical message from student module')
logger.error('It is error message from student module')
logger.warning('It is warning message from student module')
logger.info('It is info message from student module')
logger.debug('It is debug message from student module')

##Output:
##test.log file:
08/09/2022 22:51:15:CRITICAL:testlogger:It is critical message from test module
08/09/2022 22:51:15:ERROR:testlogger:It is error message from test module
08/09/2022 22:51:15:WARNING:testlogger:It is warning message from test module
08/09/2022 22:51:15:INFO:testlogger:It is info message from test module
08/09/2022 22:51:15:DEBUG:testlogger:It is debug message from test module
##student.log file:
2022-09-08 22:51:15,263:CRITICAL:studentlogger:It is critical message from student module
2022-09-08 22:51:15,263:ERROR:studentlogger:It is error message from student module

----------------------------------------------------------------------------------

##Importance of inspect module:
-It's a Python's inbuilt module:

##Example1:
##module1.py
import inspect
def getInfo():
    print(inspect.stack()) ##Complete stack trace of the caller who's calling the function

##test.py:
from module1 import getInfo
def f1():
    getInfo()
f1()

##Output:
[FrameInfo(frame=<frame at 0x000001C8D4BCC240, file 'C:\\Users\\91961\\PycharmProjects\\pythonProject\\module1.py', line 3, code getInfo>, filename='C:\\Users\\91961\\PycharmProjects\\pythonProject\\module1.py', lineno=3, function='getInfo', code_context=["    print(inspect.stack()) ##Complete stack trace of the caller who's calling the function\n"], index=0), FrameInfo(frame=<frame at 0x000001C8D463E3E0, file 'C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', line 3, code f1>, filename='C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', lineno=3, function='f1', code_context=['    getInfo()\n'], index=0), FrameInfo(frame=<frame at 0x000001C8D463A040, file 'C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', line 4, code <module>>, filename='C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', lineno=4, function='<module>', code_context=['f1()\n'], index=0)]

##Example2:
##module1.py
import inspect
def getInfo():
    print(inspect.stack()[1]) ##Caller info details
    print(inspect.stack()[1][1]) ##Calling File/Module Name
    print(inspect.stack()[1][3]) ##Caller function name

##test.py:
from module1 import getInfo
def f1():
    getInfo()
f1()

##Output:
FrameInfo(frame=<frame at 0x0000012C23B8E3E0, file 'C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', line 3, code f1>, filename='C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', lineno=3, function='f1', code_context=['    getInfo()\n'], index=0)
C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py
f1

---------------------------------------------------------------------------------

##Creation of generic logger and usage:
##module1.py
import inspect
import logging

def get_custom_logger(level):
    function_name=inspect.stack()[1][3]
    logger_name=function_name+" logger"
    logger=logging.getLogger(logger_name)
    logger.setLevel(level)
    fileHandler=logging.getLogger(logger_name)
    logger.setLevel(level) ##Setting logginfg level
    fileHandler=logging.FileHandler('generic.log',mode='a') ##To write to a file
    fileHandler.setLevel(level)
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                datefmt='%d/%m/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter) ##Associate formatter to handler
    logger.addHandler(fileHandler) ##To add handler to logger
    return logger

##test.py
from module1 import get_custom_logger
import logging
def logtest():
    logger=get_custom_logger(logging.DEBUG)
    logger.critical('Critical message from test module')
    logger.error('Error message from test module')
    logger.warning('Warning message from test module')
    logger.info('Info message from test module')
    logger.debug('Debug message from test module')
logtest()

##Output:
08/09/2022 23:47:10:CRITICAL:logtest logger:Critical message from test module
08/09/2022 23:47:10:ERROR:logtest logger:Error message from test module
08/09/2022 23:47:10:WARNING:logtest logger:Warning message from test module
08/09/2022 23:47:10:INFO:logtest logger:Info message from test module
08/09/2022 23:47:10:DEBUG:logtest logger:Debug message from test module


##Example2:
##module1.py
import inspect
import logging

def get_custom_logger(level):
    function_name=inspect.stack()[1][3]
    logger_name=function_name+" logger"
    logger=logging.getLogger(logger_name)
    logger.setLevel(level)
    #fileHandler=logging.getLogger(logger_name)
    logger.setLevel(level) ##Setting logginfg level
    fileHandler=logging.FileHandler('generic1.log',mode='a') ##To write to a file
    fileHandler.setLevel(level)
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                datefmt='%d/%m/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter) ##Associate formatter to handler
    logger.addHandler(fileHandler) ##To add handler to logger
    return logger

##test.py
from module1 import get_custom_logger
import logging
def f1():
    logger=get_custom_logger(logging.DEBUG)
    logger.critical('Critical message from f1')
    logger.error('Error message from f1')
    logger.warning('Warning message from f1')
    logger.info('Info message from f1')
    logger.debug('Debug message from f1')
def f2():
    logger=get_custom_logger(logging.WARNING)
    logger.critical('Critical message from f2')
    logger.error('Error message from f2')
    logger.warning('Warning message from f2')
    logger.info('Info message from f2')
    logger.debug('Debug message from f2')
def f3():
    logger=get_custom_logger(logging.ERROR)
    logger.critical('Critical message from f3')
    logger.error('Error message from f3')
    logger.warning('Warning message from f3')
    logger.info('Info message from f3')
    logger.debug('Debug message from f3')
f1()
f2()
f3()

##Output:
10/09/2022 23:01:34:CRITICAL:f1 logger:Critical message from f1
10/09/2022 23:01:34:ERROR:f1 logger:Error message from f1
10/09/2022 23:01:34:WARNING:f1 logger:Warning message from f1
10/09/2022 23:01:34:INFO:f1 logger:Info message from f1
10/09/2022 23:01:34:DEBUG:f1 logger:Debug message from f1
10/09/2022 23:01:34:CRITICAL:f2 logger:Critical message from f2
10/09/2022 23:01:34:ERROR:f2 logger:Error message from f2
10/09/2022 23:01:34:WARNING:f2 logger:Warning message from f2
10/09/2022 23:01:34:CRITICAL:f3 logger:Critical message from f3
10/09/2022 23:01:34:ERROR:f3 logger:Error message from f3

##Example3: To create separate logfile based on caller dynamically:
##module1.py
import inspect
import logging

def get_custom_logger(level):
    function_name=inspect.stack()[1][3]
    logger_name=function_name+" logger"
    logger=logging.getLogger(logger_name)
    logger.setLevel(level)
    #fileHandler=logging.getLogger(logger_name)
    logger.setLevel(level) ##Setting logginfg level
    fileHandler=logging.FileHandler(function_name+'.log',mode='a') ##To write to a file
    ##Or
    #fileHandler=logging.FileHandler('{}.log'.format(function_name),mode='a')
    fileHandler.setLevel(level)
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                datefmt='%d/%m/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter) ##Associate formatter to handler
    logger.addHandler(fileHandler) ##To add handler to logger
    return logger

##test.py
from module1 import get_custom_logger
import logging
def f1():
    logger=get_custom_logger(logging.DEBUG)
    logger.critical('Critical message from f1')
    logger.error('Error message from f1')
    logger.warning('Warning message from f1')
    logger.info('Info message from f1')
    logger.debug('Debug message from f1')
def f2():
    logger=get_custom_logger(logging.WARNING)
    logger.critical('Critical message from f2')
    logger.error('Error message from f2')
    logger.warning('Warning message from f2')
    logger.info('Info message from f2')
    logger.debug('Debug message from f2')
def f3():
    logger=get_custom_logger(logging.ERROR)
    logger.critical('Critical message from f3')
    logger.error('Error message from f3')
    logger.warning('Warning message from f3')
    logger.info('Info message from f3')
    logger.debug('Debug message from f3')
f1()
f2()
f3()

##Output:
#f1.log:
10/09/2022 23:07:37:CRITICAL:f1 logger:Critical message from f1
10/09/2022 23:07:37:ERROR:f1 logger:Error message from f1
10/09/2022 23:07:37:WARNING:f1 logger:Warning message from f1
10/09/2022 23:07:37:INFO:f1 logger:Info message from f1
10/09/2022 23:07:37:DEBUG:f1 logger:Debug message from f1
#f2.log:
10/09/2022 23:07:37:CRITICAL:f2 logger:Critical message from f2
10/09/2022 23:07:37:ERROR:f2 logger:Error message from f2
10/09/2022 23:07:37:WARNING:f2 logger:Warning message from f2
#f3.log:
10/09/2022 23:07:37:CRITICAL:f3 logger:Critical message from f3
10/09/2022 23:07:37:ERROR:f3 logger:Error message from f3

----------------------------------------------------------------------------------
##Need of separating logger configuration file or dict or json or yaml??
#Advantages:
-Modifications will become very easy.
-We can reuse same configurations in difeerent modules.
-Length of the code will be reduced and readability will be improved.

##Example1:
##logging_config.ini
[loggers]
keys=root,demologger

[handlers]
keys=fileHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_demologger]
level=DEBUG
handlers=fileHandler
qualname=demoLogger

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=sampleFormatter
args=('configured_log.log','w')

[formatter_sampleFormatter]
format=%(asctime)s:%(levelname)s:%(name)s:%(message)s
datefmt=%d/%m/%Y %H:%M:%S

##test.py
import logging
import logging.config
logging.config.fileConfig('logging_config.ini') ##fileConfig is a function used to load configurations present in a file
logger=logging.getLogger('demologger')
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##configured_log.log
10/09/2022 23:42:36:CRITICAL:demologger:It is critical message
10/09/2022 23:42:36:ERROR:demologger:It is error message
10/09/2022 23:42:36:WARNING:demologger:It is warning message
10/09/2022 23:42:36:INFO:demologger:It is info message
10/09/2022 23:42:36:DEBUG:demologger:It is debug message

##Example2:
##logging_config.ini
[loggers]
keys=root,demologger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=WARNING
handlers=consoleHandler

[logger_demologger]
level=WARNING
handlers=consoleHandler
qualname=demoLogger

[handler_consoleHandler]
class=StreamHandler
level=WARNING
formatter=sampleFormatter
args=(sys.stdout,) ##stdout: Standard Output device, i.e. console

[formatter_sampleFormatter]
format=%(asctime)s:%(levelname)s:%(name)s:%(message)s
datefmt=%d/%m/%Y %H:%M:%S

##test.py
import logging
import logging.config
logging.config.fileConfig('logging_config.ini') ##fileConfig is a function used to load configurations present in a file
logger=logging.getLogger('demologger')
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

##Output:
##Written onto console
10/09/2022 23:53:43:CRITICAL:demologger:It is critical message
10/09/2022 23:53:43:ERROR:demologger:It is error message
10/09/2022 23:53:43:WARNING:demologger:It is warning message