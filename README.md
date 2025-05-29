# Online and Offline Translator
## Overview
This application utilises two libraries from Pypi in order to deliver results, no matter if the user is connected to the internet or not.
- The application asks the user which method they would like to use (online or offline).
- When the user selects a method, a window pops up and prompts the user to select a text file for translation.
- The file is then translated in the terminal.
- The application asks the user whether they want to save the file. If yes, a new window pops up prompted the user to select a directory.
- Finally, the application saves the translation in a text file in the given directory, and prints the directory in the terminal.

##Notes
- The application uses a set of standard language codes for the offline translator (no details are given from the developer of the library as to which languages they use apart from ISO 639-1).
- The application counts the characters and gives a warning about the offline translator (there's a character limit of 500 characters).
- The application utilises the internal Error "LanguageNotSupportedException" of the google library to display the available languages.
For both options, error handling is implemented to loop back to the beginning, allowing the user to retry.
