import { Search, Bell } from 'lucide-react';

export function Header() {
  return (
    <header className="h-16 bg-white border-b border-[#E5E7EB] px-6 flex items-center justify-between">
      <div className="flex-1 max-w-xl">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder="Search courses, students, resources..."
            className="w-full pl-10 pr-4 py-2 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4F46E5] focus:border-transparent"
          />
        </div>
      </div>

      <div className="flex items-center gap-4">
        <button className="relative p-2 hover:bg-[#F5F7FA] rounded-lg transition-colors">
          <Bell className="w-5 h-5 text-gray-600" />
          <span className="absolute top-1 right-1 w-2 h-2 bg-[#4F46E5] rounded-full"></span>
        </button>
      </div>
    </header>
  );
}
