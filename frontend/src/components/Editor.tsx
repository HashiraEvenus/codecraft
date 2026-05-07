import { useRef } from "react";
import MonacoEditor from "@monaco-editor/react";
import type { OnMount } from "@monaco-editor/react";
import { LANGUAGE_MONACO } from "../lib/utils";
import { useTheme } from "../contexts/ThemeContext";

interface Props {
  language: string;
  value: string;
  onChange: (value: string) => void;
  onRun?: () => void;
}

export default function Editor({ language, value, onChange, onRun }: Props) {
  const { theme } = useTheme();
  const isWarm = theme === "warm-craft";

  // Ref so the Monaco command always calls the latest version of onRun
  const onRunRef = useRef(onRun);
  onRunRef.current = onRun;

  const handleMount: OnMount = (editor, monaco) => {
    // Define the warm-craft editor theme
    monaco.editor.defineTheme("warm-craft", {
      base: "vs",
      inherit: true,
      rules: [
        { token: "comment", foreground: "9e8e77", fontStyle: "italic" },
        { token: "keyword", foreground: "c2672d", fontStyle: "bold" },
        { token: "string", foreground: "6b8e4e" },
        { token: "number", foreground: "d97845" },
        { token: "type", foreground: "b87a3d" },
      ],
      colors: {
        "editor.background": "#fdfcfa",
        "editor.foreground": "#3d2f1f",
        "editor.lineHighlightBackground": "#f0ebe3",
        "editorLineNumber.foreground": "#c4b5a0",
        "editorLineNumber.activeForeground": "#8b7355",
        "editor.selectionBackground": "#e8dfd0",
        "editor.inactiveSelectionBackground": "#f0ebe3",
        "editorCursor.foreground": "#d97845",
        "editorIndentGuide.background": "#e8dfd0",
        "editorWidget.background": "#fdfcfa",
        "editorWidget.border": "#e8dfd0",
        "scrollbarSlider.background": "#c4b5a066",
        "scrollbarSlider.hoverBackground": "#a89282aa",
      },
    });

    editor.addCommand(
      monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter,
      () => onRunRef.current?.(),
    );
  };

  return (
    <div className="h-full w-full overflow-hidden rounded-b-xl">
      <MonacoEditor
        height="100%"
        language={LANGUAGE_MONACO[language] ?? language}
        value={value}
        theme={isWarm ? "warm-craft" : "vs-dark"}
        onChange={(v) => onChange(v ?? "")}
        onMount={handleMount}
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
