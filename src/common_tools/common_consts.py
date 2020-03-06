WAIT_GET = 2
WAIT_FORBIDEN = 120
DAY_SECONDS = 86400

# Wikipedia links
WIKI = 'https://uk.wikipedia.org'
WIKI_URL = WIKI + '/wiki/' +\
        '%D0%92%D1%82%D1%80%D0%B0%D1%82%D0%B8_%D1%81%D0%B8%D0%BB%D0%BE%D0%B2' +\
        '%D0%B8%D1%85_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80_%D0%B' +\
        '2%D0%BD%D0%B0%D1%81%D0%BB%D1%96%D0%B4%D0%BE%D0%BA_%D1%80%D0%BE%D1%8' +\
        '1%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B2%D1%82%D0%B' +\
        'E%D1%80%D0%B3%D0%BD%D0%B5%D0%BD%D0%BD%D1%8F_%D0%B2_%D0%A3%D0%BA%D1%' +\
        '80%D0%B0%D1%97%D0%BD%D1%83'
# Wikipedia locators
LINK_LOCATOR = '//li/b/a[contains(@title,"Втрати силових структур внаслідок ' +\
        'російського вторгнення в Україну")]'
WIKI_UKR_DEFENDER_KILLED_DATE_LOCATOR = \
        '//table/tbody/tr/td[5]/span[@style="display:none"]'
# storage
WIKI_UKR_DEFENDER_KILLED_DATE_PATH = '/home/vasylvovk/Documents/war_words/src/results/killed_defenders.json'

# Kremlin.ru links
KREMLIN_BASE_URL = 'http://kremlin.ru'
# day - 2 digit, month - 2 digit, year - 4 digit
BY_DATE_URL = '/acts/news/by-date/{day}.{month}.{year}'
# Kremlin.ru locators
MARK = 'bookmark'
ARIA_LABEL = 'Материал для чтения'
document_link_locator = '//div[@class="hentry h-entry hentry_event hentry_doc"]//a'
base_locator = '//article[@class="read__in hentry h-entry"]'
header_locator = '//h1'
date_locator = '//time[@class="read__published"]'
time_locator = '//div[@class="read__time"]'
content_description_locator = \
        '//div[@class="read__lead entry-summary p-summary"]/div/p'
content_locator = \
        '//div[@class="entry-content e-content read__internal_content"]/p'
# storages
KREMLIN_LINKS_PATH = '/home/vasylvovk/Documents/war_words/src/results/kremlin_links.json'
KREMLIN_CONTENT_PATH = '/home/vasylvovk/Documents/war_words/src/results/kremlin_data.json'
