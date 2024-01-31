import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Validate that str is HTML
    pattern = r"^<iframe.+src=(\"https?://(?:www\.)?youtube\.com/embed/(\w+)\")(?:.+)?></iframe>$"
    if matches := re.search(pattern, s, flags= re.IGNORECASE):
        # Extract YouTube URL that is part of src of an iframe
        # Returns sharable youtube.be equivilent str
        matches = re.sub(r"^\"https?://(?:www\.)?youtube\.com/embed/.+\"$", f"https://youtu.be/{matches.group(2)}", matches.group(1))
        return matches

    else:
        return None



if __name__ == "__main__":
    main()
