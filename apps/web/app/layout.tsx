import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "PulseOps",
  description: "Real-time analytics and anomaly detection platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-midnight text-white">
        {children}
      </body>
    </html>
  );
}
