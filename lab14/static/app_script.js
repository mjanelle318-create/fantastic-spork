console.log("Janelle Moncrieffe")
// collect items from the form

const itemform = document.querySelector('#itemform')
// add an event to the form
itemform.addEventListener("submit", async function(event){
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value

        try{
            //await
            // fetch
            const res = await fetch("http://127.0.0.1:5000/items",   method:"POST", headers: {"Content-type":"application/json"}
                body: JSON.stringify(name: name, price: Number(price)}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             )
            )
        }
       catch(error){


       }
})