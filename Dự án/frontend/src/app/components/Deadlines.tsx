import { AlertCircle, Bell } from 'lucide-react';

export function Deadlines() {
  const deadlines = [
    {
      title: 'ML Assignment 3: Neural Networks',
      date: 'Due Apr 25, 2026',
      type: 'assignment',
      urgent: true,
    },
    {
      title: 'Database Project Milestone 2',
      date: 'Due Apr 28, 2026',
      type: 'assignment',
      urgent: false,
    },
    {
      title: 'Computer Vision Lab Report',
      date: 'Due Apr 30, 2026',
      type: 'assignment',
      urgent: false,
    },
  ];

  const announcements = [
    {
      title: 'Spring Career Fair - Register Now',
      date: 'May 5, 2026',
      type: 'announcement',
    },
    {
      title: 'Course Registration for Fall 2026 Opens',
      date: 'May 1, 2026',
      type: 'announcement',
    },
  ];

  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <h4 className="mb-4">Upcoming & Announcements</h4>

      <div className="space-y-3 max-h-[400px] overflow-y-auto">
        {deadlines.map((item, index) => (
          <div
            key={index}
            className={`p-4 rounded-lg border ${
              item.urgent
                ? 'bg-red-50 border-red-200'
                : 'bg-[#F5F7FA] border-[#E5E7EB]'
            }`}
          >
            <div className="flex items-start gap-3">
              {item.urgent && <AlertCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />}
              <div className="flex-1">
                <p className={`${item.urgent ? 'text-red-900' : 'text-gray-900'}`}>
                  {item.title}
                </p>
                <p className="text-gray-500 mt-1">{item.date}</p>
              </div>
            </div>
          </div>
        ))}

        <div className="border-t border-[#E5E7EB] pt-3 mt-3">
          {announcements.map((item, index) => (
            <div
              key={index}
              className="p-4 rounded-lg bg-blue-50 border border-blue-200 mb-3"
            >
              <div className="flex items-start gap-3">
                <Bell className="w-5 h-5 text-[#4F46E5] flex-shrink-0 mt-0.5" />
                <div className="flex-1">
                  <p className="text-gray-900">{item.title}</p>
                  <p className="text-gray-500 mt-1">{item.date}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
