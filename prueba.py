stores = [
    {
        'name':'My wonderful store',
        'items': [
            {
                'name':'my item',
                'prices': 15.99
            }
        ]
    }
]

for bt in stores:
    print(bt['items'][0]['name'])