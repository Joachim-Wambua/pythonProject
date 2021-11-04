# Author: Joachim Wambua
# Advanced Algorithms Assignment 1

# Function responsible for checking socks and matching pairs
def matchSock(array, arr_len):
    # Initialise pair_counter & dict to hold socks and their count values
    pair_counter = 0
    # dict key holds sock color and value holds pair_counter
    sock_dict = {}
    # Looping through the array of colored socks
    for i in array:
        # if the key we are currently checking is in the dictionary...
        if i in sock_dict:
            # Then add pair to pair_counter
            pair_counter += 1
            # Since sock is already paired up and counted, remove from dict
            sock_dict.pop(i)
        else:
            # Else(sock color not in array), add key(color) and value(pair_counter) to dict
            sock_dict[i] = 1
    return pair_counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Empty array to hold user input
    sock_pile = []
    # Collect input for array length
    socks_num = int(input('How many socks are in the pile? '))
    print('Enter ' + str(socks_num) + ' Colors: ')
    # Collect Colors from user
    for k in range(socks_num):
        color = input()
        sock_pile.append(color)

    result = matchSock(sock_pile, socks_num)
    print(str(result) + ' pairs are in the pile')
