import { CheckCircle2, XCircle, Terminal } from "lucide-react";
import type { ExecutionResult, TestSummary } from "../types";

interface Props {
  runResult: ExecutionResult | null;
  testResult: TestSummary | null;
  isRunning: boolean;
  mode: "run" | "test";
}

export default function OutputPanel({ runResult, testResult, isRunning, mode }: Props) {
  if (isRunning) {
    return (
      <div className="flex items-center gap-2 p-4 text-zinc-400 text-sm">
        <span className="animate-spin inline-block h-4 w-4 border-2 border-zinc-600 border-t-violet-500 rounded-full" />
        Executing…
      </div>
    );
  }

  if (mode === "run" && runResult) {
    const hasError = runResult.stderr || runResult.exit_code !== 0;
    return (
      <div className="p-4 space-y-2 font-mono text-sm">
        {runResult.stdout && (
          <pre className="text-zinc-200 whitespace-pre-wrap">{runResult.stdout}</pre>
        )}
        {runResult.stderr && (
          <pre className="text-red-400 whitespace-pre-wrap">{runResult.stderr}</pre>
        )}
        {!runResult.stdout && !runResult.stderr && (
          <span className="text-zinc-500">No output.</span>
        )}
        {!hasError && runResult.stdout && (
          <div className="flex items-center gap-1 text-emerald-400 text-xs pt-1">
            <CheckCircle2 className="h-3.5 w-3.5" />
            Exited cleanly
          </div>
        )}
      </div>
    );
  }

  if (mode === "test" && testResult) {
    return (
      <div className="p-4 space-y-3">
        <div className="flex items-center gap-2 text-sm font-medium">
          {testResult.all_passed ? (
            <CheckCircle2 className="h-4 w-4 text-emerald-400" />
          ) : (
            <XCircle className="h-4 w-4 text-red-400" />
          )}
          <span className={testResult.all_passed ? "text-emerald-400" : "text-red-400"}>
            {testResult.passed_count}/{testResult.total} tests passed
          </span>
        </div>

        <div className="space-y-2">
          {testResult.results.map((r, i) => (
            <div
              key={i}
              className={`rounded-lg border p-3 text-xs font-mono space-y-1 ${
                r.passed
                  ? "border-emerald-800/50 bg-emerald-950/30"
                  : "border-red-800/50 bg-red-950/30"
              }`}
            >
              <div className="flex items-center gap-1.5">
                {r.passed ? (
                  <CheckCircle2 className="h-3.5 w-3.5 text-emerald-400 shrink-0" />
                ) : (
                  <XCircle className="h-3.5 w-3.5 text-red-400 shrink-0" />
                )}
                <span className="text-zinc-400">Input:</span>
                <span className="text-zinc-200">{r.input}</span>
              </div>
              {!r.passed && (
                <>
                  <div className="flex gap-1.5 pl-5">
                    <span className="text-zinc-400">Expected:</span>
                    <span className="text-emerald-300">{r.expected}</span>
                  </div>
                  <div className="flex gap-1.5 pl-5">
                    <span className="text-zinc-400">Got:</span>
                    <span className="text-red-300">{r.actual || "(empty)"}</span>
                  </div>
                </>
              )}
              {r.stderr && (
                <pre className="text-red-400 pl-5 whitespace-pre-wrap text-[11px]">{r.stderr}</pre>
              )}
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="flex items-center gap-2 p-4 text-zinc-500 text-sm">
      <Terminal className="h-4 w-4" />
      Run your code to see output here.
    </div>
  );
}
