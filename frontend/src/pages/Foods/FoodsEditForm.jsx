import { useParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { getFood, updateFood } from '../../services/foods/foods';

function FoodsEditForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [food, setFood] = useState({
    name: '',
    category: '',
    in_stock: false,
    unit: '',
  });

  useEffect(() => {
    getFood(id)
      .then((data) => setFood(data))
      .catch(() => {
        alert('Alimento não encontrado');
        navigate('/foods');
      });
  }, [id, navigate]);

  function handleChange(e) {
    const { name, value, type, checked } = e.target;
    setFood((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await updateFood(id, food);
      navigate('/foods');
    } catch (err) {
      console.error(err);
      alert('Erro ao salvar.');
    }
  }

  return (
    <form onSubmit={handleSubmit} className="form-box">
      <h3>Editar alimento - {food.name || '...'}</h3>

      <label htmlFor="name">Nome</label>
      <input
        type="text"
        id="name"
        name="name"
        value={food.name}
        onChange={handleChange}
        required
      />

      <label htmlFor="category">Categoria</label>
      <input
        type="text"
        id="category"
        name="category"
        value={food.category}
        onChange={handleChange}
      />

      <label>
        <input
          type="checkbox"
          name="in_stock"
          checked={food.in_stock}
          onChange={handleChange}
        />
        Em estoque?
      </label>

      <label htmlFor="unit">Unidade</label>
      <input
        type="text"
        id="unit"
        name="unit"
        value={food.unit}
        placeholder="ex: kg, unidade"
        onChange={handleChange}
      />

      <button type="submit" className="form-btn">
        Salvar
      </button>
      <button
        type="button"
        className="form-btn"
        onClick={() => navigate('/foods')}
      >
        Cancelar
      </button>
    </form>
  );
}

export default FoodsEditForm;
