import time
import pandas as pd # pip install pandas
# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re

sort_by_type = 'newest'

chrome_driver_path = 'selenium\chromedriver.exe'
brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
delay = 15
service = Service(executable_path=chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_argument("disable-blink-features=AutomationControlled")
# option.binary_location = brave_path

driver = webdriver.Chrome(service=service,options=option)


def extract_text(soup_obj, tag, attribute_name, attribute_value):
    txt = soup_obj.find(tag, {attribute_name: attribute_value}).text.strip() if soup_obj.find(tag, {attribute_name: attribute_value}) else ''
    return txt

rows = []

for page_number in range(251, 30)0:
    page_url = f'https://www.udemy.com/courses/development/web-development/?lang=en&p={page_number}&sort=popularity'
    driver.get(page_url)
    time.sleep(5)

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'course-list--container--3zXPS')))
    except TimeoutException:
        print('Loading exceeds delay time')
        break
    else:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        course_list = soup.find('div', {'class': 'course-list--container--3zXPS'}) # courses container
        courses = course_list.find_all('div', {'class': 'popper--popper--2r2To'}) # courses on a page
        print(len(courses))


        for course in courses:

            try:
                course_id = course.select_one('div[id]')["id"][-3:]
            except Exception:
                course_id ="error"
                continue
            if (course_id =="error"):
                course_id ="unknown"
            else:
                course_id = course.select_one('div[id]')["id"][-3:]

            try:
                course_title = course.select('h3[data-purpose*="course-title-url"]')[0].text
            except Exception:
                course_title ="error"
                continue
            if (course_title =="error"):
                course_title ="unknown"
            else:
                course_title = course.select('h3[data-purpose*="course-title-url"]')[0].text

            try:
                course_info = course.select('p[class*="course-headline"]')[0].text
            except Exception:
                course_info ="error"
                continue
            if (course_info =="error"):
                course_info ="unknown"
            else:
                course_info = course.select('p[class*="course-headline"]')[0].text

            try:
                course_url = '{0}{1}'.format("https://www.udemy.com",course.select_one('a[href]')["href"])
            except Exception:
                course_url ="error"
                continue
            if (course_url =="error"):
                course_url ="unknown"
            else:
                course_url = '{0}{1}'.format("https://www.udemy.com",course.select_one('a[href]')["href"])

            try:
                author = course.select('div[class*="course-card--instructor-list"]')[0].text
            except Exception:
                author ="error"
                continue
            if (author =="error"):
                author ="unknown"
            else:
                author = course.select('div[class*="course-card--instructor-list"]')[0].text

            try:
                price = course.select('span')[9].text[1:]
            except Exception:
                price ="error"
                continue
            if (price =="error"):
                price ="unknown"
            else:
                price = course.select('span')[9].text[1:]

            try:
                is_paid = True if course.select('span')[9].text != "FREE" else False 
            except Exception:
                is_paid ="error"
                continue
            if (is_paid =="error"):
                is_paid ="unknown"
            else:
                is_paid = True if course.select('span')[9].text != "FREE" else False 

            try:
                course_rating = extract_text(course,'span','data-purpose','rating-number')
            except Exception:
                course_rating ="error"
                continue
            if (course_rating =="error"):
                course_rating ="unknown"
            else:
                course_rating = extract_text(course,'span','data-purpose','rating-number')

            try:
                number_of_ratings = extract_text(course,'span','class','udlite-text-xs course-card--reviews-text--1yloi')[1:-1]
            except Exception:
                number_of_ratings ="error"
                continue
            if (number_of_ratings =="error"):
                number_of_ratings ="unknown"
            else:
                number_of_ratings = extract_text(course,'span','class','udlite-text-xs course-card--reviews-text--1yloi')[1:-1]
            
            try:
                course_length = course.find_all('span',{'class':'course-card--row--29Y0w'})[0].text
            except Exception:
                course_length ="error"
                continue
            if (course_length =="error"):
                course_length ="unknown"
            else:
                course_length = course.find_all('span',{'class':'course-card--row--29Y0w'})[0].text

            try:
                number_of_lectures = course.find_all('span',{'class':'course-card--row--29Y0w'})[1].text
            except Exception:
                number_of_lectures ="error"
                continue
            if (number_of_lectures =="error"):
                number_of_lectures ="unknown"
            else:
                number_of_lectures = course.find_all('span',{'class':'course-card--row--29Y0w'})[1].text
            
            try:
                difficulty_level = course.find_all('span',{'class':'course-card--row--29Y0w'})[2].text
            except Exception:
                difficulty_level ="error"
                continue
            if (difficulty_level =="error"):
                difficulty_level ="unknown"
            else:
                difficulty_level= course.find_all('span',{'class':'course-card--row--29Y0w'})[2].text
            

            driver.get(course_url)
            time.sleep(5)

            try:
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content-wrapper')))
            except TimeoutException:
                print('Loading exceeds delay time')
                break
            else:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                course_landing = soup.find('div', {'class': 'main-content-wrapper'}) # courses container

                try:
                    number_of_students = extract_text(course_landing,'div','data-purpose','enrollment')
                except Exception:
                    number_of_students ="error"
                    continue
                if (number_of_students =="error"):
                    number_of_students ="unknown"
                else:
                    number_of_students = extract_text(course_landing,'div','data-purpose','enrollment')
                
                
             # last_updated = course_landing.select('span')[25].text
            print(course_id)
            print(course_title)
            print(course_info)
            print(course_url)
            print(author)
            print(course_rating)
            print(number_of_ratings)
            print(course_length)
            print(number_of_lectures)
            print(difficulty_level)
            print(number_of_students)
            # print(last_updated)
            print(is_paid)
            print(price)
            print()

            rows.append(
                [course_id, course_title, course_info, course_url, author, course_rating, number_of_ratings, course_length, number_of_lectures, difficulty_level, number_of_students, is_paid, price]
            )

columns = ['Course ID', 'Course Title', 'Course Description','URL', 'Instructor', 'Course Rating', 'Number of Ratings', 'Course Length', 'Number of Lectures', 'Difficulty','Number of Students','Subscription Type','Price']
df = pd.DataFrame(data=rows, columns=columns)
df.to_csv('UdemyWebDev6.csv', index=False)

driver.quit()

