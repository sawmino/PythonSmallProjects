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
    print("USING STACK & QUEUE LOGICALLY WITH SIMPLE LIST")
    print("using stack")
    stack=[]
    stack.append(1)
    stack.append(2)
    print("using pop on current stack list                                                                       ")
    pop_elem=stack.pop() #the item will be removed from the last index.
    print(stack,pop_elem)
    print("using queue")
    queue=[]
    queue.append(1)
    queue.append(2)
    print("using pop on current queue list                                                                       ")
    pop_elem=queue.pop(0) # by using 0, item will be removed from the first index.
    print(queue,pop_elem)
    print("-------------------------------------")