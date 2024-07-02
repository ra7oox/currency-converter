conversion_rates = {
    "USD": 1.0,
    "EUR": 1.08,
    "GBP": 0.75,
    "INR": 73.0,
    "JPY": 110.0,
    "AUD": 1.35,
    "CAD": 1.45,
    "CNY": 6.45,
    "BRL": 5.25,
    "MAD":10
}
def main():
    currency_input=str(input("enter the currency:")).upper()

    amount_input=float(input("enter the amount:"))
    currency_convert_input=str(input("enter the currency you want to conver to it:")).upper()


    if currency_input in conversion_rates or currency_convert_input in conversion_rates:
        res=conversion_rates[currency_input]*amount_input
        print(f"the result is {res*conversion_rates[currency_convert_input]} {currency_convert_input}")
    
    else:
        print("error")
        
if __name__=="__main__":
    main()