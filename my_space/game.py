def guessing_game():
    k=randint(1,20)
    count=1
    my_num=int(input('Enter a number between 1 to 20:'))
    while my_num!=k:

        if k>my_num:
            print('Choose another')
            my_num=int(input('Enter a large number than your previous:'))
            count=count+1
            continue
        else:
            print('Choose another')
            my_num=int(input('Enter a Smaller number than your previous:'))
            count=count+1
            continue
    else:
            print("Congrats! you guessed {} times to match the number".format(count)

