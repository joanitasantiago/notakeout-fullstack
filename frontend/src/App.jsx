import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import HomePage from './pages/HomePage';
import FoodsPage from './pages/Foods/FoodsPage';
import FoodsList from './pages/Foods/FoodsList';
import FoodsForm from './pages/Foods/FoodsForm';
import RecipesPage from './pages/Recipes/RecipesPage';
import RecipesList from './pages/Recipes/RecipesList';
import RecipesForm from './pages/Recipes/RecipesForm';
import MenusPage from './pages/Menus/MenusPage';
import MenusList from './pages/Menus/MenusList';
import MenusForm from './pages/Menus/MenusForm';
import ShoppingListPage from './pages/ShoppingListPage';
import NotFound from './pages/NotFound';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/foods" element={<FoodsPage />}>
          <Route index element={<FoodsList />} />
          <Route path="new-food" element={<FoodsForm />} />
        </Route>
        <Route path="/recipes" element={<RecipesPage />}>
          <Route index element={<RecipesList />} />
          <Route path="new-recipe" element={<RecipesForm />} />
        </Route>
        <Route path="/menus" element={<MenusPage />}>
          <Route index element={<MenusList />} />
          <Route path="new-menu" element={<MenusForm />} />
        </Route>
        <Route path="/shopping-list" element={<ShoppingListPage />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
