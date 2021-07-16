# The shortest (usable) Jina program

- Uses [Jina 2.0](https://github.com/jina-ai/jina/)
- Uses minimal lines of code to actually achieve something USEFUL (i.e. index data then let user query it)

## WARNING

**[`shortest.py`](./shortest.py) is potentially unsafe**. This is because in order to cram everything into one line we have to use some dodgy hackery, namely [the rather dangerous `exec()` function](https://blog.finxter.com/python-exec/). This could mean a user gives it malicious input like:

```
import os; os.system('rm -rf ~')
```

[`sensible.py`](./sensible.py) is a much more sensibly-written (albeit longer) version that is both safe and easy to understand

## What is code?

- I'm classing "code" as anything the developer writes or imports from other files in the directory. So if `app.py` is 5 lines and I'm importing everything from `executors.py` (100 lines), that means 105 lines of code
- That goes for YAML too. Sure it's not strictly "code", but it's doing the job of code
- Screw it, I'm including comments. Good code is self-documenting code ;)

## What isn't code?

- Documentation
- Input data
- Dependencies (because if you boil it right down you're ALWAYS using dependencies unless you're coding in assembly ffs)

## Sacrifices

Condensing code to the smallest working example means sacrifices:

- No defining variables - everything is hard-coded
- No comments
- No unnecessary line breaks

## Going further

- Can replace many (but not all) line breaks with semi-colons

## Yes, but...

- "You're relying on other people's code!" - Duh. Jina Hub Executors are other people's code. Jina is other people's code. So is Python. Short of starting from scratch [with my own damn logic gates](https://www.nand2tetris.org/) I have to use other people's code, as does everyone.
