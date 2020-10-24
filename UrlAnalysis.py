
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
    
def main():
    abc = calculate_podcast_factor()
    for key in abc:
        print(key)
        
if __name__=="__main__":
    main()