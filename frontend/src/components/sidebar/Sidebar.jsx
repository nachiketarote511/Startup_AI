import { Link } from "react-router-dom";

function Sidebar() {

  return (
    <div className="w-72 bg-slate-900 border-r border-slate-800 p-5">

      <h1 className="text-xl font-bold mb-8">
        Startup Intelligence
      </h1>

      <nav className="space-y-2">

        <Link
          to="/"
          className="block p-3 rounded-lg hover:bg-slate-800"
        >
          Dashboard
        </Link>

        <Link
          to="/analysis"
          className="block p-3 rounded-lg hover:bg-slate-800"
        >
          Startup Analysis
        </Link>

        <Link
          to="/success-prediction"
          className="block p-3 rounded-lg hover:bg-slate-800"
        >
          Success Prediction
        </Link>

        <Link
          to="/failure-risk"
          className="block p-3 rounded-lg hover:bg-slate-800"
        >
          Failure Risk
        </Link>

        <Link
          to="/investor-readiness"
          className="block p-3 rounded-lg hover:bg-slate-800"
        >
          Investor Readiness
        </Link>

      </nav>

    </div>
  );
}

export default Sidebar;