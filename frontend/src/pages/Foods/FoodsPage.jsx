import { Outlet, Link } from 'react-router-dom';

function FoodsPage() {
  return (
    <section>
      <h2>Meus Alimentos</h2>

      <div style={{ marginBottom: '20px' }}>
        <Link to="/foods">Ver alimentos</Link> |{' '}
        <Link to="/foods/new-food">Cadastrar novo alimento</Link>
      </div>

      <Outlet />
    </section>
  );
}

export default FoodsPage;
