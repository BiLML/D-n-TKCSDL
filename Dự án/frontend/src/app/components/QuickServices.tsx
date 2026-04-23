import { BookOpen, CreditCard, FileText, HeadphonesIcon } from 'lucide-react';

export function QuickServices() {
  const services = [
    { icon: BookOpen, label: 'Course Registration', color: '#4F46E5' },
    { icon: CreditCard, label: 'Tuition & Fees', color: '#2563EB' },
    { icon: FileText, label: 'Transcripts', color: '#7C3AED' },
    { icon: HeadphonesIcon, label: 'IT Support', color: '#4F46E5' },
  ];

  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <h4 className="mb-4">Quick Services</h4>
      <div className="space-y-3">
        {services.map((service) => {
          const Icon = service.icon;
          return (
            <button
              key={service.label}
              className="w-full flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] hover:bg-gray-100 rounded-lg transition-colors text-left"
            >
              <div
                className="w-10 h-10 rounded-lg flex items-center justify-center"
                style={{ backgroundColor: `${service.color}15` }}
              >
                <Icon className="w-5 h-5" style={{ color: service.color }} />
              </div>
              <span className="text-gray-700">{service.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
