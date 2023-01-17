SteamClient for Python
This is my rework that I made for myself.
Original package: https://github.com/bukson/steampy 
=======


`steampy` is a library for Python, inspired by node-steam-tradeoffers, node-steam and other libraries for Node.js.
It was designed as a simple lightweight library, combining features of many steam libraries from Node.js into a single python module.
`steampy` is capable of logging into steam, fetching trade offers and handling them in simple manner, using steam user credentials
and SteamGuard file(no need to extract and pass sessionID and webCookie).
`steampy` is developed with Python 3 using type hints and many other features its supported for Windows, Linux and MacOs.

Table of Content
================

* [Installation](https://github.com/wizzzz9/steampy_rework#installation)

* [Usage](https://github.com/wizzzz9/steampy_rework#usage)

* [Examples](https://github.com/wizzzz9/steampy_rework#examples)

* [SteamClient methods](https://github.com/wizzzz9/steampy_rework#steamclient-methods)

* [Market methods](https://github.com/wizzzz9/steampy_rework#market-methods)

* [Guard module functions](https://github.com/wizzzz9/steampy_rework#guard-module-functions)

* [Test](https://github.com/wizzzz9/steampy_rework#test)

* [License](https://github.com/wizzzz9/steampy_rework#license)


Installation
============

```
pip install steampy_rework
```

Usage
=======
[Obtaining API Key](http://steamcommunity.com/dev/apikey)

[Obtaining SteamGuard from mobile device]( https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication )

[Obtaining SteamGuard using Android emulation]( https://github.com/codepath/android_guides/wiki/Genymotion-2.0-Emulators-with-Google-Play-support)


```python
proxy = "123.123.123:25565"
from steampy.client import SteamClient
client = SteamClient(proxy=f'{proxy}'OPTIONAL PARAMETER, steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
```


SteamClient methods
========

**Save steam session -> None**

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
client.save_session(path=path_for_session, username=login)
```

**Load save_session -> None**

```python
client = SteamClient(session_path=steam_gard_path)
client.login(login, password)
```

**List of exceptions: SevenDaysHoldException, TooManyRequests, ApiException, LoginRequired, InvalidCredentials,
**CaptchaRequired, ConfirmationExpected, BadSteamResponse
**Example with except:
```python
try:
	client = SteamClient(steam_guard=steam_gard_path)
	client.login(login, password)
except InvalidCredentials | CaptchaRequired as error_info:
	print(f"Error: {error_info}")
```

**Get trade offers that you send -> dict**

```python
client = SteamClient(steam_guard=steam_gard_path)
client.login(login, password)
dict_with_tradeoffers = client.get_sent_tradeoffers()
```

**Get trade offers that you recived -> dict**

```python
client = SteamClient(steam_guard=steam_gard_path)
client.login(login, password)
dict_with_tradeoffers = client.get_recived_tradeoffers()
```

**get_my_steamid_form_session() -> str**

```python
client = SteamClient(steam_guard=steam_gard_path)
client.login(login, password)
steamid64 = client.get_my_steamid_form_session()
```

**is_session_alive() -> None**

Using `SteamClient.login` method is required before usage
Check if session is alive. This method fetches main page and check
if user name is there. Thanks for vasia123 for this solution.

```python
from steampy.client import SteamClient

client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
is_session_alive = client.is_session_alive()
```

**api_call(request_method: str, interface: str, api_method: str, version: str, params: dict = None) -> requests.Response**

Directly call api method from the steam api services.

[Official steam api site](https://developer.valvesoftware.com/wiki/Steam_Web_API)

[Unofficial but more elegant](https://lab.xpaw.me/steam_api_documentation.html)

```python
from steampy.client import SteamClient

steam_client = SteamClient('MY_API_KEY')
params = {'key': 'MY_API_KEY'}
summaries =  steam_client.api_call('GET', 'IEconService', 'GetTradeOffersSummary', 'v1', params).json()
```

**decline_trade_offer(trade_offer_id: str) -> dict**

Decline trade offer that **other** user sent to us.

**cancel_trade_offer(trade_offer_id: str) -> dict**

Cancel trade offer that **we** sent to other user.

**get_my_inventory(game: GameOptions, merge: bool = True, count: int = 5000) -> dict**

Using `SteamClient.login` method is required before usage

If `merge` is set `True` then inventory items are merged from items data and items description into dict where items `id` is key
and descriptions merged with data are value.

`Count` parameter is default max number of items, that can be fetched.

Inventory entries looks like this:
```python
{'7146788981': {'actions': [{'link': 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S%owner_steamid%A%assetid%D316070896107169653',
                             'name': 'Inspect in Game...'}],
                'amount': '1',
                'appid': '730',
                'background_color': '',
                'classid': '1304827205',
                'commodity': 0,
                'contextid': '2',
                'descriptions': [{'type': 'html',
                                  'value': 'Exterior: Field-Tested'},
                                 {'type': 'html', 'value': ' '},
                                 {'type': 'html',
                                  'value': 'Powerful and reliable, the AK-47 '
                                           'is one of the most popular assault '
                                           'rifles in the world. It is most '
                                           'deadly in short, controlled bursts '
                                           'of fire. It has been painted using '
                                           'a carbon fiber hydrographic and a '
                                           'dry-transfer decal of a red '
                                           'pinstripe.\n'
                                           '\n'
                                           '<i>Never be afraid to push it to '
                                           'the limit</i>'},
                                 {'type': 'html', 'value': ' '},
                                 {'app_data': {'def_index': '65535',
                                               'is_itemset_name': 1},
                                  'color': '9da1a9',
                                  'type': 'html',
                                  'value': 'The Phoenix Collection'},
                                 {'type': 'html', 'value': ' '},
                                 {'app_data': {'def_index': '65535'},
                                  'type': 'html',
                                  'value': '<br><div id="sticker_info" '
                                           'name="sticker_info" title="Sticker '
                                           'Details" style="border: 2px solid '
                                           'rgb(102, 102, 102); border-radius: '
                                           '6px; width=100; margin:4px; '
                                           'padding:8px;"><center><img '
                                           'width=64 height=48 '
                                           'src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/eslkatowice2015/pentasports.a6b0ddffefb5507453456c0d2c35b6a57821c171.png"><img '
                                           'width=64 height=48 '
                                           'src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/eslkatowice2015/pentasports.a6b0ddffefb5507453456c0d2c35b6a57821c171.png"><img '
                                           'width=64 height=48 '
                                           'src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/eslkatowice2015/pentasports.a6b0ddffefb5507453456c0d2c35b6a57821c171.png"><img '
                                           'width=64 height=48 '
                                           'src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/cologne2015/mousesports.3e75da497d9f75fa56f463c22db25f29992561ce.png"><br>Sticker: '
                                           'PENTA Sports  | Katowice 2015, '
                                           'PENTA Sports  | Katowice 2015, '
                                           'PENTA Sports  | Katowice 2015, '
                                           'mousesports | Cologne '
                                           '2015</center></div>'}],
                'icon_drag_url': '',
                'icon_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpot7HxfDhjxszJemkV09-5lpKKqPrxN7LEmyVQ7MEpiLuSrYmnjQO3-UdsZGHyd4_Bd1RvNQ7T_FDrw-_ng5Pu75iY1zI97bhLsvQz',
                'icon_url_large': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpot7HxfDhjxszJemkV09-5lpKKqPrxN7LEm1Rd6dd2j6eQ9N2t2wK3-ENsZ23wcIKRdQE2NwyD_FK_kLq9gJDu7p_KyyRr7nNw-z-DyIFJbNUz',
                'id': '7146788981',
                'instanceid': '480085569',
                'market_actions': [{'link': 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M%listingid%A%assetid%D316070896107169653',
                                    'name': 'Inspect in Game...'}],
                'market_hash_name': 'AK-47 | Redline (Field-Tested)',
                'market_name': 'AK-47 | Redline (Field-Tested)',
                'market_tradable_restriction': '7',
                'marketable': 1,
                'name': 'AK-47 | Redline',
                'name_color': 'D2D2D2',
                'owner_descriptions': '',
                'tags': [{'category': 'Type',
                          'category_name': 'Type',
                          'internal_name': 'CSGO_Type_Rifle',
                          'name': 'Rifle'},
                         {'category': 'Weapon',
                          'category_name': 'Weapon',
                          'internal_name': 'weapon_ak47',
                          'name': 'AK-47'},
                         {'category': 'ItemSet',
                          'category_name': 'Collection',
                          'internal_name': 'set_community_2',
                          'name': 'The Phoenix Collection'},
                         {'category': 'Quality',
                          'category_name': 'Category',
                          'internal_name': 'normal',
                          'name': 'Normal'},
                         {'category': 'Rarity',
                          'category_name': 'Quality',
                          'color': 'd32ce6',
                          'internal_name': 'Rarity_Legendary_Weapon',
                          'name': 'Classified'},
                         {'category': 'Exterior',
                          'category_name': 'Exterior',
                          'internal_name': 'WearCategory2',
                          'name': 'Field-Tested'},
                         {'category': 'Tournament',
                          'category_name': 'Tournament',
                          'internal_name': 'Tournament6',
                          'name': '2015 ESL One Katowice'},
                         {'category': 'Tournament',
                          'category_name': 'Tournament',
                          'internal_name': 'Tournament7',
                          'name': '2015 ESL One Cologne'},
                         {'category': 'TournamentTeam',
                          'category_name': 'Team',
                          'internal_name': 'Team39',
                          'name': 'PENTA Sports'},
                         {'category': 'TournamentTeam',
                          'category_name': 'Team',
                          'internal_name': 'Team29',
                          'name': 'mousesports'}],
                'tradable': 1,
                'type': 'Classified Rifle'}}
```

**get_partner_inventory(partner_steam_id: str, game: GameOptions, merge: bool = True, count: int = 5000) -> dict**

Using `SteamClient.login` method is required before usage

Inventory items can be merged like in `SteamClient.get_my_inventory` method

`Count` parameter is default max number of items, that can be fetched.

**get_wallet_balance(convert_to_float: bool = True) -> Union[str, float]**

Check account balance of steam acccount. It uses `parse_price` method from utils
to covnert money string to Decimal if `convert_to_decimal` is set to `True`.

Example:
```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
wallet_balance = client.get_wallet_balance()
self.assertTrue(type(wallet_balance), decimal.Decimal)
```

market methods
==============

**fetch_price(item_hash_name: str, game: GameOptions, currency: str = Currency.USD) -> dict**

Some games are predefined in `GameOptions` class, such as `GameOptions.DOTA2`, `GameOptions.CS` and `GameOptions.TF2,
but `GameOptions` object can be constructed with custom parameters.

Currencies are defined in Currency class, [currently](https://github.com/bukson/steampy#currencies)

Default currency is USD

May rise `TooManyRequests` exception if used more than 20 times in 60 seconds.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
item = 'M4A1-S | Cyrex (Factory New)'
client.market.fetch_price(item, game=GameOptions.CS)
{'volume': '208', 'lowest_price': '$11.30 USD', 'median_price': '$11.33 USD', 'success': True}
```

**fetch_price_history(item_hash_name: str, game: GameOptions) -> dict**

Using `SteamClient.login` method is required before usage

Returns list of price history of and item.
```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
item = 'M4A1-S | Cyrex (Factory New)'
response = client.market.fetch_price_history(item, GameOptions.CS)
response['prices'][0]
    ['Jul 02 2014 01: +0', 417.777, '40']
```

Each entry in `response['prices']` is a list, with first entry being date, second entry price, and third entry a volume.



**get_my_market_listings_for_confirm() -> dict**

Using `SteamClient.login` method is required before usage

Returns market listings for confirm

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
listings = client.market.get_my_market_listings_for_confirm()
```



**get_my_market_listings() -> dict**

Using `SteamClient.login` method is required before usage

Returns market listings posted by user

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
listings = client.market.get_my_market_listings()
```


**create_sell_order(assetid: str, game: GameOptions, money_to_receive: str) -> dict**

Using `SteamClient.login` method is required before usage

Create sell order of the asset on the steam market.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
asset_id_to_sell = 'some_asset_id'
game = GameOptions.DOTA2
sell_response = client.market.create_sell_order(asset_id_to_sell, game, "10000")
```
 
⚠️ `money_to_receive` has to be in cents, so "100.00" should be passed has "10000"

**create_buy_order(market_name: str, price_single_item: str, quantity: int, game: GameOptions, currency: Currency = Currency.USD) -> dict**

Using `SteamClient.login` method is required before usage

Create buy order of the assets on the steam market.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password))
response = client.market.create_buy_order("AK-47 | Redline (Field-Tested)", "1034", 2, GameOptions.CS, Currency.EURO)
buy_order_id = response["buy_orderid"]
```
⚠️ `price_single_item` has to be in cents, so "10.34" should be passed has "1034"

**buy_item(market_name: str, market_id: str, price: int, fee: int, game: GameOptions, currency: Currency = Currency.USD) -> dict**

Using `SteamClient.login` method is required before usage

Buy a certain item from market listing.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
response = client.market.buy_item('AK-47 | Redline (Field-Tested)', '1942659007774983251', 81, 10,
                                        GameOptions.CS, Currency.RUB)
wallet_balance = response["wallet_info"]["wallet_balance"]
```

**cancel_sell_order(sell_listing_id: str) -> None**

Using `SteamClient.login` method is required before usage

Cancel previously requested sell order on steam market.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
sell_order_id = "some_sell_order_id"
response = client.market.cancel_sell_order(sell_order_id)
```

**cancel_buy_order(buy_order_id) -> dict**

Using `SteamClient.login` method is required before usage

Cancel previously requested buy order on steam market.

```python
client = SteamClient(steam_guard='PATH_TO_STEAMGUARD_FILE or dict - check tests')
client.login(login, password)
buy_order_id = "some_buy_order_id"
response = client.market.cancel_buy_order(buy_order_id)
```


guard module functions
======================

**load_steam_guard(steam_guard: str) -> dict**

If `steam_guard` is file name then load and parse it, else just parse `steam_guard` as json string.

**generate_one_time_code(shared_secret: str, timestamp: int = None) -> str**

Generate one time code for logging into Steam using shared_secret from SteamGuard file.
If none timestamp provided, timestamp will be set to current time.

**generate_confirmation_key(identity_secret: str, tag: str, timestamp: int = int(time.time())) -> bytes**

Generate mobile device confirmation key for accepting trade offer. 
Default timestamp is current time.


License
=======

MIT License

Copyright (c) 2022 [Viacheslav Patokin]viacheslavpatokin@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.