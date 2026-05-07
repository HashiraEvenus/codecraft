import { Sun, Moon } from "lucide-react";
import { useTheme } from "../contexts/ThemeContext";

export default function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();
  const isWarm = theme === "warm-craft";

  return (
    <button
      onClick={toggleTheme}
      title={isWarm ? "Switch to dark mode" : "Switch to warm mode"}
      className="btn-ghost flex items-center gap-1.5 text-sm px-3 py-2"
    >
      {isWarm ? (
        <Moon className="h-4 w-4" />
      ) : (
        <Sun className="h-4 w-4 text-amber-400" />
      )}
      {isWarm ? "Dark" : "Warm"}
    </button>
  );
}
