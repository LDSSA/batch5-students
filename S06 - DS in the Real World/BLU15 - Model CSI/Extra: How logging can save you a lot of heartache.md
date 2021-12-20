# How logging can save you a lot of heartache
## Logging in Python

Logging is a very useful tool in a programmer’s toolbox. It can help you develop a better understanding of the flow of an application and discover scenarios that you might not even have thought of while developing by going way beyond the basic "this request was successful, this request failed". 

Logs provide developers with an extra set of eyes as they can store information, like which user or IP accessed the application. If an error occurs, then they can provide more insights than a stack trace by telling you what the state of the program was before it arrived at the line of code where the error occurred.


## The Logging Module

The [logging module in Python](https://docs.python.org/3/howto/logging.html) is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. It is used by most of the third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application.

Adding logging to your Python program is as easy as this:

        import logging

By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

The logging module provides you with a default logger that allows you to get started without needing to do much configuration. The corresponding methods for each level can be called as shown in the following example:

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
````

The output of the above program would look like this:

```shell
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
````

The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger. This format, which shows the level, name, and message separated by a colon (:), is the default output format that can be configured to include things like timestamp, line number, and other details.

>Notice that the `debug()` and `info()` messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels if you want, but it might get spammy. You can also define your own severity levels by changing configurations, but it is generally not recommended as it can cause confusion with logs of some third-party libraries that you might be using.

More information on how to implement logging into your app is available in the [official documentation](https://docs.python.org/3/howto/logging.html). [This post](https://realpython.com/python-logging/), from where most of what is here was *inspired* from, also goes very indepth on this module and how to set it up. 

## DON’T discard error information

So what's the use of having logger if every time you have a problem, your code looks like this?

```python
try:
    doSomething() 
except:
     pass
```

When something goes wrong it is impossible to tell what it is, and the *author* (meaning **YOU**) knows something will go wrong because they’re actively ignoring it. Unfortunately, by doing so, they are ignoring a host of other potential problems that the developer, or the client, should know about. 

>Are you getting dupplicated IDs when you wouldn't expect them? Log it! The clients might be sending duplicated data by mistake and should be warned about it. 

>Are you not being able to save your request data to your database? Log it! You might unkowingly have reached the available capacity and sometimes log files are not accounted for in data limits. (hence no data might be lost)

## DO log information at the correct level

As everything in life, the key is in the balance. Too much information will make parsing the logs impossible, too little will make tracing of problems impossible. I hope this information is helpful to you and in your future app development endevours. :) 