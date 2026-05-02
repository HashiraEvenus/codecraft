import type { Difficulty } from "../types";

export const DIFFICULTY_COLORS: Record<Difficulty, string> = {
  beginner: "text-emerald-400 bg-emerald-400/10 border-emerald-400/20",
  intermediate: "text-amber-400 bg-amber-400/10 border-amber-400/20",
  advanced: "text-red-400 bg-red-400/10 border-red-400/20",
};

export const LANGUAGE_LABELS: Record<string, string> = {
  python: "Python",
  javascript: "JavaScript",
  typescript: "TypeScript",
};

export const LANGUAGE_MONACO: Record<string, string> = {
  python: "python",
  javascript: "javascript",
  typescript: "typescript",
};

export function cn(...classes: (string | undefined | false)[]): string {
  return classes.filter(Boolean).join(" ");
}
