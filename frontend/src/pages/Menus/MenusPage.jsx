import { Outlet, Link } from 'react-router-dom';

function MenusPage() {
  return (
    <section>
      <h2>Meus Menus</h2>

      <div style={{ marginBottom: '20px' }}>
        <Link to="/menus">Ver Menus</Link> |{' '}
        <Link to="/menus/new-menu">Cadastrar novo menu</Link>
      </div>

      <Outlet />
    </section>
  );
}

export default MenusPage;