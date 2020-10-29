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

def look_up_isbn(isbn_code):
    api_endpoint = 'https://openlibrary.org/api/books?bibkeys=ISBN:'+isbn_code+'&jscmd=data&format=json'
    
    res = requests.get(api_endpoint)
    json_rep = res.json()['ISBN:'+isbn_code]['title']
    print(str(json_rep))
    
def main():
    """
    abc = calculate_podcast_factor()
    with open('BookList.txt','w') as f:
        for key in abc:
            f.write(key+'\n')
    """
    look_up_isbn('0385545800')
    
if __name__=="__main__":
    main()