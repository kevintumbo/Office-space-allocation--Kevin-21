"""
Dojo space allocator

Usage:
    dojo_space create_room <room_type> <room_name>...
    dojo_space add_person <first_name> <last_name> <role> [<wants_accommodation>]
    dojo_space print_room <room_name>
    dojo_space print_allocation [<filename>]
    dojo_space print_unallocated [<filename>]
    dojo_space reallocate_person <first_name> <last_name> <new_room_name>
    dojo_space load_people <filename>
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

        print(self.dojo.add_person(first_name, last_name, role, accommodation))

    @docopt_cmd
    def do_print_room(self, arg):

        """
        Usage: print_room <room_name>
        """
        self.dojo.print_room(arg["<room_name>"])

    @docopt_cmd
    def do_print_allocation(self, arg):

        """
        Usage: print_allocation [<filename>]
        """
        self.dojo.print_allocations(arg["<filename>"])

    @docopt_cmd
    def do_print_unallocated(self, arg):

        """
        Usage: print_unallocated [<filename>]
        """
        self.dojo.print_unallocated(arg["<filename>"])

    @docopt_cmd
    def do_reallocate_person(self, arg):

        """
        Usage: reallocate_person <first_name> <last_name> <new_room_name>
        """

        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        new_room_name = arg["<new_room_name>"]

        print(self.dojo.reallocate_person(first_name, last_name, new_room_name))

    @docopt_cmd
    def do_load_people(self, arg):

        """
        Usage: load_people <filename>
        """

        filename = arg["<filename>"]
        print(self.dojo.load_people(filename))

    def do_quit(self, arg):

        """ Quits out of program"""

        print('See you next time!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    App().cmdloop()

print(opt)

