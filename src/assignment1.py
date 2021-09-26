from pycoingecko import CoinGeckoAPI 
def cryptoTop():   #function which will give 'n' numbers of cryptocurrency ordered by coingecko website top
    cg = CoinGeckoAPI()
    n=input()
    num=int(n)
    case1=cg.get_coins_markets(vs_currency= "usd", per_page=num)#var will take a list of dictionaries
    #ALAN XYI EBANIY
    for x in range(num):#loop will print a n number of cryptocurrency
        print(case1[x].get("name"))

