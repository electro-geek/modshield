"use client";

import { useEffect, useState } from "react";
import { apiService } from "@/services/api";
import { BarChart3, TrendingUp, AlertTriangle, UserX, ShieldCheck } from "lucide-react";

export default function AnalyticsPage() {
  const [summary, setSummary] = useState<any>(null);

  useEffect(() => {
    apiService.getAnalyticsSummary().then(setSummary);
  }, []);

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Advanced Analytics</h1>
        <p className="text-zinc-500 mt-1">Deep dive into community health and moderation efficiency.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 glass p-8 rounded-2xl cyber-border">
          <h3 className="text-xl font-bold mb-8">Toxicity Distribution</h3>
          <div className="h-80 flex items-end justify-around gap-4 px-4">
            {[65, 45, 78, 32, 55, 90, 42].map((v, i) => (
              <div key={i} className="flex-1 flex flex-col items-center gap-4">
                <div 
                  className="w-full premium-gradient rounded-xl transition-all duration-500 hover:brightness-125"
                  style={{ height: `${v}%` }}
                />
                <span className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Day {i+1}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="glass p-8 rounded-2xl cyber-border flex flex-col justify-between">
          <div>
            <h3 className="text-xl font-bold mb-2">Efficiency Rating</h3>
            <p className="text-zinc-500 text-sm">Moderator response time vs AI detection.</p>
          </div>
          <div className="py-12 flex flex-col items-center">
            <div className="relative w-48 h-48 flex items-center justify-center">
              <svg className="w-full h-full -rotate-90">
                <circle cx="96" cy="96" r="88" stroke="currentColor" strokeWidth="12" fill="transparent" className="text-zinc-800" />
                <circle cx="96" cy="96" r="88" stroke="currentColor" strokeWidth="12" fill="transparent" strokeDasharray={553} strokeDashoffset={553 * (1 - 0.92)} className="text-[#a855f7]" />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className="text-4xl font-black">92%</span>
                <span className="text-[10px] font-bold text-zinc-500 uppercase">Optimal</span>
              </div>
            </div>
          </div>
          <div className="space-y-3">
            <div className="flex justify-between text-sm">
              <span className="text-zinc-500">AI Accuracy</span>
              <span className="font-bold">98.4%</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-zinc-500">Manual Review</span>
              <span className="font-bold">1.6%</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
