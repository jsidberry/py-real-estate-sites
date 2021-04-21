from lxml import html
import requests
import wget
import bs4
import pprint as pp
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import urllib3
import re


def brute_force():
    # This is the image url.
    image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open('local_image.jpg', 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp


def beauty_soup(url):
    r = requests.request('GET', url)
    response = requests.get(url)
    # html_page = urllib3.urlopen(url)
    html = r.content
    h = r.text
    print(r)
    print(h)

    # print(html_page)

    soup = bs4.BeautifulSoup(html, "html.parser")

    # # this will return src attrib from img tag that is inside 'a' tag
    # soup.a.img['src']

    # # if you have more then one 'a' tag
    # for a in soup.find_all('a'):
    #     if a.img:
    #         print(a.img['src'])

    # images = soup.find_all('img')

def loop_thru_images(url):
    for i in range(40):
        img_url = url + str(i)
        print(img_url)
        # local_image_filename = wget.download(img_url)
        wget.download(img_url)


# initial_url = 'https://www.zillow.com/homedetails/14121-Rhone-Valley-Dr-Charlotte-NC-28278/80464594_zpid/?mmlb=g,0'
# base_url = initial_url[:-1]
# base_url = 'https://www.zillow.com/homedetails/14121-Rhone-Valley-Dr-Charlotte-NC-28278/80464594_zpid/?'

# # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)

# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# print('Buyers: ', buyers)
# print()
# print('Prices: ', prices)

# for i in range(36):
#     # print(i)
#     url = base_url + str(i)
#     # print(url)
#     print(url)
#     page = requests.get(url, stream=True)



# zpage = requests.get('')

# local_image_filename = wget.download(image_url)

# beauty_soup(base_url)
# loop_thru_images(base_url)
# wget.download(initial_url)

# for i in range(34):
#     print(i)
#     initial_url = 'https://www.zillow.com/homedetails/14121-Rhone-Valley-Dr-Charlotte-NC-28278/80464594_zpid/?mmlb=g,' + str(i)


def save_html_to_file(html_content, pg_num):
    html_path = '/Users/juans/Pictures/zillow/homepic_' + str(pg_num) + '.html' 
    with open(html_path, 'w') as html_file:
        html_file.write(html_content)
    return html_path


def put_lines_into_list(file):
    list_of_lines = []
    for line in file:
        stripped_line = line.strip()
        list_of_lines.append(stripped_line)
    return list_of_lines


def get_lines_with_jpg(file_list):
    x = 1
    new_list = []
    for item in file_list:
        if 'jpg' in item:
            new_list.append(item)
            print('\n', str(x), item)
            x += 1
    return new_list


def filter_for_jpg_url(file_list):
    x = 1
    urls = []

    # Get the URLs for the 600x pics
    for item in file_list:
        data_src_url = re.search(r'data-src(.*)jpg', item)
        if data_src_url is not None:
            tmp_results = re.search(r'//cdn(.*)600x.jpg', data_src_url.group())
            if tmp_results is not None:
                # print('\n', str(x), tmp_results.group())
                url_600x = 'http:' + tmp_results.group()
                # print(url_600x)
                urls.append(url_600x)
                x += 1

    return urls

def get_html_content(url):
    page = requests.get(url)
    if page.status_code == 200:
        content = page.text
    return content


def get_image_urls(url):
    image_url_list = []
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        # # jpgs = soup.find_all('a', {'class': 'productImage', 'href': True}) # old
        jpgs = soup.find_all('div')#, {'class': 'image'})#.find_all('source', alt="" ,src=re.compile(".jpg"))
        print(jpgs, '\n')
        # # srcs = [tag['src'] for tag in soup.select('picture[src]')]
        # print(jpgs)
    #     jpgs = soup.find_all('class')
    #     picture = html.fromstring(url)
    #     img_link = picture.xpath('/html/body/div[9]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[5]/div[1]/div/picture/source[2]')
    #     print(img_link)
    #     # for jpg in jpgs:
    #     #     # jpg_url = 'https:' + jpg['data-href']
    #     #     print(jpg.img['srcset'])
    #         # image_url_list.append(jpg_url[:-13])

    # return image_url_list
	# //*[@id="gallery"]/div/div/div/div/div[1]/div/div/picture/img
    # /html/body/div[9]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[5]/div[1]/div/picture/source[2]

    
if __name__ == '__main__':
    base_link = 'https://www.zillow.com/homes/1045-Leadenhall-St-Johns-Creek,-GA,-30022_rb/35817032_zpid/?mmlb=g,'
    # base_link = 'https://www.zillow.com/homedetails/14121-Rhone-Valley-Dr-Charlotte-NC-28278/80464594_zpid/?mmlb=g,'

    for page_number in range(3):
        page_url = base_link + str(page_number)
        # print(page_url)
        # page = requests.get(page_url)
        page = get_image_urls(page_url)
        # content = page.text
        # html_file_path = save_html_to_file(content, page_number)
        # with open(html_file_path, "r") as a_file:
        #     file_list = put_lines_into_list(a_file)
        #     jpg_list = get_lines_with_jpg(file_list)
        #     # url_list = filter_for_jpg_url(jpg_list)
        #     # wget_images(url_list)

    print('\n DONE!')

