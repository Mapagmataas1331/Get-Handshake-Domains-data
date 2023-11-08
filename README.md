# get multiple handshake domains current data from namebase.io

It's python script to get domain data from namebase.io,
it saves output in json file, you can check custom.handshakesPassData.json for example

In getCustom.py you can edit:
    domains = {'c', 'com', 'mapagmataas', '🥇1', '🏴󠁧� 󠁥󠁮󠁧󠁿', 'sesdgdgfdfg', 'xn--f28h81f', 'schoolco', 'cfdgdfg'}
to get data from domains you need

or create own function to format names, like i did in getEmojis.py

for it to work you need:
    pip install namebase_marketplace

and for emoji:
    pip install emoji
