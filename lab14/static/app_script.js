
// CREATE AN ITEM
document.querySelector("#itemform").addEventListener("submit", async function (e) {

    e.preventDefault();

    const name = document.querySelector("#name").value;
    const price = document.querySelector("#price").value;

    try {
        const res = await fetch("/items", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: name,
                price: Number(price)
            })
        });

        const data = await res.json();

        document.querySelector("#response").innerHTML =
            "Response: " + JSON.stringify(data);

        loaditems();

    } catch (error) {
        document.querySelector("#response").innerHTML =
            "Response: ERROR " + error;
    }
});


// LOAD ALL ITEMS
async function loaditems() {

    try {
        const res = await fetch("/items");
        const data = await res.json();

        const list = document.querySelector("#itemslist");
        list.innerHTML = "";

        for (const id in data) {

            const item = data[id];
            const li = document.createElement("li");

            li.innerHTML = `
                ID = ${id} | Name = ${item.name} | Price = ${item.price}

                <button onclick="showupdateform('${id}', '${item.name}', '${item.price}')">
                    Update
                </button>

                <button onclick="deleteitem('${id}')">
                    Delete
                </button>
            `;

            list.appendChild(li);
        }

    } catch (error) {
        document.querySelector("#response").innerHTML =
            "Error loading items: " + error;
    }
}


// SHOW UPDATE FORM
function showupdateform(id, name, price) {

    document.querySelector("#updatesection").style.display = "block";

    document.querySelector("#updateID").value = id;
    document.querySelector("#updateName").value = name;
    document.querySelector("#updatePrice").value = price;
}


// UPDATE ITEM
async function updateItem() {

    const id = document.querySelector("#updateID").value;
    const name = document.querySelector("#updateName").value;
    const price = document.querySelector("#updatePrice").value;

    try {
        const res = await fetch(`/items/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: name,
                price: Number(price)
            })
        });

        const html = await res.text();
        document.body.innerHTML = html;

    } catch (error) {
        alert("Error updating item: " + error);
    }
}


// DELETE ITEM
async function deleteitem(id) {

    try {
        const res = await fetch(`/items/${id}`, {
            method: "DELETE"
        });

        const html = await res.text();
        document.body.innerHTML = html;

    } catch (error) {
        alert("Error deleting item: " + error);
    }
}
