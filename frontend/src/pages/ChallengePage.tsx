import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ArrowLeft, Play, FlaskConical, CheckCircle2, XCircle, Loader2 } from "lucide-react";
import Navbar from "../components/Navbar";
import Editor from "../components/Editor";
import OutputPanel from "../components/OutputPanel";
import ChallengePanel from "../components/ChallengePanel";
import DifficultyBadge from "../components/DifficultyBadge";
import { api } from "../lib/api";
import type { Challenge, ExecutionResult, TestSummary } from "../types";

export default function ChallengePage() {
  const { state } = useLocation() as { state: { challenge: Challenge } | null };
  const navigate = useNavigate();

  const challenge: Challenge | null = state?.challenge ?? null;

  const [code, setCode] = useState(challenge?.starter_code ?? "");
  const [runResult, setRunResult] = useState<ExecutionResult | null>(null);
  const [testResult, setTestResult] = useState<TestSummary | null>(null);
  const [outputMode, setOutputMode] = useState<"run" | "test">("run");
  const [isRunning, setIsRunning] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"idle" | "pass" | "fail">("idle");

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

  async function handleSubmit() {
    setIsRunning(true);
    setOutputMode("test");
    setTestResult(null);
    setSubmitStatus("idle");
    try {
      const result = await api.testCode(challenge!.language, code, challenge!.test_cases);
      setTestResult(result);
      setSubmitStatus(result.all_passed ? "pass" : "fail");
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
            className="flex items-center gap-1.5 bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 text-zinc-200 text-sm font-medium px-3 py-1.5 rounded-lg transition-colors disabled:opacity-50"
          >
            {isRunning && outputMode === "run" ? (
              <Loader2 className="h-3.5 w-3.5 animate-spin" />
            ) : (
              <Play className="h-3.5 w-3.5 text-emerald-400" />
            )}
            Run
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
            <Editor language={challenge.language} value={code} onChange={setCode} />
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
