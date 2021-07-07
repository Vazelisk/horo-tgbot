import requests
import re
from bs4 import BeautifulSoup


def data_downloader():
    result = requests.get('https://horo.mail.ru/')
    html = result.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = []
    for post in soup.find_all('a', {
                              'class': 'p-imaged-item p-imaged-item_circle p-imaged-item_rune '
                                       'p-imaged-item_shadow_inner'}):
        posts.append(str(post))

    return posts


# достаем линки для каждого знака зодиака
# сделано для каждого знака зодиака отдельно, потому что если что вдруг поменяется на сайте
# всё сразу не рухнет
def link_compiler(posts):
    links = []
    for post in posts:
        link = re.search('href="(.+?)"', post)
        link = link.group(1)
        if 'aries' in link:
            aries_link = 'https://horo.mail.ru' + link
            links.append(aries_link)
        if 'taurus' in link:
            taurus_link = 'https://horo.mail.ru' + link
            links.append(taurus_link)
        if 'gemini' in link:
            gemini_link = 'https://horo.mail.ru' + link
            links.append(gemini_link)
        if 'cancer' in link:
            cancer_link = 'https://horo.mail.ru' + link
            links.append(cancer_link)
        if 'leo' in link:
            leo_link = 'https://horo.mail.ru' + link
            links.append(leo_link)
        if 'virgo' in link:
            virgo_link = 'https://horo.mail.ru' + link
            links.append(virgo_link)
        if 'libra' in link:
            libra_link = 'https://horo.mail.ru' + link
            links.append(libra_link)
        if 'scorpio' in link:
            scorpio_link = 'https://horo.mail.ru' + link
            links.append(scorpio_link)
        if 'sagittarius' in link:
            sagittarius_link = 'https://horo.mail.ru' + link
            links.append(sagittarius_link)
        if 'capricorn' in link:
            capricorn_link = 'https://horo.mail.ru' + link
            links.append(capricorn_link)
        if 'aquarius' in link:
            aquarius_link = 'https://horo.mail.ru' + link
            links.append(aquarius_link)
        if 'pisces' in link:
            pisces_link = 'https://horo.mail.ru' + link
            links.append(pisces_link)

    return links


def get_prophecy(link):
    result = requests.get(link)
    html = result.text
    soup = BeautifulSoup(html, 'html.parser')
    post = soup.find('div', {'class': 'article__item article__item_alignment_left article__item_html'})
    match = post.prettify()
    match = cleaner(match)
    return match


def cleaner(match):
    match = re.search('<p>\n(.*)</div>', match, re.DOTALL)
    match = match.group(1)
    match = re.sub(r'[a-z<>"/=_\n]', '', match)
    match = re.sub(r'\s\s\s\s', '\n', match)
    match = re.sub(r'\s\s', '', match)
    return match


def final():
    posts = data_downloader()
    links = link_compiler(posts)
    horoscopes = {'aries': [], 'taurus': [], 'gemini': [], 'cancer': [], 'leo': [], 'virgo': [], 'libra': [],
                  'scorpio': [],
                  'sagittarius': [], 'capricorn': [], 'aquarius': [], 'pisces': []}
    for link in links:
        prophecy = get_prophecy(link)
        n = re.search('prediction/([a-z]*)/', link)
        n = n.group(1)
        horoscopes[n] = prophecy

    return horoscopes


if __name__ == '__main__':
    d = final()
