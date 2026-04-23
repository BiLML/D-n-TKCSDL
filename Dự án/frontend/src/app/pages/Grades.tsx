import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

export function Grades() {
  const gpaData = [
    { semester: 'Fall 2024', gpa: 3.6 },
    { semester: 'Spring 2025', gpa: 3.7 },
    { semester: 'Fall 2025', gpa: 3.8 },
  ];

  const currentCourses = [
    {
      code: 'CS-401',
      name: 'Machine Learning Fundamentals',
      credits: 4,
      grade: 'A',
      gradePoint: 4.0,
    },
    {
      code: 'CS-305',
      name: 'Advanced Database Systems',
      credits: 3,
      grade: 'A-',
      gradePoint: 3.7,
    },
    {
      code: 'MATH-301',
      name: 'Linear Algebra',
      credits: 4,
      grade: 'B+',
      gradePoint: 3.3,
    },
    {
      code: 'CS-410',
      name: 'Neural Networks & Deep Learning',
      credits: 4,
      grade: 'A',
      gradePoint: 4.0,
    },
    {
      code: 'CS-402L',
      name: 'Computer Vision Lab',
      credits: 2,
      grade: 'A',
      gradePoint: 4.0,
    },
  ];

  const totalCreditsEarned = 87;
  const totalCreditsRequired = 120;
  const percentage = (totalCreditsEarned / totalCreditsRequired) * 100;

  const creditsData = [
    { name: 'Earned', value: percentage },
    { name: 'Remaining', value: 100 - percentage },
  ];

  const COLORS = ['#4F46E5', '#E5E7EB'];

  return (
    <div className="grid grid-cols-4 gap-6">
      <div className="col-span-3 row-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h3 className="mb-6">GPA Trend</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={gpaData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
              <XAxis dataKey="semester" stroke="#6B7280" />
              <YAxis domain={[0, 4.0]} stroke="#6B7280" />
              <Tooltip
                contentStyle={{
                  backgroundColor: '#fff',
                  border: '1px solid #E5E7EB',
                  borderRadius: '8px',
                }}
              />
              <Line
                type="monotone"
                dataKey="gpa"
                stroke="#4F46E5"
                strokeWidth={3}
                dot={{ fill: '#4F46E5', r: 6 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="col-span-1 row-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h4 className="mb-4">Total Credits</h4>
          <div className="flex flex-col items-center">
            <div className="relative w-32 h-32">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={creditsData}
                    cx="50%"
                    cy="50%"
                    innerRadius={45}
                    outerRadius={60}
                    startAngle={90}
                    endAngle={-270}
                    dataKey="value"
                  >
                    {creditsData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index]} />
                    ))}
                  </Pie>
                </PieChart>
              </ResponsiveContainer>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className="text-[#4F46E5]">{totalCreditsEarned}</span>
                <span className="text-gray-500">/{totalCreditsRequired}</span>
              </div>
            </div>
            <div className="mt-4 text-center">
              <p className="text-gray-500">Credits Earned</p>
              <p className="text-[#4F46E5] mt-1">{percentage.toFixed(1)}% Complete</p>
            </div>
          </div>
        </div>
      </div>

      <div className="col-span-4">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h3 className="mb-6">Current Semester - Fall 2026</h3>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[#E5E7EB]">
                  <th className="text-left py-3 px-4 text-gray-600">Course Code</th>
                  <th className="text-left py-3 px-4 text-gray-600">Course Name</th>
                  <th className="text-center py-3 px-4 text-gray-600">Credits</th>
                  <th className="text-center py-3 px-4 text-gray-600">Grade</th>
                  <th className="text-center py-3 px-4 text-gray-600">Grade Point</th>
                </tr>
              </thead>
              <tbody>
                {currentCourses.map((course, index) => (
                  <tr
                    key={index}
                    className="border-b border-[#E5E7EB] last:border-b-0 hover:bg-[#F5F7FA] transition-colors"
                  >
                    <td className="py-4 px-4 text-gray-900">{course.code}</td>
                    <td className="py-4 px-4 text-gray-900">{course.name}</td>
                    <td className="py-4 px-4 text-center text-gray-700">{course.credits}</td>
                    <td className="py-4 px-4 text-center">
                      <span className="px-3 py-1 bg-[#4F46E5] text-white rounded-full">
                        {course.grade}
                      </span>
                    </td>
                    <td className="py-4 px-4 text-center text-gray-700">{course.gradePoint.toFixed(1)}</td>
                  </tr>
                ))}
              </tbody>
              <tfoot>
                <tr className="bg-[#F5F7FA]">
                  <td colSpan={2} className="py-4 px-4 text-gray-900">
                    Semester GPA
                  </td>
                  <td className="py-4 px-4 text-center text-gray-700">
                    {currentCourses.reduce((sum, c) => sum + c.credits, 0)}
                  </td>
                  <td colSpan={2} className="py-4 px-4 text-center text-[#4F46E5]">
                    3.8
                  </td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
