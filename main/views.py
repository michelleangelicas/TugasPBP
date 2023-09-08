from django.shortcuts import render

# Create your views here.
def show_main(request):
    items = [
        {
            'name': 'Diamond',
            'amount': 3,
            'description': 'Diamonds are an extremely rare material that do not need to be smelted in order to be used. You must use an Iron or Diamond Pickaxe to collect them.'
        },
        {
            'name': 'Emerald',
            'amount': 9,
            'description': 'Emeralds are rare minerals that are used primarily as the currency for trading with villagers and wandering traders.'
        },
        {
            'name': 'Charcoal',
            'amount': 23,
            'description': 'Charcoal is an item obtained by smelting logs or wood. It is used as fuel, or for crafting torches and campfires.'
        },
        # Tambahkan item lain di sini dengan format yang sama
    ]

    context = {
        'items': items,
    }

    return render(request, "main.html", context)
