import sys
from markdown import *

def main(input):
  f = file(input, "r+")
  text = f.read()
  text = header(text)
  text = subheader(text)
  text = block(text)
  text = code(text)
  text = bold(text)
  text = italic(text)
  text = bullet(text)
  text = linebreak(text)
  text = formlist(text)
  text = url(text)
  text = character(text)
  text = html(text)

  print (text)

if __name__ == "__main__":
  main("example.md")