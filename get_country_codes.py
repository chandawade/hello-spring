def get_country_codes(prices):
    p = ""
    for i in country_prices:
        if i.isalpha() or i == "," or i == " ": 
            p = p + i[0]
    return (p)