import time
from pathlib import Path

inbox = Path("Inbox")
needs_action = Path("Needs_Action")

print("Watcher start ho gaya...")

while True:
    for file in inbox.glob("*"):
        new_file = needs_action / file.name
        
        if not new_file.exists():
            new_file.write_text(file.read_text())
            print(f"{file.name} Needs_Action me move ho gaya")
    
    time.sleep(5)