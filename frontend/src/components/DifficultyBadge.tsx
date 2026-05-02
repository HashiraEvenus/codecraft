import type { Difficulty } from "../types";
import { DIFFICULTY_COLORS } from "../lib/utils";

interface Props {
  difficulty: Difficulty;
  className?: string;
}

export default function DifficultyBadge({ difficulty, className = "" }: Props) {
  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium border capitalize ${DIFFICULTY_COLORS[difficulty]} ${className}`}
    >
      {difficulty}
    </span>
  );
}
