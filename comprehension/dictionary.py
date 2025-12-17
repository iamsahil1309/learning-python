tea_prices_inr = {
    "masala chai" : 40,
    "green tea" : 50,
    "lemon tea" : 200
}

tea_price_usd = {tea : price/80 for tea,price in tea_prices_inr.items()}

print(tea_price_usd)