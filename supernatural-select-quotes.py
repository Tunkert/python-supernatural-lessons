with open('supernatural-quotes.txt') as f:
    content_list = f.readlines()

    for item in content_list:
        if content_list.index(item) % 2 == 0:
            print(item)
