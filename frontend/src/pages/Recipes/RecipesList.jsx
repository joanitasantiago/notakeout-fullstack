import { useNavigate } from 'react-router-dom';

function RecipesList() {
  const navigate = useNavigate();

  return (
    <div>
      <h3> Lista de Receitas </h3>
      <button type="button" onClick={() => navigate('/recipes/new')}>
        + Adicionar receita
      </button>
    </div>
  );
}

export default RecipesList;
