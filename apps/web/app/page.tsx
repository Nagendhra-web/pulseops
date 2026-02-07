import KpiCard from "../components/KpiCard";
import TimeSeriesChart from "../components/TimeSeriesChart";
import AnomalyFeed from "../components/AnomalyFeed";
import { fetchAnomalies, fetchMetric } from "../lib/api";

function latestValue(points: { date: string; value: number }[]) {
  if (points.length === 0) return 0;
  return points[points.length - 1].value;
}

function sumValues(points: { date: string; value: number }[]) {
  return points.reduce((acc, cur) => acc + cur.value, 0);
}

export default async function DashboardPage() {
  const [dau, revenue, churn, anomalies] = await Promise.all([
    fetchMetric("dau"),
    fetchMetric("revenue"),
    fetchMetric("churn"),
    fetchAnomalies(),
  ]);

  return (
    <main className="mx-auto max-w-6xl space-y-8 px-6 py-10">
      <header className="flex flex-col gap-2">
        <p className="text-xs uppercase tracking-[0.3em] text-slate-400">
          PulseOps
        </p>
        <h1 className="text-3xl font-semibold">Executive Overview</h1>
        <p className="text-sm text-slate-400">
          Real-time KPI monitoring and anomaly intelligence.
        </p>
      </header>

      <section className="grid gap-4 md:grid-cols-3">
        <KpiCard
          title="Daily Active Users"
          value={latestValue(dau.points).toLocaleString()}
          subtitle="Last 24 hours"
        />
        <KpiCard
          title="Revenue"
          value={`$${sumValues(revenue.points).toFixed(2)}`}
          subtitle="30-day rolling"
        />
        <KpiCard
          title="Churn Events"
          value={latestValue(churn.points).toLocaleString()}
          subtitle="Last 24 hours"
        />
      </section>

      <section className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-6">
          <TimeSeriesChart title="Daily Active Users" data={dau.points} />
          <TimeSeriesChart title="Revenue" data={revenue.points} />
          <TimeSeriesChart title="Churn" data={churn.points} />
        </div>
        <AnomalyFeed anomalies={anomalies.anomalies} />
      </section>
    </main>
  );
}
