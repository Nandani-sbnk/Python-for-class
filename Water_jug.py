from collections import defaultdict

jug1 ,jug2 ,jug3 = 4, 3 ,2

visited=defaultdict(lambda:False)



def waterjug(amt1,amt2):

    if(amt1==jug3 and amt2==0) or (amt2==jug3 and amt1==0):
        print(amt1,amt2)
        return True
    

    if visited[(amt1,amt2)] == False:

        print(amt1,amt2)


        visited[(amt1,amt2)]=True


        return (
            waterjug(amt1,0) or 
            waterjug(0,amt2) or 
            waterjug(jug1,amt2) or 
            waterjug(amt1,jug2) or 
            waterjug(amt1+ min(amt2,(jug1-amt1)),
                     amt2 - min(amt2,(jug1-amt1))) or 
            waterjug(amt1 - min(amt1 ,(jug2-amt2)),
                     amt2 + min(amt1 ,(jug2-amt2)))
        )
    
    else:
        return False
    
waterjug(0,0)