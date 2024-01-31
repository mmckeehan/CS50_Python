import seasons

def test_date_validation():
    assert seasons.date_validation("1985-04-14") == "1985-04-14"
    assert seasons.date_validation("") == "Invalid Date"
    assert seasons.date_validation("April 14, 1985") == "Invalid Date"
    assert seasons.date_validation("04-14-1985") == "Invalid Date"
    assert seasons.date_validation("4-14-1985") == "Invalid Date"

def test_quick_maths():
    assert seasons.quick_maths("1985-04-14") == "Twenty million, three hundred ninety-three thousand, two hundred eighty"
    assert seasons.quick_maths("2024-01-21") == "One thousand, four hundred forty"
