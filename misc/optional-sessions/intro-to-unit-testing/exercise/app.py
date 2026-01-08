products = ['apple', 'orange', 'banana', 'lemon']

def add_item(item, list):
    if type(item) is str:
        if item in list:
            print('Item already exists')
        else:
            list.append(item)
    else:
        print('You must enter a string')
    return list

# Common Case: Add new item
# add_item('lime', products)

# Edge Case: Add existing item
# add_item('apple', products)

# Corner Case: Add boolean to list
# add_item(False, products)


def delete_item(item, list):
    if item in list:
        list.remove(item)
    else:
        print('Item is not in list')
    return list

# Common Case: Delete existing item
# delete_item('apple', products)

# Edge Case: Delete item that doesn't exist
# delete_item('kiwi', products)


def update_item(existing_item, new_item, list):
    if existing_item in list:
        for i, item in enumerate(list):
            if item == existing_item:
                list[i] = new_item
    else:
        print('Input item is not in list')
    return list

# Common Case: Update existing item
# update_item('apple', 'kiwi', products)

# Edge Case: Update item that doesn't exist
# update_item('kiwi', 'cherry', products)


def read_txt(file_path):
    with open(file_path) as f:
        list = []
        for line in f:
            line = line.strip()
            list.append(line)
    return list

# Common Case: Check that read from txt file writes to list correctl including removing the white space characters
# read_txt('example.txt')
