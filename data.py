# data.py
# This file stores all the restaurant data as Python dictionaries.
# Each restaurant is a dictionary (key-value pairs), and all restaurants
# are stored in a list called RESTAURANTS.
# In the future, this can be replaced with a database.

RESTAURANTS = [

    # ── TOKYO ────────────────────────────────────────────────────────────────

    {
        "id": "ichiran-shinjuku",           # Unique ID used in the URL
        "name": "Ichiran Shinjuku",
        "city": "tokyo",                    # Used to filter by city
        "area": "Shinjuku",
        "ramen_type": "Tonkotsu",
        "description": (
            "One of Japan's most famous ramen chains, Ichiran is perfect for solo travelers. "
            "You order from a vending machine, sit in your own private booth, and enjoy a "
            "rich, creamy tonkotsu broth without any social pressure. Open 24 hours — "
            "ideal after a late night out in Shinjuku."
        ),
        "price_range": "¥1,000 – ¥1,500",
        "hours": "24 hours",
        "address": "3-34-11 Shinjuku, Shinjuku-ku, Tokyo",
        "google_maps_url": "https://www.google.com/maps/search/Ichiran+Shinjuku",
        "tags": ["tonkotsu", "solo-dining", "tourist-friendly", "late-night", "chain"],
    },
    {
        "id": "fuunji-shinjuku",
        "name": "Fuunji",
        "city": "tokyo",
        "area": "Shinjuku",
        "ramen_type": "Tsukemen (Dipping Noodles)",
        "description": (
            "Fuunji is famous for its thick, intensely flavored dipping broth. "
            "You dip chewy noodles into a rich tare — it's a completely different "
            "ramen experience. Expect a short queue during lunch. Cash only."
        ),
        "price_range": "¥900 – ¥1,200",
        "hours": "11:00 – 15:00, 17:30 – 21:00 (closed Sunday)",
        "address": "2-14-3 Yoyogi, Shibuya-ku, Tokyo",
        "google_maps_url": "https://www.google.com/maps/search/Fuunji+Shinjuku+Tokyo",
        "tags": ["tsukemen", "rich-broth", "queue", "cash-only", "local-favorite"],
    },
    {
        "id": "afuri-harajuku",
        "name": "AFURI",
        "city": "tokyo",
        "area": "Harajuku",
        "ramen_type": "Yuzu Shio (Salt)",
        "description": (
            "AFURI is known for its light, refreshing yuzu-flavored shio (salt) ramen. "
            "Unlike heavy tonkotsu, this broth is delicate and citrusy — great for people "
            "who prefer something less rich. The restaurant has a modern, stylish interior. "
            "Vegetarian options available."
        ),
        "price_range": "¥1,200 – ¥1,800",
        "hours": "11:00 – 23:00",
        "address": "1-1-7 Jingumae, Shibuya-ku, Tokyo",
        "google_maps_url": "https://www.google.com/maps/search/AFURI+Harajuku+Tokyo",
        "tags": ["shio", "yuzu", "light-broth", "vegetarian-option", "tourist-friendly", "stylish"],
    },
    {
        "id": "nagi-shinjuku",
        "name": "Nagi Shinjuku Golden Gai",
        "city": "tokyo",
        "area": "Shinjuku",
        "ramen_type": "Niboshi (Sardine) Shoyu",
        "description": (
            "Hidden in the legendary Golden Gai alley, Nagi serves a bold niboshi "
            "(dried sardine) shoyu ramen. The tiny counter-only seating and alley atmosphere "
            "make it a memorable experience. This is the kind of place that feels authentically Tokyo."
        ),
        "price_range": "¥900 – ¥1,100",
        "hours": "18:00 – 05:00",
        "address": "1-1-10 Kabukicho, Shinjuku-ku, Tokyo",
        "google_maps_url": "https://www.google.com/maps/search/Nagi+Golden+Gai+Shinjuku",
        "tags": ["shoyu", "niboshi", "late-night", "atmospheric", "small-restaurant"],
    },

    # ── OSAKA ─────────────────────────────────────────────────────────────────

    {
        "id": "kinryu-dotonbori",
        "name": "Kinryu Ramen Dotonbori",
        "city": "osaka",
        "area": "Dotonbori",
        "ramen_type": "Tonkotsu Shoyu",
        "description": (
            "A true Osaka icon. Kinryu's giant dragon sign is one of the most photographed "
            "spots in Dotonbori. Open 24 hours with tables outside — perfect for a late-night "
            "bowl after exploring Namba. Simple, satisfying, and very affordable."
        ),
        "price_range": "¥600 – ¥900",
        "hours": "24 hours",
        "address": "2-4 Dotonbori, Chuo-ku, Osaka",
        "google_maps_url": "https://www.google.com/maps/search/Kinryu+Ramen+Dotonbori+Osaka",
        "tags": ["tonkotsu", "shoyu", "late-night", "tourist-friendly", "budget", "iconic"],
    }
    ,
    {
        "id": "satsumaya-hotarugaike",
        "name": "Satsumaya Ramen",
        "city": "osaka",
        "area": "Hotarugaike",
        "ramen_type": "Shoyu (Soy Sauce)",
        "description": (
            "Thick, chewy homemade noodles served in a strong soy-sauce pork broth that pairs "
            "perfectly with rice. Free extra noodles and unlimited rice make it great value. "
            "The popular MAX Ramen is topped with extra pork, egg, and vegetables — a must-try."
        ),
        "price_range": "¥1,000 – ¥2,000",
        "hours": "11:00 – 14:30, 17:30 – 01:00",
        "address": "Hotarugaike, Toyonaka, Osaka",
        "google_maps_url": "https://maps.app.goo.gl/YXsBvEfAdo2KwdQF9",
        "tags": ["shoyu", "local-favorite", "great-value", "late-night"],
    }
    ,
    {
        "id": "kamukura-shinsaibashi",
        "name": "Kamukura",
        "city": "osaka",
        "area": "Shinsaibashi",
        "ramen_type": "Shoyu (Soy Sauce)",
        "description": (
            "Kamukura is beloved for its clean, clear shoyu broth that lets the chicken and "
            "seafood flavors shine. Located near Shinsaibashi shopping street, it's a great "
            "stop after a day of shopping. The noodles are thin and the portion is generous."
        ),
        "price_range": "¥700 – ¥1,000",
        "hours": "11:00 – 03:00",
        "address": "2-7-13 Shinsaibashisuji, Chuo-ku, Osaka",
        "google_maps_url": "https://www.google.com/maps/search/Kamukura+Shinsaibashi+Osaka",
        "tags": ["shoyu", "light-broth", "tourist-friendly", "late-night", "chain"],
    },
    {
        "id": "ippudo-osaka",
        "name": "Ippudo Shinsaibashi",
        "city": "osaka",
        "area": "Shinsaibashi",
        "ramen_type": "Tonkotsu",
        "description": (
            "Ippudo is one of Japan's most internationally recognized ramen brands, "
            "originating from Fukuoka. Their Akamaru Modern — a rich tonkotsu with "
            "miso-based paste — is the must-order. Great for tourists already familiar "
            "with Ippudo from overseas locations."
        ),
        "price_range": "¥900 – ¥1,400",
        "hours": "11:00 – 23:00",
        "address": "1-4-15 Nishi-Shinsaibashi, Chuo-ku, Osaka",
        "google_maps_url": "https://www.google.com/maps/search/Ippudo+Shinsaibashi+Osaka",
        "tags": ["tonkotsu", "tourist-friendly", "chain", "international-brand"],
    },
    {
        "id": "takoyaki-ramen-namba",
        "name": "Menya Gokkei",
        "city": "osaka",
        "area": "Namba",
        "ramen_type": "Spicy Miso",
        "description": (
            "Menya Gokkei is a local favourite in Namba known for its bold, spicy miso ramen. "
            "The broth is deep and complex with a satisfying heat. They offer spice level choices, "
            "so you can adjust to your preference. The thick noodles pair perfectly with the rich miso."
        ),
        "price_range": "¥800 – ¥1,200",
        "hours": "11:30 – 22:00",
        "address": "2-9-14 Namba, Chuo-ku, Osaka",
        "google_maps_url": "https://www.google.com/maps/search/Menya+Gokkei+Namba+Osaka",
        "tags": ["miso", "spicy", "local-favorite", "thick-noodles"],
    },
]


# ── Helper functions ──────────────────────────────────────────────────────────
# These functions let app.py fetch specific data from the list above.

def get_all_restaurants():
    """Return the full list of all restaurants."""
    return RESTAURANTS


def get_restaurants_by_city(city_name):
    """
    Return only restaurants that match the given city.
    city_name should be 'tokyo' or 'osaka' (lowercase).
    """
    # List comprehension: go through each restaurant and keep ones where city matches
    return [r for r in RESTAURANTS if r["city"] == city_name]


def get_restaurant_by_id(restaurant_id):
    """
    Return a single restaurant dict that matches the given id.
    Returns None if no match is found.
    """
    for restaurant in RESTAURANTS:
        if restaurant["id"] == restaurant_id:
            return restaurant
    return None  # Return None if nothing was found
