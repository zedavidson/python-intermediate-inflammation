# Add an extra level of indentation (extra 4 spaces) to distinguish arguments from the rest of the code that follows
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Use hanging indents to add an indentation level like paragraphs of text where all the lines in a paragraph are
# indented except the first one
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Using hanging indent again, but closing bracket aligned with the first non-blank character of the previous line
a_long_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.66, 1], [0.66, 0.83, 1], [0.77, 0.88, 1]]
    ]

# Using hanging indent again, but closing bracket aligned with the start of the multiline contruct
a_long_list2 = [
    1,
    2,
    3,
    # ...
    79
]
