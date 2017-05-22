# Typograph Service

An example of a typograph with a web-interface, that corrects your text by following certain rules:

* substitute quotes '' and "" by « »
* substitute a hyphen - by a dash – when it is necessary
* substitute a hyphen by a short dash in telephone numbers
* link short words to the following words by a non-breaking space
* link numbers to the following words or words to the following numbers by a non-breaking space
* delete extra spaces or newlines

The code is based on Flask(http://flask.pocoo.org/docs/0.11/quickstart/), which can be installed by 
```#! bash
$ pip install -r requirements.txt
```

# Usage

Run in the console
```#! bash
$ python server.py
```
The application is then available at the address http://localhost:5000/ and ready to be used.



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
