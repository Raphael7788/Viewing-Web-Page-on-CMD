#!usr/bin/env python3
# -*- coding: UTF-8 -*-
# Viewing Page Source from a specific website on CMD
from urllib import urlopen

doc = urlopen("https://www.wired.com/story/why-an-old-theory-of-everything-is-gaining-new-life/").read()
print doc
