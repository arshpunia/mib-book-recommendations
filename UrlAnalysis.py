import requests


def calculate_podcast_factor():
    pod_fac = {}
    with open('MoreLinks.txt','r') as m:
        more_urls = m.readlines()
        ##print(more_urls)
        for url in more_urls:
            url = url.strip('\n')
            if url in pod_fac:
                pod_fac[url] = pod_fac[url]+1
            else:
                pod_fac[url] = 1
    return pod_fac

def get_authors(isbn_code):
    api_endpoint = 'https://openlibrary.org/api/books?bibkeys=ISBN:'+isbn_code+'&jscmd=data&format=json'
    
    res = requests.get(api_endpoint)
    
    book_authors_list = res.json()['ISBN:'+isbn_code]['authors']
    authors_list = []
    for author in book_authors_list:
        authors_list.append(author['name'])
    
    return authors_list
    
def get_book_title(isbn_code):
    api_endpoint = 'https://openlibrary.org/api/books?bibkeys=ISBN:'+isbn_code+'&jscmd=data&format=json'
    
    res = requests.get(api_endpoint)
    print(str(res))
    print(str(res.json()))
    
    if 'subtitle' in res.json()['ISBN:'+isbn_code]:
        book_title = res.json()['ISBN:'+isbn_code]['title']+': '+res.json()['ISBN:'+isbn_code]['subtitle']
    else:
        book_title = res.json()['ISBN:'+isbn_code]['title']
        
    print(str(book_title))

def bla():
    with open('AmazonLinks.txt','r') as f:
        isbn_lines = f.readlines()
        for line in isbn_lines:
            
            isbn = line[0:10].strip('\n')
            print(str(isbn))
            authors_list = get_authors(isbn)
            print(line[10:]+'\t'+str(authors_list))

def main():
    """
    abc = calculate_podcast_factor()
    with open('BookList.txt','w') as f:
        for key in abc:
            f.write(key+'\n')
    """
    ##get_book_title('038535147X')
    bla()
    
if __name__=="__main__":
    main()