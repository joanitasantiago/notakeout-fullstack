import { useNavigate } from 'react-router-dom';

function FoodsForm() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();

    console.log('Alimento Cadastrado!');

    navigate('/foods');
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Cadastrar novo alimento</h3>
      <button type="submit">Cadastrar</button>
    </form>
  );
}

export default FoodsForm;
