import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
    if re.search(pattern, ip):
        ip_num_validate = ip.split(".")
        for octet in ip_num_validate:
            if 0 <= int(octet) < 256:
                is_true = True
            else:
                return False
    else:
        return False

    if is_true == True:
        return True


if __name__ == "__main__":
    main()
