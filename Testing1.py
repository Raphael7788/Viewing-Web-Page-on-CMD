import urllib.request
with urllib.request.urlopen("https://www.wired.com/story/signal-foundation-whatsapp-brian-acton/") as url:
    s = url.read()
#I'm guessing this would output the html source code?
print(s)
