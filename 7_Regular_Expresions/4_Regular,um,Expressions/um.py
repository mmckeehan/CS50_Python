import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r"\bum\b"
    if re.search(pattern, s, re.IGNORECASE):
        s_count = len(re.findall(pattern, s, re.IGNORECASE))
        return int(s_count)
    else:
        return 0

if __name__ == "__main__":
    main()
