#!/usr/bin/env python3

from googletrans import Translator

def translate_text(text, src='en', dest='ur'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def main():
    text = input("Enter the English text to translate: ")
    translation = translate_text(text)
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()
