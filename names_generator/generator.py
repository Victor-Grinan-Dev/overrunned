from names_generator.viking_name import NameMe
from names_generator.common_names import People
# import heroes


def generate(n: int = 1, name_type="normal", fullname=True, print_on: bool = False,):
    max_len = 26
    INDEX_TOTAL_LEN = 6
    heading_printed = False

    name_list = []
    fixed_name = ""
    name = None

    # printing
    for index in range(n):

        if name_type.lower() == "viking":
            name = NameMe.generate_fullname()
        elif name_type.lower() == "chaos":
            name = NameMe.generate_c
        # create regular people name
        else:
            if fullname:
                name = People.generate(fullname=True)
            else:
                name = People.generate(fullname=False)
            # list_len = 0
            #
            # # separate name by spaces in a list
            # name_holder = name.split(" ")
            # for element in name_holder:
            #     list_len += len(element)
            #
            # for element in name_holder:
            #     for character in element:
            #         if character == "-":
            #             fixed_name += "_"
            #         else:
            #             fixed_name += character
            #
            #     name_list.append(fixed_name)
            #     fixed_name = ""
            #
            # longest = ""
            # for element in name_holder:
            #     if len(element) > len(longest):
            #         longest = element
            #
            # if print_on:
            #
            #     if len(name) > max_len:
            #         max_len = len(name)
            #
            #     if not heading_printed:
            #         # heading
            #         print("index ".upper(), "generated name".upper(), " " * (max_len - 14))
            #         heading_printed = True
            #
            #     # index
            #     s_index = f"{index + 1}"
            #     index_spaces = INDEX_TOTAL_LEN - len(s_index)
            #     print(f"{index + 1}:", end=" " * index_spaces)
            #
            #     #  figure out spaces
            #     name_spaces = max_len - len(name)
            #     print(name, end=" " * name_spaces)
            #
            #     divs = len(name_holder) * 4
            #     list_len += 5 + divs
            #     holder_spaces = max_len - list_len
            #     print(name_holder, end=" " * holder_spaces)
            #
            #     longest_spaces = max_len - len(longest)
            #     print(f"{longest}", end=" " * longest_spaces)
            #     [print(s, end=" ") for s in name_list]
            #     print("")

        return name


if __name__ == '__main__':
    for _ in range(10):
        print(generate(print_on=True, name_type="normal"))
