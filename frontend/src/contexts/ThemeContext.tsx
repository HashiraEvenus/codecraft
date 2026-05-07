import { createContext, useContext, useState, useEffect } from "react";

export type Theme = "dark" | "warm-craft";

interface ThemeContextValue {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  theme: "dark",
  toggleTheme: () => {},
});

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => {
    try {
      return (localStorage.getItem("codecraft:theme") as Theme) || "dark";
    } catch {
      return "dark";
    }
  });

  useEffect(() => {
    document.body.classList.remove("theme-dark", "theme-warm-craft");
    document.body.classList.add(`theme-${theme}`);
    try {
      localStorage.setItem("codecraft:theme", theme);
    } catch {}
  }, [theme]);

  const toggleTheme = () =>
    setTheme((t) => (t === "dark" ? "warm-craft" : "dark"));

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}
