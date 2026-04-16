export default function Header() {
  return (
    <section className="flex flex-col items-center justify-center text-center py-24 px-4">
      <span className="bg-purple-600/20 text-purple-400 text-sm px-4 py-1 rounded-full border border-purple-500/30 mb-6">
        Ton assistant cinéma
      </span>
      <h1 className="text-5xl font-bold text-white mb-4">
        Trouve ton prochain film <br /> en 30 secondes
      </h1>
      <p className="text-gray-400 text-lg mb-8">
        Décris ton humeur, MooVy fait le reste
      </p>
      <span className="bg-purple-600 text-white px-8 py-3 rounded-full font-medium cursor-default">
        Coming Soon
      </span>
    </section>
  );
}
