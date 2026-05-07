import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { CheckCircle2, Circle, TrendingUp, BookOpen, Layers } from "lucide-react";
import Navbar from "../components/Navbar";
import { api } from "../lib/api";
import { useProgress } from "../hooks/useProgress";
import { CURRICULUM } from "../lib/curriculum";
import type { ChallengeSummary, Difficulty } from "../types";

const DIFFICULTY_ORDER: Difficulty[] = ["beginner", "intermediate", "advanced"];
const DIFFICULTY_COLORS: Record<Difficulty, string> = {
  beginner: "bg-emerald-500",
  intermediate: "bg-amber-500",
  advanced: "bg-red-500",
};
const DIFFICULTY_TEXT: Record<Difficulty, string> = {
  beginner: "text-emerald-400",
  intermediate: "text-amber-400",
  advanced: "text-red-400",
};

export default function StatsPage() {
  const { progress } = useProgress();
  const completedSet = new Set(progress.completedChallengeIds);

  const [library, setLibrary] = useState<ChallengeSummary[]>([]);
  useEffect(() => {
    api.getLibrary().then(setLibrary).catch(() => {});
  }, []);

  const libraryById = Object.fromEntries(library.map((c) => [c.id, c]));

  const totalChallenges = library.length;
  const totalCompleted = progress.totalCompleted;
  const overallPct = totalChallenges > 0 ? Math.round((totalCompleted / totalChallenges) * 100) : 0;

  // Per-difficulty stats
  const diffStats = DIFFICULTY_ORDER.map((diff) => {
    const all = library.filter((c) => c.difficulty === diff);
    const done = all.filter((c) => completedSet.has(c.id)).length;
    return { diff, total: all.length, done };
  });

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />

      <main className="flex-1 mx-auto w-full max-w-4xl px-4 sm:px-6 py-10 space-y-10 animate-fade-in">
        {/* Header */}
        <div className="space-y-1">
          <h1 className="text-2xl font-bold text-zinc-50">Your Progress</h1>
          <p className="text-zinc-400 text-sm">A breakdown of what you've completed across the curriculum.</p>
        </div>

        {/* Overall card */}
        <div className="card p-6 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <TrendingUp className="h-5 w-5 text-violet-400" />
              <span className="font-semibold text-zinc-100">Overall Completion</span>
            </div>
            <span className="text-2xl font-bold text-zinc-50">{overallPct}%</span>
          </div>
          <div className="h-3 rounded-full bg-zinc-800 overflow-hidden">
            <div
              className="h-full rounded-full bg-gradient-to-r from-violet-600 to-violet-400 transition-all duration-500"
              style={{ width: `${overallPct}%` }}
            />
          </div>
          <div className="flex items-center justify-between text-sm text-zinc-400">
            <span>{totalCompleted} completed</span>
            <span>{totalChallenges - totalCompleted} remaining</span>
          </div>
        </div>

        {/* Per-difficulty breakdown */}
        <div className="space-y-3">
          <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">By Difficulty</h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {diffStats.map(({ diff, total, done }) => {
              const pct = total > 0 ? Math.round((done / total) * 100) : 0;
              return (
                <div key={diff} className="card p-4 space-y-3">
                  <div className="flex items-center justify-between">
                    <span className={`text-sm font-medium capitalize ${DIFFICULTY_TEXT[diff]}`}>{diff}</span>
                    <span className="text-xs text-zinc-500">{done}/{total}</span>
                  </div>
                  <div className="h-2 rounded-full bg-zinc-800 overflow-hidden">
                    <div
                      className={`h-full rounded-full transition-all duration-500 ${DIFFICULTY_COLORS[diff]}`}
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                  <span className="text-xs text-zinc-500">{pct}% complete</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Per-stage breakdown */}
        <div className="space-y-3">
          <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">By Stage</h2>
          <div className="space-y-2">
            {CURRICULUM.map((stage, i) => {
              const done = stage.challengeIds.filter((id) => completedSet.has(id)).length;
              const total = stage.challengeIds.length;
              const pct = Math.round((done / total) * 100);
              return (
                <div key={stage.id} className="card p-4">
                  <div className="flex items-center gap-3">
                    <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-zinc-800 border border-zinc-700 text-xs font-bold text-zinc-400">
                      {i + 1}
                    </div>
                    <div className="flex-1 min-w-0 space-y-1.5">
                      <div className="flex items-center justify-between gap-2">
                        <span className="text-sm font-medium text-zinc-200 truncate">{stage.title}</span>
                        <span className="text-xs text-zinc-500 shrink-0">{done}/{total}</span>
                      </div>
                      <div className="h-1.5 rounded-full bg-zinc-800 overflow-hidden">
                        <div
                          className="h-full rounded-full bg-violet-500 transition-all duration-500"
                          style={{ width: `${pct}%` }}
                        />
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Recent completions */}
        {progress.completedChallengeIds.length > 0 && (
          <div className="space-y-3">
            <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">Completed Challenges</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {progress.completedChallengeIds.map((id) => {
                const c = libraryById[id];
                if (!c) return null;
                return (
                  <div key={id} className="card p-3 flex items-center gap-3">
                    <CheckCircle2 className="h-4 w-4 text-emerald-400 shrink-0" />
                    <span className="text-sm text-zinc-300 flex-1 min-w-0 truncate">{c.title}</span>
                    <span className="text-xs text-zinc-600 capitalize">{c.difficulty}</span>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {progress.completedChallengeIds.length === 0 && library.length > 0 && (
          <div className="card p-8 text-center space-y-3">
            <Circle className="h-10 w-10 text-zinc-700 mx-auto" />
            <p className="text-zinc-400">No challenges completed yet.</p>
            <Link to="/dashboard" className="btn-primary inline-flex items-center gap-1.5 text-sm">
              <BookOpen className="h-3.5 w-3.5" />
              Start practicing
            </Link>
          </div>
        )}

        <div className="flex items-center justify-center gap-4 text-sm">
          <Link to="/learn" className="text-violet-400 hover:text-violet-300 transition-colors flex items-center gap-1.5">
            <Layers className="h-3.5 w-3.5" />
            Learning Path
          </Link>
          <span className="text-zinc-700">·</span>
          <Link to="/library" className="text-violet-400 hover:text-violet-300 transition-colors flex items-center gap-1.5">
            <BookOpen className="h-3.5 w-3.5" />
            Browse Library
          </Link>
        </div>
      </main>
    </div>
  );
}
