#How can we declare strings in different ways
# you can create a string using single quotes
name='ram'
print(name)
# we can create a string using double quotes
name="ramesh"
print(name)
# we can create a string using triple single quotes
name='''rahul'''
print(name)
# we can create a string using triple double quotes.
name="""sai"""
print(name)
# triplequotes are used to create multiline string
para="""hi
   hello
bye"""
print(para)
# we can also specify each character in a seperate single or double quotes
name='r''a''h''u'"l"
print(name)
'''When a string contains quotes, 
using a different type of quote 
to enclose the string can make it 
easier to include quotes inside
the string without needing escape characters:'''
test1="hello ' hi"
print(test1)
test2='hello " " hi'
print(test2)
# when u insert the \ -- the character that just follows the \ is taken as a part of the string without any special meaning
test3="hello\" \"hi"
print(test3)
# In addition to using triple quotes for multi-line strings, you can use the backslash (\) to continue a string onto the next line without including a newline character
test4="this is a long string "\
      " that split across multiple lines"\
" for better readability."
print(test4)
