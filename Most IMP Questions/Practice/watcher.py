import re
import os
import time
import random
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# for a safer side git pull before any other operation
os.popen("git pull")

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"
print(f"{GREEN}Hey Chandrashekhar All the best Do bunch of problems today 👍🏻💖{RESET}")


class Watcher:
    # set the Path of the directory to monitor
    DIRECTORY_TO_WATCH = "C:\GFG_DataScience\LeetCode\Most IMP Questions\Practice"


    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    counter = 0

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            

        elif event.event_type == 'modified':
            GREEN = "\033[1;32m"
            RED = "\033[1;31m"
            RESET = "\033[0m"
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)
            # to extract specific file name from the event path
            if '~' in event.src_path:
                value = event.src_path.split("~")[-1]
            else:
                value = event.src_path.split("\\")[-1]
            # to check which value gets printed
            print(value)
            # if the file is not Untitled then only perform operations
            if value != 'Untitled.ipynb':
                # get all the possible values such that it can related to changes
                s = ["changes", "update", "modification","Made modifications", "Updated code", "Implemented alterations", "Tweaked the code", "Adjusted the program", "Modified the source code", "Refactored the code", "Edited", "Made adjustments"]
                # pre_msg for commit messagfe
                pre_msg = ["Added Some Code to","Modified","Changes in ", "Added new functionality to", "Introduced code changes to","Integrated new code into","Updated code in","Made changes to","Tweaked code in","Edited code in","Adjusted code in","Refactored code in","Revised code in","Reworked code in","Altered code in","Improved code in"]
                # emojis
                emojis = ['👀','💖','🥳','🙌','🚩','😎','🥰','🫣','👻','💪','✌','✍','👑','🚀','❤️‍','🔥']
                # it returns the output of what all changes we have done to the file
                diff_output = subprocess.check_output(['git', 'diff', f'{value}']).decode()
                # this is the pattern to find def function present in it or not
                pattern = r"def\s+(\w+)\("
                print("Inside the While loop 🌀")
#                 print("Diff Output", diff_output)
                # Use re.search() to find the first match of the pattern in the input string
                match = re.findall(pattern, diff_output)
                if match: print("Match Found 👍🏻")
                else: print("Match Not Found 👎🏻")
                # set initial value to None
                commit_message = None
                # if a match is founf then change the commit_message with the function name
                if match:
                    commit_message = f"{random.choice(pre_msg)} `{match[0]}` function {random.choice(emojis)}"
                    Handler.counter = 0
                    n = 0
                # else select random from s and change the value of commit_message
                else:
#                     commit_message = random.choice(s)
                      # check if the counter has reached 20
                        n = 20
                        if Handler.counter == n:
                           # reset the counter
                           Handler.counter = 0
                           # choose a random commit message from s
                           commit_message = random.choice(s) + random.choice(emojis)
                        else:
                            # increment the counter
                            Handler.counter += 1
                # print the commit message to see in terminal
                k = f"{RED}You haven't made changes in the functions so your commit will be added after {n - Handler.counter} changes in your file:({RESET}" if (20 - Handler.counter) > 0 else f"{GREEN}Your commit will be added now:){RESET}"

                print(f"Counter: {Handler.counter}")
                if commit_message != None:
                    print(f"commit message is {GREEN}'{commit_message}'{RESET}")
                    # now git add the file
                    os.popen(f'git add "{value}"')
                    # time.sleep so that there will be no load at once at cmd
                    time.sleep(1)
                    os.popen(f'git commit -m "{commit_message}"') 
                    # finally git push 🥳
                    time.sleep(1)
                    os.popen("git push")
                    # os.popen("^C")
                    time.sleep(1)
                    # this timer such that it will again see in after 10 seconds
                    print(f"{GREEN}Git Pushed Successfully{RESET} 🥳")
                else:
                    print(k)
            
                time.sleep(10)
            # if not untitled then send message
            else:
                print(f"{value} is common so it wouldn't be added Rename it to add")
#             print("test")

            

if __name__ == '__main__':
    w = Watcher()
    w.run()