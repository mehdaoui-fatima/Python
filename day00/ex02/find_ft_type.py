def all_thing_is_obj(object: any):
    object_type = type(object)
    if (object_type == type(tuple())):
        print(f'Tuple : {object_type}')

    elif (object_type == type(list())):
        print(f'List : {object_type}')

    elif (object_type == type(set())):
        print(f'Set : {object_type}')

    elif (object_type == type(dict())):
        print(f'Set : {object_type}')

    elif (object_type == type('')):
        print(f'{object} is in the kitchen : {object_type}')
    else:
        print(f'Type not found')
    return 42
