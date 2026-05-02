export interface Concept {
  title: string;
  explanation: string;
  examples: string[];
  watch_out: string;
}

export interface Challenge {
  title: string;
  description: string;
  starter_code: string;
  test_cases: TestCase[];
  hint: string;
  solution: string;
  concepts: Concept[];
  docs_url: string;
  topic: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  language: string;
}

export interface TestCase {
  input: string;
  expected_output: string;
}

export interface TestResult {
  input: string;
  expected: string;
  actual: string;
  passed: boolean;
  stderr?: string;
}

export interface TestSummary {
  results: TestResult[];
  all_passed: boolean;
  passed_count: number;
  total: number;
}

export interface ExecutionResult {
  stdout: string;
  stderr: string;
  exit_code: number;
  signal?: string;
}

export interface Topic {
  id: string;
  name: string;
  icon: string;
  description: string;
}

export type Difficulty = "beginner" | "intermediate" | "advanced";
export type Language = "python" | "javascript" | "typescript";

export interface UserProgress {
  totalCompleted: number;
}
