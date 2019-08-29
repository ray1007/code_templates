import argparse

"""
For each project, fill in this template for specific cmd arguments.
"""

# Put the argument parser in a function and return the args.
# Later on, import and call it in the main function.
def create_main_parser():
    parser = argparse.ArgumentParser()

    # TODO Add arguemnts below.
    # Templates for positional arguments:
    parser.add_argument("posarg1", type=int, help="<description>")
    
    # Note: argmuent dest name will convert `-` to `_`. This gives `pos_arg2`
    parser.add_argument("pos-arg2", type=int, help="<description>")

    # Templates for optional arguments:
    parser.add_argument("--optarg1", type=int, 
                        default=10,
                        help="<description>")

    # if the argument represents a binary value
    parser.add_argument("--optarg2", action="store_true", help="<description>")

    # if the argument has fixed choices.
    parser.add_argument("--verbosity", type=int, choices=[0, 1, 2],                     
                        help="increase output verbosity")

    # if we want to gather arguments into a list. 
    parser.add_argument("--optarg3", nargs="*", help="<description>")

    # when the argument type is file
    parser.add_argument("--input", type=argparse.FileType('r'))
    parser.add_argument("--output", type=argparse.FileType('w'))

    # `type` can take any callable that takes a single string argument and returns the converted value
    parser.add_argument("foo", type=perfect_square)


    # When the program has multiple functionnalities, we might want subparsers.
    # Note main parser's arguments must come before subparsers.
    # Use `dest` to help identify which subcommand was used.
    subparsers = parser.add_subparsers(title="<subparser description>", dest="subcommand")

    # We will create arguments of subparsers in functions for readibility.
    add_functionA_subparser(subparsers)
    add_functionB_subparser(subparsers)
    # TODO add more sub commands below.

    # Parsed arguments will only contain attributes for the main parser and the subparser.
    return parser

# This is a fuction used for `type`.
def perfect_square(string):
    import math
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = "%r is not a perfect square" % string
        raise argparse.ArgumentTypeError(msg)
    return value

def add_functionA_subparser(subparsers):
    a_parser = subparsers.add_parser("func-a", help="subcommand a")
    a_parser.add_argument("yay", type=int, help="<yay>")

def add_functionB_subparser(subparsers):
    b_parser = subparsers.add_parser('func-b', help='b help')
    b_parser.add_argument('--baz', choices='XYZ', help='baz help')

# TODO add more sub command functions below.


# This is the funciton to be imported. 
# Putting this function here so the above functions could be defined in custom order.
def parse_args():
    parser = create_main_parser() 
    return parser.parse_args()
