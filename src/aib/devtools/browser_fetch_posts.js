// Run this in browser console while logged into metaculus.com
// Fetches individual post data (with resolutions + CP) for all specified post IDs.
// Downloads a combined JSON file when done.

(async () => {
  const POST_IDS = [
    41955, 41956, 41957, 41958, 41959, 41960, 41961, 41962, 41963, 41964,
    41965, 41966, 41967, 41968, 41969, 41970, 41971, 41972, 41973, 41974,
    41976, 41978, 41979, 41980, 41981, 41982, 41983, 41984, 41985, 41986,
    41987, 41988, 41989, 41990, 41991, 41992, 41993, 41994, 41995, 41996,
    41997, 41998, 41999, 42000, 42001, 42002, 42003, 42004, 42005, 42006,
    42007, 42008, 42009, 42010, 42011, 42012, 42014
  ];

  const DELAY_MS = 30000; // 3 seconds between requests
  const results = [];
  const errors = [];

  console.log(`Fetching ${POST_IDS.length} posts...`);

  for (let i = 0; i < POST_IDS.length; i++) {
    const id = POST_IDS[i];
    try {
      console.log(`[${i + 1}/${POST_IDS.length}] Fetching post ${id}...`);
      const resp = await fetch(`/api/posts/${id}/`, {
        headers: { 'Accept': 'application/json' }
      });

      if (resp.status === 429) {
        const retryAfter = resp.headers.get('Retry-After');
        const wait = retryAfter ? parseInt(retryAfter) * 1000 : 30000;
        console.warn(`Rate limited on ${id}, waiting ${wait/1000}s...`);
        await new Promise(r => setTimeout(r, wait));
        // Retry once
        const retry = await fetch(`/api/posts/${id}/`, {
          headers: { 'Accept': 'application/json' }
        });
        if (retry.ok) {
          results.push(await retry.json());
        } else {
          errors.push({ id, status: retry.status });
        }
      } else if (resp.ok) {
        results.push(await resp.json());
      } else {
        errors.push({ id, status: resp.status });
      }
    } catch (e) {
      console.error(`Error fetching ${id}:`, e);
      errors.push({ id, error: e.message });
    }

    if (i < POST_IDS.length - 1) {
      await new Promise(r => setTimeout(r, DELAY_MS));
    }
  }

  console.log(`Done! ${results.length} fetched, ${errors.length} errors`);
  if (errors.length > 0) console.warn('Errors:', errors);

  // Download as JSON
  const blob = new Blob([JSON.stringify(results, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'minibench_posts.json';
  a.click();
  URL.revokeObjectURL(url);
  console.log('Downloaded minibench_posts.json');
})();
