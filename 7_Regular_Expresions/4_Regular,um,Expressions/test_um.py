from um import count

def test_count():
    assert count("yummy") == 0
    assert count("Um... like... um... Pokemon!") == 2
    assert count("Admiral Pidgeon said 'Um, where did the rum go?'") == 1
