let myLibrary = [];

function Book(title, author, pages, read) {
  this.id = crypto.randomUUID();
  this.title = title;
  this.author = author;
  this.pages = pages;
  this.read = read;
}

Book.prototype.toggle = function () {
  this.read = !this.read;
};

function addBookToLibrary(title, author, pages, read) {
  const newBook = new Book(title, author, pages, read);
  myLibrary.push(newBook);
}

function displayLibrary() {
  const libraryDiv = document.getElementById("library");
  libraryDiv.innerHTML = "";

  myLibrary.forEach((book) => {
    const card = document.createElement("div");
    card.classList.add("book-card");
    card.dataset.id = book.id;

    card.innerHTML = `
      <h3>${book.title}</h3>
      <p>Author: ${book.author}</p>
      <p>Pages: ${book.pages}</p>
      <p>Status: ${book.read ? "Read" : "Not read"}</p>
      <button class="toggle-read">Toggle Read</button>
      <button class="remove-book">Remove</button>
    `;

    libraryDiv.appendChild(card);
  });
}

document.getElementById("library").addEventListener("click", (e) => {
  const card = e.target.closest(".book-card");
  console.log(card)
  if (!card) return;

  const bookId = card.dataset.id;
  const book = myLibrary.find((b) => b.id === bookId);

  if (e.target.classList.contains("remove-book")) {
    myLibrary = myLibrary.filter((b) => b.id !== bookId);
    displayLibrary();
  }

  if (e.target.classList.contains("toggle-read")) {
    book.toggle();
    displayLibrary();
  }
});

// add books
const form = document.getElementById("bookForm");
const newBookBtn = document.getElementById("newBookBtn");

newBookBtn.addEventListener("click", () => {
  form.hidden = !form.hidden;
});

form.addEventListener("submit", (e) => {
  e.preventDefault(); // prevent page reload

  const title = document.getElementById("title").value;
  const author = document.getElementById("author").value;
  const pages = document.getElementById("pages").value;
  const read = document.getElementById("read").checked;

  addBookToLibrary(title, author, pages, read);
  displayLibrary();

  form.reset();
  form.hidden = true;
});

addBookToLibrary("The Hobbit", "J.R.R. Tolkien", 295, true);
addBookToLibrary("1984", "George Orwell", 328, false);
displayLibrary();
