import asyncio
from pyppeteer import launch

async def main():
    try:
    # Launch the browser
        browser = await launch(headless=False, executablePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        page = await browser.newPage()

        # Navigate to the Marketscreener website
        await page.goto('https://www.marketscreener.com/')

        # Wait for the search bar to load
        await page.waitForSelector('#autocomplete')

        print("Got here")
        # Type 'Tesla' into the search bar and press Enter
        await page.type("#autocomplete", 'Tesla')
        await page.keyboard.press('Enter')

        # Wait for the search results to load
        #await page.waitForSelector('a[href*="/quote/stock/"]')
        await page.waitForSelector("#instrumentSearchTable")

        # Get the link of the first search result
        first_result = await page.querySelector('#instrumentSearchTable a[href*="/quote/stock/"]')
        link = await page.evaluate('(element) => element.href', first_result)
        print("First search result link:", link)

        # Close the browser
        await browser.close()
        print("Done")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
asyncio.run(main())