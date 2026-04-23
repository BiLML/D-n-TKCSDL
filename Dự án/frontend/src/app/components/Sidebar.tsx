import { LayoutDashboard, Calendar, Award, DollarSign, Settings, ChevronLeft } from 'lucide-react';
import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

export function Sidebar() {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const location = useLocation();

  const navItems = [
    { icon: LayoutDashboard, label: 'Dashboard', path: '/' },
    { icon: Calendar, label: 'Schedule', path: '/schedule' },
    { icon: Award, label: 'Grades', path: '/grades' },
    { icon: DollarSign, label: 'Finance', path: '/finance' },
    { icon: Settings, label: 'Settings', path: '/settings' },
  ];

  return (
    <aside
      className={`${
        isCollapsed ? 'w-16' : 'w-64'
      } bg-white border-r border-[#E5E7EB] transition-all duration-300 flex flex-col`}
    >
      <div className="p-6 border-b border-[#E5E7EB] flex items-center justify-between">
        {!isCollapsed && <h2 className="text-[#4F46E5]">SIS Portal</h2>}
        <button
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="p-1.5 hover:bg-[#F5F7FA] rounded-lg transition-colors"
        >
          <ChevronLeft className={`w-5 h-5 transition-transform ${isCollapsed ? 'rotate-180' : ''}`} />
        </button>
      </div>

      <nav className="flex-1 p-4">
        <ul className="space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            return (
              <li key={item.label}>
                <Link
                  to={item.path}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                    isActive
                      ? 'bg-[#4F46E5] text-white'
                      : 'text-gray-600 hover:bg-[#F5F7FA]'
                  }`}
                >
                  <Icon className="w-5 h-5 flex-shrink-0" />
                  {!isCollapsed && <span>{item.label}</span>}
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </aside>
  );
}
