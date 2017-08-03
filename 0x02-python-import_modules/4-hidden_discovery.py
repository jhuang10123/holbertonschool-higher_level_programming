#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden_list = dir(hidden_4)

    for i in range(len(hidden_list)):
        if hidden_list[:2] != "__":
            print(hidden_list[i])
