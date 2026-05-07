import { useState, useEffect, useRef } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ArrowLeft, Play, FlaskConical, CheckCircle2, XCircle, Loader2, ChevronRight } from "lucide-react";
import Navbar from "../components/Navbar";
import Editor from "../components/Editor";
import OutputPanel from "../components/OutputPanel";
import ChallengePanel from "../components/ChallengePanel";
import DifficultyBadge from "../components/DifficultyBadge";
import { api } from "../lib/api";
import { useProgress } from "../hooks/useProgress";
import { CURRICULUM } from "../lib/curriculum";
import type { Challenge, ExecutionResult, TestSummary } from "../types";

function getNextPathId(currentId: string): string | null {
  const allIds = CURRICULUM.flatMap((s) => s.challengeIds);
  const idx = allIds.indexOf(currentId);
  if (idx === -1 || idx >= allIds.length - 1) return null;
  return allIds[idx + 1];
}

export default function ChallengePage() {
  const { state } = useLocation() as { state: { challenge: Challenge } | null };
  const navigate = useNavigate();
  const { markCompleted, isCompleted } = useProgress();

  const challenge: Challenge | null = state?.challenge ?? null;

  const [code, setCode] = useState(() => {
    if (!challenge) return "";
    try {
      return localStorage.getItem(`codecraft:code:${challenge.id}`) ?? challenge.starter_code;
    } catch {
      return challenge.starter_code;
    }
  });

  const [runResult, setRunResult] = useState<ExecutionResult | null>(null);
  const [testResult, setTestResult] = useState<TestSummary | null>(null);
  const [outputMode, setOutputMode] = useState<"run" | "test">("run");
  const [isRunning, setIsRunning] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"idle" | "pass" | "fail">("idle");
  const [loadingNext, setLoadingNext] = useState(false);

  // Debounce-save code to localStorage whenever it changes
  useEffect(() => {
    if (!challenge) return;
    const key = `codecraft:code:${challenge.id}`;
    const timer = setTimeout(() => {
      try { localStorage.setItem(key, code); } catch {}
    }, 500);
    return () => clearTimeout(timer);
  }, [code, challenge?.id]);

  // Reset all state when navigating challenge → challenge (same route, new state)
  const prevIdRef = useRef(challenge?.id);
  useEffect(() => {
    if (!challenge || challenge.id === prevIdRef.current) return;
    prevIdRef.current = challenge.id;
    try {
      setCode(localStorage.getItem(`codecraft:code:${challenge.id}`) ?? challenge.starter_code);
    } catch {
      setCode(challenge.starter_code);
    }
    setRunResult(null);
    setTestResult(null);
    setOutputMode("run");
    setShowSolution(false);
    setSubmitStatus("idle");
  }, [challenge?.id]);

  if (!challenge) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center space-y-4">
          <p className="text-zinc-400">No challenge loaded.</p>
          <button onClick={() => navigate("/dashboard")} className="btn-primary">
            Go to Dashboard
          </button>
        </div>
      </div>
    );
  }

  async function handleRun() {
    setIsRunning(true);
    setOutputMode("run");
    setRunResult(null);
    try {
      const result = await api.runCode(challenge!.language, code);
      setRunResult(result);
    } catch {
      setRunResult({ stdout: "", stderr: "Execution service unavailable.", exit_code: 1 });
    } finally {
      setIsRunning(false);
    }
  }

  const nextPathId = getNextPathId(challenge.id);

  async function handleNextChallenge() {
    if (!nextPathId || loadingNext) return;
    setLoadingNext(true);
    try {
      const next = await api.getChallenge(nextPathId);
      navigate("/challenge", { state: { challenge: next } });
    } catch {
      setLoadingNext(false);
    }
  }

  async function handleSubmit() {
    setIsRunning(true);
    setOutputMode("test");
    setTestResult(null);
    setSubmitStatus("idle");
    try {
      const result = await api.testCode(challenge!.language, code, challenge!.test_cases);
      setTestResult(result);
      setSubmitStatus(result.all_passed ? "pass" : "fail");
      if (result.all_passed) {
        markCompleted(challenge!.id);
      }
    } catch {
      setTestResult(null);
    } finally {
      setIsRunning(false);
    }
  }

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      <Navbar />

      {/* Top bar */}
      <div className="flex items-center gap-3 px-4 py-2.5 border-b border-zinc-800 bg-zinc-900/60 flex-wrap">
        <button
          onClick={() => navigate("/dashboard")}
          className="flex items-center gap-1.5 text-sm text-zinc-400 hover:text-zinc-200 transition-colors"
        >
          <ArrowLeft className="h-4 w-4" />
          Dashboard
        </button>

        <div className="h-4 w-px bg-zinc-700" />

        <span className="text-sm font-medium text-zinc-200 flex-1 min-w-0 truncate">
          {challenge.title}
        </span>

        <DifficultyBadge difficulty={challenge.difficulty} />

        {/* Submit status badge */}
        {submitStatus === "pass" && (
          <div className="flex items-center gap-1.5 text-xs text-emerald-400 bg-emerald-950/30 border border-emerald-800/40 px-2.5 py-1 rounded-full">
            <CheckCircle2 className="h-3.5 w-3.5" />
            All tests passed!
          </div>
        )}
        {submitStatus === "pass" && nextPathId && (
          <button
            onClick={handleNextChallenge}
            disabled={loadingNext}
            className="flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg btn-primary disabled:opacity-60"
          >
            {loadingNext ? <Loader2 className="h-3 w-3 animate-spin" /> : <ChevronRight className="h-3 w-3" />}
            Next Challenge
          </button>
        )}
        {submitStatus !== "pass" && isCompleted(challenge.id) && (
          <div className="flex items-center gap-1.5 text-xs text-emerald-400 bg-emerald-950/30 border border-emerald-800/40 px-2.5 py-1 rounded-full">
            <CheckCircle2 className="h-3.5 w-3.5" />
            Completed
          </div>
        )}
        {submitStatus === "fail" && (
          <div className="flex items-center gap-1.5 text-xs text-red-400 bg-red-950/30 border border-red-800/40 px-2.5 py-1 rounded-full">
            <XCircle className="h-3.5 w-3.5" />
            Some tests failed
          </div>
        )}

        <div className="flex items-center gap-2 ml-auto">
          <button
            onClick={handleRun}
            disabled={isRunning}
            title="Run code (Ctrl+Enter)"
            className="flex items-center gap-1.5 bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 text-zinc-200 text-sm font-medium px-3 py-1.5 rounded-lg transition-colors disabled:opacity-50"
          >
            {isRunning && outputMode === "run" ? (
              <Loader2 className="h-3.5 w-3.5 animate-spin" />
            ) : (
              <Play className="h-3.5 w-3.5 text-emerald-400" />
            )}
            Run
            <kbd className="hidden sm:inline text-xs text-zinc-600 font-mono">⌘↵</kbd>
          </button>
          <button
            onClick={handleSubmit}
            disabled={isRunning}
            className="btn-primary flex items-center gap-1.5 text-sm px-3 py-1.5"
          >
            {isRunning && outputMode === "test" ? (
              <Loader2 className="h-3.5 w-3.5 animate-spin" />
            ) : (
              <FlaskConical className="h-3.5 w-3.5" />
            )}
            Submit
          </button>
        </div>
      </div>

      {/* Main split layout */}
      <div className="flex-1 overflow-hidden flex">
        {/* Left: challenge panel */}
        <div className="w-[380px] shrink-0 border-r border-zinc-800 overflow-y-auto">
          <ChallengePanel
            challenge={challenge}
            showSolution={showSolution}
            onShowSolution={() => setShowSolution(true)}
          />
        </div>

        {/* Right: editor + output */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Editor — takes available space */}
          <div className="flex-1 overflow-hidden">
            <Editor language={challenge.language} value={code} onChange={setCode} onRun={handleRun} />
          </div>

          {/* Output panel */}
          <div className="h-52 shrink-0 border-t border-zinc-800 bg-zinc-900/60 overflow-y-auto">
            <div className="flex items-center gap-3 px-4 py-2 border-b border-zinc-800/60">
              <button
                onClick={() => setOutputMode("run")}
                className={`text-xs font-medium transition-colors ${outputMode === "run" ? "text-zinc-200" : "text-zinc-500 hover:text-zinc-300"}`}
              >
                Output
              </button>
              <button
                onClick={() => setOutputMode("test")}
                className={`text-xs font-medium transition-colors ${outputMode === "test" ? "text-zinc-200" : "text-zinc-500 hover:text-zinc-300"}`}
              >
                Test Results
              </button>
            </div>
            <OutputPanel
              runResult={runResult}
              testResult={testResult}
              isRunning={isRunning}
              mode={outputMode}
            />
          </div>
        </div>
      </div>

    </div>
  );
}
