  
                      #! -------------------   Online Examination System ---------------------------!#
  
  
  
def online_exam():
    
    container=[
               
        {"q":"Q1-->  Python is written in which language ? " , "options":"a)C++  b)C  c)Python d)None ","ans":"b"},
        {"q":"Q2-->  Which is not the python data type ? " , "options":"a)List b)Dictionary  c)Array   d)Tuple ","ans":"c"},
        {"q":"Q3-->  Which is the exponential operator? " , "options":"a)*** b)**  c)^ d)* ","ans":"b"},
        {"q":"Q4-->  Which loop take variable initialization first ? " , "options":"a)for  b)while c)do-while  d)None ","ans":"b"},
        {"q":"Q5-->  Which data structure can't store duplicates value ? " , "options":"a)List  b)Set  c)Dictionary(value)  d)Tuple ","ans":"b"}
        
              ]
    
    total_marks=10
    correct=0
    wrong=0
    skip=0
    
    print()
    print()
    print("----------------------📌✨ Python Online Examination ✨📌 --------------------------\n") 
    print()
    print("👍Read The Instruction First Before Starting the Exam !!")
    print("👍There are total 5 MCQs type questions.") 
    print("👍Choose Your Options:--\n  [a/b/c/d] according to the Questions.")
    print('👍Choose "s" for  Skip Questions.')
    print()
    
    for question in container :
        print()
        print(question["q"])
        print(question["options"])   
        
        while(True):
            choose_opt=input("choose Your Correct option(a/b/c/d/s) : ")
            if(choose_opt=="a" or choose_opt=="b" or choose_opt=="c" or choose_opt=="d" or choose_opt=="s"):
                break
            else:
                print("Invalid Options: Enter a ,b c, d or s to skip.")
        
          
        if (choose_opt==question["ans"]):
            correct+=1
        elif (choose_opt=="s"):
            skip+=1
        else:
            wrong+=1
                    
        
    obtained_marks=2*correct
    percentage=(obtained_marks/total_marks)*100
          

    print()
    print(f"Corrected: {correct} | Wrong: {wrong} | Skipped: {skip}")   
    print(f"Score:{obtained_marks}/{total_marks} | Percentage: {percentage:.2f}%  |",end="")
    if(percentage>40):
        print("Result: Pass")
    elif(percentage==40):
        print("Result:Pass")
        print("(minimum pass marks)")
    
    else:
        print("Result: Fail")
        
        
        
if __name__=="__main__":
    online_exam()
