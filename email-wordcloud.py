import configparser
from imap_tools import MailBox, AND
from lxml.html.clean import clean_html
from wordcloud import WordCloud, STOPWORDS

config = configparser.ConfigParser()
config.read('config.ini')

def main():
    with MailBox(config['DEFAULT']['imap_url']).login(config['DEFAULT']['username'], config['DEFAULT']['password'], initial_folder=config['DEFAULT']['folder']) as mailbox:
        body = [msg.text or msg.html for msg in mailbox.fetch()]
        string_body = ",".join(str(x) for x in body)
        cleaned_body = remove_html_tags(clean_html(string_body))

    with open("results.txt", "w") as results:
        results.write(cleaned_body)

    wordcloud = WordCloud(stopwords=STOPWORDS).generate(cleaned_body)
    wordcloud.to_file('cloud-results.png')

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

if __name__ == '__main__':
    main()