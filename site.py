import sys
from playwright.sync_api import Playwright, sync_playwright

if __name__ == "__main__":
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        number
        url = str(sys.argv[2])
        url
    else:
        print("No number received from Flask.")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    for _ in range(number):
        page.goto(url)
        page.wait_for_timeout(1000)

    context.close()
    browser.close()
    
with sync_playwright() as playwright:
    run(playwright)
