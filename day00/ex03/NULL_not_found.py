
def NULL_not_found(object: any):
    

    if isinstance(object, type(None)) and object == None:
        print(f'Nothing: {object} {type(object)}')

    elif isinstance(object, float) and object != object:
        print(f'Cheese: {object} {type(object)}')

    elif type(object) is bool and object == False:
        print(f'Fake: {object} {type(object)}')

    elif isinstance(object, int) and object == 0:
        print(f'Zero: {object} {type(int())}')
        
    elif isinstance(object, str) and object == '': 
        print(f'Empty: {object} {type(object)}')
  
    else: 
        print(f'Type not Found')
        return 1

    return 0   
    