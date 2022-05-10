def enumerate_new_list(new_list):
    for index, value in enumerate(new_list):
        print(f"{index}. {value}")


def user_input(new_list):
    while True:
        num = input()
        try:
            num = int(num)
            if 0 <= num < len(new_list):
                num = num
            else:
                raise ValueError
            break
        except Exception as e:
            print("Please choose a valid option")
            print(enumerate_new_list(new_list))
    return num
