from bs4 import BeautifulSoup
import requests
 
category = 'soft development'
url = requests.get(f'https://internshala.com/internships/{category}-internship/').text
soup = BeautifulSoup(url,'lxml')
containers = soup.find_all('div', class_= 'container-fluid individual_internship visibilityTrackerItem')
for container in containers:
    company_name = container.find('h4', class_ ='heading_6 company_name').text.replace(' ','')
    position = container.find('h3',class_ ='heading_4_5 profile').text
    location = container.find('a', class_ ='location_link view_detail_button').text
    published = container.find('div', class_ ='status-container').text
    more_info=container.div.h3.a['href']
    if 'Few' in published:
        print(f'''
              Company_name:{company_name.strip()}\n
              position:{position.strip()}\n
              Location:{location.strip()}\n
              Published:{published.strip()}\n
              More Info:{more_info.strip()}\n\n
              ''')

        

