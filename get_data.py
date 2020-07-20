import os
import requests
import bs4
from urllib.request import urlretrieve



""" file locations and tools for getting required data """

RATINGS_DATA_PATH = "\\Users\\eanor\\Downloads\\all_csv_files.csv"
METADATA_FOLDER = "\\Users\\eanor\\Downloads"
SAMPLE_EXPENSES_PATH = "\\Users\\eanor\\Documents\\recommender-for-spending-categories\\sample_expenses_relabeled"



""" scraping metadata """

AMAZON_REVIEWS_URL = "http://deepyeti.ucsd.edu/jianmo/amazon/index.html"
METADATA_DESTINATION_FOLDER = "\\Users\\eanor\\Downloads"

def get_metadata_urls():
    resp = requests.get(AMAZON_REVIEWS_URL)
    assert(resp.status_code == 200)
    soup = bs4.BeautifulSoup(resp.text, features="lxml")
    table = soup.table
    split_rows = (
        row.find_all('td')
        for row
        in table.find_all('tr')
    )
    return {
        name_td.text: metadata_td.a['href']
        for name_td, reviews_td, metadata_td
        in split_rows
    }

def get_metadata(categories=None, except_categories=None):

    metadata_urls = get_metadata_urls()

    if categories is None:
        categories = metadata_urls.keys()
    
    if except_categories is None:
        except_categories = []

    for category, url in metadata_urls.items():
        if category in categories and category not in except_categories:
            filename = url.split('/')[-1]
            print(f"Downloading {filename}...")
            urlretrieve(url, os.path.join(METADATA_DESTINATION_FOLDER, filename))



if __name__ == "__main__":
    get_metadata(["Magazine Subscriptions"])