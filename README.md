# Whats-app Message Scheduler

Command line tool to schedule send of whats-app messages.

## How it works:

It uses your current browser profile ( firefox / chrome )  to send messages using your that browsers Whats-App access token.

- Doesn't require login
- Just a broser with enables cookies
  and logged in to whatsapp web

## Usage

` whatsappcmd send -m "Whats upp" -to "+49 1523 1094410" `
`` 
positional arguments:
  send                 send a message

optional arguments:
  -h, --help           show this help message and exit
  -m M                 message
  -to TO               contact: by name
  --browser BROWSER    set browser firefox (default) / chrome
  --visible [VISIBLE]  should the botted browser be visible when run then add
                       this option
``

## Dependencies

- selenium
- chrome of firefox
