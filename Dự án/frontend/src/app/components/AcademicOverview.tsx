import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

export function AcademicOverview() {
  const gpa = 3.8;
  const maxGpa = 4.0;
  const percentage = (gpa / maxGpa) * 100;

  const data = [
    { name: 'Current', value: percentage },
    { name: 'Remaining', value: 100 - percentage },
  ];

  const COLORS = ['#4F46E5', '#E5E7EB'];

  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <h4 className="mb-4">Academic Overview</h4>
      <div className="flex flex-col items-center">
        <div className="relative w-32 h-32">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={45}
                outerRadius={60}
                startAngle={90}
                endAngle={-270}
                dataKey="value"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index]} />
                ))}
              </Pie>
            </PieChart>
          </ResponsiveContainer>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-[#4F46E5]">{gpa}</span>
            <span className="text-gray-500">/4.0</span>
          </div>
        </div>
        <div className="mt-4 text-center">
          <p className="text-gray-500">Current GPA</p>
          <p className="text-gray-600 mt-2">Credits: 87/120</p>
        </div>
      </div>
    </div>
  );
}
