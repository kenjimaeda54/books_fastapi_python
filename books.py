from email.policy import default
from typing import Dict, Literal, List, Optional

from fastapi import FastAPI, Body
import uvicorn


app = FastAPI()




BOOKS = [
    {"title": "Title One","author": "Author One","category": "science"},
    {"title": "Title Two","author": "Author Two","category": "math"},
    {"title": "Title Three","author": "Author Three","category": "portugues"},
    {"title": "Title Four","author": "Author Four","category": "english"},
    {"title": "Title Five","author": "Author One","category": "science"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS




@app.get("/books/{title}")
async def read_only_book(title: str):
    for book in BOOKS:
        #casefold é para comparar  e como se fosse um lowercase mais agressivo
        if book.get("title").casefold() == title.casefold():
            return book

#tem que ser dessa maneira o / porque ja temos acima o {title}
@app.get("/books/{book_author}/")
async def read_books_by_author_and_category(book_author: str,category: str):
    return_book = []
    for book in BOOKS:
        if book.get("author").casefold() ==  book_author.casefold() and \
              book.get("category").casefold() == category.casefold():
               return_book.append(book)
    return return_book


@app.post("/books")
async  def create_book(new_book=Body()):
     BOOKS.append(new_book)

@app.put("/books")
async def update_book(new_book=Body()):
    #vai criar uma seguencia no range() 0 ate a quantiade de BOOKS
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == new_book.get("title").casefold():
            BOOKS[i] = new_book

@app.delete("/books/{title_book}")
async def delete_book(title_book: str):
     for i in range(len(BOOKS)):
         if BOOKS[i].get("title").casefold() == title_book.casefold():
             BOOKS.remove(BOOKS[i])
             break

@app.get("/books/get_all/{name_author}")
async def read_all_by_author(name_author: str):
    return_book = []
    for book in BOOKS:
        if book.get("author").casefold() == name_author.casefold():
            return_book.append(book)
    return return_book


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)