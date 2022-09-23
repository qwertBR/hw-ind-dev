import threading

cur_digit = 1
condition_variable = threading.Condition()


def thread_function(inp_digit, print_amount):
    global condition_variable
    global cur_digit

    for i in range(print_amount):
        with condition_variable:
            condition_variable.wait_for(lambda: cur_digit == inp_digit, timeout=10)
            print(inp_digit, end="")
            cur_digit = cur_digit % 3 + 1
            condition_variable.notify_all()


n = int(input())

threads = []

for threand_num in range(1, 4):
    threads.append(threading.Thread(target=thread_function, args=(threand_num, n)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
