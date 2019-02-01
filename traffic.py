#Ariel Robinson
#traffic.py
#Problem:
#To calculate the average amount of cars that traveled each road
#Certification of Authenticity:
# I certify that this lab is my own work, but I 
#discussed it with Professor Stavley & Marge in CSL

def traffic():
    print("Examine the traffic patterns")
#the user enters the total amount of roads
    totalRoads=eval(input("How many roads were surveyed? "))
    total=0    
    for i in range(1,totalRoads+1):
#the user enters the total amounds of days each road was surveyed
        totalDays=eval(input("How many days was road" +" "+str(i)
        +" "+"surveyed? "))
        currentRoadTotal=0
        for j in range (1,totalDays+1):
#the user enters the amount of cars that were on the road    
            carsTraveled=eval(input("How many cars traveled on day"+" "
            + str(j)+"?"+ " "))
            total=carsTraveled+total
            currentRoadTotal=carsTraveled+currentRoadTotal
#calculates the average of cars per day             
            carAverage=currentRoadTotal/totalDays
        print("Road", str(i),"had an average of" ,
        carAverage ,"vehicles per day.")
#calculates the average of all the roads
    totalCarsAverage=total/totalRoads
#prints results of total cars on all roads and average vehicles per road
    print("Total number of vehicles traveled on all roads:",total)
    print("Average number of vehicles per road:",
    round(totalCarsAverage,2))
        

traffic()                   
                     
                    

                              
            

    
            

        

                               
        
            
