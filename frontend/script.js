let currentRole = "general";

function setRole(role) {
    currentRole = role;
    alert("Role set to: " + role);
}

async function sendMessage() {
    let input = document.getElementById("message");
    let message = input.value;

    if (message.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Show user message
    chatbox.innerHTML += `<div class="message user">You: ${message}</div>`;

    input.value = "";

    // API Call
    let response = await fetch("https://simple-chatbot-python-fastapi-render.onrender.com/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            role: currentRole,
            message: message
        })
    });

    let data = await response.json();

    // Show bot response
    chatbox.innerHTML += `<div class="message bot">Bot: ${data.response}</div>`;

    // Auto scroll
    chatbox.scrollTop = chatbox.scrollHeight;
}