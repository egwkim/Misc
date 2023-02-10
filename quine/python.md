[
py:="""
"Python code here!"
"But without triple double-quotes and some md syntaxes..."
""
"Instead of using #, you need to create a string literal"
"for comments."
""
"This python code is a quine,"
"but you can modify it to whatever you want!"
""
"Print an opening square bracket"
print(chr(91))
""
"Print python code"
print(f'py:={chr(34)*3}{py}{chr(34)*3},')
""
"Print markdown code and other things"
print(f'md:={chr(34)*3}{md}{chr(34)*3},*map(exec,py.splitlines()){chr(93)} # -->')
""",
md:="""
]:#
<!-- Markdown Code here -->

# Hello world! 👋

This is a markdown file, but also a python code which prints out itself.

So... this is a python [quine](https://en.wikipedia.org/wiki/Quine_(computing))
and also a [polyglot](https://en.wikipedia.org/wiki/Polyglot_(computing)).


## How does it work?

Python code is inside the [Markdown link label](https://www.markdownguide.org/basic-syntax/#reference-style-links) so that it isn't displayed. In python, it is interpreted as a list. In the list, there are two string literals containing the python code and markdown code respectively. The main python code is stored in a variable called `py`, and executed later.

Markdown code is inside the python string literal, which is stored in a variable called `md`. The markdown link ends at the beginning of the string, and the text following it is displayed as markdown text.

Python code is executed at the end of the file. It is mapped with a exec command, and then unpacked to be executed. It prints out the whole file using two variables `py` and `md`.

Check out the raw code for further detail.

## Make your own python-markdown polyglot!

You can modify this file to your taste. But be careful! When editing python code, you can't use some markdown syntaxes. For example, using `#` for comments will break the markdown link. Also, when modifying both parts of the code, backslash will not work correctly.

## My thoughts...

Using exec might feel like cheating, but it works anyway 😅

Maybe I'll try this later without using exec, and with escape sequences. 

<!-- """,*map(exec,py.splitlines())] # -->
