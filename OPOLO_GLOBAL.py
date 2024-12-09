

class Program:
    '''Description: Build a system to manage and calculate student grades. 
    
    Key Features:
    Enroll students in courses.

    Input and update student grades.

    Calculate average grades and generate performance reports.

    '''
    def __init__(self, name, acroym):
        self.program_name = name
        self.program_acroym = acroym
        self.program_cohorts = []
        
    def add_cohort(self, cohort):
        self.program_cohorts.append(cohort)
        
    def display_cohorts(self):
        print(" " * 25 + "COHORT'S")
        print("_" * 56)
        for cohort in self.program_cohorts:
            print(f"Cohort Name: {cohort.cohort_name}")
        print("_" * 56)
        print("")
        
    def __str__(self):
        return f"{self.program_name}"
            

class Cohort:
    def __init__(self, name):
        self.cohort_name = name
        self.cohort_members = []
    
    def add_member(self, member):
       if member.member_cohort is None:
            self.cohort_members.append(member)
            member.member_cohort = self
       else:
           print(f"Error: {member.member_name} is already part of the cohort '{member.member_cohort.cohort_name}'.")
    
    def display_members(self):
        '''
        print(" " * 18 + f"{self.cohort_name} members")
        print("_" * 58)
        for member in self.cohort_members:
            print(member.member_name)
        '''  
        print(" " * 18 + f"{self.cohort_name} members")
        print("_" * 58)
        for member in self.cohort_members:
            member.display_info()
            print("-" * 20)
        
        print("_" * 58)
        

class Member:
    def __init__(self, name, cohort = None, topic = ""):
        self.member_name = name
        self.member_cohort = None
        self.member_topic = topic
        self.member_grade = {} 
        
        if cohort:
            cohort.add_member(self)
            
    def add_grade(self, grade, topic):
        self.member_grade[topic] = grade
        
    def calculate_average(self):
        if not self.member_grade:
            return 0
        return sum(self.member_grade.values()) / len(self.member_grade)

    def display_info(self):
        print(f"Student Name: {self.member_name}")
        print(f"Grades: {self.member_grade}")
        print(f"Average Grade: {self.calculate_average():.2f}")

