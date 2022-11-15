from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for name, properties in melons.items():
        print(name.upper())
        for property, value in properties.items():
            print(f"{property}: {value}")

print_melon(melons)


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
