import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  Brackets, Cpu, Database, Layers, CheckCircle2, Terminal,
  Sparkles, Loader2, AlertCircle,
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
  const { progress, recordChallenge } = useProgress();

  const [topics, setTopics] = useState<Topic[]>([]);
  const [selectedTopic, setSelectedTopic] = useState<string>("");
  const [difficulty, setDifficulty] = useState<Difficulty>("beginner");
  const [language, setLanguage] = useState<Language>("python");
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
      const challenge = await api.generateChallenge(selectedTopic, difficulty, language);
      recordChallenge();
      navigate("/challenge", { state: { challenge } });
    } catch {
      setError("Failed to generate challenge. Is the backend running?");
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
          <div>
            <div className="font-medium text-zinc-100">Local-first personal practice</div>
            <p className="text-zinc-500 mt-1">
              Challenges use your own Gemini key, and code runs on your own machine.
            </p>
          </div>
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
        <div className="text-center text-xs text-zinc-600">
          {progress.totalCompleted} total challenges completed
        </div>
      </main>
    </div>
  );
}
