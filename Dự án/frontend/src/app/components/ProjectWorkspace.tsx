import { FolderKanban, GraduationCap, Github } from 'lucide-react';

export function ProjectWorkspace() {
  const links = [
    { icon: FolderKanban, label: 'Lab Projects', count: 4 },
    { icon: GraduationCap, label: 'LMS Portal', count: null },
    { icon: Github, label: 'GitHub Repos', count: 7 },
  ];

  return (
    <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
      <h4 className="mb-4">Project Workspace</h4>
      <div className="space-y-3">
        {links.map((link) => {
          const Icon = link.icon;
          return (
            <button
              key={link.label}
              className="w-full flex items-center justify-between px-4 py-3 bg-[#F5F7FA] hover:bg-gray-100 rounded-lg transition-colors"
            >
              <div className="flex items-center gap-3">
                <Icon className="w-5 h-5 text-[#4F46E5]" />
                <span className="text-gray-700">{link.label}</span>
              </div>
              {link.count !== null && (
                <span className="px-2.5 py-1 bg-[#4F46E5] text-white rounded-full">
                  {link.count}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
