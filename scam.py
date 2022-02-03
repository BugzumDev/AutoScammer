# AutoScammer v:1.0
# Made by: BugzumDev

# I am NOT responsible for any damage
# Please don't go out and scam people with this

# Libaries
from fbchat import Client
from fbchat.models import *

# log in
client = Client("<email>", "<password>")

# Thread setup
thread_id = "1234567890"
thread_type = ThreadType.GROUP

# basic runtime information
scamname = "<scamName>"
scamtemplate = "1"
language = "hu"

# Scam template 1
scamdevice = "<scamDevice>"
scamend = "-t"

# Scamtemplate 2
scamvalue = "<scamAmount>"

# Just some basic info
scamlink = "<scamLink>"
scamemoji = "🤑📱"

# Scam templates
if scamtemplate == "1":
    if language == "hu":
        scammsg = "Gratulálunk " + scamname + "! Ön nyert egy új " + scamdevice + scamend + "! Az ezközt megrendelheted ingyenesen itt: " + scamlink + " " + scamemoji
    elif language == "en":
        scammsg = "Congratulations " + scamname + "! You just won a " + scamdevice + scamend + "! You can redeem the device here: " + scamlink + " " + scamemoji
elif scamtemplate == "2":
    if language == "hu":
        scammsg = scamname + ", önnek még van " + scamvalue + " összege az amazon számláján ami hamarosan lejár! Kattincson ide az összeg felhasználásához: " + scamvalue
    elif language == "en":
        scammsg = scamname + ", you still have a " + scamvalue + " gift card that is going to expire! You can use the card here: " + scamvalue
elif scamtemplate == "costum":
    scammsg = "<costumMessage>"
elif scamtemplate == "3":
    if language == "hu":
        scammsg = "Hé, szeretnél beszélgetni? Kattincs ide ha igen: " + scamlink
    elif language == "en":
        scammsg = "Hey, do you want to talk? Click here: " + scamlink


# Send message
client.send(Message(text=scammsg), thread_id=thread_id, thread_type=thread_type)