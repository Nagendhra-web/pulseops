"use client";

import {
  LineChart,
  Line,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

type Point = { date: string; value: number };

type Props = {
  title: string;
  data: Point[];
};

export default function TimeSeriesChart({ title, data }: Props) {
  return (
    <div className="rounded-xl bg-slate p-5">
      <div className="mb-4 flex items-center justify-between">
        <h3 className="text-sm uppercase tracking-[0.2em] text-slate-300">
          {title}
        </h3>
      </div>
      <div className="h-56">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="date" tick={{ fill: "#94a3b8", fontSize: 12 }} />
            <YAxis tick={{ fill: "#94a3b8", fontSize: 12 }} />
            <Tooltip contentStyle={{ background: "#0f172a", border: "none" }} />
            <Line
              type="monotone"
              dataKey="value"
              stroke="#38BDF8"
              strokeWidth={2}
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
