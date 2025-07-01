import { useNavigate } from 'react-router-dom';

function MenusForm() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();

    console.log('Menu Cadastrado!');

    navigate('/menus');
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Cadastrar novo menu</h3>
      <button type="submit">Cadastrar</button>
    </form>
  );
}

export default MenusForm;
