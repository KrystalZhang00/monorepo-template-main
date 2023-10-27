from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api")
def first_api():
    return {"msg": "hello_world"}


@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}


@app.get("/books/{path_param}/")
def first_apiV5(path_param: str, title: str):
    return {"msg": f"{path_param} and {title}"}


@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}


@app.put("/books/update_book/{book_id}")
def update_book(book_id: int, updated_book=Body()):
    return {"book_id": book_id, "updated_book": updated_book}


@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    return {"msg": f"Book with id {book_id} has been deleted!"}




