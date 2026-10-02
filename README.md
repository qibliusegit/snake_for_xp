# Snake for Windows XP #

tl;dr snake made in pygame but works with xp

<img width="1107" height="853" alt="image" src="https://github.com/user-attachments/assets/46cd37e0-92a3-4317-8e3a-e7b9465a64a2" />


So I found out recently that Windows XP supports up to Python 3.4 (why, I don't know, but I'm not complaning). And after doing a little digging, I also discovered that pygame is compatible with Windows XP. So what better to do than to make a game for Windows XP?

The game itself is just a standard game of snake, where you eat fruits and try not to hit the edges of the screen.

---
## Setup ##
All of the packages you need are in this repo (outside of Windows XP itself, go source an .iso yourself :p).

Things you need to install:
1. Python 3.4 (.exe file)
2. Pygame (.whl file)
*(the rest of these are optional, for if you want to make your own executables)*
3. pywin32 (.exe file)
4. pywin32_ctypes (.whl file)
5. altgraph (.whl file)
6. future (.whl file)
7. macholib (.whl file)
8. pefile (.zip file)
9. PyInstaller (.tar.gz file)

Once you've installed all of these, either by running them or using `python -m pip install filename.filetype`, you're all set! Just run the snake file in snake_executable/dist/snake/snake.exe and enjoy!

--- 
## Future Plans ##
My only real current future plan is to get collision within the snake working, so hitting your body also ends the game.
