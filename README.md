# webpage-static_mon v1.0 Help File

# Description:
This python program is designed to be used as a cron job that monitors a webpage and alerts the user when that page has been updated.  The input is a URL the user defines in the program and the output is a printed message if the webpage has changed. Note: This program monitors general html pages that do not require a browser to rendor content (for example, a webpage that performs a database search query to display information).  For display dynamic content, see my other project webpage-dynamic_mon.

# Why is this program needed?:
There are a number of instances for when a user may want to know when a webpage has been updated.  The user is waiting for an announcement, a price change, or to monitor their own website for unauthorized changes.  Rather than manually check the website this program can be used to automate the process.  This program was specifially designed to be used a cron job on an existing webserver using minimal python libraries.

# References:
Portions of this program were borrowed from Paul Bitutsky and his blog on a similar project using a Raspbery Pi.  Please visit Paul's  original post or visit his github page to see a more advanced version of this program. Links are below.

Blog: https://medium.com/swlh/tutorial-creating-a-webpage-monitor-using-python-and-running-it-on-a-raspberry-pi-df763c142dac

Github: https://github.com/pbitutsky/webmonitor

# Disclaimer:
Please do not abuse this program by overarlly monitoring webpages.  Each monitor request does consume resources of the website owner.  Please be considerate.

# Prerequisites:
   Python v2 is needed to execute the program.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2.
   1. Download and install python from https://www.python.org/downloads/ . Note: Choose any version of Python that starts with "2", not "3".
   1. Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".

   MacOS users:  None, both python and the necessary libraries should be natively installed.
		
   Linux users:  None, both python and the necessary libraries should be natively installed.

# Execution instructions  
  Prior to running the program you will need to edit one field inside webpage_mon.py, changing it to the desired webpage to monitor.

    URL_TO_MONITOR = "https://www.example.com/page"
 
  Run wegpage_mon from a command prompt or terminal window with:
  
    python webpage_mon.py
   
  If you would like the program to run on a schedule it can be added as a cron job as initially designed.

# Use of Regular Expressions
  Regular expressions are used to generate search patterns for content which should be ignored when comparing webpages.  For example, there may be a date/time, nonce, or counter which is constantly changing on the webpage thus causing false positives that the webpage has changed.  While Regular Expressions are not the ideal choice to remove such content, it is however the most efficient when using the most minimal python libraries as possible.
  
# Latest Updates
* v1.0.

# Planned Updates:
* Python v3 support.
* Add diff function to display changed content.
