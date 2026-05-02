import { useState } from "react";
import { Lightbulb, Eye, ChevronDown, ChevronUp, BookOpen, FileText } from "lucide-react";
import type { Challenge } from "../types";
import DifficultyBadge from "./DifficultyBadge";
import ConceptsPanel from "./ConceptsPanel";
import { LANGUAGE_LABELS } from "../lib/utils";

interface Props {
  challenge: Challenge;
  showSolution: boolean;
  onShowSolution: () => void;
}

type Tab = "challenge" | "reference";

export default function ChallengePanel({ challenge, showSolution, onShowSolution }: Props) {
  const [tab, setTab] = useState<Tab>("challenge");
  const [hintVisible, setHintVisible] = useState(false);
  const [casesExpanded, setCasesExpanded] = useState(false);

  return (
    <div className="h-full flex flex-col">
      {/* Tabs */}
      <div className="flex border-b border-zinc-800 shrink-0">
        <button
          onClick={() => setTab("challenge")}
          className={`flex items-center gap-1.5 px-4 py-3 text-sm font-medium border-b-2 transition-colors ${
            tab === "challenge"
              ? "border-violet-500 text-violet-300"
              : "border-transparent text-zinc-500 hover:text-zinc-300"
          }`}
        >
          <FileText className="h-3.5 w-3.5" />
          Challenge
        </button>
        <button
          onClick={() => setTab("reference")}
          className={`flex items-center gap-1.5 px-4 py-3 text-sm font-medium border-b-2 transition-colors ${
            tab === "reference"
              ? "border-violet-500 text-violet-300"
              : "border-transparent text-zinc-500 hover:text-zinc-300"
          }`}
        >
          <BookOpen className="h-3.5 w-3.5" />
          Reference
          {challenge.concepts?.length > 0 && (
            <span className="ml-1 flex h-4 w-4 items-center justify-center rounded-full bg-violet-600/30 text-[10px] text-violet-300">
              {challenge.concepts.length}
            </span>
          )}
        </button>
      </div>

      {/* Tab content */}
      <div className="flex-1 overflow-y-auto">
        {tab === "challenge" && (
          <div className="p-5 space-y-5 animate-fade-in">
            {/* Header */}
            <div className="space-y-2">
              <div className="flex items-center gap-2 flex-wrap">
                <DifficultyBadge difficulty={challenge.difficulty} />
                <span className="text-xs text-zinc-500 bg-zinc-800 px-2 py-0.5 rounded-md border border-zinc-700">
                  {LANGUAGE_LABELS[challenge.language] ?? challenge.language}
                </span>
                <span className="text-xs text-zinc-500 bg-zinc-800 px-2 py-0.5 rounded-md border border-zinc-700 capitalize">
                  {challenge.topic}
                </span>
              </div>
              <h2 className="text-lg font-semibold text-zinc-50 leading-snug">{challenge.title}</h2>
            </div>

            {/* Description */}
            <div className="text-sm text-zinc-300 leading-relaxed whitespace-pre-wrap">
              {challenge.description}
            </div>

            {/* Reference nudge */}
            {challenge.concepts?.length > 0 && (
              <button
                onClick={() => setTab("reference")}
                className="flex items-center gap-2 text-xs text-violet-400 hover:text-violet-300 bg-violet-950/20 border border-violet-800/30 rounded-lg px-3 py-2 w-full transition-colors"
              >
                <BookOpen className="h-3.5 w-3.5 shrink-0" />
                <span>
                  Need a refresher? View the{" "}
                  <span className="font-medium">{challenge.concepts.length} concepts</span> for this challenge →
                </span>
              </button>
            )}

            {/* Test Cases */}
            <div className="card overflow-hidden">
              <button
                className="w-full flex items-center justify-between px-4 py-3 text-sm font-medium text-zinc-300 hover:text-zinc-50 transition-colors"
                onClick={() => setCasesExpanded((v) => !v)}
              >
                <span>Test Cases ({challenge.test_cases.length})</span>
                {casesExpanded ? (
                  <ChevronUp className="h-4 w-4 text-zinc-500" />
                ) : (
                  <ChevronDown className="h-4 w-4 text-zinc-500" />
                )}
              </button>

              {casesExpanded && (
                <div className="border-t border-zinc-800 divide-y divide-zinc-800/60">
                  {challenge.test_cases.map((tc, i) => (
                    <div key={i} className="px-4 py-3 font-mono text-xs space-y-1">
                      <div className="flex gap-2">
                        <span className="text-zinc-500 w-16 shrink-0">Input</span>
                        <span className="text-violet-300">{tc.input}</span>
                      </div>
                      <div className="flex gap-2">
                        <span className="text-zinc-500 w-16 shrink-0">Output</span>
                        <span className="text-emerald-300">{tc.expected_output}</span>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Hint */}
            <div>
              <button
                className="flex items-center gap-2 text-sm text-amber-400 hover:text-amber-300 transition-colors"
                onClick={() => setHintVisible((v) => !v)}
              >
                <Lightbulb className="h-4 w-4" />
                {hintVisible ? "Hide hint" : "Show hint"}
              </button>
              {hintVisible && (
                <p className="mt-2 text-sm text-zinc-300 bg-amber-950/20 border border-amber-800/30 rounded-lg p-3 leading-relaxed animate-slide-up">
                  {challenge.hint}
                </p>
              )}
            </div>

            {/* Solution */}
            <div>
              {!showSolution ? (
                <button
                  className="flex items-center gap-2 text-sm text-zinc-400 hover:text-zinc-200 transition-colors"
                  onClick={onShowSolution}
                >
                  <Eye className="h-4 w-4" />
                  Reveal solution
                </button>
              ) : (
                <div className="space-y-2 animate-slide-up">
                  <div className="flex items-center gap-2 text-sm text-zinc-400">
                    <Eye className="h-4 w-4" />
                    Solution
                  </div>
                  <pre className="card p-4 text-xs text-emerald-300 font-mono overflow-x-auto whitespace-pre-wrap leading-relaxed">
                    {challenge.solution}
                  </pre>
                </div>
              )}
            </div>
          </div>
        )}

        {tab === "reference" && (
          <ConceptsPanel
            concepts={challenge.concepts ?? []}
            docsUrl={challenge.docs_url ?? ""}
            language={challenge.language}
          />
        )}
      </div>
    </div>
  );
}
