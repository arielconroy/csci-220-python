#Ariel Robinson
#weightedAverage.py
#Problem:
# User enters in name of text file with data.
#The data from the file is used,
# to calculated the weighted average of the grades and class average
#Certification of Authenticity: 
#I certify that this lab is my own work, but I
#discussed it with: Marge in CSL

def weightedAverage():
    infoFile=input("Enter the name of file with grades : ")
    file=open(infoFile,"r")
    totalStudents=0
    numStudentsGrades=0
    for line in file:
        lineInfo=line.split()
        #gives list of names
        names=lineInfo[0:2]
        totalGrades=0
        #adds together the total amount of students
        totalStudents=totalStudents+1
        #gives list of grades
        gradeInfo=lineInfo[2:len(lineInfo)]
        for i in range(0,len(gradeInfo),2):
            #changes grades and grade weights from strings to ints
            grade=eval(gradeInfo[i+1])
            gradeWeight=eval(gradeInfo[i])
            #calculates the grade weight 
            totalGrades=totalGrades+(gradeWeight*grade)
        #calculates each person average number of grades
            averageGrades=totalGrades/100
        numStudentsGrades=numStudentsGrades+averageGrades
        #print(averageGrades)
    #calculates the class average
        classAverage=numStudentsGrades/totalStudents
        print(lineInfo[0]+" "+lineInfo[1]+"'s","Average: ",
        averageGrades)
    #prints the class average 
    print("Class Average: ", round(classAverage,2))
        
    file.close()

weightedAverage()
