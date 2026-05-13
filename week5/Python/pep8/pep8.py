import ruff 

def calculatePrice(Items,tax=0.17):
    Total = 0 
    for I in Items: 
        Total = Total + I*(1+tax) 
        return(Total) 
    
