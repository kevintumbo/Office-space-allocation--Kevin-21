class Person(object):

    """ class Room """

    def __init__(self, person_name):
        self.person_name = person_name


class Fellow(Person):

    """ class Fellow inheriting from parent class Room """

    def __init__(self, person_name):
        super().__init__(person_name)
        self.role = "Fellow"


class Staff(Person):

    """ class Staff inheriting from parent class Room """

    def __init__(self, person_name):
        super().__init__(person_name)
        self.role = "Staff"



