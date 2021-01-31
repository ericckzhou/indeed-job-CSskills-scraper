from bs4 import BeautifulSoup
import requests

def find_req(description:str):
    required = []
    #you can add more requirements if needed
    #common strings employers use
    req = ['SQL', 'Java', 'Python', 'C++', 'HTML', 'CSS', 'Javascript', 'Object-oriented', 'React', 'Angular', 'XML', 
    'Linux', '.NET', 'Ruby', 'PHP', 'Android', 'iOS', 'Git', 'bash', 'Tcl', 'Perl', 'C#']
    for r in req:
        if (description.find(r) != -1):
            required.append(r)
    return required

#copy and paste the link after searching
link = str(input("Enter the link: "))
try:
    r = requests.get(link)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

html_text = requests.get(link).text
soup = BeautifulSoup(html_text, 'lxml')
job_links = soup.find_all('h2', class_='title')

job_titles = []
links = []

for job_link in job_links:
    job_title = job_link.text.strip()
    job_titles.append(job_title)
    start_index = str(job_link).find('href=')
    end_index = start_index + 7
    while (str(job_link)[end_index] != '"'):
        end_index+=1
    link = "https://ca.indeed.com" + str(job_link)[start_index + 6: end_index]
    links.append(link)

job_pages_html_text = []
job_requirements = []
for link in links:
    html_text2 = requests.get(link).text
    require = find_req(html_text2)
    job_requirements.append(require)

f = open("jobs.txt", 'w')
for i in range(0, len(links)):
    print(job_titles[i])
    print(job_requirements[i])
    #print(links[i])
    print()
    for letter in job_titles[i]:
        f.write(letter)
    f.write('\n')
    for skill in job_requirements[i]:
        f.write(skill + ', ')
    f.write('\n' + links[i] + '\n\n')
print("Check the output, jobs.txt file for your saved search!")
f.close()

