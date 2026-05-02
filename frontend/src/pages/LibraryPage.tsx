import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  BookOpen,
  CheckCircle2,
  Circle,
  Loader2,
  Play,
  RotateCcw,
} from "lucide-react";
import Navbar from "../components/Navbar";
import DifficultyBadge from "../components/DifficultyBadge";
import { api } from "../lib/api";
import { LANGUAGE_LABELS } from "../lib/utils";
import { useProgress } from "../hooks/useProgress";
import type { ChallengeSummary, Difficulty, Topic } from "../types";

const DIFFICULTIES: Difficulty[] = ["beginner", "intermediate", "advanced"];

type StatusFilter = "all" | "open" | "completed";

export default function LibraryPage() {
  const navigate = useNavigate();
  const { progress, toggleCompleted, isCompleted } = useProgress();

  const [topics, setTopics] = useState<Topic[]>([]);
  const [library, setLibrary] = useState<ChallengeSummary[]>([]);
  const [statusFilter, setStatusFilter] = useState<StatusFilter>("all");
  const [loading, setLoading] = useState(true);
  const [openingId, setOpeningId] = useState<string | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadLibrary() {
      try {
        const [topicData, libraryData] = await Promise.all([
          api.getTopics(),
          api.getLibrary(),
        ]);
        setTopics(topicData);
        setLibrary(libraryData);
      } catch {
        setError("Could not load the exercise library. Is the backend running?");
      } finally {
        setLoading(false);
      }
    }

    loadLibrary();
  }, []);

  const filteredLibrary = useMemo(() => {
    return library.filter((challenge) => {
      const completed = progress.completedChallengeIds.includes(challenge.id);
      if (statusFilter === "completed") return completed;
      if (statusFilter === "open") return !completed;
      return true;
    });
  }, [library, progress.completedChallengeIds, statusFilter]);

  const completedCount = library.filter((challenge) => isCompleted(challenge.id)).length;
  const progressPercent = library.length > 0 ? Math.round((completedCount / library.length) * 100) : 0;

  async function openChallenge(challengeId: string) {
    setOpeningId(challengeId);
    try {
      const challenge = await api.getChallenge(challengeId);
      navigate("/challenge", { state: { challenge } });
    } catch {
      setError("Could not open that challenge.");
    } finally {
      setOpeningId(null);
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />

      <main className="flex-1 mx-auto w-full max-w-6xl px-4 sm:px-6 py-10 space-y-8 animate-fade-in">
        <section className="space-y-4">
          <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
            <div className="space-y-2">
              <div className="inline-flex items-center gap-2 text-xs font-medium text-violet-300 bg-violet-500/10 border border-violet-500/20 px-3 py-1.5 rounded-full">
                <BookOpen className="h-3.5 w-3.5" />
                Exercise Library
              </div>
              <h1 className="text-3xl font-bold text-zinc-50">Track what you have practiced</h1>
              <p className="text-zinc-400 max-w-2xl">
                Browse every challenge by topic and difficulty. Completed exercises are skipped by default on the dashboard, but you can uncheck them here when you want to practice again.
              </p>
            </div>

            <div className="card p-4 min-w-[220px]">
              <div className="flex items-baseline justify-between gap-4">
                <span className="text-sm text-zinc-400">Completed</span>
                <span className="text-2xl font-bold text-zinc-50">{progressPercent}%</span>
              </div>
              <div className="mt-3 h-2 rounded-full bg-zinc-800 overflow-hidden">
                <div
                  className="h-full rounded-full bg-violet-500 transition-all"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
              <div className="mt-2 text-xs text-zinc-500">
                {completedCount} of {library.length} exercises done
              </div>
            </div>
          </div>

          <div className="flex flex-wrap gap-2">
            {(["all", "open", "completed"] as StatusFilter[]).map((filter) => (
              <button
                key={filter}
                onClick={() => setStatusFilter(filter)}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium border capitalize transition-colors ${
                  statusFilter === filter
                    ? "bg-violet-600 border-violet-500 text-white"
                    : "bg-zinc-900 border-zinc-700 text-zinc-300 hover:border-zinc-500"
                }`}
              >
                {filter === "open" ? "Not done" : filter}
              </button>
            ))}
          </div>
        </section>

        {error && (
          <div className="rounded-lg border border-red-800/30 bg-red-950/20 p-3 text-sm text-red-400">
            {error}
          </div>
        )}

        {loading ? (
          <div className="card p-8 flex items-center justify-center gap-2 text-zinc-400">
            <Loader2 className="h-4 w-4 animate-spin" />
            Loading exercise library...
          </div>
        ) : (
          <div className="space-y-6">
            {topics.map((topic) => {
              const topicChallenges = filteredLibrary.filter((challenge) => challenge.topic === topic.id);
              if (topicChallenges.length === 0) return null;

              const topicTotal = library.filter((challenge) => challenge.topic === topic.id).length;
              const topicCompleted = library.filter(
                (challenge) => challenge.topic === topic.id && isCompleted(challenge.id)
              ).length;

              return (
                <section key={topic.id} className="card overflow-hidden">
                  <div className="border-b border-zinc-800 p-5 flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
                    <div>
                      <h2 className="text-lg font-semibold text-zinc-50">{topic.name}</h2>
                      <p className="text-sm text-zinc-500">{topic.description}</p>
                    </div>
                    <div className="text-sm text-zinc-400">
                      {topicCompleted}/{topicTotal} done
                    </div>
                  </div>

                  <div className="divide-y divide-zinc-800/70">
                    {DIFFICULTIES.map((difficulty) => {
                      const challenges = topicChallenges.filter((challenge) => challenge.difficulty === difficulty);
                      if (challenges.length === 0) return null;

                      return (
                        <div key={difficulty} className="p-5 space-y-3">
                          <div className="flex items-center gap-2">
                            <DifficultyBadge difficulty={difficulty} />
                            <span className="text-xs text-zinc-500">
                              {challenges.length} {challenges.length === 1 ? "exercise" : "exercises"}
                            </span>
                          </div>

                          <div className="grid gap-3 md:grid-cols-2">
                            {challenges.map((challenge) => {
                              const completed = isCompleted(challenge.id);
                              return (
                                <article
                                  key={challenge.id}
                                  className={`rounded-xl border p-4 transition-colors ${
                                    completed
                                      ? "border-emerald-800/40 bg-emerald-950/10"
                                      : "border-zinc-800 bg-zinc-950/40 hover:border-zinc-700"
                                  }`}
                                >
                                  <div className="flex items-start gap-3">
                                    <button
                                      onClick={() => toggleCompleted(challenge.id)}
                                      className="mt-0.5 text-zinc-500 hover:text-emerald-400 transition-colors"
                                      aria-label={completed ? "Mark incomplete" : "Mark complete"}
                                    >
                                      {completed ? (
                                        <CheckCircle2 className="h-5 w-5 text-emerald-400" />
                                      ) : (
                                        <Circle className="h-5 w-5" />
                                      )}
                                    </button>

                                    <div className="min-w-0 flex-1 space-y-2">
                                      <div>
                                        <h3 className="font-medium text-zinc-100 leading-snug">{challenge.title}</h3>
                                        <div className="mt-1 flex flex-wrap gap-2 text-xs text-zinc-500">
                                          <span>{LANGUAGE_LABELS[challenge.language] ?? challenge.language}</span>
                                          <span>{challenge.test_count} tests</span>
                                          <span>{challenge.concept_count} concepts</span>
                                        </div>
                                      </div>

                                      <div className="flex flex-wrap gap-2">
                                        <button
                                          onClick={() => openChallenge(challenge.id)}
                                          disabled={openingId === challenge.id}
                                          className="btn-primary text-xs flex items-center gap-1.5 px-3 py-1.5"
                                        >
                                          {openingId === challenge.id ? (
                                            <Loader2 className="h-3.5 w-3.5 animate-spin" />
                                          ) : (
                                            <Play className="h-3.5 w-3.5" />
                                          )}
                                          Practice
                                        </button>
                                        {completed && (
                                          <button
                                            onClick={() => toggleCompleted(challenge.id)}
                                            className="btn-outline text-xs flex items-center gap-1.5 px-3 py-1.5"
                                          >
                                            <RotateCcw className="h-3.5 w-3.5" />
                                            Reset
                                          </button>
                                        )}
                                      </div>
                                    </div>
                                  </div>
                                </article>
                              );
                            })}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </section>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
}
