# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def get_links_from_urls(urls):
#     all_links = []
#     response = requests.get(urls)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for link in soup.find_all('a'):
#         path = link.get('href')
#         if path and path.startswith('/'):
#             path = urljoin(urls, path)
        
#         all_links.append(path)

# #     check_content(all_links)

# # def check_content(all_links):
#     if all_links is None:
#         print("Error: all_links is None")
#         return
    
#     for link in all_links:
#         if link is None or "#" in link:
#             continue
            
#         response = requests.get(link)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         for judul in soup.find_all('p'):
#             text = judul.text.strip()
#             # value.append(text)
#             print(text)
#             break
#         return text
 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links_from_urls(urls):
    all_links = []
    response = requests.get(urls)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/'):
            path = urljoin(urls, path)
        
        all_links.append(path)

    # Check content from the collected links
    return check_content(all_links)

def check_content(all_links):
    if not all_links:
        print("Error: No links found")
        return "Error: No links found"
    
    all_text = []
    for link in all_links:
        if link is None or "#" in link:
            continue
            
        try:
            response = requests.get(link)
            response.raise_for_status()  # Ensure we notice bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = " ".join([p.text.strip() for p in soup.find_all('p')])
            all_text.append(page_text)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {link}: {e}")
            continue
    
    return "\n\n".join(all_text) if all_text else "No text found"



def get_links_from_url_singel_page(urls):
    all_text = []

    try:
        response = requests.get(urls)
        response.raise_for_status()  # Ensure we notice bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = " ".join([p.text.strip() for p in soup.find_all('p')])
        all_text.append(page_text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {urls}: {e}")
        
    
    return "\n\n".join(all_text) if all_text else "No text found"

