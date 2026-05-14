"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, MessageSquare, BarChart3, Users, Settings, Shield, LogOut } from "lucide-react";
import { cn } from "@/lib/utils";

const menuItems = [
  { name: "Dashboard", icon: LayoutDashboard, href: "/dashboard" },
  { name: "Mod Queue", icon: MessageSquare, href: "/dashboard/queue" },
  { name: "Analytics", icon: BarChart3, href: "/dashboard/analytics" },
  { name: "Users", icon: Users, href: "/dashboard/users" },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 h-screen w-64 bg-card border-r border-border flex flex-col z-50">
      <div className="p-8">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 premium-gradient rounded-xl flex items-center justify-center shadow-lg shadow-purple-500/20">
            <Shield className="text-white w-6 h-6" />
          </div>
          <div>
            <span className="font-black text-lg tracking-tighter block leading-none">MODSHIELD</span>
            <span className="text-[10px] font-bold text-primary tracking-[0.2em] uppercase">Intelligence</span>
          </div>
        </div>
      </div>

      <nav className="flex-1 px-4 space-y-1">
        <div className="text-[10px] font-bold text-zinc-500 uppercase tracking-widest px-4 mb-4">Main Menu</div>
        {menuItems.map((item) => {
          const isActive = pathname === item.href || (item.href === "/dashboard" && pathname === "/dashboard");
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex items-center gap-3 px-4 py-3.5 rounded-xl transition-all duration-300 group relative",
                isActive 
                  ? "bg-primary/10 text-white" 
                  : "text-zinc-500 hover:text-zinc-200 hover:bg-zinc-900/50"
              )}
            >
              <item.icon className={cn(
                "w-5 h-5",
                isActive ? "text-primary" : "group-hover:text-zinc-300"
              )} />
              <span className="font-semibold text-sm">{item.name}</span>
              {isActive && (
                <>
                  <div className="absolute left-0 top-1/4 bottom-1/4 w-1 bg-primary rounded-r-full shadow-[0_0_10px_#a855f7]" />
                  <div className="ml-auto w-1.5 h-1.5 rounded-full bg-primary" />
                </>
              )}
            </Link>
          );
        })}
      </nav>

      <div className="p-4 mt-auto">
        <div className="p-4 rounded-2xl bg-zinc-900/50 border border-border flex items-center gap-3 group cursor-pointer hover:bg-zinc-900 transition-colors">
          <div className="w-9 h-9 rounded-full bg-zinc-800 border border-border flex items-center justify-center font-bold text-sm">M</div>
          <div className="flex-1 min-w-0">
            <p className="text-xs font-bold truncate">Moderator</p>
            <p className="text-[10px] text-zinc-500 truncate">System Admin</p>
          </div>
          <LogOut className="w-4 h-4 text-zinc-600 group-hover:text-zinc-400 transition-colors" />
        </div>
      </div>
    </aside>
  );
}
