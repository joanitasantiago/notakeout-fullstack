import { useNavigate } from 'react-router-dom';

function FoodsList() {
  const navigate = useNavigate();

  return (
    <div>
      <h3> Lista de Alimentos </h3>
      <button type="button" onClick={() => navigate('/foods/new')}>
        + Adicionar alimento
      </button>
    </div>
  );
}

export default FoodsList;