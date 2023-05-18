'use strict';
document.addEventListener('DOMContentLoaded', () => {
  const socket = io();
  // console.log(socket)
  const messageContainer = document.getElementById('message-container');
  // console.log(messageContainer)
  const messageInput = document.getElementById('message-input');
  // console.log(messageInput)
  const sendButton = document.getElementById('send-button');
  // console.log(sendButton)

  // console.log('nitto')
  sendButton.addEventListener('click', () => {
    const message = messageInput.value;   // 入力されたメッセージを取得
    socket.emit('message', message);      // サーバーにメッセージを送信
    messageInput.value='';                // 入力欄をクリア
  });

  socket.on('message', (message) => {
    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    messageContainer.appendChild(newMessage);
  })
});