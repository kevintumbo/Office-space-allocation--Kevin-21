class Person(object):

    """ class Room """

    def __init__(self, person_name, role=None):
        self.person_name = person_name
        self.role = role


class Fellow(Person):

    """ class Fellow inheriting from parent class Room """

    def __init__(self, person_name):
        super().__init__(person_name, role="FELLOW")


class Staff(Person):

    """ class Staff inheriting from parent class Room """

    def __init__(self, person_name):
        super().__init__(person_name, role="STAFF")




