@echo off
cd "C:\GFG_DataScience\LeetCode\Most IMP Questions\Practice"
call "C:\ProgramData\anaconda3\Library\bin\conda.bat" activate "C:\GFG_DataScience\env"
start jupyter notebook
start cmd /k "call "C:\ProgramData\anaconda3\Library\bin\conda.bat" deactivate & cd "C:\GFG_DataScience\LeetCode\Most IMP Questions\Practice" & python "C:\GFG_DataScience\LeetCode\Most IMP Questions\Practice\watcher.py" & pause"