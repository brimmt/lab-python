const button = document.querySelector(".box .submit");

button.addEventListener('click', (event) => {
    event.preventDefault();

button.textContent = "Loading";
setTimeout(() => {
    button.textContent = "Submit";
    alert("Form Submitted!")}, 2000);
});


 // Connect to FastAPI

 const form = document.getElementById("registerForm");

 form.addEventListener("submit", async(event) => {
    event.preventDefault();
 
 

 // This is how you grab input values

 const username = document.getElementById("username").value;
 const age = document.getElementById('age').value;
 const email = document.getElementById('email').value;

 try{
    const response = await fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: {
            "Content-Type" : "application/json",
        },
        body: JSON.stringify({username, age: Number(age), email}), });

        if(!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
            return;
        }
       const data = await response.json();
    alert(`User created! ID: ${data.id}, Username: ${data.username}`);
  } catch (error) {
    console.error("Error:", error);
    alert("Something went wrong. Check the console for details.");
  }
    });


 