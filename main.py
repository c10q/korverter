# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


koverter_map = {
    'a': '에이',
    'b': '비',
    'c': '씨',
    'd': '디',
    'e': '이',
    'f': '에프',
    'g': '지',
    'h': '에이치',
    'i': '아이',
    'j': '제이',
    'k': '케이',
    'l': '엘',
    'm': '엠',
    'n': '엔',
    'o': '오',
    'p': '피',
    'q': '큐',
    'r': '알',
    's': '에스',
    't': '티',
    'u': '유',
    'v': '비',
    'w': '더블유',
    'x': '엑스',
    'y': '와이',
    'z': '지',
    ' ': '~ '
}


def korverter():
    # Use a breakpoint in the code line below to debug your script.

    while True:
        text = input()

        if text == 'exit':
            break

        if 96 < ord(text[-1]) < 123:
            text += '~'

        result = ''
        for i in text:
            if koverter_map.get(i.lower()):
                result += koverter_map[i.lower()]
            else:
                result += i

        print(f"{result}")

    print('FINISH')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    korverter()
