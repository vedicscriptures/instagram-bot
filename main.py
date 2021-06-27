# slok=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
# for ch in range(1,19):
#     for sl in range(1,1+slok[ch-1]): 
#           print(f'curl "https://bhagavadgitaapi.in/gita.svg?api_key={{apikey}}&ch={ch}&sl={sl}" -o "BG_{ch}_{sl}.svg"')

import asyncio
from pyppeteer import launch

async def main(ch,sl):
    browser = await launch()
    page = await browser.newPage()
    with open(f'input/BG_{ch}_{sl}.svg','r') as file:
        contentHtml = file.read()
        await page.setContent(contentHtml)
        await page.screenshot({'path': f'output/BG_{ch}_{sl}.png', 'clip': {'x': 0, 'y': -25, 'width': 640, 'height': 640}})
        await browser.close()

#5.28,5.29
slok=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
# for ch in range(1,19):
#     for sl in range(1,1+slok[ch-1]): 
#         asyncio.get_event_loop().run_until_complete(main(ch,sl))
asyncio.get_event_loop().run_until_complete(main(5,29))
