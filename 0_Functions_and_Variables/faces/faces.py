def main():
    face = input()
    convert(face)

def convert(emote):
    print(emote.replace(":)", "🙂").replace(":(", "🙁"))



main()
