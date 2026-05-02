import MonacoEditor from "@monaco-editor/react";
import { LANGUAGE_MONACO } from "../lib/utils";

interface Props {
  language: string;
  value: string;
  onChange: (value: string) => void;
}

export default function Editor({ language, value, onChange }: Props) {
  return (
    <div className="h-full w-full overflow-hidden rounded-b-xl">
      <MonacoEditor
        height="100%"
        language={LANGUAGE_MONACO[language] ?? language}
        value={value}
        theme="vs-dark"
        onChange={(v) => onChange(v ?? "")}
        options={{
          fontSize: 14,
          fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
          fontLigatures: true,
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          lineNumbers: "on",
          renderLineHighlight: "line",
          tabSize: 2,
          wordWrap: "on",
          padding: { top: 16, bottom: 16 },
          smoothScrolling: true,
          cursorBlinking: "smooth",
          bracketPairColorization: { enabled: true },
        }}
      />
    </div>
  );
}
