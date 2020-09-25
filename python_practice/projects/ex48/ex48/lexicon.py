# scan() function takes one arg and returns a list of tuple in format:
# [('type_arg', 'arg')]
def scan(input_str):

    dict = {'direction': ['east', 'west', 'north', 'south'],
            'verb': ['go', 'eat', 'kill', 'run'],
            'stop': ['the', 'in', 'of'],
            'noun': ['bear', 'princess', 'honey'],
            'number': [i for i in range(99999)],
            'error': ['ASDFASDFASDF', 'IAS'],
            }

    str_list = [i for i in input_str.split()]
    tuples_list = []

    for i in str_list:
        for j in dict.values():
            for val in j:
                try:
                    if val == i or val == i.lower() or val == i.upper():
                        for key in dict.keys():
                            if dict[key] == j:
                                tuples_list.append((key, i))
                            else:
                                pass
                    elif val == int(i):
                        for key in dict.keys():
                            if dict[key] == j:
                                tuples_list.append((key, i))
                            else:
                                pass
                    else:
                        pass
                except ValueError:
                    pass

    return tuples_list
