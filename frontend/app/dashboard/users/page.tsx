"use client";

import { useEffect, useState } from "react";
import { apiService } from "@/services/api";
import { UserX, ShieldAlert, History, Search } from "lucide-react";
import { cn } from "@/lib/utils";

export default function UsersPage() {
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    apiService.getRiskyUsers().then(setUsers);
  }, []);

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">User Risk Intelligence</h1>
          <p className="text-zinc-500 mt-1">Identify and track repeat offenders and suspicious behavior.</p>
        </div>
        <div className="relative group">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500 group-hover:text-[#a855f7] transition-colors" />
          <input 
            type="text" 
            placeholder="Search username..." 
            className="bg-[#151518] border border-zinc-800 rounded-xl py-2 pl-10 pr-4 text-sm focus:outline-none focus:border-[#a855f7] transition-all w-64"
          />
        </div>
      </div>

      <div className="glass rounded-2xl overflow-hidden cyber-border">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-zinc-800 bg-zinc-900/30 text-[10px] font-bold uppercase tracking-widest text-zinc-500">
              <th className="px-6 py-4">Username</th>
              <th className="px-6 py-4">Risk Level</th>
              <th className="px-6 py-4">Violations</th>
              <th className="px-6 py-4">Account Age</th>
              <th className="px-6 py-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-800">
            {users.length > 0 ? (
              users.map((user) => (
                <tr key={user.id} className="hover:bg-zinc-900/30 transition-colors">
                  <td className="px-6 py-6 font-bold text-sm">u/{user.reddit_username}</td>
                  <td className="px-6 py-6">
                    <div className="flex items-center gap-2">
                      <div className={cn("w-2 h-2 rounded-full", user.risk_score > 70 ? "bg-red-500" : "bg-amber-500")} />
                      <span className="text-xs font-bold">{user.risk_score > 70 ? "HIGH" : "MEDIUM"}</span>
                    </div>
                  </td>
                  <td className="px-6 py-6 text-sm text-zinc-400">{user.total_violations} instances</td>
                  <td className="px-6 py-6 text-sm text-zinc-400">{user.account_age_days} days</td>
                  <td className="px-6 py-6 text-right">
                    <button className="text-[10px] font-bold uppercase tracking-widest px-3 py-1.5 rounded-lg border border-zinc-800 hover:bg-white hover:text-black transition-all">
                      View Profile
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={5} className="px-6 py-12 text-center text-zinc-500 font-medium italic">
                  No risky users identified yet. Monitoring subreddit for activity...
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
