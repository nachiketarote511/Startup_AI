import MainLayout from "../layout/MainLayout";

function Dashboard() {
  const stats = [
    { title: "STARTUPS ANALYZED", value: "12,847" },
    { title: "AVG HEALTH SCORE", value: "76.3" },
    { title: "INVESTOR READY", value: "2,143" },
    { title: "HIGH GROWTH", value: "1,876" },
    { title: "HIGH RISK", value: "934" },
    { title: "MARKET OPPORTUNITIES", value: "428" },
  ];

  return (
    <MainLayout>
      <div className="space-y-8">

        <div className="rounded-3xl border border-slate-800 bg-gradient-to-r from-[#111f40] to-[#0a1630] p-10">
          <h1 className="text-6xl font-bold mb-4">
            Startup Intelligence Platform
          </h1>

          <p className="text-slate-400 max-w-4xl">
            AI powered startup analytics, prediction and
            investor intelligence engine.
          </p>
        </div>

        <div className="grid grid-cols-6 gap-5">
          {stats.map((item) => (
            <div
              key={item.title}
              className="bg-[#0c1730] border border-slate-800 rounded-2xl p-5"
            >
              <p className="text-xs text-slate-400">
                {item.title}
              </p>

              <h2 className="text-4xl font-bold mt-2">
                {item.value}
              </h2>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-2 gap-6">

          <div className="h-[420px] rounded-3xl bg-[#0c1730] border border-slate-800 p-6">
            <h2 className="font-semibold mb-4">
              Signal Velocity
            </h2>
          </div>

          <div className="h-[420px] rounded-3xl bg-[#0c1730] border border-slate-800 p-6">
            <h2 className="font-semibold mb-4">
              Investor Readiness
            </h2>
          </div>

        </div>

      </div>
    </MainLayout>
  );
}

export default Dashboard;