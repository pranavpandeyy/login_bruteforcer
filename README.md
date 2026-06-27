# Login Brute Forcer

A Python-based dictionary attack tool that automates 
credential testing on web login forms.

## What it does
Takes a wordlist and systematically tries each password 
against a target login page — simulating how attackers 
test for weak credentials in real penetration tests.

## Features
- Multithreaded — tries multiple passwords simultaneously
- Smart session handling — maintains cookies across requests
- CSRF token extraction — works on token-protected forms
- Configurable wordlist — supports rockyou.txt and custom lists
- Clean output with timestamps and attempt counter

## Built With
- Python 3
- requests — HTTP session management
- threading — concurrent password attempts
- BeautifulSoup — CSRF token parsing

## Tested On
- DVWA (Damn Vulnerable Web Application)

## Usage
python3 bruteforcer.py

## Disclaimer
For educational and authorized testing only.
Never use against systems without explicit permission.
