import { useState, useCallback } from "react";
import type { UserProgress } from "../types";

const STORAGE_KEY = "codecraft_progress";

function loadProgress(): UserProgress {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
  } catch {}
  return {
    totalCompleted: 0,
  };
}

function saveProgress(p: UserProgress) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
}

export function useProgress() {
  const [progress, setProgress] = useState<UserProgress>(() => loadProgress());

  const recordChallenge = useCallback(() => {
    setProgress((prev) => {
      const updated = {
        ...prev,
        totalCompleted: prev.totalCompleted + 1,
      };
      saveProgress(updated);
      return updated;
    });
  }, []);

  return { progress, recordChallenge };
}
