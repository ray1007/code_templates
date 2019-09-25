## Basic templates for Python


### builtin.py
Frequently used built-in modules.

- `logging`
  - [tutorial (real python blog)](https://realpython.com/python-logging/)
  - [further readings (real python blog)](https://realpython.com/python-logging-source-code/)

### common_dsalg.py
Containing some common data structure & algorithm implemented with built-in functionality/code/lib. Frequently used in leetcode practice.

- use iterator to save memory.
- `itertools`: permuation, combination, product. [realpython blog](https://realpython.com/python-itertools/)

- formatting string with `f-string`.
- `operators`: call basic operators as functions.
- common data structures
  - `list`
  - `collections.deque`: queue, deque, stack
  - `heapq`: default is min heap
  - `set`: hash set
  - `dict`: hash map
  - `union find`, [code example](https://leetcode.com/articles/redundant-connection/), [time complexity note](http://www.cs.jhu.edu/~mdinitz/classes/IntroAlgorithms/Fall2018/Lectures/lecture9.pdf)

---

### arg_parser.py
- For parsing command line arguments, use [arg_parser.py](./arg_parser.py)
- references: 
  - [`argparse` python doc](https://docs.python.org/3.6/library/argparse.html)
  - [StackOverflow #1](https://stackoverflow.com/questions/46719811/best-practices-for-writing-argparse-parsers) [StackOverflow #2](https://stackoverflow.com/questions/17073688/how-to-use-argparse-subparsers-correctly)
  - [Use case](https://github.com/tdozat/Parser-v3/blob/master/main.py)
  - [Medium blog post](https://medium.com/@george.shuklin/argparse-how-to-get-command-name-for-subparsers-d836483e9511)

---

### decorators.py
> My notes
> - **high-order function**: a function that returns a function.
> - **decorator**: a function that takes a function input, calls this function in an created inner(wrapper) function and returns the inner function, or directly return the function.
> - When we want a decorator to receive arguments, we define it as a fuction that returns a decorator function.
> - decorators could also be callble objects. This has similarity with React Components where we have **function component** and **class component**. python decorator could be a callable class, so it could store states.
> - how we fix the definition: **decorator**: a ~~function~~callable object that takes a function input, calls this function in an created inner function and returns the inner function, or directly return the function.

- references: 
  - RealPython [blog1](https://realpython.com/primer-on-python-decorators/), [blog2](https://realpython.com/inner-functions-what-are-they-good-for/)
  - Common use cases: [stackoverflow](https://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators
), [some wiki](https://wiki.python.org/moin/PythonDecoratorLibrary
)

---

### plot.py
My templates for drawing plots with `matplotlib`.

---

### anti_patterns.py
things we should avoid.

---

## Templates for Applications

### db_manager.py
