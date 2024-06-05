import asyncio

import get_url_from_website as step1
import get_data_from_website as step2
import get_board_from_data as step3

async def find_board(company):
    print(company)
    url = await step1.get_url(company) #e.g. https://www.marketscreener.com/quote/stock/TESLA-INC-6344549/
    print(url)
    url += "company" #e.g. https://www.marketscreener.com/quote/stock/TESLA-INC-6344549/company
    data = await step2.get_shareholders(url)
    print(data)
    board_members = step3.get_names(data)
    return board_members

async def main(): 
    company = "Gilead Sciences"
    result = await find_board(company)
    print(result)

asyncio.run(main())