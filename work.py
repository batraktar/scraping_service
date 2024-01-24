import codecs
from bs4 import BeautifulSoup as BS

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtm1+xm1,application/xm];q=0.9,*/*;q=0.8'
           }


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua/'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='pjax-job-list')
        if main_div:
            div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_lst:
                title = div.find('h2')
                href = title.a['href']
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text,
                             'url': domain + href,
                             'description': content,
                             'company': company})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


# def rabota(url):
#     jobs = []
#     errors = []
#     domain = 'https://robota.ua'
#     resp = requests.get(url, headers=headers)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         main_div = soup.find('div', attrs={'class': 'santa-flex santa-flex-col santa-gap-y-20'})
#         if main_div:
#             div_lst = main_div.find_all('div', attrs={'class': 'santa--mb-20 ng-star-inserted santa-min-h-0'})
#             for div in div_lst:
#                 title = div.find('h2')
#                 href = title.a['href']
#                 content = div.p.text
#                 company = 'No name'
#                 logo = div.find('img')
#                 if logo:
#                     company = logo['alt']
#                 jobs.append({'title': title.text,
#                              'url': domain + href,
#                              'description': content,
#                              'company': company})
#             else:
#                 errors.append({'url': url, 'title': 'Div does not exists'})
#     else:
#         errors.append({'url': url, 'title': 'Page do not response'})
#
#     return jobs, errors
#


def dou(url):
    jobs = []
    errors = []
    # domain = 'https://www.work.ua/'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='vacancyListId')
        if main_div:
            li_lst = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_lst:
                if "__hot" not in li['class']:
                    title = li.find('div', attrs={'class': 'title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'sh-info'})
                    content = cont.text
                    company = 'No name'
                    a = title.find('a', attrs={'class': 'company'})
                    if a:
                        company = a.text
                    jobs.append({'title': title.text,
                                 'url': href,
                                 'description': content,
                                 'company': company})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://jobs.dou.ua/vacancies/?category=Python'
    jobs, errors = dou(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
