from bs4 import BeautifulSoup
import requests
 

url = requests.get('https://internshala.com/internships/work-from-home-internships/').text
soup = BeautifulSoup(url,'lxml')
containers = soup.find_all('div', class_= 'container-fluid individual_internship visibilityTrackerItem')
for index,container in enumerate(containers):
    company_name = container.find('h4', class_ ='heading_6 company_name').text.replace(' ','')
    position = container.find('h3',class_ ='heading_4_5 profile').text
    location = container.find('a', class_ ='location_link view_detail_button').text
    published = container.find('div', class_ ='status-container').text
    more_info=container.div.h3.a['href']
    if 'Few' in published:
        with open(f'intern/{index}.txt','w') as f:
            f.write(f'Company Name: {company_name.strip()}\n')
            f.write(f'Position: {position.strip()}\n')
            f.write(f'Location: {location.strip()}\n')
            f.write(f'Published: {published.strip()}\n')
            f.write(f'More Details: {more_info.strip()}\n')
            print(f'File saved: {index}')
        

