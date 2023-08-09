import csrfToken from './getCsrfToken.js';

const toggleLikeBtn = document.getElementById('toggle-like');
const likeCount = document.getElementById('like-count');
const recipeId = parseInt(toggleLikeBtn.dataset.recipe);

const getLikeStatus = async () => {
  const response = await fetch(
    'http://127.0.0.1:8000/blog/api/liked-recipes/',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({
        recipe_id: recipeId,
      }),
    }
  );
  const data = await response.json();
  return data;
};

const toggleLike = async (endpoint) => {
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

const updateLikeDisplay = (liked) => {
  liked
    ? toggleLikeBtn.classList.replace('bg-transparent', 'bg-emerald-200')
    : toggleLikeBtn.classList.replace('bg-emerald-200', 'bg-transparent');
};

getLikeStatus().then((data) => {
  const likedRecipes = data.liked_recipes;
  const isLiked = likedRecipes.includes(recipeId);
  updateLikeDisplay(isLiked);
});

toggleLikeBtn.removeEventListener('click', toggleLikeBtnClick);
toggleLikeBtn.addEventListener('click', toggleLikeBtnClick);

function toggleLikeBtnClick() {
  const isLiked = toggleLikeBtn.classList.contains('bg-emerald-200');
  const endpoint = isLiked ? 'unlike' : 'like';
  toggleLike(endpoint).then((response) => {
    if (response.status === 'success') {
      updateLikeDisplay(!isLiked);
      likeCount.textContent = isLiked
        ? parseInt(likeCount.textContent) - 1
        : parseInt(likeCount.textContent) + 1;
    }
  });
}
