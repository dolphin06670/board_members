import requests
from bs4 import BeautifulSoup

def get_link(ticker):
    # Construct the SEC EDGAR search URL
    search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type=DEF+14A&dateb=&owner=exclude&start=0&count=40"
    
    # Make a request to the SEC EDGAR database
    response = requests.get(search_url)
    if response.status_code != 200:
        return f"Error: Unable to access SEC EDGAR database (Status code: {response.status_code})"

    soup = BeautifulSoup(response.content, 'lxml')

    # Find the link to the latest DEF 14A filing
    filing_link = None
    for link in soup.find_all('a', href=True):
        if "DEF 14A" in link.text:
            filing_link = "https://www.sec.gov" + link['href']
            break

    if not filing_link:
        return "Error: No DEF 14A filing found for the company."

    return filing_link

def get_board_members(filing_link):
    # Request the DEF 14A filing page
    response = requests.get(filing_link)
    if response.status_code != 200:
        return f"Error: Unable to access DEF 14A filing (Status code: {response.status_code})"

    soup = BeautifulSoup(response.content, 'lxml')

    # Extract board member names (this example assumes board members are listed in a specific way)
    board_members = []
    for section in soup.find_all('table'):
        if "Board of Directors" in section.text or "Director Nominees" in section.text:
            for row in section.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) > 1:
                    name = columns[0].text.strip()
                    if name and name != "Name":
                        board_members.append(name)
            break

    if not board_members:
        return "Error: No board member names found in the DEF 14A filing."

    return board_members

# Example usage
#ticker_symbol = "AAPL"  # Apple Inc.
link = "https://www.sec.gov/Archives/edgar/data/1018724/000119312520108422/d897711ddef14a.htm#toc897711_15"
board_members = get_board_members(link)
print(board_members)