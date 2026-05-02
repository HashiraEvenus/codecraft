import { Link } from "react-router-dom";
import { Code2, Sparkles, Play, BookOpen, ArrowRight, CheckCircle2 } from "lucide-react";

const FEATURES = [
  {
    icon: Sparkles,
    title: "AI-Generated Challenges",
    body: "Generate fresh practice prompts locally using your own Gemini API key.",
  },
  {
    icon: Play,
    title: "Local Code Execution",
    body: "Run Python, JavaScript, and TypeScript on your own machine without hosted execution costs.",
  },
  {
    icon: BookOpen,
    title: "Hints, Solutions, References",
    body: "Use hints and concept notes when you are stuck, then reveal the solution when you are ready.",
  },
];

const LOCAL_FEATURES = [
  "No hosted code execution bill",
  "Your Gemini API key stays local",
  "Python, JavaScript, TypeScript",
  "Hints and solutions included",
];

function CodeMockup() {
  return (
    <div className="card overflow-hidden shadow-2xl shadow-violet-900/20 w-full max-w-2xl mx-auto">
      {/* Window chrome */}
      <div className="flex items-center gap-1.5 px-4 py-3 border-b border-zinc-800 bg-zinc-900/80">
        <span className="h-3 w-3 rounded-full bg-red-500/70" />
        <span className="h-3 w-3 rounded-full bg-amber-500/70" />
        <span className="h-3 w-3 rounded-full bg-emerald-500/70" />
        <span className="ml-3 text-xs text-zinc-500 font-mono">reverse_string.py</span>
      </div>
      {/* Challenge + code */}
      <div className="grid grid-cols-2 divide-x divide-zinc-800 text-xs font-mono">
        <div className="p-4 space-y-3 bg-zinc-900/40">
          <div className="flex gap-2">
            <span className="px-1.5 py-0.5 rounded text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 text-[10px]">beginner</span>
            <span className="px-1.5 py-0.5 rounded text-zinc-400 bg-zinc-800 border border-zinc-700 text-[10px]">strings</span>
          </div>
          <p className="text-zinc-300 font-sans text-[11px] leading-relaxed">
            Write a function that reverses a string without using built-in reverse methods.
          </p>
          <div className="space-y-1.5 pt-1">
            <div className="text-zinc-500 text-[10px] uppercase tracking-wide">Test Cases</div>
            {[["solution('hello')", '"olleh"'], ["solution('abc')", '"cba"']].map(([inp, out]) => (
              <div key={inp} className="flex gap-2 text-[11px]">
                <span className="text-violet-300">{inp}</span>
                <span className="text-zinc-600">→</span>
                <span className="text-emerald-300">{out}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="p-4 bg-[#1e1e1e]">
          <pre className="text-[11px] leading-relaxed">
            <span className="text-blue-400">def </span>
            <span className="text-yellow-300">solution</span>
            <span className="text-zinc-300">(s: </span>
            <span className="text-blue-300">str</span>
            <span className="text-zinc-300">) -&gt; </span>
            <span className="text-blue-300">str</span>
            <span className="text-zinc-300">{":"}</span>
            {"\n"}
            {"    "}
            <span className="text-zinc-500"># your code here</span>
            {"\n"}
            {"    "}
            <span className="text-pink-400">result </span>
            <span className="text-zinc-300">= </span>
            <span className="text-orange-300">""</span>
            {"\n"}
            {"    "}
            <span className="text-blue-400">for </span>
            <span className="text-zinc-300">char </span>
            <span className="text-blue-400">in </span>
            <span className="text-pink-400">s</span>
            <span className="text-zinc-300">{":"}</span>
            {"\n"}
            {"        "}
            <span className="text-pink-400">result </span>
            <span className="text-zinc-300">= char + </span>
            <span className="text-pink-400">result</span>
            {"\n"}
            {"    "}
            <span className="text-blue-400">return </span>
            <span className="text-pink-400">result</span>
          </pre>
        </div>
      </div>
      {/* Output bar */}
      <div className="flex items-center gap-3 px-4 py-2.5 border-t border-zinc-800 bg-zinc-900/60 text-[11px] font-mono">
        <CheckCircle2 className="h-3.5 w-3.5 text-emerald-400 shrink-0" />
        <span className="text-emerald-400">2/2 tests passed</span>
        <span className="text-zinc-600 ml-auto">Executed in 142ms</span>
      </div>
    </div>
  );
}

export default function Landing() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Nav */}
      <header className="sticky top-0 z-40 border-b border-zinc-800/60 bg-zinc-950/80 backdrop-blur-sm">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 flex h-14 items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="flex h-7 w-7 items-center justify-center rounded-md bg-violet-600">
              <Code2 className="h-4 w-4 text-white" />
            </div>
            <span className="font-bold text-zinc-50 tracking-tight">CodeCraft</span>
          </div>
          <Link to="/dashboard" className="btn-primary text-sm flex items-center gap-1.5">
            Start Coding <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero */}
        <section className="relative pt-20 pb-16 px-4 sm:px-6 overflow-hidden">
          {/* Background glow */}
          <div className="absolute inset-0 -z-10 overflow-hidden pointer-events-none">
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-violet-600/8 rounded-full blur-3xl" />
          </div>

          <div className="mx-auto max-w-7xl text-center space-y-6">
            <div className="inline-flex items-center gap-2 text-xs font-medium text-violet-300 bg-violet-500/10 border border-violet-500/20 px-3 py-1.5 rounded-full">
              <Sparkles className="h-3.5 w-3.5" />
              Local-first · AI-powered · Personal practice
            </div>

            <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight leading-none">
              Level Up Your <br />
              <span className="gradient-text">Coding Skills</span>
            </h1>

            <p className="text-zinc-400 text-lg max-w-xl mx-auto leading-relaxed">
              Practice with AI-generated challenges tailored to your topic and difficulty. Run code on your own machine and keep the app simple.
            </p>

            <div className="flex items-center justify-center gap-3 flex-wrap">
              <Link to="/dashboard" className="btn-primary text-base px-6 py-2.5 flex items-center gap-2">
                Start Practicing <ArrowRight className="h-4 w-4" />
              </Link>
              <a href="#local" className="btn-outline text-base px-6 py-2.5">
                How It Works
              </a>
            </div>
          </div>

          {/* Mockup */}
          <div className="mt-14 mx-auto max-w-5xl px-4">
            <CodeMockup />
          </div>
        </section>

        {/* Features */}
        <section className="py-20 px-4 sm:px-6 border-t border-zinc-800/60">
          <div className="mx-auto max-w-7xl">
            <div className="text-center mb-12 space-y-2">
              <h2 className="text-2xl sm:text-3xl font-bold text-zinc-50">
                Everything you need to practice effectively
              </h2>
              <p className="text-zinc-400">No fluff — just the tools that make practice stick.</p>
            </div>
            <div className="grid sm:grid-cols-3 gap-5">
              {FEATURES.map(({ icon: Icon, title, body }) => (
                <div key={title} className="card p-6 space-y-3 hover:border-zinc-700 transition-colors">
                  <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-violet-600/15 border border-violet-500/20">
                    <Icon className="h-5 w-5 text-violet-400" />
                  </div>
                  <h3 className="font-semibold text-zinc-50">{title}</h3>
                  <p className="text-sm text-zinc-400 leading-relaxed">{body}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Local setup */}
        <section id="local" className="py-20 px-4 sm:px-6 border-t border-zinc-800/60">
          <div className="mx-auto max-w-7xl">
            <div className="text-center mb-12 space-y-2">
              <h2 className="text-2xl sm:text-3xl font-bold text-zinc-50">Built for local use</h2>
              <p className="text-zinc-400">Bring your own Gemini key and run everything from your machine.</p>
            </div>

            <div className="grid sm:grid-cols-2 gap-5 max-w-4xl mx-auto">
              <div className="card p-6 space-y-5">
                <div>
                  <h3 className="font-semibold text-zinc-50 text-lg">Personal Practice</h3>
                  <p className="text-sm text-zinc-500 mt-1">No subscription layer. No per-run executor API.</p>
                </div>
                <ul className="space-y-2.5 text-sm">
                  {LOCAL_FEATURES.map((f) => (
                    <li key={f} className="flex items-center gap-2 text-zinc-300">
                      <CheckCircle2 className="h-4 w-4 text-zinc-500 shrink-0" />
                      {f}
                    </li>
                  ))}
                </ul>
                <Link to="/dashboard" className="btn-outline w-full flex items-center justify-center text-sm">
                  Get Started
                </Link>
              </div>

              <div className="card p-6 space-y-4 border-violet-500/30 bg-violet-950/10">
                <h3 className="font-semibold text-zinc-50 text-lg">What you need</h3>
                <div className="space-y-3 text-sm text-zinc-300">
                  <p>Install Python and Node if you want local execution for those languages.</p>
                  <p>Add your Gemini API key to the backend `.env` file.</p>
                  <p>Run the backend and frontend locally, then practice from your browser.</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-zinc-800/60 py-8 px-4 sm:px-6">
        <div className="mx-auto max-w-7xl flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-zinc-500">
          <div className="flex items-center gap-2">
            <div className="flex h-5 w-5 items-center justify-center rounded bg-violet-600">
              <Code2 className="h-3 w-3 text-white" />
            </div>
            <span className="font-medium text-zinc-400">CodeCraft</span>
          </div>
          <span>© {new Date().getFullYear()} CodeCraft. All rights reserved.</span>
        </div>
      </footer>
    </div>
  );
}
