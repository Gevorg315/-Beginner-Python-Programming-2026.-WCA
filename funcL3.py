# def get_user_param(prompt_tex=''):
#     """Get parameter from user."""
#     value = input(prompt_tex)
#     if value.isdigit():
#         return int(value)
#     else:
#         print(f'{value} is not a number')
#         return None
#
#
# shape_type = input('Please, provide a shape for calculate square: ')
#
# if shape_type == 'square':
#     a = get_user_param('side length:')
#     s = a ** 2
#     print(f'square area: {s}')
#
# elif shape_type == 'rectangle':
#     a = get_user_param('length:')
#     b = get_user_param('width:')
#     s = a * b
#     print(f'rectangle area: {s}')
#
# elif shape_type == 'circle':
#     r = get_user_param('radius:')
#     s = 3.14 * r ** 2
#     print(f'circle area: {s}')
#
# else:
#     print(f"I don't know {shape_type} shape :-(")


def get_user_param(prompt_tex=''):
    """Get parameter from user."""
    value = input(prompt_tex)
    if value.isdigit():
        return int(value)
    else:
        print(f'{value} is not a number')
        return None


def square_area(side_length):
    """Calculate area for square."""
    return side_length ** 2


def rectangle_area(length, width):
    """Calculate area fro rectangle."""
    return length * width


def circle_area(radius):
    """Calculate area for circle."""
    return 3.14 * r ** 2

shape_type = input('Please, provide a shape you want to calculate area: ')

if shape_type == 'square':
    a = get_user_param('side length:')
    print(f'square area: {square_area(a)}')

elif shape_type == 'rectangle':
    a = get_user_param('length:')
    b = get_user_param('width:')
    print(f'rectangle area: {rectangle_area(a, b)}')

elif shape_type == 'circle':
    r = get_user_param('radius:')
    print(f'circle area: {circle_area(r)}')

else:
    print(f"I don't know {shape_type} shape :-(")