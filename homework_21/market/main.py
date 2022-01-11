from market import Market

if __name__ == '__main__':
    # E.g.
    market = Market()
    apple = market.search_product()
    print(apple)
    print(apple.calculate_food_energy(2))
