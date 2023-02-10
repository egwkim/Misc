[
py:="""
print(chr(91))
print(f'py:={chr(34)*3}{py}{chr(34)*3},')
print(f'md:={chr(34)*3}{md}{chr(34)*3},*map(exec,py.splitlines()){chr(93)} # -->')
""",
md:="""
]:#
<!-- Markdown Code here -->

# Coding for fun! 🤣🤣

`Coding is fun! Coding is fascinating! Coding is hilarious!`

Collection of some humorous, coding-related random stuffs.

By the way, the title of this repository is from [Humoresque (Dvořák)](https://www.youtube.com/watch?v=2B9kZ2jguwk)

***

## About this file

This page looks like an ordinary markdown file... ***but is it?***

Actually, this file is a valid python code, which prints itself!

## How does it work?

Check out [python.md](/quine/python.md) for details.

<!-- """,*map(exec,py.splitlines())] # -->
