class School():

    def __init__(self, name=None):
        self.name = name
        self.roster = {}
        
    def roster(self):
        return self.roster
    
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
        return self.roster
    
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
  # Go thru each value from the dictionary (a list) and sort that list
        for v in self.roster.values():
  # Note that this will sort inplace (in memory) so we don't have to do a reassign
            v.sort()
  # And just following the structure to return the sorted roster
  # Note that the School object's roster is now sorted (not just a copy)
        return self.roster
