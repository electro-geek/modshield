"use client";

import { useEffect, useState } from "react";
import { apiService } from "@/services/api";
import { Shield, AlertTriangle, CheckCircle, TrendingUp, ArrowUpRight, Activity } from "lucide-react";
import { cn } from "@/lib/utils";

export default function DashboardPage() {
  const [summary, setSummary] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiService.getAnalyticsSummary()
      .then(data => {
        setSummary(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return (
    <div className="flex flex-col items-center justify-center h-[60vh] gap-4">
      <div className="w-12 h-12 border-4 border-primary/20 border-t-primary rounded-full animate-spin" />
      <p className="text-zinc-500 font-medium animate-pulse">Syncing with Reddit...</p>
    </div>
  );

  const stats = [
    { name: "Flagged Content", value: summary?.total_flagged || 0, icon: AlertTriangle, color: "text-amber-500", bg: "bg-amber-500/10" },
    { name: "Actions Taken", value: summary?.total_actions || 0, icon: CheckCircle, color: "text-emerald-500", bg: "bg-emerald-500/10" },
    { name: "Avg Risk Score", value: summary?.avg_risk_score || 0, icon: Shield, color: "text-purple-500", bg: "bg-purple-500/10" },
    { name: "Community Health", value: `${summary?.community_health || 0}%`, icon: TrendingUp, color: "text-blue-500", bg: "bg-blue-500/10" },
  ];

  return (
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-700">
      <header className="mb-12 flex justify-between items-end">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-[10px] font-black uppercase tracking-[0.3em] text-zinc-500">Live Status</span>
          </div>
          <h1 className="text-4xl font-black tracking-tight text-white">Network Overview</h1>
          <p className="text-zinc-500 mt-2 font-medium">AI Moderator Copilot active across all monitored subreddits.</p>
        </div>
        <div className="glass px-6 py-3 rounded-2xl flex items-center gap-4 border-border">
          <Activity className="w-5 h-5 text-primary" />
          <div className="text-right">
            <p className="text-[10px] font-bold text-zinc-500 uppercase tracking-widest">Global Latency</p>
            <p className="text-sm font-black">24ms</p>
          </div>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        {stats.map((stat) => (
          <div key={stat.name} className="glass p-6 rounded-3xl border-border stat-card group">
            <div className="flex justify-between items-start mb-6">
              <div className={cn("p-3 rounded-2xl", stat.bg)}>
                <stat.icon className={cn("w-6 h-6", stat.color)} />
              </div>
              <div className="flex items-center gap-1 px-2 py-1 rounded-full bg-zinc-800/50 text-[10px] font-bold text-zinc-400">
                Live <div className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse ml-1" />
              </div>
            </div>
            <div>
              <p className="text-xs font-bold text-zinc-500 uppercase tracking-widest mb-1">{stat.name}</p>
              <p className="text-3xl font-black text-white">{stat.value}</p>
            </div>
            <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-primary/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 glass p-8 rounded-[2rem] border-border relative overflow-hidden">
          <div className="flex justify-between items-center mb-10">
            <h2 className="text-xl font-black text-white flex items-center gap-3">
              <TrendingUp className="w-5 h-5 text-primary" />
              Toxicity Trends
            </h2>
          </div>
          
          <div className="h-64 flex items-end gap-3 px-2">
            {(summary?.trends && summary.trends.length > 0) ? (
              summary.trends.map((item: any, i: number) => (
                <div key={i} className="flex-1 group relative">
                  <div 
                    className="bg-primary/20 hover:bg-primary rounded-xl transition-all duration-500 w-full cursor-pointer relative z-10"
                    style={{ height: `${item.value}%` }}
                  ></div>
                </div>
              ))
            ) : (
              <div className="w-full h-full flex items-center justify-center border border-dashed border-zinc-800 rounded-2xl">
                <p className="text-zinc-600 text-sm font-medium italic">Insufficient data for trends</p>
              </div>
            )}
          </div>
          <div className="flex justify-between mt-8 text-[10px] text-zinc-600 px-4 uppercase tracking-[0.2em] font-black">
            <span>MON</span>
            <span>TUE</span>
            <span>WED</span>
            <span>THU</span>
            <span>FRI</span>
            <span>SAT</span>
            <span>SUN</span>
          </div>
        </div>

        <div className="glass p-8 rounded-[2rem] border-border">
          <div className="flex items-center gap-3 mb-8">
             <Activity className="w-5 h-5 text-primary" />
             <h2 className="text-xl font-black text-white">Live Alerts</h2>
          </div>
          <div className="space-y-4">
            {summary?.recent_alerts?.length > 0 ? (
              summary.recent_alerts.map((alert: any, i: number) => (
                <div key={i} className="flex items-center gap-4 p-4 rounded-2xl hover:bg-zinc-800/30 transition-all border border-transparent hover:border-border cursor-pointer group">
                  <div className="w-2 h-2 rounded-full bg-primary" />
                  <div className="flex-1 min-w-0">
                    <p className="text-xs font-bold text-white truncate">{alert.message}</p>
                    <p className="text-[10px] text-zinc-500 uppercase tracking-wider">{alert.time}</p>
                  </div>
                </div>
              ))
            ) : (
              <div className="py-12 text-center">
                <div className="w-12 h-12 rounded-full bg-zinc-900 flex items-center justify-center mx-auto mb-4 border border-border">
                  <Shield className="w-6 h-6 text-zinc-700" />
                </div>
                <p className="text-xs text-zinc-500 font-medium italic">No active threats detected.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
