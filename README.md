# The shortest (usable) Jina program

- Uses [Jina 2.0](https://github.com/jina-ai/jina/)
- Uses minimal lines of code to actually achieve something USEFUL (i.e. index data then let user query it)

## What is code?

- I'm classing "code" as anything the developer writes or imports from other files in the directory. So if `app.py` is 5 lines and I'm importing everything from `executors.py` (100 lines), that means 105 lines of code
- That goes for YAML too. Sure it's not strictly "code", but it's doing the job of code
- Screw it, I'm including comments. Good code is self-documenting code ;)

## What isn't code?

- Documentation
- Input data

## Caveats

- At the time of writing [Jina Hub](https://hub.jina.ai) hasn't yet been released for Jina 2.0. So anything with `jinahub://foobarbaz` won't work just yet.

## Sacrifices

Condensing code to the smallest working example means sacrifices:

- No defining variables - everything is hard-coded
- Just import the whole damn module, no importing subclasses. This means longer (but fewer) lines of code
- No comments
- No unnecessary line breaks

## Going further

- Can replace many (but not all) line breaks with semi-colons
- Can turn the whole program into an escaped single string, then run that with `exec()` function

Why don't I do these? The existing sacrifices were bad enough. The above two just feel dirty and unpythonic.

## Yes, but...

- "You're relying on other people's code!" - Duh. Jina Hub Executors are other people's code. Jina is other people's code. So is Python. Short of starting from scratch [with my own damn logic gates](https://www.nand2tetris.org/) I have to use other people's code, as does everyone.

## Warning

- Don't run [Black](https://github.com/psf/black/blob/master/plugin/black.vim) on this code. It will add line breaks, etc.
