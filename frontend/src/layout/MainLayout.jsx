import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

function MainLayout({ children }) {
  return (
    <div className="bg-[#040b1d] min-h-screen text-white">
      <Sidebar />

      <div className="ml-[260px]">
        <Topbar />

        <main className="p-8">
          {children}
        </main>
      </div>
    </div>
  );
}

export default MainLayout;