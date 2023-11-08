import json
from namebase_marketplace import marketplace

marketplace = marketplace.Marketplace()

class handshakeDict(dict):
    def getHandshakeInfo(self, key):
        try:
            handshakeName = key.encode('idna').decode('ascii')
            domain = marketplace.get_domain_info(handshakeName)
            data = {
                'closeAmount': False,
                'reserved': False,
                'highestStakeAmount': False
            }

            if (domain['reserved']):
                data['reserved'] = True
                if 'reserved' not in self:
                    self['reserved'] = {}
                self['reserved'][key] = {
                    'punycode': handshakeName,
                    'link': f'https://www.namebase.io/domains/{handshakeName}',
                    'data': data,
                }
            elif not domain['bids']:
                if 'neverOnAuction' not in self:
                    self['neverOnAuction'] = {}
                self['neverOnAuction'][key] = {
                    'punycode': handshakeName,
                    'link': f'https://www.namebase.io/domains/{handshakeName}',
                    'data': data,
                }
            elif (domain['closeAmount'] != None):
                data['closeAmount'] = domain['closeAmount']
                if 'sold' not in self:
                    self['sold'] = {}
                self['sold'][key] = {
                    'punycode': handshakeName,
                    'link': f'https://www.namebase.io/domains/{handshakeName}',
                    'data': data,
                }
            else:
                data['highestStakeAmount'] = domain['highestStakeAmount']
                if 'OnAuction' not in self:
                    self['OnAuction'] = {}
                self['OnAuction'][key] = {
                    'punycode': handshakeName,
                    'link': f'https://www.namebase.io/domains/{handshakeName}',
                    'data': data,
                }

            print(f'{handshakeName}({key}) ')

        except Exception as e:
            if 'errorOccurred' not in self:
                self['errorOccurred'] = {}
            self['errorOccurred'][key] = True
            print(f' Error: "{e}" on "{key}"')

    def saveHandshakesPassData(self, fileName='handshakesPassData.json'):
        with open(fileName, 'w', encoding='utf-8') as json_file:
            json.dump(self, json_file, ensure_ascii=False, indent=4)
