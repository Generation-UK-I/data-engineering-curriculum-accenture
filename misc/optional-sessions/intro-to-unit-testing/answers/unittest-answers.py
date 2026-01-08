from app import add_item, delete_item, update_item, read_txt


def test_add_existing_item_to_list():
    # Assemble
    new_item = 'apple'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['apple', 'orange', 'banana', 'lemon']

    # Act
    actual = add_item(new_item, products)

    # Assert
    assert expected == actual

test_add_existing_item_to_list()


def test_add_new_item_to_list():
    # Assemble
    new_item = 'kiwi'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['apple', 'orange', 'banana', 'lemon', 'kiwi']
    
    # Act
    actual = add_item(new_item, products)

    # Assert
    assert expected == actual

test_add_new_item_to_list()


def test_add_boolean_item_to_list():
    # Assemble
    new_item = False
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['apple', 'orange', 'banana', 'lemon']
    
    # Act
    actual = add_item(new_item, products)

    # Assert
    assert expected == actual

test_add_boolean_item_to_list()


def test_delete_item_from_list():
    # Assemble
    item = 'apple'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['orange', 'banana', 'lemon']

    # Act
    actual = delete_item(item, products)

    # Assert
    assert expected == actual

test_delete_item_from_list()


def test_delete_item_that_doesnt_exist_from_list():
    # Assemble
    item = 'cherry'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['apple', 'orange', 'banana', 'lemon']

    # Act
    actual = delete_item(item, products)

    # Assert
    assert expected == actual

test_delete_item_that_doesnt_exist_from_list()


def test_update_existing_item_in_list():
    # Assemble
    existing_item = 'apple'
    new_item = 'water melon'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['water melon', 'orange', 'banana', 'lemon']
    
    # Act
    actual = update_item(existing_item, new_item, products)

    # Assert
    # print(f'actual outcome: {actual}')
    # print(f'expected outcome: {expected}')
    assert expected == actual

test_update_existing_item_in_list()


def test_update_item_that_doesnt_exist_in_list():
    # Assemble
    non_item = 'lime'
    new_item = 'water'
    products = ['apple', 'orange', 'banana', 'lemon']
    expected = ['apple', 'orange', 'banana', 'lemon']
    
    # Act
    actual = update_item(non_item, new_item, products)
    
    # Assert
    assert expected == actual

test_update_item_that_doesnt_exist_in_list()


def test_reads_file_into_list():
    # Assemble
    file_path = 'example.txt'
    expected = ['orange', 'green', 'yellow']
    # Act
    actual = read_txt(file_path)

    # Assert
    # print(f'actual outcome: {actual}')
    # print(f'expected outcome: {expected}')
    assert expected == actual

test_reads_file_into_list()
