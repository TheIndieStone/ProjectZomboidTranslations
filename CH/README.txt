1. Make sure you're using Big5 encoding.
	To ensure that you're file is in the correct encoding, I recommend you to edit them using Notepad++ and check the encoding settings.
	I also recommend AGAINST making edits straight on GitHub, as we've seen instances where GitHub would convert a file into UTF-8 encoding, thus causing the entire file to be displayed incorrectly.

2. Make sure you don't use any full-form symbols, the font does NOT support them as of build 41, and I don't expect it to work anytime soon.
	Example:
		Instead of:
			你好，我（就是我！）是一個句子。
		You should enter:
			你好, 我 (就是我! ) 是一個句子. 
