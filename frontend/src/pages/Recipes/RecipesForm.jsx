import { useNavigate } from 'react-router-dom';

function RecipesForm() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();

    console.log('Receita cadastrada!');

    navigate('/recipes');
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Cadastrar nova receita</h3>
      <button type="submit">Cadastrar</button>
    </form>
  );
}

export default RecipesForm;
