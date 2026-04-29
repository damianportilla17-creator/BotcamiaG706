const form = document.getElementById("chatForm");
const input = document.getElementById("userInput");
const messages = document.getElementById("messages");
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if(!text) return;
    messages.innerHTML += `<div class="msg user">Tu: ${text}</div>`;
    input.value="";
const response = await fetch("/chat",{
    method:"POST",
    headers: {"content-Type": "application/x-www-form-urlencpded"},
    body: `message=${encodeURIComponent(text)}`
});
const data = await response.json();
messages.innerHTML += `<div class="msg bot">Bot: ${data.response}</div>`;
messages.scrollTop = messages.scrollHeight;
});