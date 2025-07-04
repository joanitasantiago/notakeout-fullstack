import { Outlet } from 'react-router-dom';

function RecipesPage() {
  return (
    <div className="container">
      <h2>Minhas receitas</h2>
      <Outlet />
    </div>
  );
}

export default RecipesPage;
