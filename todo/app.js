let todos = [];

const add = document.getElementById("add-btn");

window.addEventListener("load", () => {
  const saved = localStorage.getItem("todos");
  if (saved) {
    // json string to object 
    const parsed = JSON.parse(saved);

    todos = Array.isArray(parsed) ? parsed : Object.values(parsed);
  } else {
    todos = [];
  }
  renderTodos();
});

const saveToLocalStorage = () => {
    localStorage.setItem("todos", JSON.stringify(todos));
}

const addTodo = () => {
  const input = document.getElementById("todo-input");
  const text = input.value.trim();

  if (text === "") return alert("please enter your task");

  todos.push({
    id: Date.now(),
    text: text,
    isEditing: false,
  });
  console.log(todos);
  input.value = "";
  saveToLocalStorage()
  renderTodos();
};

const renderTodos = () => {
  const ul = document.getElementById("todo-list");
  ul.innerHTML = "";

  todos.forEach((todo) => {
    const li = document.createElement("li");
    if (todo.isEditing === true) {
      li.innerHTML = `
        <input id='edit-${todo.id}' value='${todo.text}'>
        <button onClick="saveTodo(${todo.id})">SAVE</button>
        <button onClick="cancelTodo(${todo.id})">CANCEL</button>
        `;
    } else {
       li.innerHTML = `<span>${todo.text}</span>
            <button onClick="editTodo(${todo.id})">EDIT</button>
        <button onClick="deleteTodo(${todo.id})">DELETE</button>`;
    }
    ul.appendChild(li)
  });
};

const editTodo = (id) => {
        todos = todos.map(todo => {
            todo.id === id ? {...todo, isEditing : true} : todo
        })
        saveToLocalStorage()
        renderTodos()
}

const saveTodo = (id) => {
    const input = document.getElementById(`edit-${id}`)
    const newText = input.value.trim()

    if(!newText) return

    todos = todos.map(todo => {
        todo.id === id ? {...todo, text : newText, isEditing : false} : todo
    })
    saveToLocalStorage()
    renderTodos()
}

const deleteTodo = (id) => {
    todos = todos.filter(todo => todo.id !== id)
    saveToLocalStorage()
    renderTodos()
}

add.addEventListener("click", addTodo);
