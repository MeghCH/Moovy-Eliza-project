import { RiRobot3Line } from "@remixicon/react";

export default function Demo() {
  const films = [
    { title: "Scream", rating: "8.3", genre: "Horror" },
    { title: "Rosemary's baby", rating: "8.1", genre: "Horror" },
    { title: "Shining", rating: "8.5", genre: "Thriller / Horror" },
  ];
  const feature = {
    icon: <RiRobot3Line className="text-4x" />,
  };

  return (
    <section className="flex flex-col items-center py-24 px-4">
      <p className="text-gray-400 text-sm tracking-widest uppercase mb-8">
        Voir en action
      </p>

      <div className="w-full max-w-3xl bg-white/5 border border-white/10 rounded-2xl p-8 flex flex-col gap-6">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center shrink-0">
            <span className="text-white text-xs">{feature.icon}</span>
          </div>
          <div
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              backgroundColor: "rgba(255,255,255,0.1)",
              color: "white",
              borderRadius: "0px 12px 12px 12px",
            }}
          >
            Un film pour frissonner un dimanche ?
          </div>
        </div>

        <div className="flex justify-end">
          <div
            style={{
              padding: "8px 24px",
              fontSize: "14px",
              backgroundColor: "#7c3aed",
              color: "white",
              borderRadius: "12px 0px 12px 12px",
            }}
          >
            Oui, un vieux film
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center shrink-0">
            <span className="text-white text-xs">{feature.icon}</span>
          </div>
          <div
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              backgroundColor: "rgba(255,255,255,0.1)",
              color: "white",
              borderRadius: "0px 12px 12px 12px",
            }}
          >
            Voici 3 films parfaits pour toi :
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 mt-2">
          {films.map((film, index) => (
            <div
              key={index}
              className="flex flex-col bg-white/5 border border-white/10 rounded-xl overflow-hidden"
            >
              <div className="w-full h-50 bg-white/10" />

              <div className="p-3 flex flex-col gap-1">
                <p className="text-white text-sm font-medium">{film.title}</p>
                <p className="text-yellow-500 text-xs">★ {film.rating}</p>
                <span className="text-xs text-gray-400 bg-white/10 rounded-full px-2 py-0.5 w-fit">
                  {film.genre}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
