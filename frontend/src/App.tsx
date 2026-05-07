import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Landing from "./pages/Landing";
import Dashboard from "./pages/Dashboard";
import ChallengePage from "./pages/ChallengePage";
import LibraryPage from "./pages/LibraryPage";
import LearnPage from "./pages/LearnPage";
import StatsPage from "./pages/StatsPage";
import { ThemeProvider } from "./contexts/ThemeContext";

export default function App() {
  return (
    <ThemeProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/learn" element={<LearnPage />} />
        <Route path="/library" element={<LibraryPage />} />
        <Route path="/challenge" element={<ChallengePage />} />
        <Route path="/stats" element={<StatsPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
    </ThemeProvider>
  );
}
