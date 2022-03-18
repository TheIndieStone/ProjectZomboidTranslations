# IMPORTANT RULES TO FOLLOW

THE RULES WRITTEN HERE ARE FOR TRADITIONAL CHINESE (CH) TRANSLATIONS, IF YOU'RE CONTRIBUTING TRANSLATIONS OF OTHER LANGUAGES, PLEASE REFER TO THEIR OWN SPECIFIC RULES.

## 1. Make sure you're using Big5 encoding.

To ensure that you're file is in the correct encoding, it is recommended that you edit them using Notepad++ and always check the encoding settings.
	
It is also recommended that you **DO NOT** make edits straight on GitHub, as we've seen instances where GitHub would convert a file into UTF-8 encoding, thus causing the entire file to be displayed incorrectly.

## 2. Make sure you are **NOT** using any full-form symbols, the font **DOES NOT** support them as of build 41, and I don't expect it to work anytime soon.

### Example:

Instead of:

`你好，我（就是我！）是一個句子。`

You should enter:

`你好, 我 (就是我! ) 是一個句子. `

## 3. If you're using TranslationZed, keep the following quirks in mind:

- It does **NOT** support Recorded_Media.
- It fails to recognize keywords containing "=" correctly.
- It fails to recognize multi-line keywords correctly. (You'll see the keyword ending with ".." instead of properly showing the next line)
