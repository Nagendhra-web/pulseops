type Anomaly = {
  date: string;
  metric: string;
  value: number;
  score: number;
  explanation: string;
};

type Props = {
  anomalies: Anomaly[];
};

export default function AnomalyFeed({ anomalies }: Props) {
  return (
    <div className="rounded-xl bg-slate p-5">
      <h3 className="text-sm uppercase tracking-[0.2em] text-slate-300">
        Anomalies
      </h3>
      <div className="mt-4 space-y-4">
        {anomalies.length === 0 ? (
          <p className="text-sm text-slate-400">No anomalies detected.</p>
        ) : (
          anomalies.map((anomaly) => (
            <div
              key={`${anomaly.metric}-${anomaly.date}`}
              className="rounded-lg border border-slate-700 p-4"
            >
              <div className="flex items-center justify-between">
                <p className="text-sm font-semibold uppercase text-accent">
                  {anomaly.metric}
                </p>
                <p className="text-xs text-slate-400">{anomaly.date}</p>
              </div>
              <p className="mt-2 text-sm text-slate-200">
                {anomaly.explanation}
              </p>
              <p className="mt-2 text-xs text-slate-500">
                Value: {anomaly.value.toFixed(2)} · Score:{" "}
                {anomaly.score.toFixed(2)}
              </p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
