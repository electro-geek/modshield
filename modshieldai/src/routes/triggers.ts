import { Hono } from 'hono';
import type { OnAppInstallRequest, TriggerResponse } from '@devvit/web/shared';

export const triggers = new Hono();

// LIVE PRODUCTION URL
const BACKEND_URL = 'https://modshield.vercel.app/api';

triggers.post('/on-app-install', async (c) => {
  const input = await c.req.json<OnAppInstallRequest>();
  console.log('App installed to subreddit: r/' + input.subreddit?.name);

  return c.json<TriggerResponse>(
    {
      status: 'success',
    },
    200
  );
});

triggers.post('/on-post-submit', async (c) => {
  const input = await c.req.json();
  const post = input.post;
  const subreddit = input.subreddit;

  // IMPORTANT: Use context-aware fetch for Reddit permissions
  const redditFetch = (c.env as any)?.context?.fetch || fetch;
  const targetUrl = `${BACKEND_URL}/analyze/`;

  console.log(`Sending post ${post.id} to: ${targetUrl}`);

  try {
    const response = await redditFetch(targetUrl, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        post_id: post.id,
        title: post.title,
        content: post.body || post.title,
        author: post.authorName,
        subreddit: subreddit.name
      }),
    });
    console.log(`Backend response: ${response.status}`);
  } catch (err) {
    console.error(`Failed to send post to ${targetUrl}:`, err);
  }

  return c.json({ status: 'success' }, 200);
});

triggers.post('/on-comment-submit', async (c) => {
  const input = await c.req.json();
  const comment = input.comment;
  const subreddit = input.subreddit;

  // IMPORTANT: Use context-aware fetch for Reddit permissions
  const redditFetch = (c.env as any)?.context?.fetch || fetch;
  const targetUrl = `${BACKEND_URL}/analyze/`;

  try {
    const response = await redditFetch(targetUrl, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        post_id: comment.id,
        title: "Comment",
        content: comment.body,
        author: comment.authorName,
        subreddit: subreddit.name
      }),
    });
    console.log(`Backend response: ${response.status}`);
  } catch (err) {
    console.error(`Failed to send comment to ${targetUrl}:`, err);
  }

  return c.json({ status: 'success' }, 200);
});
