function Navbar() {

  return (
    <div className="h-16 border-b border-slate-800 px-6 flex items-center justify-between">

      <input
        type="text"
        placeholder="Search startups..."
        className="bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 w-80"
      />

      <div>

        <div className="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center">
          M
        </div>

      </div>

    </div>
  );
}

export default Navbar;