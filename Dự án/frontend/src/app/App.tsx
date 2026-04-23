import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Sidebar } from './components/Sidebar';
import { Header } from './components/Header';
import { Dashboard } from './pages/Dashboard';
import { Schedule } from './pages/Schedule';
import { Grades } from './pages/Grades';
import { Finance } from './pages/Finance';
import { Settings } from './pages/Settings';

export default function App() {
  return (
    <BrowserRouter>
      <div className="size-full flex bg-[#F5F7FA]">
        <Sidebar />

        <div className="flex-1 flex flex-col min-h-screen">
          <Header />

          <main className="flex-1 p-6">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/schedule" element={<Schedule />} />
              <Route path="/grades" element={<Grades />} />
              <Route path="/finance" element={<Finance />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}