def delete(dict, key):
    for keys in key:
        dict.pop(keys)
    return dict

dict = {'firstName':"Clare", 'lastName':"Cruz", "birthYear":"2000","nationality":'nativeamerican'}
print(delete(dict, ["lastName","birthYear"]))
