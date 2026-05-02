import { AlertTriangle, ExternalLink, BookOpen } from "lucide-react";
import type { Concept } from "../types";

interface Props {
  concepts: Concept[];
  docsUrl: string;
  language: string;
}

export default function ConceptsPanel({ concepts, docsUrl, language }: Props) {
  if (!concepts?.length) {
    return (
      <div className="flex items-center gap-2 p-5 text-zinc-500 text-sm">
        <BookOpen className="h-4 w-4" />
        No concepts available for this challenge.
      </div>
    );
  }

  return (
    <div className="p-5 space-y-5 animate-fade-in">
      {/* Intro nudge */}
      <p className="text-xs text-zinc-500 leading-relaxed">
        These are the exact concepts you need to solve this challenge.
        Read through them, try the examples, then head back to the editor.
      </p>

      {/* Concept cards */}
      {concepts.map((concept, i) => (
        <div key={i} className="space-y-3">
          <div className="flex items-center gap-2">
            <span className="flex h-5 w-5 items-center justify-center rounded-full bg-violet-600/20 border border-violet-500/30 text-[10px] font-bold text-violet-400">
              {i + 1}
            </span>
            <h3 className="text-sm font-semibold text-zinc-100">{concept.title}</h3>
          </div>

          {/* Explanation */}
          <p className="text-sm text-zinc-300 leading-relaxed pl-7">{concept.explanation}</p>

          {/* Code examples */}
          {concept.examples?.length > 0 && (
            <div className="pl-7 space-y-1.5">
              {concept.examples.map((ex, j) => (
                <pre
                  key={j}
                  className="bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-xs font-mono text-violet-300 overflow-x-auto"
                >
                  {ex}
                </pre>
              ))}
            </div>
          )}

          {/* Watch out */}
          {concept.watch_out && (
            <div className="pl-7">
              <div className="flex items-start gap-2 bg-amber-950/20 border border-amber-800/30 rounded-lg px-3 py-2.5">
                <AlertTriangle className="h-3.5 w-3.5 text-amber-400 shrink-0 mt-0.5" />
                <p className="text-xs text-amber-200/80 leading-relaxed">
                  <span className="font-medium text-amber-300">Watch out: </span>
                  {concept.watch_out}
                </p>
              </div>
            </div>
          )}

          {i < concepts.length - 1 && (
            <div className="pl-7 pt-1">
              <div className="h-px bg-zinc-800/60" />
            </div>
          )}
        </div>
      ))}

      {/* Docs link */}
      {docsUrl && (
        <a
          href={docsUrl}
          target="_blank"
          rel="noreferrer"
          className="flex items-center gap-2 text-xs text-zinc-400 hover:text-violet-300 transition-colors pt-2 border-t border-zinc-800/60"
        >
          <BookOpen className="h-3.5 w-3.5" />
          Official {language} documentation
          <ExternalLink className="h-3 w-3 ml-auto" />
        </a>
      )}
    </div>
  );
}
