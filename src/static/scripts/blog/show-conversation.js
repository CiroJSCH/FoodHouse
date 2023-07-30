const currentConversation = document.getElementById('current-conversation');

const urlParams = new URLSearchParams(window.location.search);
const conversationId = urlParams.get('conversation');

if (conversationId) {
  currentConversation.classList.toggle('hidden');
}
