import { Clock, MapPin } from 'lucide-react';

export function WeeklySchedule() {
  const todayClasses = [
    {
      time: '09:00 - 10:30',
      subject: 'Machine Learning Fundamentals',
      room: 'CS-301',
      color: '#4F46E5',
    },
    {
      time: '11:00 - 12:30',
      subject: 'Advanced Database Systems',
      room: 'CS-205',
      color: '#7C3AED',
    },
    {
      time: '14:00 - 15:30',
      subject: 'Computer Vision Lab',
      room: 'LAB-402',
      color: '#2563EB',
    },
    {
      time: '16:00 - 17:30',
      subject: 'Neural Networks & Deep Learning',
      room: 'CS-301',
      color: '#4F46E5',
    },
  ];

  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <div className="flex items-center justify-between mb-6">
        <h3>Today's Schedule</h3>
        <span className="text-gray-500">Wednesday, Apr 23</span>
      </div>

      <div className="space-y-4">
        {todayClasses.map((classItem, index) => (
          <div
            key={index}
            className="flex items-start gap-4 p-4 bg-[#F5F7FA] rounded-xl hover:bg-gray-100 transition-colors"
          >
            <div
              className="w-1 h-full rounded-full flex-shrink-0"
              style={{ backgroundColor: classItem.color }}
            ></div>
            <div className="flex-1">
              <h4 className="text-gray-900">{classItem.subject}</h4>
              <div className="flex items-center gap-4 mt-2">
                <div className="flex items-center gap-1 text-gray-500">
                  <Clock className="w-4 h-4" />
                  <span>{classItem.time}</span>
                </div>
                <div className="flex items-center gap-1 text-gray-500">
                  <MapPin className="w-4 h-4" />
                  <span>{classItem.room}</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
