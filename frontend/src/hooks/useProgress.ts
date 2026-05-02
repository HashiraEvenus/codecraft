import { useState, useCallback } from "react";
import type { UserProgress } from "../types";

const STORAGE_KEY = "codecraft_progress";

function loadProgress(): UserProgress {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw) as Partial<UserProgress>;
      const completedChallengeIds = Array.isArray(parsed.completedChallengeIds)
        ? Array.from(new Set(parsed.completedChallengeIds))
        : [];

      return {
        totalCompleted: completedChallengeIds.length,
        completedChallengeIds,
      };
    }
  } catch {}
  return {
    totalCompleted: 0,
    completedChallengeIds: [],
  };
}

function saveProgress(p: UserProgress) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
}

export function useProgress() {
  const [progress, setProgress] = useState<UserProgress>(() => loadProgress());

  const markCompleted = useCallback((challengeId: string) => {
    setProgress((prev) => {
      if (prev.completedChallengeIds.includes(challengeId)) {
        return prev;
      }

      const completedChallengeIds = [...prev.completedChallengeIds, challengeId];
      const updated = {
        totalCompleted: completedChallengeIds.length,
        completedChallengeIds,
      };
      saveProgress(updated);
      return updated;
    });
  }, []);

  const unmarkCompleted = useCallback((challengeId: string) => {
    setProgress((prev) => {
      const completedChallengeIds = prev.completedChallengeIds.filter((id) => id !== challengeId);
      const updated = {
        totalCompleted: completedChallengeIds.length,
        completedChallengeIds,
      };
      saveProgress(updated);
      return updated;
    });
  }, []);

  const toggleCompleted = useCallback((challengeId: string) => {
    setProgress((prev) => {
      const isCompleted = prev.completedChallengeIds.includes(challengeId);
      const completedChallengeIds = isCompleted
        ? prev.completedChallengeIds.filter((id) => id !== challengeId)
        : [...prev.completedChallengeIds, challengeId];
      const updated = {
        totalCompleted: completedChallengeIds.length,
        completedChallengeIds,
      };
      saveProgress(updated);
      return updated;
    });
  }, []);

  const isCompleted = useCallback(
    (challengeId: string) => progress.completedChallengeIds.includes(challengeId),
    [progress.completedChallengeIds]
  );

  return { progress, markCompleted, unmarkCompleted, toggleCompleted, isCompleted };
}
