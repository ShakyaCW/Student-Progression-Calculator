# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1867607
# Date: 4/17/2022

full_marks = 120
marks_range = [0,20,40,60,80,100,120]

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
star = ("*")

progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

def user_identification():    #This function is to identify whether the user is a student or a staff member
    user_input = input('''
if you are a student            : Enter 1
if you are a staff member       : Enter 2

Enter your choice here \t: ''')
     
    while user_input != "1" and user_input != "2" :
        print ("Invalid choice ")
        user_input = input('''
if you are a student            : Enter 1
if you are a staff member       : Enter 2

Enter your choice here \t: ''')
    return user_input
    
def student_version() :    #This is the basic student version
    while True :
        try :
            global pass_credits
            pass_credits = int(input("\nPlease enter your credits at Pass : "))
            if pass_credits not in marks_range :    #Validate the entered mark to see if it belongs to the relevent marks range
                print ("Out of range")
                continue
            global defer_credits    
            defer_credits = int(input("Please enter your credits at Defer : "))
            if defer_credits not in marks_range :
                print ("Out of range")
                continue
            global fail_credits    
            fail_credits = int(input("Please enter your credis at Fail : "))
            if fail_credits not in marks_range :
                print ("Out of range")
                continue
            total = pass_credits + defer_credits + fail_credits
          
            if total != full_marks :    #Validate the total marks to see if it is equal to 120 or not
                print ("Total incorrect")
                continue
        
        except ValueError :    #Validate the entered mark to see if it is an Integer or not
            print ("Integer required")
            continue
        
        if pass_credits >= 100 :
            if pass_credits == 120 :
                progress_list.append(f"Progress - {pass_credits},{defer_credits},{fail_credits}")    #append the entered marks to the progress_list
                print ("Progress")       #display the progression outcome as defined by the University regulations
                global progress_count
                progress_count += 1
            else :
                trailer_list.append(f"Progress (module trailer) - {pass_credits},{defer_credits},{fail_credits}")
                print ("Progress(modele trailer)")
                global trailer_count
                trailer_count += 1
        elif 40 <= pass_credits <= 80 :
            if fail_credits == 80 :
                exclude_list.append(f"Exclude - {pass_credits},{defer_credits},{fail_credits}")
                print ("Exclude")
                global exclude_count
                exclude_count += 1
            else :
                retriever_list.append(f"Module retriever - {pass_credits},{defer_credits},{fail_credits}")
                print ("Do not Progress - module retriever")
                global retriever_count
                retriever_count += 1
        else :
            if fail_credits == 80 or fail_credits == 100 or fail_credits == 120 :
                exclude_list.append(f"Exclude - {pass_credits},{defer_credits},{fail_credits}")
                print ("Exclude")
                exclude_count += 1
            else :
                retriever_list.append(f"Module retriever - {pass_credits},{defer_credits},{fail_credits}")
                print ("Do not Progress - module retriever")
                retriever_count += 1
        break
    

def horizontal_histogram():    #Horizontal histogram
    print ("----------------------------------------------------\n--------------- Horizontal Histogram ---------------\n")
    print (f"Progress {progress_count} \t: {star*progress_count}")
    print (f"Trailer {trailer_count} \t: {star*trailer_count}")
    print (f"Retriever {retriever_count} \t: {star*retriever_count}")
    print (f"Exclude {exclude_count} \t: {star*exclude_count}")
    print ("")
    print (f"{progress_count+trailer_count+retriever_count+exclude_count} Outcomes in total.")

def vertical_histogram():    #Vertical histogram
    print ("----------------------------------------------------\n---------------- Vertical Histogram ----------------\n") 
    print (f"Progress {progress_count} | Trailer {trailer_count} | Retriever {retriever_count} | Exclude {exclude_count}")
    print("")
    outcome_list = [[],[],[],[]]    #made the main list and 4 lists in it to store the number of stars(*) equal to the number of students in each progression status
    for i in range (progress_count) :    #first list is for progress count
        outcome_list[0].append ("*")
    for i in range (trailer_count) :     #second list is for trailer count
        outcome_list[1].append ("*")
    for i in range (retriever_count) :   #third list is for retriever count
        outcome_list[2].append ("*")
    for i in range (exclude_count) :     #forth list is for exclude count
        outcome_list[3].append ("*")
    
    #Reference - Stackoverflow
    #got the basic idea from a Stackoverflow thred for the following function
    def longest (outcome_list):        #this fuction is to identify the longest list from 4 lists in main list
        longest_list = max (len(sub_list) for sub_list in outcome_list)  
        return longest_list            #fuction returns the lenth of the longest list
    for x in range (longest(outcome_list)) :
        for i in outcome_list :
            try :
                print ("   ",i[x],"    ", end = "   ")    #print the elements of 4 lists in outcome list vertically
            except :
                print ("            ", end = " ")         #if elements of a list are less than longest(outcome_list)
        print ()
    print (f"{progress_count+trailer_count+retriever_count+exclude_count} Outcomes in total.") 

def progression():        #print the elements of lists
    print ("")
    for m in progress_list:
        print(m)  
    for n in trailer_list:
        print(n)
    for o in retriever_list:
        print(o)
    for p in exclude_list:
        print(p)        
    
#final program
identification = user_identification()                           
if identification == "1" :              #this program will run if the user is a student
    student_version()
    horizontal_histogram()
    vertical_histogram()
    progression()
if identification == "2" :             #this program will run if the user is a staff member
    staff_input = "y"
    while staff_input.lower() == "y":
        student_version()
        staff_input = input ("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        while staff_input.lower() != "y" and staff_input.lower() != "q" :
            print ("\nInvalid Option Entered")
            staff_input = input ("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        continue           
    if staff_input.lower() == "q" :
        horizontal_histogram()
        vertical_histogram()
        progression()
