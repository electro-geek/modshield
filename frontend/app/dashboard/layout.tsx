import { Sidebar } from "@/components/sidebar/Sidebar";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex bg-background min-h-screen text-zinc-100 selection:bg-primary/30">
      <Sidebar />
      <main className="flex-1 ml-64 p-10 overflow-x-hidden">
        <div className="max-w-6xl mx-auto space-y-10">
          {children}
        </div>
      </main>
    </div>
  );
}
