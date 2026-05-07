import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  BookOpen, Brackets, Cpu, Database, Layers, CheckCircle2, Terminal,
  Loader2, ChevronRight, Trophy, MapPin,
} from "lucide-react";
import Navbar from "../components/Navbar";
import { api } from "../lib/api";
import { useProgress } from "../hooks/useProgress";
import { CURRICULUM } from "../lib/curriculum";
import type { ChallengeSummary } from "../types";

// ─── Icon map (must match icon strings in curriculum.ts) ───────────────────
const STAGE_ICONS: Record<string, React.ElementType> = {
  BookOpen, Brackets, Cpu, Database, Layers, CheckCircle2, Terminal,
};

// ─── Helpers ────────────────────────────────────────────────────────────────
function ProgressBar({
  value,
  max,
  done,
  thin = false,
}: {
  value: number;
  max: number;
  done: boolean;
  thin?: boolean;
}) {
  const pct = max > 0 ? Math.round((value / max) * 100) : 0;
  return (
    <div className={`w-full bg-zinc-800 rounded-full overflow-hidden ${thin ? "h-1" : "h-2"}`}>
      <div
        className={`h-full rounded-full transition-all duration-500 ${
          done ? "bg-emerald-500" : "bg-gradient-to-r from-violet-600 to-violet-400"
        }`}
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}

// ─── Challenge card ──────────────────────────────────────────────────────────
function ChallengeCard({
  challenge,
  completed,
  launching,
  onClick,
}: {
  challenge: ChallengeSummary;
  completed: boolean;
  launching: boolean;
  onClick: () => void;
}) {
  const diffColour: Record<string, string> = {
    beginner:     "text-emerald-400 bg-emerald-400/10 border-emerald-400/20",
    intermediate: "text-amber-400   bg-amber-400/10   border-amber-400/20",
    advanced:     "text-red-400     bg-red-400/10     border-red-400/20",
  };

  return (
    <button
      onClick={onClick}
      className={`group relative text-left p-3 rounded-lg border transition-all duration-150 ${
        completed
          ? "border-emerald-500/40 bg-emerald-950/15 hover:border-emerald-400/60"
          : "border-zinc-700/60 bg-zinc-900/40 hover:border-violet-500/50 hover:bg-zinc-900"
      }`}
    >
      {/* Top row: badge + checkmark */}
      <div className="flex items-start justify-between gap-1 mb-2">
        <span
          className={`inline-flex px-1.5 py-0.5 rounded text-xs font-medium border capitalize ${
            diffColour[challenge.difficulty]
          }`}
        >
          {challenge.difficulty}
        </span>
        {completed && (
          <CheckCircle2 className="h-3.5 w-3.5 text-emerald-400 flex-shrink-0 mt-px" />
        )}
      </div>

      {/* Title */}
      <p
        className={`text-xs font-medium leading-snug ${
          completed
            ? "text-emerald-100/80"
            : "text-zinc-300 group-hover:text-zinc-100"
        }`}
      >
        {challenge.title}
      </p>

      {/* Loading overlay */}
      {launching && (
        <div className="absolute inset-0 flex items-center justify-center bg-zinc-900/70 rounded-lg">
          <Loader2 className="h-4 w-4 animate-spin text-violet-400" />
        </div>
      )}
    </button>
  );
}

// ─── Main page ───────────────────────────────────────────────────────────────
export default function LearnPage() {
  const navigate = useNavigate();
  const { progress } = useProgress();

  const [library, setLibrary] = useState<Record<string, ChallengeSummary>>({});
  const [loadingLib, setLoadingLib] = useState(true);
  const [launching, setLaunching] = useState<string | null>(null);

  useEffect(() => {
    api
      .getLibrary()
      .then((items) => {
        const map: Record<string, ChallengeSummary> = {};
        items.forEach((c) => {
          map[c.id] = c;
        });
        setLibrary(map);
      })
      .catch(() => {})
      .finally(() => setLoadingLib(false));
  }, []);

  const completedSet = new Set(progress.completedChallengeIds);

  // Overall path stats — only count Python challenges that exist in the library
  const pathIds = CURRICULUM.flatMap((s) => s.challengeIds).filter(
    (id) => library[id]
  );
  const totalInPath = pathIds.length;
  const completedInPath = pathIds.filter((id) => completedSet.has(id)).length;
  const overallPct =
    totalInPath > 0 ? Math.round((completedInPath / totalInPath) * 100) : 0;
  const allDoneOverall = totalInPath > 0 && completedInPath === totalInPath;

  // First uncompleted challenge across all stages (for the global "Continue" button)
  const nextGlobalId = CURRICULUM.flatMap((s) => s.challengeIds).find(
    (id) => library[id] && !completedSet.has(id)
  );

  async function launchChallenge(id: string) {
    if (launching) return;
    setLaunching(id);
    try {
      const challenge = await api.getChallenge(id);
      navigate("/challenge", { state: { challenge } });
    } catch {
      setLaunching(null);
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 sm:px-6 py-10 space-y-8 animate-fade-in">

        {/* ── Page header ─────────────────────────────────────────────── */}
        <div className="space-y-1">
          <h1 className="text-2xl font-bold text-zinc-50">Learning Path</h1>
          <p className="text-zinc-400 text-sm">
            A structured curriculum from Python basics to algorithms and data structures.
          </p>
        </div>

        {/* ── Overall progress card ────────────────────────────────────── */}
        <div className="card p-5 space-y-4">
          <div className="flex items-start justify-between gap-4">
            <div>
              <div className="text-zinc-100 font-semibold">Overall Progress</div>
              {loadingLib ? (
                <div className="text-zinc-600 text-sm mt-0.5">Loading challenges…</div>
              ) : (
                <div className="text-zinc-500 text-sm mt-0.5">
                  {completedInPath} of {totalInPath} challenges completed
                </div>
              )}
            </div>

            <div className="text-right flex-shrink-0">
              <div className="text-2xl font-bold text-violet-400">{overallPct}%</div>
              {allDoneOverall && (
                <div className="flex items-center gap-1 text-xs text-emerald-400 justify-end mt-0.5">
                  <Trophy className="h-3 w-3" />
                  Complete!
                </div>
              )}
            </div>
          </div>

          <ProgressBar value={completedInPath} max={totalInPath} done={allDoneOverall} />

          {/* Continue Learning / Start buttons */}
          <div className="flex items-center gap-3">
            {nextGlobalId && (
              <button
                onClick={() => launchChallenge(nextGlobalId)}
                disabled={!!launching}
                className="btn-primary flex items-center gap-2 text-sm disabled:opacity-60"
              >
                {launching === nextGlobalId ? (
                  <>
                    <Loader2 className="h-3.5 w-3.5 animate-spin" />
                    Loading…
                  </>
                ) : (
                  <>
                    <ChevronRight className="h-3.5 w-3.5" />
                    {completedInPath === 0 ? "Start Learning" : "Continue Learning"}
                  </>
                )}
              </button>
            )}
            {allDoneOverall && (
              <span className="text-sm text-emerald-400 font-medium">
                🎉 You've completed every challenge in the path!
              </span>
            )}
          </div>
        </div>

        {/* ── Stage list ───────────────────────────────────────────────── */}
        {loadingLib ? (
          <div className="flex items-center justify-center py-20">
            <Loader2 className="h-6 w-6 animate-spin text-zinc-600" />
          </div>
        ) : (
          <div className="space-y-4">
            {CURRICULUM.map((stage, index) => {
              const Icon = STAGE_ICONS[stage.icon] ?? MapPin;

              // Only show challenges that actually exist in the library
              const stageChallenges = stage.challengeIds
                .map((id) => library[id])
                .filter((c): c is ChallengeSummary => c !== undefined);

              if (stageChallenges.length === 0) return null;

              const stageCompleted = stageChallenges.filter((c) =>
                completedSet.has(c.id)
              ).length;
              const stageDone =
                stageCompleted === stageChallenges.length && stageChallenges.length > 0;

              // First uncompleted in this stage; fall back to first overall for "Review"
              const continueId =
                stage.challengeIds.find(
                  (id) => library[id] && !completedSet.has(id)
                ) ?? stage.challengeIds.find((id) => library[id]);

              return (
                <div key={stage.id} className="card overflow-hidden">

                  {/* Stage header */}
                  <div className="p-4 sm:p-5 border-b border-zinc-800/60">
                    <div className="flex items-start justify-between gap-4">

                      {/* Left: icon + title + progress */}
                      <div className="flex items-start gap-3 min-w-0">
                        <div
                          className={`flex-shrink-0 flex h-9 w-9 items-center justify-center rounded-lg border transition-colors ${
                            stageDone
                              ? "bg-emerald-900/30 border-emerald-500/30"
                              : "bg-violet-600/15 border-violet-500/20"
                          }`}
                        >
                          <Icon
                            className={`h-4 w-4 ${
                              stageDone ? "text-emerald-400" : "text-violet-400"
                            }`}
                          />
                        </div>

                        <div className="flex-1 min-w-0 space-y-2">
                          {/* Title row */}
                          <div className="flex items-center gap-2 flex-wrap">
                            <span className="text-xs font-mono text-zinc-600 tabular-nums">
                              {String(index + 1).padStart(2, "0")}
                            </span>
                            <h2 className="text-sm font-semibold text-zinc-100">
                              {stage.title}
                            </h2>
                            {stageDone && (
                              <span className="inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full bg-emerald-900/40 text-emerald-400 border border-emerald-700/30">
                                <CheckCircle2 className="h-3 w-3" />
                                Complete
                              </span>
                            )}
                          </div>

                          {/* Description */}
                          <p className="text-xs text-zinc-500 leading-relaxed">
                            {stage.description}
                          </p>

                          {/* Progress bar + fraction */}
                          <div className="flex items-center gap-2">
                            <div className="w-28">
                              <ProgressBar
                                value={stageCompleted}
                                max={stageChallenges.length}
                                done={stageDone}
                                thin
                              />
                            </div>
                            <span className="text-xs text-zinc-600 tabular-nums">
                              {stageCompleted}/{stageChallenges.length}
                            </span>
                          </div>
                        </div>
                      </div>

                      {/* Right: Continue / Review button */}
                      {continueId && (
                        <button
                          onClick={() => launchChallenge(continueId)}
                          disabled={!!launching}
                          className="flex-shrink-0 flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg border transition-all duration-150 disabled:opacity-50 border-zinc-700 bg-zinc-800 text-zinc-300 hover:border-zinc-500 hover:text-zinc-100"
                        >
                          {launching === continueId ? (
                            <Loader2 className="h-3 w-3 animate-spin" />
                          ) : (
                            <ChevronRight className="h-3 w-3" />
                          )}
                          {stageDone ? "Review" : "Continue"}
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Challenge grid */}
                  <div className="p-3 sm:p-4 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2">
                    {stageChallenges.map((c) => (
                      <ChallengeCard
                        key={c.id}
                        challenge={c}
                        completed={completedSet.has(c.id)}
                        launching={launching === c.id}
                        onClick={() => launchChallenge(c.id)}
                      />
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* ── Footer ──────────────────────────────────────────────────── */}
        <p className="text-center text-xs text-zinc-600 pb-4">
          More challenges are added regularly — the path grows with the library.
        </p>
      </main>
    </div>
  );
}
