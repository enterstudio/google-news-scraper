from utils import get_articles

if __name__ == '__main__':
    # https://news.google.co.jp
    # https://news.google.com/?output=rss&hl=fr
    # RSS Feed does not work for Japanese language.
    get_articles('Toyota')
