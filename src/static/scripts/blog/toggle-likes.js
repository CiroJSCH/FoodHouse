import csrfToken from './getCsrfToken.js';

const toggleLikeBtn = document.getElementById('toggle-like');
const likeCount = document.getElementById('like-count');

const userLikedRecipes = async () => {
  const response = await fetch('http://127.0.0.1:8000/blog/api/liked-recipes/');
  const data = await response.json();
  return data;
};

const updateLike = (data) => {
  const likedRecipes = data.liked_recipes;
  const recipeId = parseInt(toggleLikeBtn.dataset.recipe);
  if (likedRecipes.includes(recipeId)) {
    toggleLikeBtn.classList.replace('bg-transparent', 'bg-emerald-200');
    toggleLikeBtn.removeEventListener('click', toggleLike);
    toggleLikeBtn.addEventListener('click', async () => {
      const response = await toggleLike(recipeId, 'unlike');
      if (response.status === 'success') {
        userLikedRecipes().then(updateLike);
      }
    });
  } else {
    toggleLikeBtn.classList.replace('bg-emerald-200', 'bg-transparent');
    toggleLikeBtn.removeEventListener('click', toggleLike);
    toggleLikeBtn.addEventListener('click', async () => {
      const response = await toggleLike(recipeId, 'like');
      if (response.status === 'success') {
        userLikedRecipes().then(updateLike);
      }
    });
  }
  likeCount.textContent = data.total;
};

const _ = userLikedRecipes().then(updateLike);

const toggleLike = async (recipeId, endpoint) => {
  const response = await fetch(`http://127.0.0.1:8000/blog/api/${endpoint}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',
    body: JSON.stringify({
      recipe_id: recipeId,
    }),
  });

  const data = await response.json();
  return data;
};
