from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text #pull request to get source code as text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print('HEADLINE',headline)
    summary = article.find('div', class_='entry-content').p.text #getting the article part as text
    print('SUMMARY',summary)


    try: #avoids from an error at the output if the content doesn't have an youtube video
        video_source = article.find('iframe', class_='youtube-player')['src']  # getting youtube url
        video_id = video_source.split('/')[4]  # getting a related part with ID of the video
        video_id = video_id.split('?')[0]  # getting exact ID of the video
        yt_link = f'https://www.youtube.com/watch?v={video_id}'

    except Exception as e:
        yt_link = None

    print('YOUTUBE', yt_link)
    print()

#print(soup.prettify()) #prints formatted code of the website