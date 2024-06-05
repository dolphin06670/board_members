import asyncio
from pyppeteer import launch

'''
Gets raw, unfiltered board data from a website
Given the right URl
'''
async def main():
    #url = 'https://www.marketscreener.com/quote/stock/AMAZON-COM-INC-12864605/company/'
    url = "https://www.marketscreener.com/quote/stock/TESLA-INC-6344549/company"
    content = await get_shareholders(url)
    print(content)

async def get_shareholders(url):
    browser = await launch(headless=True, executablePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    page = await browser.newPage()
    await page.goto(url)

    # Example: Extracting company description
    #await page.screenshot({'path': 'example.png'}) #Screenshots page
    '''
    content = await page.evaluate('document.body.textContent', force_expr=True)
    
    print("Content")
    print(content)
    '''
    #content = await page.content()
    try:
        content = await page.evaluate("document.body.innerText")

        flag = content.index("Members of the board") #Start of the right section
        end_flag = content.index("Share class") #End of the right section
        result = content[flag:end_flag]
    except: 
        result = None

    await browser.close()
    return result #Returns all the text in "Members of the Board" section, which includes stuff like names, but also stuff like pay

#asyncio.run(main())

