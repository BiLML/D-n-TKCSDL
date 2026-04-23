import { StudentProfile } from '../components/StudentProfile';
import { AcademicOverview } from '../components/AcademicOverview';
import { WeeklySchedule } from '../components/WeeklySchedule';
import { QuickServices } from '../components/QuickServices';
import { ProjectWorkspace } from '../components/ProjectWorkspace';
import { Deadlines } from '../components/Deadlines';

export function Dashboard() {
  return (
    <div className="grid grid-cols-4 gap-6 auto-rows-[minmax(200px,auto)]">
      <div className="col-span-2 row-span-1">
        <StudentProfile />
      </div>

      <div className="col-span-1 row-span-1">
        <AcademicOverview />
      </div>

      <div className="col-span-1 row-span-2">
        <Deadlines />
      </div>

      <div className="col-span-2 row-span-2">
        <WeeklySchedule />
      </div>

      <div className="col-span-1 row-span-2">
        <QuickServices />
      </div>

      <div className="col-span-1 row-span-1">
        <ProjectWorkspace />
      </div>
    </div>
  );
}
