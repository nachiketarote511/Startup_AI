import { Bell, Search } from "lucide-react";

function Topbar() {
  return (
    <header className="h-[72px] border-b border-slate-800 bg-[#081223] flex items-center justify-between px-8">
      <div className="relative w-[500px]">
        <Search
          className="absolute left-4 top-3 text-slate-500"
          size={18}
        />

        <input
          placeholder="Search startups, founders, sectors..."
          className="w-full bg-[#0f1c32] border border-slate-700 rounded-xl py-3 pl-11 text-white outline-none"
        />
      </div>

      <div className="flex items-center gap-6">
        <Bell className="text-slate-400" />

        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-full bg-violet-600 flex items-center justify-center font-bold">
            SA
          </div>

          <div>
            <p className="text-sm text-white font-semibold">
              Sara Alvarez
            </p>

            <p className="text-xs text-slate-400">
              Atlas Capital
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Topbar;