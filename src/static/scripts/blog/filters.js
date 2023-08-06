const filterRecipes = () => {
  const filterCheckboxes = document.querySelectorAll('.filter-cbx');

  filterCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', function () {
      const selectedCategories = [];
      const selectedDurations = [];

      filterCheckboxes.forEach((cb) => {
        if (cb.checked) {
          const category =
            cb.getAttribute('data-category')?.charAt(0).toUpperCase() +
            cb.getAttribute('data-category')?.slice(1);
          const duration = parseInt(cb.getAttribute('data-duration'));

          category && selectedCategories.push(category);

          duration && selectedDurations.push(duration);
        }
      });

      const allRecipes = document.querySelectorAll('.recipe-card');
      allRecipes.forEach((recipe) => {
        const recipeCategories = recipe
          .getAttribute('data-categories')
          .split(', ');
        const recipeDuration = parseInt(recipe.getAttribute('data-duration'));

        const showCategory =
          selectedCategories.length === 0 ||
          selectedCategories.every((category) =>
            recipeCategories.includes(category)
          );

        const showDuration =
          selectedDurations.length === 0 ||
          selectedDurations.every((duration) => recipeDuration <= duration);

        showCategory && showDuration
          ? recipe.classList.remove('hidden')
          : recipe.classList.add('hidden');
      });
    });
  });
};

document.addEventListener('DOMContentLoaded', filterRecipes);
window.addEventListener('beforeunload', () => {
  removeFilterEvent();
});
window.addEventListener('unload', () => {
  removeFilterEvent();
});
