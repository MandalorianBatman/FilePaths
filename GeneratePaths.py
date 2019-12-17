import json

def Get_Path(paths):
    def get_children(ippath, e_dict):
        remaining_path = '/'.join(ippath.split('/')[1:])
        try:
            splitted_path = ippath.split('/')[0]
            if splitted_path:
                e_dict[splitted_path] = {}
                e_dict[splitted_path].update(get_children(remaining_path, e_dict[ippath.split('/')[0]]))
                return e_dict
            else:
                return e_dict
        except:
            return remaining_path
    
    def merge_dictionaries(new_dictionary, main_dictionary):
        key = list(new_dictionary.keys())[0]
        if list(new_dictionary[key].keys())[0] in list(main_dictionary[key].keys()):
            merge_dictionaries(new_dictionary[key], main_dictionary[key])
        else:
            main_dictionary[key][list(new_dictionary[key].keys())[0]] = new_dictionary[key][list(new_dictionary[key].keys())[0]]
    
    End_Dictionary = dict()
    for path in paths.split(' '):
        end_dict = dict()
        output = get_children(path, end_dict)
        if output:
            if list(output.keys())[0] not in list(End_Dictionary.keys()):
                End_Dictionary.update(output)
            else:
                merge_dictionaries(output, End_Dictionary)
        else:
            continue
    return End_Dictionary

def main():
    paths = 'alpha/beta/gamma/delta alpha/beta/sigma beta/phi/pi/rho'
    output = Get_Path(paths)
    print(str(json.dumps(output, sort_keys=True, indent=4, separators=('', ''))).replace('{', '').replace('}', '').replace('"', ''))
main()