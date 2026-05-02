import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  Brackets, Cpu, Database, Layers, CheckCircle2, Terminal,
  Sparkles, Loader2, AlertCircle, BookOpen,
} from "lucide-react";
import Navbar from "../components/Navbar";
import { api } from "../lib/api";
import { useProgress } from "../hooks/useProgress";
import type { Difficulty, Language, Topic } from "../types";

const ICON_MAP: Record<string, React.ElementType> = {
  Brackets, Cpu, Database, Layers, CheckCircle2, Terminal,
};

const DIFFICULTIES: { value: Difficulty; label: string; desc: string }[] = [
  { value: "beginner", label: "Beginner", desc: "Loops, conditions, basic logic" },
  { value: "intermediate", label: "Intermediate", desc: "Algorithms, data structures" },
  { value: "advanced", label: "Advanced", desc: "Optimization, complex patterns" },
];

const LANGUAGES: { value: Language; label: string }[] = [
  { value: "python", label: "Python" },
  { value: "javascript", label: "JavaScript" },
  { value: "typescript", label: "TypeScript" },
];

export default function Dashboard() {
  const navigate = useNavigate();
  const { progress } = useProgress();

  const [topics, setTopics] = useState<Topic[]>([]);
  const [selectedTopic, setSelectedTopic] = useState<string>("");
  const [difficulty, setDifficulty] = useState<Difficulty>("beginner");
  const [language, setLanguage] = useState<Language>("python");
  const [includeCompleted, setIncludeCompleted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    api.getTopics().then(setTopics).catch(() => {});
  }, []);

  async function handleGenerate() {
    if (!selectedTopic) return;

    setLoading(true);
    setError("");

    try {
      const excludedIds = includeCompleted ? [] : progress.completedChallengeIds;
      const challenge = await api.generateChallenge(selectedTopic, difficulty, language, excludedIds);
      navigate("/challenge", { state: { challenge } });
    } catch {
      setError(
        includeCompleted
          ? "Failed to generate challenge. Is the backend running?"
          : "No fresh matching challenge found. Try enabling completed exercises or choosing another topic."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 sm:px-6 py-10 space-y-10 animate-fade-in">
        {/* Header */}
        <div className="space-y-1">
          <h1 className="text-2xl font-bold text-zinc-50">What will you build today?</h1>
          <p className="text-zinc-400 text-sm">
            Pick a topic, set the difficulty, and generate a local practice challenge.
          </p>
        </div>

        <div className="card p-4 flex items-start gap-3 text-sm text-zinc-300">
          <Sparkles className="h-4 w-4 text-violet-400 mt-0.5 shrink-0" />
          <div className="flex-1">
            <div className="font-medium text-zinc-100">Local-first personal practice</div>
            <p className="text-zinc-500 mt-1">
              AI-assisted challenges come from the bundled exercise library, and code runs on your own machine.
            </p>
          </div>
          <Link to="/library" className="btn-outline text-xs flex items-center gap-1.5 shrink-0">
            <BookOpen className="h-3.5 w-3.5" />
            View Library
          </Link>
        </div>

        {/* Topic selection */}
        <div className="space-y-3">
          <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">Choose a Topic</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {topics.map((topic) => {
              const Icon = ICON_MAP[topic.icon] ?? Brackets;
              const isSelected = selectedTopic === topic.id;
              return (
                <button
                  key={topic.id}
                  onClick={() => setSelectedTopic(topic.id)}
                  className={`card p-4 text-left space-y-2 transition-all duration-150 hover:border-zinc-600 ${
                    isSelected
                      ? "border-violet-500/60 bg-violet-950/20 ring-1 ring-violet-500/20"
                      : ""
                  }`}
                >
                  <div className={`flex h-8 w-8 items-center justify-center rounded-lg transition-colors ${
                    isSelected ? "bg-violet-600/20 border border-violet-500/30" : "bg-zinc-800 border border-zinc-700"
                  }`}>
                    <Icon className={`h-4 w-4 ${isSelected ? "text-violet-400" : "text-zinc-400"}`} />
                  </div>
                  <div>
                    <div className={`text-sm font-medium ${isSelected ? "text-violet-300" : "text-zinc-200"}`}>
                      {topic.name}
                    </div>
                    <div className="text-xs text-zinc-500 leading-relaxed mt-0.5">{topic.description}</div>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Difficulty */}
        <div className="space-y-3">
          <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">Difficulty</h2>
          <div className="flex flex-wrap gap-2">
            {DIFFICULTIES.map(({ value, label, desc }) => (
              <button
                key={value}
                onClick={() => setDifficulty(value)}
                className={`flex-1 min-w-[140px] card p-3 text-left transition-all duration-150 hover:border-zinc-600 ${
                  difficulty === value ? "border-violet-500/60 bg-violet-950/20 ring-1 ring-violet-500/20" : ""
                }`}
              >
                <div className={`text-sm font-medium ${difficulty === value ? "text-violet-300" : "text-zinc-200"}`}>
                  {label}
                </div>
                <div className="text-xs text-zinc-500 mt-0.5">{desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Language */}
        <div className="space-y-3">
          <h2 className="text-sm font-medium text-zinc-300 uppercase tracking-wide">Language</h2>
          <div className="flex gap-2 flex-wrap">
            {LANGUAGES.map(({ value, label }) => (
              <button
                key={value}
                onClick={() => setLanguage(value)}
                className={`px-4 py-2 rounded-lg text-sm font-medium border transition-all duration-150 ${
                  language === value
                    ? "bg-violet-600 border-violet-500 text-white"
                    : "bg-zinc-900 border-zinc-700 text-zinc-300 hover:border-zinc-500"
                }`}
              >
                {label}
              </button>
            ))}
          </div>
        </div>

        {/* Practice mode */}
        <label className="card p-4 flex items-start gap-3 cursor-pointer hover:border-zinc-700 transition-colors">
          <input
            type="checkbox"
            checked={includeCompleted}
            onChange={(event) => setIncludeCompleted(event.target.checked)}
            className="mt-1 h-4 w-4 accent-violet-500"
          />
          <span>
            <span className="block text-sm font-medium text-zinc-100">Include completed exercises</span>
            <span className="block text-sm text-zinc-500 mt-1">
              Keep this off for fresh practice. Turn it on when you want to retest solved challenges.
            </span>
          </span>
        </label>

        {/* Error */}
        {error && (
          <div className="flex items-center gap-2 text-sm text-red-400 bg-red-950/20 border border-red-800/30 rounded-lg p-3">
            <AlertCircle className="h-4 w-4 shrink-0" />
            {error}
          </div>
        )}

        {/* Generate */}
        <button
          onClick={handleGenerate}
          disabled={!selectedTopic || loading}
          className="btn-primary w-full py-3 text-base flex items-center justify-center gap-2"
        >
          {loading ? (
            <>
              <Loader2 className="h-4 w-4 animate-spin" />
              Generating your challenge…
            </>
          ) : (
            <>
              <Sparkles className="h-4 w-4" />
              Generate Challenge
            </>
          )}
        </button>

        {/* Stats footer */}
        <div className="text-center text-xs text-zinc-600 space-y-2">
          <div>{progress.totalCompleted} total challenges completed</div>
          <Link to="/library" className="text-violet-400 hover:text-violet-300 transition-colors">
            Track progress in the exercise library
          </Link>
        </div>
      </main>
    </div>
  );
}
