import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        midnight: "#0F172A",
        slate: "#1E293B",
        accent: "#38BDF8"
      }
    }
  },
  plugins: []
};

export default config;
