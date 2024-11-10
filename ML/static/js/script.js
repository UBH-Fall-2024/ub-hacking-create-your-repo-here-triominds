document.getElementById("send-btn").addEventListener("click", function() {
  const userInput = document.getElementById("user-input").value;

  // Send a POST request to the /chat endpoint
  fetch("/chat", {
    method: "POST",  // Ensure POST is used, not GET
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ messageText: userInput })  // Send the user input as JSON
  })
  .then(response => response.json())
  .then(data => {
    const chatBox = document.getElementById("chat-box");
    const userMessage = `<div class="user-msg">${userInput}</div>`;
    const botReply = `<div class="bot-msg">${data.answer}</div>`;
    chatBox.innerHTML += userMessage + botReply;
    document.getElementById("user-input").value = "";  // Clear input field after sending
  })
  .catch(error => console.error("Error:", error));
});
