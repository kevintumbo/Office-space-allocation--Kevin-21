class Person(object):

    """ class Room """

    def __init__(self, person_name, accomodation, role=None):
        self.person_name = person_name
        self.role = role
        self.accomodation = accomodation


class Fellow(Person):

    """ class Fellow inheriting from parent class Room """

    def __init__(self, person_name, accomodation):
        super().__init__(person_name, accomodation, role="FELLOW")


class Staff(Person):

    """ class Staff inheriting from parent class Room """

    def __init__(self, person_name):
        super().__init__(person_name, role="STAFF", accomodation="N")




