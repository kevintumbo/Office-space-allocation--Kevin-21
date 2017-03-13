"""
Dojo space allocator

Usage:
    dojo_space create_room <room_type> <room_name>...
    dojo_space add_person <first_name> <last_name> <role> [<wants_accommodation>]
    dojo_space (-i | --interactive)

Options:
    -i, --interactive  Interactive Mode

"""

import cmd
import sys
from dojo import Dojo
from docopt import docopt, DocoptExit


def docopt_cmd(func):

    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App(cmd.Cmd):

    intro = 'A Room Allocation system for Andela Kenya facility Known As the dojo'
    prompt = '(dojo_space)'
    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):

        """
        Usage: create_room <room_type> <room_name>...
        """
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]

        if room_type == "office" or room_type == "living":
            self.dojo.create_room(room_type, room_name)
        else:
            print("You've entered an invalid room type. Please choose either office or living")

    @docopt_cmd
    def do_add_person(self, arg):

        """
        Usage: add_person <first_name> <last_name> <role> [<wants_accommodation>]
        """

        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        role = arg["<role>"]
        accommodation = arg["<wants_accommodation>"]

        self.dojo.add_person(first_name, last_name, role, accommodation)

    def do_quit(self, arg):

        """ Quits out of program"""

        print('See you next time!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    App().cmdloop()

print(opt)

