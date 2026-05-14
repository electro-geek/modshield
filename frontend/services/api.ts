const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000/api";

export const apiService = {
  async getQueue() {
    const res = await fetch(`${BACKEND_URL}/moderation/queue`);
    return res.json();
  },

  async performAction(postId: string, action: string, reason: string, moderator: string) {
    const res = await fetch(`${BACKEND_URL}/moderation/action`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ post_id: postId, action, reason, moderator }),
    });
    return res.json();
  },

  async getAnalyticsSummary() {
    const res = await fetch(`${BACKEND_URL}/analytics/summary`);
    return res.json();
  },

  async getRiskyUsers() {
    const res = await fetch(`${BACKEND_URL}/users/`);
    return res.json();
  },
};
