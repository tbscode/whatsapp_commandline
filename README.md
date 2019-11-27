experimental python selenium whatsapp bot.

# Whats-app Message Scheduler

Command line tool to schedule send of whats-app messages.

- well so far only sends messages
- but it will be able to schedule them
- *only works with cookies enabled*

## How it works:

It uses your current browser profile ( firefox / chrome )  to send messages using your that browsers Whats-App access token.

- Doesn't require login
- Just a browser with enables cookies and cache
  and logged in to whatsapp web

1. Login to whatapp web with your browser
2. check the keep logged in box
3. close the browser: done

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

### Or interactive

When sending multiple messages keeps the whatappweb session open, commands are the same.

```
(bash) user@pc: python whatsappcmd.py start
Namespace(action='start', browser='firefox', m=None, timeout=15, to=None, visible=1)
trying to connect to firefox browser
connected to browser
waiting for load ..
 > send -m "Message" -to "<Contact Name>"
```



### Tested

- Ubuntu 18.04 with firefox

## Dependencies

- selenium
- chrome of firefox
- and the chrome / [firefox](https://github.com/mozilla/geckodriver/releases) driver has to be in your ` $PATH `
