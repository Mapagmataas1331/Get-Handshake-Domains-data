from getHandshakes import *
import emoji


pre = ''; after = ''

if __name__ == '__main__':
    emoji_data = handshakeDict()

    current = 0
    total = len(emoji.EMOJI_DATA.items())

    for emoji_char, _ in emoji.EMOJI_DATA.items():
        if (current % 50 == 0):
            print(f'  {current}/{total}')
        emoji_data.getHandshakeInfo(pre + emoji_char + after)
        current += 1

    if not emoji_data:
        print('No emojis were convertible to Punycode.')
    else:
        emoji_data.saveHandshakesPassData('emoji.handshakesPassData.json')
        print('Emoji symbols have been saved to emoji_symbols.json')
