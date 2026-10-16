import requests
from bs4 import BeautifulSoup
import csv

#url of main page and main_page_soup
main_page_url = "https://books.toscrape.com/"
main_page_response = requests.get(main_page_url).text
main_page_soup = BeautifulSoup(main_page_response, "lxml");

#list with original topic titles
themes = main_page_soup.find("ul", class_="nav nav-list")
old_themes_list = []
for name in themes.find_all("a"):
    text_cleaned = name.text.strip()
    if text_cleaned and text_cleaned != "Books":
        old_themes_list.append(text_cleaned)

#a list with topics modified for search purposes
item_counter = 2
themes_list = []
for item in old_themes_list:
    item = item.lower().replace(' ', '-')
    item += f"_{item_counter}"
    themes_list.append(item)
    item_counter += 1

#main program loop
answer = ""
while True:
    #choosing a topic
    print("------------------------------------------------------------------ALL TOPICS OF BOOKS------------------------------------------------------------------")
    for item in themes_list:
        print(f"{item},  ", end=' ')
    print()
    print("Enter the topic or (type everything u want for leave(no book name from list!)): ")
    answer = input()
    if answer not in themes_list:
        break

    #creating a new URL and a BeautifulSoup class object
    url = f"https://books.toscrape.com/catalogue/category/books/{answer}/index.html"
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "lxml")

    #calculating the maximum possible number of books on a chosen topic
    pages_li_item = soup.find("li", class_="current")
    total_pages = 1
    if pages_li_item is not None:
        pages_count_string = pages_li_item.text
        words = pages_count_string.split()
        total_pages = int(words[-1])

    total_books_count = 0
    if total_pages > 1:
        #only count the books on the last page, since there are always 20 on all the others.
        last_page_url = f"https://books.toscrape.com/catalogue/category/books/{answer}/page-{total_pages}.html"
        last_page_responce = requests.get(last_page_url).text
        last_page_soup = BeautifulSoup(last_page_responce, "lxml")
        books_elements = last_page_soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        total_books_count = len(books_elements)
        total_pages -= 1
        for i in range(total_pages):
            total_books_count += 20
    else:
        books_elements = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        total_books_count = len(books_elements)

    print()
    print(f"How many books do you want to parse? (min: 1, max: {total_books_count}): ")
    books_count = 0
    while True:
        books_count = int(input())
        if books_count < 1 or books_count > total_books_count:
            print("The number of books cannot be less than 1 or greater than the total quantity!")
            continue
        else:
            break


    #a main algorithm for parsing books and saving them to a .txt file
    #list of all books
    book_info_list = []
    if (books_count <= 20):
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        books_need = all_books[:books_count]
        for book in books_need:
            #title of book
            title = book.find("h3").find("a")["title"]
            #price of book
            chars_price = book.find("p", class_="price_color").text
            price_ready = chars_price[1:].replace('.', ',') + "£"
            #availability of book
            availability = book.find("p", class_="instock availability").text.strip()
            #dictionary for 1 book
            book_info = {
                "title": title,
                "price": price_ready,
                "availability": availability
            }
            book_info_list.append(book_info)
    else:
        current_page = 1
    
        while len(book_info_list) < books_count:
            new_url = f"https://books.toscrape.com/catalogue/category/books/{answer}/page-{current_page}.html"
            new_response = requests.get(new_url)
            new_response.encoding = 'utf-8'
            new_soup = BeautifulSoup(new_response.text, "lxml")

            all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

            for book in all_books:
                if len(book_info_list) >= books_count:
                    break

                title = book.find("h3").find("a")["title"]
                chars_price = book.find("p", class_="price_color").text
                price_ready = chars_price[1:].replace('.', ',') + "£"
                availability = book.find("p", class_="instock availability").text.strip()

                book_info = {
                    "title": title,
                    "price": price_ready,
                    "availability": availability
                }
                book_info_list.append(book_info)

                current_page += 1

    #writing to a .csv file for easy reading
    columns = ["title", "price", "availability"]
    state_flag = True
    try:
        with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=columns, delimiter=";")
            writer.writeheader()
            writer.writerows(book_info_list)
    except PermissionError:
        print("\n")
        print("ERROR. Close all programs that have a .csv file open!")
        print("\n")
        state_flag = False
    if (state_flag):
        print("All data has been hastily recorded!")
        print("\n")