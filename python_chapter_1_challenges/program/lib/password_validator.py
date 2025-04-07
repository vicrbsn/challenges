# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string


# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)

# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

characters = ['!', '@', '$', '%', '&']
def is_valid(password):
    character = False
    if len(password) > 7:
        for item in characters:
            if item in password:
                character = True
                return True
        if character == False:
            return False
    else:
        return False