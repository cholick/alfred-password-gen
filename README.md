### alfred-password-gen
This workflow adds memorable password generation with the keyword `password`.

The `password` keyword can optionally be followed by a number ranging 10-25 to control password length. The
default is 15.

Selecting a password adds it to the clipboard.

The dictionary likely still has several offensive or triggering words: I did a quick pass through to remove
some, but I'm sure I missed many.

![screenshot](/docs/screenshot.png)

### Installation
Download the newest version via [the latest release](https://github.com/cholick/alfred-password-gen/releases/latest)

### Why?
Using a password manager, most passwords should just be completely random. A memorable algorith is useful in situations like
* WiFi (to share with someone)
* Netflix (to more readily type it into the TV)
* Something you need to memorize (a device login)


### Notes
[dictionary/process.py](dictionary/process.py) takes [2of12inf.txt](2of12inf.txt) and produces [dictionary/processed.py](dictionary/processed.py) after doing some cleanup.

Word source: [12Dicts](http://wordlist.aspell.net/12dicts-readme/)

Alfred Docs
* https://www.alfredapp.com/help/workflows/actions/run-script/
* https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
