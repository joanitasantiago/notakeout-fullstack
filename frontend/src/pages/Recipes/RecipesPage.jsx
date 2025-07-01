import { Outlet, Link } from 'react-router-dom';

function RecipesPage() {
  return (
    <section>
      <h2>Minhas Receitas</h2>

      <div style={{ marginBottom: '20px' }}>
        <Link to="/recipes">Ver receitas</Link> |{' '}
        <Link to="/recipes/new-recipe">Cadastrar nova receita</Link>
      </div>

      <Outlet />
    </section>
  );
}

export default RecipesPage;
