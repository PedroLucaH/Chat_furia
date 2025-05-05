const socket = io();

const inputUser = document.getElementById('username');
const inputMsg = document.getElementById('message-input');

inputMsg.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const msg = inputMsg.value.trim();
        const user = inputUser.value.trim() || 'Anônimo';

        if (msg) {
            socket.send({ user, msg });
            inputMsg.value = '';
        }
    }
});

socket.on('message', function (data) {
    const messages = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${data.user}:</strong> ${data.msg.replace(/\n/g, '<br>')}`;
    messages.appendChild(messageElement);
    messages.scrollTop = messages.scrollHeight;
});
