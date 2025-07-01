import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import HomePage from './pages/HomePage';
import FoodsPage from './pages/FoodsPage';
import RecipesPage from './pages/RecipesPage';
import NotFound from './pages/NotFound';
import MenusPage from './pages/MenusPage';
import ShoppingListPage from './pages/ShoppingListPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/foods" element={<FoodsPage />} />
        <Route path="/recipes" element={<RecipesPage />} />
        <Route path="/menus" element={<MenusPage />} />
        <Route path="/shopping-list" element={<ShoppingListPage />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
