import { useNavigate } from 'react-router-dom';

function RecipesForm() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    navigate('/recipes');
  }

  return (
    <div>
      <h3>Cadastrar nova receita</h3>
      <form onSubmit={handleSubmit}>
        <button type="submit"> Salvar </button>
        <button type="button" onClick={() => navigate('/recipes')}>
          Cancelar
        </button>
      </form>
    </div>
  );
}

export default RecipesForm;
