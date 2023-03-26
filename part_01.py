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
            pass_credits = int(input("\nPlease enter your credits at Pass : "))
            if pass_credits not in marks_range :    #Validate the entered mark to see if it belongs to the relevent marks range
                print ("Out of range")
                continue
            defer_credits = int(input("Please enter your credits at Defer : "))
            if defer_credits not in marks_range :
                print ("Out of range")
                continue
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
                print ("Progress")    #display the progression outcome as defined by the University regulations
                global progress_count
                progress_count += 1
            else :
                print ("Progress(modele trailer)")
                global trailer_count
                trailer_count += 1
        elif 40 <= pass_credits <= 80 :
            if fail_credits == 80 :
                print ("Exclude")
                global exclude_count
                exclude_count += 1
            else :
                print ("Do not Progress - module retriever")
                global retriever_count
                retriever_count += 1
        else :
            if fail_credits == 80 or fail_credits == 100 or fail_credits == 120 :
                print ("Exclude")
                exclude_count += 1
            else :
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

identification = user_identification()    #final program                      
if identification == "1" :                #this program will run if the user is a student
    student_version()
    horizontal_histogram()
if identification == "2" :                #this program will run if the user is a staff member 
    staff_input = "y"
    while staff_input.lower() == "y":
        student_version()
        staff_input = input ("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        while staff_input.lower() != "y" and staff_input.lower() != "q" :
            print ("\nInvalid Option Entered")
            staff_input = input ("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
              
    if staff_input.lower() == "q" :       
        horizontal_histogram()


    


            
