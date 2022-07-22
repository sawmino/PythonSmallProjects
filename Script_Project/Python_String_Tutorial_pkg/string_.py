def print_data():
    name = "saw"
    age = 25
    print("Test String")
    string_data = "Hello, I am %s and  I am %i years old." % (name, age)
    print(string_data)
    print("-------------------------------------")
    print("using f string literal")
    string_data_1= f"Hello, {name}"
    string_data_2= f"1+1 is {1+1}"
    print('f"Hello, {name}" is '+ string_data_1)
    print('f"1+1 is {1+1}" is ' + string_data_2)
    print("-------------------------------------")
    print("using stack")
    stack=[]
    stack.append(1)
    stack.append(2)
    print("using pop on current list                                                                       ")
    pop_elem=stack.pop()
    print(stack,pop_elem)
