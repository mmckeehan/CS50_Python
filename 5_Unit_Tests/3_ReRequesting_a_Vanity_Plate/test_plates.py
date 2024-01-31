from plates import is_valid

#Start with two letters
def test_is_valid_start():
   assert is_valid("CS50") == True
   assert is_valid("50") == False
   assert is_valid("H") == False

#Max 6, min 2 char
def test_is_valid_char_limit():
    assert is_valid("NRVOUS") == True
    assert is_valid("OUTTATIME") == False

# No num in middle
def test_is_valid_ends_w_num():
    assert is_valid("CS50A") == False
    assert is_valid("CS50") == True

# First number cannot be '0'
def test_is_valid_no_lead_zero():
    assert is_valid("ECT088") == False
    assert is_valid("CS50") == True

# No non-alphaNumeric
def test_is_valid_alphanum():
    assert is_valid("PI3.14") == False

