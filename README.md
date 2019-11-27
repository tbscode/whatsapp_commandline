experimental python selenium whatsapp bot.

# Whats-app Message Scheduler

Command line tool to schedule send of whats-app messages.

- well so far only sends messages
- but it will be able to schedule them

## How it works:

It uses your current browser profile ( firefox / chrome )  to send messages using your that browsers Whats-App access token.

- Doesn't require login
- Just a browser with enables cookies and cache
  and logged in to whatsapp web

## Usage

` python whatsappcmd.py send -m "Whats upp" -to "<Contact Name>" `

```sh
positional arguments:
  send                 send a message
optional arguments:
  -h, --help           show this help message and exit
  -m M                 message
  -to TO               contact: by name
  --browser BROWSER    set browser firefox (default) / chrome
  --visible [VISIBLE]  should the botted browser be visible when run then add
                       this option
```

### Tested

- Ubuntu 18.04 with firefox

## Dependencies

- selenium
- chrome of firefox
