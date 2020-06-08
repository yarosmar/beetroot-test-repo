# Task 1

def logger(func):
    def wrapper(*args):
        listed_args = list(map(str, args))      
        print("Called function {} with {}".format(func.__name__, ", ".join(listed_args)))
        result = func(*args)
        print("Result", result)
    return wrapper  

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Task 2

def stop_words(words):    
    def replace_asterisks(func):
        def wrapper(*args):
            slogan = func(*args)
            for word in words:
                slogan = slogan.replace(word, '*')
            return slogan
                
        return wrapper
    return replace_asterisks

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW"

print(create_slogan('Steve'))

# Task 3

def arg_rules(type_, max_length, contains):
    def check_rules(func):
        def wrapper(name):
            is_of_type = True
            if type(name) != type_:
                print("Argument should be string")
                is_of_type = False
                
            length_is_ok = True
            if len(name) > max_length:
                print("Max length is 15")
                length_is_ok = False

            has_symbols = True
            for symb in contains:
                if symb not in name:
                    print("{} not in name {}".format(symb, name))
                    has_symbols = False
                    
            if has_symbols and is_of_type and length_is_ok:
                return func(name)
            return False
        return wrapper
    return check_rules

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))

print(create_slogan('S@SH05'))






















