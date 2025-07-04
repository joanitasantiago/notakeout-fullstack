import { Outlet } from 'react-router-dom';

function FoodsPage() {
  return (
    <div className="container">
      <h2>Meus alimentos</h2>
      <Outlet />
    </div>
  );
}

export default FoodsPage;
