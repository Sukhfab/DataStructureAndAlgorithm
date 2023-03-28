class stu_class:
    def __init__(self, names, program, gpa, is_passed):
        self.name = names
        self.program = program
        self.gpa = gpa
        self.is_passed = is_passed

    def if_passed(self):
        if self.is_passed == True:
            return True
        else:
            return False