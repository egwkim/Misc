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
"Print markdown string and other things at the end"
print(f'md:={chr(34)*3}{md}{chr(34)*3},*map(exec,py.splitlines()){chr(93)} # -->')
""",
md:="""
]:#
<!-- Markdown here -->

# Hello world! 👋

This is a markdown file, but also a python code which prints out itself.

So... this is a python [quine](https://en.wikipedia.org/wiki/Quine_(computing))
and also a [polyglot](https://en.wikipedia.org/wiki/Polyglot_(computing)).


## How does it work?

*I recommend that you try it yourself first!*

The code starts with an opening square brackets `[`.

In markdown, it is recognized as the start of a 
[Markdown link label](https://www.markdownguide.org/basic-syntax/#reference-style-links)
so the text inside isn't displayed.
At some point we have to close it with something like `]:#`.

In python, it is interpreted as the start of a list.
Unlike markdown, we have to close it with a single `]`.

Here's the trick.
We can create a python string literal in a list, and close the markdown link in it.
Then we write some markdown codes, start a markdown comment, and then close the python string literal and list inside it.

```markdown
[
'''
]:#

# Markdown code
 - Another markdown code

<!-- '''] # -->
```

We just created a python - markdown polyglot!

However, the python code does nothing yet. 
To run python codes, I created another string containing the code and used `exec()` to execute it.

```python
[
py:='''
print("Hello, world!")
''',
md:='''
]:#

# Markdown code
 - Another markdown code

<!-- ''',*map(exec, py.splitlines())] # -->
```

I also saved markdown string in a variable to print it later.

From here, we just have to print some special characters, `py` and `md`, and some more characters at the end.

The complete code looks like this:

```python
[
py:='''
print(chr(91))
print(f'py:={chr(39)*3}{py}{chr(39)*3},')
print(f'md:={chr(39)*3}{md}{chr(39)*3},*map(exec, py.splitlines()){chr(93)} # -->')
''',
md:='''
]:#

# Markdown code
 - Another markdown code

<!-- ''',*map(exec, py.splitlines())] # -->
```

## Make your own python-markdown polyglot!

You can modify [this file](./python-template.md) to your taste.
But be careful! When editing python code, you can't use some special characters.
For example, using `#` for comments can break the markdown link. An empty new line also breaks the link.

When modifying both parts of the code, backslash will break quine.


## My thoughts...

Using exec might feel like cheating, but it works anyway 😅

Maybe I'll try this later without using exec, and with allowing escape sequences and triple quotes.

<!-- """,*map(exec,py.splitlines())] # -->
