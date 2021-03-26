"""
Sudoku validator v1.0

Features:
    - Creates sudoku board by user inputs
    - Checks if Sudoku board is valid in every way in order to maximize correctness

"""


def create_list():
    nums = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth']
    print("Type one row's numbers in one line,\nafter inputting all the rows, the algorithm will determine\nwhether sudoku board is valid or not")
    sudoku_table = []
    for row in range(9):
        r = str(input(nums[row] + " row: "))
        temp_row = [i for i in r]
        sudoku_table.append(temp_row)
    print(sudoku_table)
    return sudoku_table


def create_boxes(table):
    test_val = []
    final_val = []  # 27 lists of in-line triplets
    for box in range(9):
        count = 0
        temp_triple = []
        temp_row = []
        for el in range(9):  # Division of one row into 3 list triplets
            temp_triple.append(table[box][el])
            count += 1
            if len(temp_triple) == 3:
                temp_row.append(temp_triple)
                temp_triple = []
                count = 0
        test_val.append(temp_row)
    print(test_val)

    # creating box triplets
    x_adder = 0
    for i in range(3):
        temp_box_triplet = []
        three_counter = 0
        for row in test_val:
            temp_box_triplet.append(row[x_adder])
            three_counter += 1

            if three_counter == 3:  # when there are 3 elements in the list, final_val gets updated
                final_val.append(temp_box_triplet)
                temp_box_triplet = []
                three_counter = 0
        x_adder += 1

    return final_val


def checker(enh_table, basic_table):  # enh_table = table divided by special triplets in create_boxes function
    sample_val = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    box_valid = True
    ordered_list = []
    count = 1

    # Unpacking the lists
    for box in enh_table:
        for triple in box:
            for el in triple:
                ordered_list.append(el)
        ordered_list.sort()

        # Checking if boxes are good
        if sample_val == ordered_list:
            print("Box", str(count) + ": PASSED")
            count += 1
        else:
            box_valid = False
            print("Box", str(count) + ": FAILED")
        ordered_list = []

    print("Box validation:", box_valid)

    # Lines (horizontal, vertical)
    # Horizontal

    h_valid = True
    for row in range(len(basic_table)):
        print(basic_table[row])
        if sorted(basic_table[row]) == sample_val:
            print("Row", str(row) + ": PASSED")
        else:
            h_valid = False
            print("Row", str(row) + ": FAILED")

    print("Horizontal validation:", h_valid)

    # Vertical

    v_valid = True
    for row_index in range(len(basic_table)):
        temp_verticals = []
        for index in range(len(basic_table)):
            temp_verticals.append(basic_table[index][row_index])

        if sorted(temp_verticals) == sample_val:
            print("Vertical", str(row_index) + ": PASSED")
        else:
            v_valid = False
            print("Vertical", str(row_index) + ": FAILED")

    print("Vertical validation:", v_valid)

    # Ending sequence: Testing if all of the tests are True

    if box_valid and h_valid and v_valid:
        print("This sudoku board is valid. Good job!")


board = create_list()
checker(create_boxes(board), board)
