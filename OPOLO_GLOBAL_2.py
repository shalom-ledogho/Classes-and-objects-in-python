
#from cohort_data import Member

from OPOLO_GLOBAL import Program, Cohort, Member


if __name__ == "__main__":
    # Create a program
    OPOLO_GLOBAL = Program("Tech up skill powered by bank of industries(BOI)", acroym = "BOI")
    
    print(" " * 5,OPOLO_GLOBAL)
    print("_" * 56)
    
    # Create a cohort
    cohort_4 = Cohort("Front-end Dev")
    cohort_3 = Cohort("Python/(DJANGO)")
    cohort_2 = Cohort("Product Design")
    cohort_1 = Cohort("Web Design/Content Development")
    
    # Add cohort to Program
    OPOLO_GLOBAL.add_cohort(cohort_4)
    OPOLO_GLOBAL.add_cohort(cohort_3)
    OPOLO_GLOBAL.add_cohort(cohort_2)
    OPOLO_GLOBAL.add_cohort(cohort_1)
   
    # Create members
    shalom = Member(
        "Shalom Ledogho", 
        topic = "Objects and Classes")
        
    benedicta = Member(
        "Benedicta",
        cohort = cohort_3,
        topic = "cohort_3 functions")#this member will be automatically added upon creation
        
    alex = Member(
        "Alex Tommy", 
        topic = "File handling")
        
    david = Member(
        "David", 
        topic = "HTML block level elements")
        
    chimela = Member(
        "Chimela",
        cohort = cohort_3,
        topic = "Python Date and Time")#this member will be automatically added upon creation 
    
    # Add members to cohorts
    cohort_3.add_member(shalom)
    #cohort_3.add_member(benedicta)
    #cohort_3.add_member(chimela)
    cohort_4.add_member(david)
    cohort_3.add_member(alex)
    
    # Attempt to add a member to another cohort
    cohort_2.add_member(shalom)  # Should display an error message
    
    # Add grade to cohort members
    shalom.add_grade(
        grade = 85, 
        topic = shalom.member_topic
        )
  
    # Display cohorts and members
    OPOLO_GLOBAL.display_cohorts()
    
    cohort_3.display_members()
    
    #print(OPOLO_GLOBAL)
    
    
    
    
    
