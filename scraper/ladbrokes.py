from scraper.base import get_driver, wait_for_element, human_sleep, scroll_down
from bs4 import BeautifulSoup

def scrape_ladbrokes():
    driver = get_driver()
    URL = "https://www.ladbrokes.com.au/sports/darts" #choose sport to scrape
    driver.get(URL)

    wait_for_element(driver, ".price-button-odds-price") #adjust selector later

    # scroll down a few times to combat lazy loading
    for _ in range(5):
        scroll_down(driver, 600)

    human_sleep(1,2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract events
    events = []
    for event_div in soup.select("div.cursor-pointer.flex-col.bg-system-secondary"):
        first_team = event_div.select_one(".flex-shrink.truncate")
        second_team = event_div.select_one(".flex-shrink.truncate.text-center")

        if not first_team or not second_team:
            continue

        teams = f"{first_team.text.strip()} vs {second_team.text.strip()}"

        odds_elements = event_div.select("span[data-testid='price-button-odds']")
        odds = []
        for odd in odds_elements:
            try:
                odds.append(float(odd.text.strip()))
            except ValueError:
                continue
        
        events.append({
            "bookie": "Ladbrokes",
            "teams": teams,
            "odds": odds
        })

    return events