## importing the required libraries
import requests
import  time
from bs4 import BeautifulSoup
## input the undesired skills
undesired_skills = 'sql'
print(f"undesired_skills is {undesired_skills}")

def get_jobdetails():
    # #get the request from url
    request=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=India').text
    ##print(request)
    soup=BeautifulSoup(request,'html.parser')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        job_date = job.find('span', class_='sim-posted').text
        if 'few' in job_date:
            job_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            job_skills=job.find('span',class_='srp-skills').text.replace(' ','')
            job_url=job.h2.a['href']
            if undesired_skills not in job_skills:
                with open(f'test-{index}.txt','w') as f:
                    f.write(f"Company Name   : {job_name.strip()}\n")
                    f.write(f"Job Url        : {job_url.strip()}\n")
                    f.write(f"Required Skills: {job_skills.strip()}")
                    print(f'file saved-{index}')


if __name__=='__main__':
    while True:
        wait_time=100
        print(f"wait time in sec {wait_time}")
        get_jobdetails()
        print(f"waiting for {wait_time} seconds")
        time.sleep(wait_time)
