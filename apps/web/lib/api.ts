export const API_BASE =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error(`Failed to fetch ${path}`);
  }
  return res.json();
}

export async function fetchMetric(name: string) {
  return fetchJson<{ name: string; points: { date: string; value: number }[] }>(
    `/metrics/${name}`
  );
}

export async function fetchAnomalies() {
  return fetchJson<{
    anomalies: {
      date: string;
      metric: string;
      value: number;
      score: number;
      explanation: string;
      top_dimensions: Record<string, { value: string; count: number }[]>;
    }[];
    total_anomalies: number;
    lookback_days: number;
  }>(`/metrics/anomalies`);
}
