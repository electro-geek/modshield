"use client";

import { useEffect, useState } from "react";
import { apiService } from "@/services/api";
import { Shield, Check, X, AlertCircle, Info, ExternalLink } from "lucide-react";
import { cn } from "@/lib/utils";

export default function QueuePage() {
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchQueue();
  }, []);

  const fetchQueue = () => {
    setLoading(true);
    apiService.getQueue().then(data => {
      setItems(data);
      setLoading(false);
    }).catch(() => setLoading(false));
  };

  const handleAction = async (postId: string, action: string) => {
    try {
      await apiService.performAction(postId, action, `AI suggested ${action}`, "admin");
      setItems(items.filter(item => item.post_id !== postId));
    } catch (err) {
      console.error("Action failed", err);
    }
  };

  if (loading && items.length === 0) return <div className="text-zinc-500 animate-pulse p-8">Initializing neural moderation queue...</div>;

  return (
    <div className="space-y-8 pb-12">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Moderation Queue</h1>
        <p className="text-zinc-500 mt-1">AI-prioritized content requiring review.</p>
      </div>

      <div className="space-y-6">
        {items.length === 0 ? (
          <div className="glass p-12 rounded-2xl text-center border-dashed border-2 border-zinc-800">
            <Check className="w-12 h-12 text-emerald-500 mx-auto mb-4" />
            <h3 className="text-xl font-bold">Queue Clear!</h3>
            <p className="text-zinc-500">Your community is safe and sound.</p>
          </div>
        ) : (
          items.map((item) => (
            <div key={item.post_id} className="glass rounded-2xl overflow-hidden border border-zinc-800 hover:border-zinc-700 transition-all group">
              <div className="flex flex-col md:flex-row">
                <div className="p-6 md:w-2/3 border-b md:border-b-0 md:border-r border-zinc-800">
                  <div className="flex items-center gap-3 mb-4">
                    <span className={cn(
                      "text-[10px] font-bold px-2 py-1 rounded border",
                      item.risk_score > 70 ? "bg-red-500/10 text-red-500 border-red-500/20" : 
                      item.risk_score > 30 ? "bg-amber-500/10 text-amber-500 border-amber-500/20" :
                      "bg-emerald-500/10 text-emerald-500 border-emerald-500/20"
                    )}>
                      {item.risk_score > 70 ? "CRITICAL RISK" : item.risk_score > 30 ? "MEDIUM RISK" : "LOW RISK"}
                    </span>
                    <span className="text-xs text-zinc-500 uppercase tracking-widest font-bold">r/{item.subreddit}</span>
                    <span className="text-xs text-zinc-600">• by u/{item.author}</span>
                  </div>
                  <h3 className="text-lg font-bold mb-2 group-hover:text-[#a855f7] transition-colors">{item.title}</h3>
                  <p className="text-zinc-400 text-sm line-clamp-3 leading-relaxed mb-4">{item.content}</p>
                  <div className="flex items-center gap-4">
                    <button className="text-xs text-zinc-500 flex items-center gap-1 hover:text-white transition-colors">
                      <ExternalLink className="w-3 h-3" /> View on Reddit
                    </button>
                  </div>
                </div>

                <div className="p-6 md:w-1/3 bg-[#0a0a0c]/50">
                  <div className="mb-6">
                    <div className="flex items-center gap-2 mb-2">
                      <Shield className="w-4 h-4 text-[#a855f7]" />
                      <span className="text-xs font-bold uppercase tracking-widest text-[#a855f7]">AI Analysis</span>
                    </div>
                    <div className="p-3 rounded-xl bg-zinc-900/50 border border-zinc-800">
                      <p className="text-sm font-semibold text-white mb-1">
                        Suggested: <span className="uppercase text-[#a855f7]">{item.suggested_action}</span>
                      </p>
                      <p className="text-xs text-zinc-400 italic">"{item.reasoning}"</p>
                    </div>
                  </div>

                  <div className="flex gap-3">
                    <button 
                      onClick={() => handleAction(item.post_id, "approve")}
                      className="flex-1 flex items-center justify-center gap-2 py-2.5 rounded-xl bg-emerald-500/10 text-emerald-500 border border-emerald-500/20 hover:bg-emerald-500 hover:text-white transition-all font-bold text-sm"
                    >
                      <Check className="w-4 h-4" /> Approve
                    </button>
                    <button 
                      onClick={() => handleAction(item.post_id, "remove")}
                      className="flex-1 flex items-center justify-center gap-2 py-2.5 rounded-xl bg-red-500/10 text-red-500 border border-red-500/20 hover:bg-red-500 hover:text-white transition-all font-bold text-sm"
                    >
                      <X className="w-4 h-4" /> Remove
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
