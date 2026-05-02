import axios from "axios";
import type { Challenge, ChallengeSummary, ExecutionResult, TestSummary, Topic } from "../types";

const client = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  timeout: 60_000,
});

export const api = {
  async generateChallenge(
    topic: string,
    difficulty: string,
    language: string,
    excludeIds: string[] = []
  ): Promise<Challenge> {
    const { data } = await client.post("/api/challenges/generate", {
      topic,
      difficulty,
      language,
      exclude_ids: excludeIds,
    });
    return data;
  },

  async getTopics(): Promise<Topic[]> {
    const { data } = await client.get("/api/challenges/topics");
    return data;
  },

  async getLibrary(): Promise<ChallengeSummary[]> {
    const { data } = await client.get("/api/challenges/library");
    return data;
  },

  async getChallenge(challengeId: string): Promise<Challenge> {
    const { data } = await client.get(`/api/challenges/library/${challengeId}`);
    return data;
  },

  async runCode(language: string, code: string): Promise<ExecutionResult> {
    const { data } = await client.post("/api/execution/run", {
      language,
      code,
    });
    return data;
  },

  async testCode(
    language: string,
    code: string,
    test_cases: { input: string; expected_output: string }[]
  ): Promise<TestSummary> {
    const { data } = await client.post("/api/execution/test", {
      language,
      code,
      test_cases,
    });
    return data;
  },
};
