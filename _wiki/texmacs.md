---
layout: wiki
title: texmacs
---

# TeXmacs

中文参考文献有问题

---

* math
\varepsilon \epsilon
\sigma
\varphi \phi
\tau


mind map from Yin Wang
## basic usage

### typing text
1. usually, just type
2. type math formulas
   * Type `$` same key as in TeX
   * Now you can just type TeX commands
     - \sum
     - Except that you press `enter` key after each command, it will fill in a TeX quality formula immediately.
     - Now you can add more things in-place
       1. press `_i=0`
       2. press right arrow key to get out of subscript, then press `^n`
       3. I guess you get it, now finish it
       4. As easy as TeX, oh no, a lot easier!
3. typing more cleverly
   * intuitive ligatures(in math mode)
     - type `->` (type `-` and immediately followed by `>`) press `Tab`
     - type `=>`
     - type `=/`
     - type `=>/`
     - type `>=` press `Tab`
   * cycle through "related similar math symbols"
     - press `Tab` immediately after entering a symbol in math mode
     - repeat pressing `Tab` will show more options
     - eventually cycle back to the first symbol
4. create structures(ways to do this)
    1. keyboard shortcuts
       - fastest way
       - hard to remember
       - so, just remember a few extremely useful ones
    2. menu options
       - slowest way
       - not too hard to find
       - if you go to the menu many times to find the same thing,
         maybe it's better to memorize a hotkey for it?
    3. Toolbox buttons
       - faster than menus
       - good for frequently used functions
    4. `backslash` commands (like TeX)
       - example `\section` `\sum`
       - relatively fast
       - still need to remember them
       - but not as hard as keyboards shortcuts
    5. context menus (new in version 1.7)
       - example
       - only display options relevant to current "mode" and
         cursor position
       - why is it good idea?
         * I see the object...
         * ... show me what I can do about it!
         * I don't care about other objects
5. delete structures
   1. to see: the status bar shows the surrounding context of the
      cursor
   2. to do: you can delete the innermost tag
      - keyboard shortcut
        * Windows/Linux `Ctrl-backspace`
        * Mac `Option-backspace`
      - context menu
      - the effect is immediate
6. switch structures (ways to do this)
   1. keyboard
      - keys
        * Windows/Linux `Ctrl-Tab`
        * Mac `Option-Tab`
      - examples
        * switch math from/to display: vary useful because you
          can immediately compare which style is better
        * cycle through other structures
          - different styles of enumerations
          - different font style
            * em
            * underline
            * strong
          - different levels of document structures
            * chapter
            * section
            * subsection
            * paragraph
   2. context menu
7. navigate through structures
   1. keys
      - Windows/Linux `Ctrl-PgUp` `Ctrl-PgDn`
      - Mac `Option-PgUp` `Option-PgDn`
   2. context menu

### creating tables/matrices
   1. start a table
      - How often do I type a table to warrant remembering a hotkey
      - I usually just use a toolbox item
      - Or, if you are TeXnician, type `\tabular` and hit return
      - result: an empty table
   2. create cells
      - just type in the first cell
      - Add column/row
        * Windows/Linux Alt+some arrow key
        * Mac ctrl+some arrow key
        * result
      - need border?
        * press our old friend "structure cycle" key
        * until you see
   3. create a matrix
      - get in math mode with `$`, type `\matrix` and return
      - The rest is the same as a table
   4. create something like this? (equation set)
      - Hint { \tabular
      - how about this? (vector)
### image
1. insert -> big/small figure ;then insert image
image size and positon are controled by px

### reference
1. use bibtex, {\cite|chen2014}

    @article{chen2014,
      title={AN IMPROVED ANALYTICAL METHOD FOR RESTRAINED RC STRUCTURES SUBJECTED TO STATIC AND DYNAMIC LOADS},
      author={CHEN, LI and FANG, QIN and GUO, ZHIKUN and LIU, JINCHUN},
      journal={International Journal of Structural Stability and Dynamics},
      volume={14},
      number={01},
      year={2014},
      publisher={World Scientific Publishing Company}
    }



## Use style files
### create and use macros
   - definition: in any document, use `\assign` to enter an 
     assignment, and assign a `\macro` definition to a name
     * this equal to Scheme code:
          
          (define hi
           (lambda ()
            "Hello World"))

       - \assign == define
       - \macro == lambda
     * in idiotic slow motion
       - type `\assign`
       - press return
       - enter hi as macro name
       - Use right arrow key to go the field on the right
       - type \macro
       - press return
       - Enter Hello World
       - Press return until the <assign ...> disappear
   - invocation
     * type `\hi`.
     * you should see "Hello world" appear on screen
     * this is equivalent to a function call in Scheme `(hi)`
   - Macro with arguments
     * just type a argument name after you see <macro|..>.
       press `Tab` key and it will open another slot where 
       you can enter the body of the macro
     * to reference the argument in macro body, use backslash
       commands like `\name`
       - this is equivalent to Scheme code ...
       - there is a keyboard shortcut for this, but I think there
         are too many keys to remember. I would just type it.
     * to invoke the macro, use backslash commands `\hello`
       - the cursor will be put at the argument position after
         hitting return, waiting for the argument name.
### create a style file
   1. create a new file
   2. enter the macro definitions as in the earlier instructions
   3. save the file to `$HOME/.TeXmacs/styles` with extension `.ts`,
      for example `mystyle.ts`
   4. if you want to see the macro definitions (instead of letting
      them disappear after you hit enter, choose:
      `Document->Style->source`)
### use a style file
   1. Once you save your style file, "mystyle" should immediately
      appear in the menu `Document->Style`
   2. To use it, just open a new file, and choose "mystyle" 
      as the style.
### What is cool about this?
   1. The definition and use are fully visual!
      - I can define my macro in a fully visual way ...
        * Notice that the macro body is in TeX-quality as you
          define it
      - And use it in a fully visual way ...
        * After enter `\seq` and press enter 
        * I get
          - notice that the cursor is at "argument position",
            waiting for an argument
        * As I type the argument "a", I instantly get ...
          - Notice that "a" appears in both position simultaneously
          - ... and in TeX quality !!
        * I I want to change the argument, I just delete "a"
          and type something else ...
          - the result instantly change
      - Another example
   2. Instant change
      - When style files are changed, the files which uses this
        style *instantly* change in another window
### What is not so cool (yet)?
   The way macros are defined is not very convenient yet,
   needs some improvement


