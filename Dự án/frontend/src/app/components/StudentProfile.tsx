import { User } from 'lucide-react';

export function StudentProfile() {
  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <div className="flex items-center gap-4">
        <div className="w-16 h-16 bg-gradient-to-br from-[#4F46E5] to-[#7C3AED] rounded-full flex items-center justify-center">
          <User className="w-8 h-8 text-white" />
        </div>
        <div className="flex-1">
          <h3>Alex Johnson</h3>
          <p className="text-gray-500">ID: ST2024-8956</p>
          <p className="text-[#4F46E5] mt-1">Data Science & AI Engineering</p>
          <p className="text-gray-500">Year 3 • Fall 2026</p>
        </div>
      </div>
    </div>
  );
}
