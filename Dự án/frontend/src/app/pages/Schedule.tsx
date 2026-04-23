import { Clock, MapPin, Calendar as CalendarIcon } from 'lucide-react';

export function Schedule() {
  const timeSlots = [
    '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00'
  ];

  const weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  const classes = [
    {
      day: 0,
      startTime: '09:00',
      duration: 1.5,
      subject: 'Linear Algebra',
      room: 'MATH-201',
      color: '#4F46E5',
    },
    {
      day: 0,
      startTime: '14:00',
      duration: 1.5,
      subject: 'Computer Vision Lab',
      room: 'LAB-402',
      color: '#2563EB',
    },
    {
      day: 1,
      startTime: '10:00',
      duration: 1.5,
      subject: 'Machine Learning Fundamentals',
      room: 'CS-301',
      color: '#7C3AED',
    },
    {
      day: 1,
      startTime: '16:00',
      duration: 1.5,
      subject: 'Neural Networks & Deep Learning',
      room: 'CS-301',
      color: '#4F46E5',
    },
    {
      day: 2,
      startTime: '09:00',
      duration: 1.5,
      subject: 'Machine Learning Fundamentals',
      room: 'CS-301',
      color: '#7C3AED',
    },
    {
      day: 2,
      startTime: '11:00',
      duration: 1.5,
      subject: 'Advanced Database Systems',
      room: 'CS-205',
      color: '#2563EB',
    },
    {
      day: 2,
      startTime: '14:00',
      duration: 1.5,
      subject: 'Computer Vision Lab',
      room: 'LAB-402',
      color: '#2563EB',
    },
    {
      day: 3,
      startTime: '09:00',
      duration: 1.5,
      subject: 'Linear Algebra',
      room: 'MATH-201',
      color: '#4F46E5',
    },
    {
      day: 3,
      startTime: '13:00',
      duration: 1.5,
      subject: 'Advanced Database Systems',
      room: 'CS-205',
      color: '#2563EB',
    },
    {
      day: 4,
      startTime: '10:00',
      duration: 1.5,
      subject: 'Neural Networks & Deep Learning',
      room: 'CS-301',
      color: '#4F46E5',
    },
  ];

  const upcomingExams = [
    {
      subject: 'Machine Learning Fundamentals',
      date: 'May 2, 2026',
      time: '10:00 AM',
      room: 'CS-301',
    },
    {
      subject: 'Linear Algebra',
      date: 'May 5, 2026',
      time: '09:00 AM',
      room: 'MATH-201',
    },
    {
      subject: 'Advanced Database Systems',
      date: 'May 8, 2026',
      time: '11:00 AM',
      room: 'CS-205',
    },
  ];

  const getClassPosition = (startTime: string, duration: number) => {
    const hour = parseInt(startTime.split(':')[0]);
    const minutes = parseInt(startTime.split(':')[1]);
    const startHour = 8;
    const top = ((hour - startHour) * 80) + (minutes / 60 * 80);
    const height = duration * 80;
    return { top, height };
  };

  return (
    <div className="grid grid-cols-4 gap-6">
      <div className="col-span-3">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3>Weekly Schedule</h3>
            <div className="flex items-center gap-2 text-gray-500">
              <CalendarIcon className="w-5 h-5" />
              <span>Week of April 21 - 25, 2026</span>
            </div>
          </div>

          <div className="grid grid-cols-6 gap-0 border border-[#E5E7EB] rounded-xl overflow-hidden">
            <div className="bg-[#F5F7FA] border-r border-[#E5E7EB]">
              <div className="h-12 border-b border-[#E5E7EB] flex items-center justify-center">
                <span className="text-gray-500">Time</span>
              </div>
              {timeSlots.map((time) => (
                <div key={time} className="h-20 border-b border-[#E5E7EB] flex items-center justify-center">
                  <span className="text-gray-600">{time}</span>
                </div>
              ))}
            </div>

            {weekDays.map((day, dayIndex) => (
              <div key={day} className="border-r border-[#E5E7EB] last:border-r-0 relative">
                <div className="h-12 border-b border-[#E5E7EB] bg-[#F5F7FA] flex items-center justify-center">
                  <span className="text-gray-700">{day}</span>
                </div>
                <div className="relative" style={{ height: `${timeSlots.length * 80}px` }}>
                  {timeSlots.map((_, index) => (
                    <div
                      key={index}
                      className="absolute w-full border-b border-[#E5E7EB]"
                      style={{ top: `${index * 80}px`, height: '80px' }}
                    ></div>
                  ))}
                  {classes
                    .filter((c) => c.day === dayIndex)
                    .map((classItem, index) => {
                      const { top, height } = getClassPosition(classItem.startTime, classItem.duration);
                      return (
                        <div
                          key={index}
                          className="absolute left-1 right-1 rounded-lg p-2 text-white overflow-hidden"
                          style={{
                            top: `${top}px`,
                            height: `${height - 8}px`,
                            backgroundColor: classItem.color,
                          }}
                        >
                          <p className="font-medium text-sm leading-tight">{classItem.subject}</p>
                          <div className="flex items-center gap-1 mt-1">
                            <MapPin className="w-3 h-3" />
                            <span className="text-xs">{classItem.room}</span>
                          </div>
                        </div>
                      );
                    })}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="col-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h4 className="mb-4">Upcoming Exams</h4>
          <div className="space-y-4">
            {upcomingExams.map((exam, index) => (
              <div
                key={index}
                className="p-4 bg-[#F5F7FA] rounded-xl border border-[#E5E7EB]"
              >
                <h4 className="text-gray-900 mb-2">{exam.subject}</h4>
                <div className="space-y-1 text-gray-600">
                  <div className="flex items-center gap-2">
                    <CalendarIcon className="w-4 h-4" />
                    <span>{exam.date}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Clock className="w-4 h-4" />
                    <span>{exam.time}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <MapPin className="w-4 h-4" />
                    <span>{exam.room}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
