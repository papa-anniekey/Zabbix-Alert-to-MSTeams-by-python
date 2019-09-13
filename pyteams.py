#!/usr/bin/env python3
import pymsteams
import sys

id = "<Set your own Incoming Webhook ID>"

args = sys.argv

myTeamsMessage = pymsteams.connectorcard(id)
myTeamsMessage.title(args[1])
myTeamsMessage.text(args[2])

myTeamsMessage.send()
