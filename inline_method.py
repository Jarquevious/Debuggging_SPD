# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.


class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(Person):
    LEGAL_DRINKING_AGE = 18
    guest_age = Person.age
    if guest_age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")




 
James = Person(17.9)
Mark = Person(24)
Sue = Person(35)
Kesha = Person(17)

enter_night_club(James)
enter_night_club(Kesha)
enter_night_club(Sue)
enter_night_club(Mark)
        
