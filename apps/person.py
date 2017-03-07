class Person(object):
    def __init__(self, person_name):
        self.person_name = person_name


class Fellow(Person):
    def __init__(self, person_name):
        super().__init__(person_name)
        self.role = "Fellow"


class Staff(Person):
    def __init__(self, person_name):
        super().__init__(person_name)
        self.role = "Staff"



