## alfred-password-gen
This workflow adds memorable password generation with the keyword `password`.

The `password` keyword can optionally be followed by a number ranging 10-35 to control password length. The
default is 16.

Selecting a password adds it to the clipboard.

<img src="/docs/screenshot.png" width="600">

### Installation
Download the newest version via [the latest release](https://github.com/cholick/alfred-password-gen/releases/latest)

### Why?
Using a password manager, most passwords should just be completely random. A memorable algorith is useful in situations like
* WiFi (sharing or entry on devices)
* Streaming apps (to more readily type it into the TV on systems that don't have an easy logic from computer code)
* Something that needs memorization (a device login)

### Notes
* The dictionary likely still has several offensive or triggering words: I did a quick pass through to remove
some, but I'm sure I missed many.
* [12Dicts](http://wordlist.aspell.net/12dicts-readme/) is the source dictionary.
* [dictionary/process.py](dictionary/process.py) takes [dictionary/2of12inf.txt](dictionary/2of12inf.txt) and produces [dictionary/processed.py](dictionary/processed.py) after doing some cleanup. This only needs running again if the source words change.
* Alfred workflow docs
  - https://www.alfredapp.com/help/workflows/actions/run-script/
  - https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
