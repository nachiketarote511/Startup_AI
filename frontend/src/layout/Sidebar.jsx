import {
  LayoutDashboard,
  Search,
  Trophy,
  TriangleAlert,
  Briefcase,
  HeartPulse,
  Users,
  Landmark,
  Target,
  Sparkles,
  Swords,
  Lightbulb,
  FlaskConical,
  Radar,
  ScanSearch,
  Network,
  Database,
  GitBranch,
  FileText,
  Settings,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menuItems = [
  {
    title: "OVERVIEW",
    items: [
      { name: "Dashboard", icon: LayoutDashboard, path: "/" },
      { name: "Startup Analysis", icon: Search, path: "/startup-analysis" },
    ],
  },

  {
    title: "AI SCORES",
    items: [
      { name: "Success Prediction", icon: Trophy, path: "/success-prediction" },
      { name: "Failure Risk", icon: TriangleAlert, path: "/failure-risk" },
      { name: "Investor Readiness", icon: Briefcase, path: "/investor-readiness" },
      { name: "Startup Health", icon: HeartPulse, path: "/startup-health" },
      { name: "Founder Strength", icon: Users, path: "/founder-strength" },
      { name: "Funding Strength", icon: Landmark, path: "/funding-strength" },
      { name: "Market Opportunity", icon: Target, path: "/market-opportunity" },
      { name: "Growth Potential", icon: Sparkles, path: "/growth-potential" },
      { name: "Innovation", icon: FlaskConical, path: "/innovation" },
      { name: "Competition", icon: Swords, path: "/competition" },
    ],
  },

  {
    title: "INTELLIGENCE",
    items: [
      { name: "Recommendations", icon: Lightbulb, path: "/recommendations" },
      { name: "What-If Simulator", icon: Radar, path: "/what-if" },
      { name: "Competitor Discovery", icon: ScanSearch, path: "/competitors" },
      { name: "Market Gap", icon: Target, path: "/market-gap" },
      { name: "Startup Clustering", icon: Database, path: "/clustering" },
      { name: "Knowledge Graph", icon: Network, path: "/knowledge-graph" },
      { name: "Startup Explorer", icon: GitBranch, path: "/explorer" },
    ],
  },

  {
    title: "SYSTEM",
    items: [
      { name: "Reports", icon: FileText, path: "/reports" },
      { name: "Settings", icon: Settings, path: "/settings" },
    ],
  },
];

function Sidebar() {
  return (
    <aside className="w-[260px] bg-[#081223] border-r border-slate-800 h-screen overflow-y-auto fixed left-0 top-0">
      <div className="p-6 border-b border-slate-800">
        <h1 className="text-xl font-bold text-white">
          Startup Intel
        </h1>

        <p className="text-xs text-slate-400 mt-1">
          VC PLATFORM
        </p>
      </div>

      <div className="p-4">
        {menuItems.map((section) => (
          <div key={section.title} className="mb-6">
            <p className="text-[11px] text-slate-500 tracking-widest mb-3">
              {section.title}
            </p>

            {section.items.map((item) => {
              const Icon = item.icon;

              return (
                <NavLink
                  key={item.name}
                  to={item.path}
                  className={({ isActive }) =>
                    `flex items-center gap-3 px-4 py-3 rounded-xl mb-1 transition ${
                      isActive
                        ? "bg-slate-800 text-white"
                        : "text-slate-400 hover:bg-slate-900"
                    }`
                  }
                >
                  <Icon size={18} />
                  <span>{item.name}</span>
                </NavLink>
              );
            })}
          </div>
        ))}
      </div>
    </aside>
  );
}

export default Sidebar;