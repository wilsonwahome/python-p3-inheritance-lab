#!/usr/bin/env python

from user import User

import random

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"]  

    def teach(self):

        import random
        return random.choice(self.knowledge)