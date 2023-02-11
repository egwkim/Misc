[py:="""
print(f'{chr(91)}py:={chr(34)*3}{py}{chr(34)*3},md:={chr(34)*3}{md}{chr(34)*3},*map(exec,py.splitlines()){chr(93)}#-->')
""",md:="""]:#

# Markdown code
 - Another markdown code

<!--""",*map(exec,py.splitlines())]#-->
