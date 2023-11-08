from getHandshakes import *

if __name__ == '__main__':
    handshakeDict = handshakeDict()

    domains = {'c', 'com', 'mapagmataas', '🥇1', '🏴󠁧� 󠁥󠁮󠁧󠁿', 'sesdgdgfdfg', 'xn--f28h81f', 'schoolco', 'cfdgdfg'}

    for name in domains:
        handshakeDict.getHandshakeInfo(name)

    if not handshakeDict:
        print('Got no domains.')
    else:
        handshakeDict.saveHandshakesPassData('custom.handshakesPassData.json')
        print('domains have been saved to custom.handshakesPassData.json')
