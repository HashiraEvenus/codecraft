import { Link, useLocation } from "react-router-dom";
import { Code2 } from "lucide-react";

interface NavbarProps {
  rightSlot?: React.ReactNode;
}

export default function Navbar({ rightSlot }: NavbarProps) {
  const { pathname } = useLocation();

  return (
    <header className="sticky top-0 z-40 border-b border-zinc-800/60 bg-zinc-950/80 backdrop-blur-sm">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 flex h-14 items-center justify-between">
        <Link to="/" className="flex items-center gap-2 group">
          <div className="flex h-7 w-7 items-center justify-center rounded-md bg-violet-600 group-hover:bg-violet-500 transition-colors">
            <Code2 className="h-4 w-4 text-white" />
          </div>
          <span className="font-bold text-zinc-50 tracking-tight">CodeCraft</span>
        </Link>

        <nav className="flex items-center gap-1">
          {pathname !== "/" && (
            <Link to="/dashboard" className="btn-ghost text-sm">
              Dashboard
            </Link>
          )}
          {rightSlot}
          {pathname === "/" && (
            <Link to="/dashboard" className="btn-primary text-sm">
              Start Coding
            </Link>
          )}
        </nav>
      </div>
    </header>
  );
}
