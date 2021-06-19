# Python Packages
import requests
import bs4


class Answer:

    def __init__(self, text):
        self.text = text


class Question:

    def __init__(self, div):
        self.answers = [Answer(span.text.strip()) for span in div.find_all('span') if
                        ('class' in span.attrs and 'label-text' in str(span))]


class Survey:

    def __init__(self):
        self._url = r'https://www.surveymonkey.ca/r/FKJ5KJK'
        response = requests.get(self._url)
        soup = bs4.BeautifulSoup(response.content)
        self.questions = [Question(div) for div in soup.find_all('div', attrs={'class': 'question-row'})]


if __name__ == '__main__':
    s = Survey()
    print('set break')
