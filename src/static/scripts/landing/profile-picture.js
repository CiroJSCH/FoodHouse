const profilePicContainer = document.getElementById(
  'profile-picture-container'
);
const fileInput = document.getElementById('file-input');

profilePicContainer.addEventListener('click', () => {
  fileInput.click();
});
