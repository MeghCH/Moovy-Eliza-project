const genres = [
  { percentage: "10%", label: "DRAME" },
  { percentage: "20%", label: "HORROR" },
  { percentage: "30%", label: "THRILLER" },
  { percentage: "5%", label: "ROMANCE" },
  { percentage: "25%", label: "AVENTURE" },
  { percentage: "10%", label: "SCI-FI" },
];

export default function ProfilePage() {
  return (
    <main className="min-h-screen px-8 py-12 flex flex-col items-center">
      <h1 className="text-white text-3xl font-semibold mb-10">Hy Sarah</h1>

      <div className="grid grid-cols-3 gap-6 max-w-4xl mx-auto">
        {genres.map((genre) => (
          <div
            key={genre.label}
            className="flex flex-col items-center justify-center text-center bg-white/5 border border-purple-600/40 rounded-2xl p-8 aspect-square hover:bg-white/10 transition-colors"
          >
            <span className="text-white text-4xl font-medium mb-2">
              {genre.percentage}
            </span>
            <span className="text-purple-400 text-base font-semibold tracking-widest">
              {genre.label}
            </span>
          </div>
        ))}
      </div>
    </main>
  );
}