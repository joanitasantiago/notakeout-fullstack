import { useNavigate } from 'react-router-dom';

function RecipesEditForm() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    navigate('/recipes');
  }

  return (
    <div>
      <h3>Editar Receita ~nome~ </h3>
      <form onSubmit={handleSubmit}>
        <button type="submit"> Salvar alterações </button>
        <button type="button" onClick={() => navigate('/recipes')}>
          Cancelar
        </button>
      </form>
    </div>
  );
}

export default RecipesEditForm;
