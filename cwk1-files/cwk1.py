"""
Introduction to Programming Coursework 1

@author: Karl Samuel Kassis
"""


def valid_puzzle(puzzle: list) -> bool:

    # define the variable that stores the previous element
    previous_element = puzzle[0].upper()
    # going through the elements in puzzle
    for element in puzzle:
        # checking for:
        # 1-if element is a string
        # 2-if element has the same length as the previous element
        # 3-if puzzle is a list
        if not (element is str and
                len(element) == len(previous_element) and
                puzzle is list):
            return False

        # updates last item just before element changes its value
        previous_element = element

    return True


def similarity_grouping(data: list) -> list:
    # check if data is a list
    if data is not list:
        return []

    # creating the return sorted list with the first element of data
    return_list = [[data[0]]]

    # going through the elements in data except the first thats already
    # taken care of
    for element_in_data in range(1, len(data)):

        # going through the elements of the sorted list
        for sublist_of_f in range(len(return_list)):

            # adding elements in data with an existing sublist,
            # in return list, in the corresponding one
            if data[element_in_data] == return_list[sublist_of_f][0]:
                return_list[sublist_of_f].append(data[element_in_data])

                # breaking just so the same element in data is not added
                # multiple times
                break

        # if no element in data matched to a sublist in the return list then
        # we create a new one with the element in it
        else:
            return_list.append([data[element_in_data]])

    return return_list


def highest_count_items(data: str) -> list:
    # we create the return list
    return_list = []
    # we create the variable that stores the biggest number of
    # repitions of a word
    max_count = 0
    # word1 and word2 store temporary names used for
    # counting
    word1 = ''
    word2 = ''

    # letter1 will be used to construct word1
    for letter1 in data:
        # count will be used to count the repitions of words
        count = 0
        # its true if a word was constructed since words are separated
        # by commas
        if letter1 == ',':
            # letter2 will be used to construct word2

            for letter2 in data:
                # its true if a word was constructed since words are
                # separated by commas
                if letter2 == ',':
                    # then we found a repition of a word so we add 1 to count
                    if word1 == word2:
                        count += 1
                    # we reset word2 because the word it coutains was counted
                    word2 = ''
                # used to ignore spaces since they could spoil the final result
                elif letter2 == ' ':
                    continue
                # here the letter2 is added to word2 because at this point it
                # can only be a letter
                else:
                    word2 += letter2

            # if count is bigger than the max last recorded the max is updated
            if count > max_count:
                max_count = count

                # we replace the last list_count with the new most repeated
                # word and its count
                return_list = [[word1, max_count]]

            # if count equals max_count then we have to make sure that
            # it is the same word that will be added

            # to do this we will use any which returns True
            # if it finds that word1 is already in a list in list_count
            elif count == max_count and not any(word1 == return_list
                                                [sublist_index][0]
                                                for sublist_index in
                                                range(len(return_list))):

                # if the condition is satisfied we add the word and its count
                # to the list_count
                return_list.append([word1, max_count])

            # we reset word1 because the word it coutains was counted
            word1 = ''

        # used to ignore spaces since they could spoil the final result
        elif letter1 == ' ':
            continue
        # here the letter1 is added to word2 because at this point
        # it can only be a letter
        else:
            word1 += letter1

    return return_list


def valid_char_in_string(popList: list, charSet: list) -> bool:
    # we create the list containing the characters of popList
    list_of_char = []
    # we check that charSet has the right format
    if charSet is list:

        # here we add every character of every word in popList in list_of_char
        for word in popList:
            for char in word:
                list_of_char.append(char)

        # we loop through the char in charSet
        for char in charSet:
            # here filter removes, every char in charSet, from list_of_char
            list_of_char = list(filter(lambda element_in_list:
                                       (element_in_list != char),
                                       list_of_char))

        # list_of_char should be empty if all of its character were in charSet
        if list_of_char == []:
            return True
    # the function return false if charSet is not a list or
    # if list_of_char wasnt empty
    return False


def total_price(unit: int) -> float:
    price = 0
    # the loop keeps on until all units were counted and added to the price
    while unit != 0:
        # we check if unit contains a sixpack
        if unit >= 6:
            unit -= 6
            price += 5
        # if not then unit it only contains multiple single units
        else:
            unit -= 1
            price += 1.25
    # we apply the discount if the condition for it is met
    if price >= 20:
        price -= price/10
    return price


if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
